#!/usr/bin/env python3
"""
Append a new (translated) meeting/presentation update to the correct
account's Activity cell in the Selution account activity tracker.

DESIGN NOTE: an earlier version of this script tried to insert a brand
new spreadsheet row for each update. That was reverted after testing
showed openpyxl does not reliably shift merged-cell ranges during row
insertion, which silently corrupted unrelated rows in a file that uses
merged cells (this tracker does). Appending text into the account's
existing Activity cell (with a dated separator line) is the safe
alternative: it only ever changes the .value of ONE cell that already
exists, so there is no possibility of shifting or corrupting any other
row, column, or merge in the workbook. This matches how the file is
already used in practice (existing Activity cells already contain
multiple dated bullet points stacked in one cell).

Always run with --dry-run first and read the printed preview (old text
vs. new text) before running for real. Nothing is written in dry-run.

Usage:
  python append_entry.py --file "<path to .xlsx>" --account "Soroka Cardio" \
      --entry "Translated English text of the update." --date "7.7" [--dry-run]
"""
import argparse
import json
import sys
from openpyxl import load_workbook


def norm(s):
    return " ".join(str(s or "").strip().lower().split())


HEADER_LABELS = {"account", "accuont", "account manager", "accuont owner", "owner"}


def find_header_row(ws, max_scan=15):
    """Return (header_row_idx) by scanning the first max_scan rows for a
    row containing both an 'account'-like and an 'activity'-like cell."""
    for r in range(1, max_scan + 1):
        has_account = False
        has_activity = False
        for c in range(1, ws.max_column + 1):
            v = ws.cell(row=r, column=c).value
            if v is None:
                continue
            nv = norm(v)
            if "accuont" in nv or nv == "account" or "account" in nv:
                has_account = True
            if "activity" in nv:
                has_activity = True
        if has_account and has_activity:
            return r
    return None


def find_columns(ws, header_row):
    """Map semantic column names to column indices using the header row
    AND the row right below it (this sheet repeats/clarifies headers on
    two stacked rows: 'accuont' then 'Account')."""
    cols = {}
    for r in (header_row, header_row + 1):
        for c in range(1, ws.max_column + 1):
            v = ws.cell(row=r, column=c).value
            if v is None:
                continue
            nv = norm(v)
            if ("accuont" in nv or nv == "account") and "manager" not in nv and "owner" not in nv:
                cols.setdefault("account", c)
            if "activity" in nv:
                cols.setdefault("activity", c)
    return cols


def find_account_row(ws, account_col, header_row, target_account):
    """Find the single anchor row where this account's block starts
    (the row that actually holds the account name). Returns row idx or
    None. If several rows loosely match, prefers an exact match, then
    the first substring match."""
    target_norm = norm(target_account)
    exact, partial = [], []
    for r in range(header_row + 1, ws.max_row + 1):
        v = ws.cell(row=r, column=account_col).value
        if v is None:
            continue
        nv = norm(v)
        if nv in HEADER_LABELS:
            continue
        if nv == target_norm:
            exact.append(r)
        elif target_norm in nv or nv in target_norm:
            partial.append(r)
    if exact:
        return exact[0]
    if partial:
        return partial[0]
    return None


def list_known_accounts(ws, account_col, header_row):
    seen = []
    for r in range(header_row + 1, ws.max_row + 1):
        v = ws.cell(row=r, column=account_col).value
        if v is not None and str(v).strip() and norm(v) not in HEADER_LABELS:
            seen.append(str(v).strip())
    return seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--account", required=True)
    ap.add_argument("--entry", required=True)
    ap.add_argument("--date", default="")
    ap.add_argument("--sheet", default=None, help="Sheet name; defaults to the first sheet")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    wb = load_workbook(args.file)
    ws = wb[args.sheet] if args.sheet else wb[wb.sheetnames[0]]

    header_row = find_header_row(ws)
    if header_row is None:
        print(json.dumps({"status": "error", "message": "Could not find a header row with Account/Activity columns."}))
        sys.exit(1)

    cols = find_columns(ws, header_row)
    if "account" not in cols or "activity" not in cols:
        print(json.dumps({"status": "error", "message": f"Could not identify Account/Activity columns. Found: {cols}"}))
        sys.exit(1)

    account_col = cols["account"]
    activity_col = cols["activity"]

    row = find_account_row(ws, account_col, header_row, args.account)
    if row is None:
        known = list_known_accounts(ws, account_col, header_row)
        print(json.dumps({
            "status": "not_found",
            "message": f"No account matching '{args.account}' found in this sheet.",
            "known_accounts": known,
        }, ensure_ascii=False, indent=2))
        sys.exit(2)

    activity_cell = ws.cell(row=row, column=activity_col)
    old_text = activity_cell.value or ""
    new_line = f"[{args.date}] {args.entry}" if args.date else args.entry
    new_text = f"{old_text}\n\n{new_line}" if str(old_text).strip() else new_line

    summary = {
        "status": "preview" if args.dry_run else "applied",
        "file": args.file,
        "sheet": ws.title,
        "matched_account": ws.cell(row=row, column=account_col).value or "(continuation row)",
        "cell": f"row {row}, col {activity_col}",
        "old_text": old_text,
        "new_text": new_text,
    }

    if args.dry_run:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    activity_cell.value = new_text
    wb.save(args.file)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
