---
name: deb-account-tracker-log
description: DEB / Selution account tracker logger — Matan (a medical device rep) writes short Hebrew notes about meetings, calls, and clinical presentations he gives to doctors/hospitals. This skill translates each note into English, matches it to the right hospital account, and gets it into the shared team tracker in Dropbox — without Matan having to open the Excel file himself or type in English. Requires local file-system access (Claude Code / Claude Desktop running on Matan's machine) — not usable from a browser-only session.
---

# DEB / Selution account tracker logger

Matan (a medical device rep) writes short Hebrew notes about meetings, calls, and clinical presentations he gives to doctors/hospitals. This skill translates each note into English, matches it to the right hospital account, and gets it into the shared team tracker in Dropbox — without Matan having to open the Excel file himself or type in English.

There are two distinct modes. Figure out which one applies from what the user says (see "Which mode?" below) — don't ask them to specify a mode by name.

## Hard constraints — read before doing anything

1. **Never insert new spreadsheet rows into the tracker files**, and never call `ws.insert_rows()` / `ws.delete_rows()` on them. Testing during this skill's development showed openpyxl does not reliably move merged-cell ranges when rows are inserted — it silently corrupted unrelated rows elsewhere in the sheet (data from one hospital's block leaked into another's). The tracker uses merged cells for the Account/Owner columns, so this risk is real, not theoretical. Only ever append text to an existing cell's value using `scripts/append_entry.py` (or the same technique) — never restructure rows.
2. **Never touch the real tracker .xlsx files during the week.** Logging mode only ever writes to the local staging folder. The real files in Dropbox are only opened during an explicit weekly-build request, and even then, always dry-run first (see below).
3. **Always run `append_entry.py` with `--dry-run` first**, show the user the `old_text` → `new_text` diff for every entry, and get their OK before running the same command again without `--dry-run`.
4. This skill depends on real file-system tools (Read/Write/Bash with local disk access). If those tools aren't available in the current session, tell the user this needs Claude Code / Claude Desktop with file access, not the plain claude.ai chat — don't try to fake it with a download link.

## Key paths (hardcoded for this user — verify they still exist before using)

- Local staging folder (logging mode writes here, nothing else touches it): `C:\Users\matan\OneDrive\Desktop\duke ms\Devices\DEB\עדכונים זמניים לקובץ מעקב`
- Cardio tracker (real file, local Dropbox sync): `C:\Users\matan\Duke Dropbox\Uri & Cordis team\Selution 2026 Tracking\cardio\account activity tracker 2026.xlsx`
- Endo tracker (real file, local Dropbox sync): `C:\Users\matan\Duke Dropbox\Uri & Cordis team\Selution 2026 Tracking\endo\account activity tracker 2026.xlsx`

If any of these paths don't exist when you check, stop and ask Matan — don't guess at a different path, since these are shared team files.

See `references/accounts.md` for the known hospital accounts (with their Hebrew names, which tracker file each belongs to, and known doctors) and for the translation style guide. Read it before translating or matching accounts — matching the account correctly matters more than translating beautifully.

## Which mode?

- User is describing something that happened (a meeting, a call, a presentation, what a doctor said) → **Logging mode**.
- User is asking to build/prepare/finalize/update the actual tracker file, or says something like "it's Thursday" / "weekly update" → **Weekly build mode**.
- Unclear which hospital/account a note belongs to → ask; don't guess on a shared business document. `references/accounts.md` has the full list.

## Logging mode (during the week)

1. Read the Hebrew note. Identify:
   - Which account/hospital it belongs to (fuzzy-match against `references/accounts.md`; ask if genuinely ambiguous)
   - Which tracker file that account lives in (cardio or endo — some hospitals, like Soroka and Carmel, have accounts in both files for different departments; ask which one if the note doesn't make it obvious)
   - The date the meeting happened (ask if not stated; don't assume "today" silently for something that clearly already happened)
2. Translate to English following the style guide in `references/accounts.md`.
3. Write one small text file into the staging folder (create the folder if it somehow doesn't exist yet). Filename pattern: `YYYY-MM-DD_<tracker>_<account-slug>.txt` (e.g. `2026-07-07_cardio_soroka.txt`). File contents:

   ```
   tracker: cardio
   account: Soroka Cardio
   date: 7.7
   ---
   <translated English entry text>
   ```

4. Tell Matan in one short line what you saved and where — don't narrate the whole file-parsing process. Do not touch the real tracker file in this mode.

## Weekly build mode

1. List every file in the staging folder. If it's empty, say so and stop.
2. Read and parse each one (tracker / account / date / entry text).
3. Group entries by tracker file (cardio vs endo), then by account.
4. For each entry, run:

   ```
   python scripts/append_entry.py --file "<full tracker path>" \
     --account "<account>" --entry "<translated text>" --date "<date>" --dry-run
   ```

   Collect every preview. If any entry's account isn't found, stop and ask Matan instead of guessing (the script's error lists known accounts to help him pick).
5. Show Matan a clear summary of every change that would be made (account → old text snippet → new text snippet, across both tracker files as applicable) and ask him to confirm before writing anything for real.
6. Once confirmed, re-run the same commands without `--dry-run`, one entry at a time. If several entries land in the same account, that's fine — run them one after another; each one appends to the (by-then-updated) cell.
7. Confirm the tracker file(s) were updated (Dropbox will sync automatically in the background — no manual upload needed).
8. Only after Matan explicitly confirms the tracker looks right, delete the staging files you just processed (leave anything you didn't process, e.g. files added after you started, untouched).

## The append script

`scripts/append_entry.py` finds the right cell by reading the sheet's actual header row and account column at runtime (it does not assume fixed row/column numbers, since the file's exact layout can drift). It appends the new entry as a new dated paragraph inside the account's existing Activity cell — it never adds, removes, or reorders rows, and never touches any other cell. Run `python scripts/append_entry.py --help` for the full argument list.
