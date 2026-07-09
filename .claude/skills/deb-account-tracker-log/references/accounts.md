# Known accounts

Both tracker files share the same block structure: each account is a row with an **Account** name cell, an **Account Manager** (owner) cell, and a wide **Activity** cell containing the free-text meeting history (dated paragraphs, usually starting with `*` per bullet point). There is also a `Sheet1` in the cardio tracker mapping center → department → doctor → owner across *all* departments (cardio, endo, angio) — useful for resolving which rep owns a doctor even when the meeting notes live in the other tracker file.

Match accounts case-insensitively and tolerate Hebrew/English variants below. If a note's hospital doesn't match anything here, don't guess — ask Matan (it may be a new account).

## Cardio tracker (`cardio/account activity tracker 2026.xlsx`)

| Account (as in file) | Hebrew name(s) | Owner(s) | Known doctors |
|---|---|---|---|
| Soroka Cardio | סורוקה | Noa & Matan | Dr. Aref, Dr. Moni (dept. head), Dr. Alaa, Dr. Kafri, Dr. Rosenstein |
| Kaplan Cardio | קפלן | Sigal & Matan | Dr. Poles (retiring, ~10mo), Dr. Haberman (his successor, target KOL), Dr. Gera, Dr. Sela, Dr. Yonash |
| Hilel Yafe Cardio | הלל יפה / הילל יפה | Sigal & Matan | Prof Rugin, Dr. Majdi, Prof Abu-Fani |
| Sharei Zedek | שערי צדק / שע"צ | Noa & Matan | Dr. Juabeh, Dr. Mansra, Dr. Anna |
| Ichilov | איכילוב / סוראסקי | Noa & Matan | Prof Maayan, Dr. Bazan, Dr. Skali, Dr. Arbel |
| Carmel (Cardio dept.) | כרמל | Sigal & Matan | Dr. Zisman-Keren |

## Endo tracker (`endo/account activity tracker 2026.xlsx`)

| Account (as in file) | Hebrew name(s) | Owner(s) | Known doctors |
|---|---|---|---|
| Meir | מאיר | Noa & Matan | Dr. Michail, Dr. Meisam (runs their Galilee registry participation), Dr. Bachar |
| Soroka (Endo dept.) | סורוקה | Noa & Matan | Dr. Dima, Dr. Maxim, Dr. Anatoli, Dr. Greenberg, Dr. Nahel |
| Carmel (Endo dept.) | כרמל | Sigal & Matan | Dr. Hashem, Dr. Nujidat |

**Accounts that exist in both files** (same hospital name, completely separate department/doctors/history in each): Soroka, Carmel. Always confirm the department before deciding which tracker file a note belongs to.

**No KOL checklist folder exists for endo doctors yet** (only `cardio/KOL/` exists) — irrelevant to this skill, but relevant context if asked.

## Translation & style guide

The tracker is written in English, first person, informal-clinical tone. Match it:

- Write as Matan speaking: "I met with...", "I gave a presentation...", "We scheduled...".
- Keep doctor names as "Dr. X" / "Prof Y" (don't translate names).
- Keep clinical/technical terms in their standard English form: DEB, DCB, PCI, BTK, ATK, SFA, ISR, bail-out, lesion preparation, etc. — don't translate them, even loosely.
- Preserve dates in the file's `D.M` convention (e.g. `14.6`, `9.7`), not ISO format, inside the entry text itself.
- Use `*` for separate discrete points within one entry, matching the existing paragraphs.
- Keep it concise — summarize rambling Hebrew notes down to the same density as existing entries, don't pad.
- If the note mentions a doctor not listed in the tables above, flag them as a new contact in your summary back to Matan (don't silently drop this — Matan may want to add them to Sheet1 separately).
