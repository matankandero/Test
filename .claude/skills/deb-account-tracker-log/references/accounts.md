# Known accounts (as of July 2026)

This list was read directly from the two tracker files. It will drift over
time (new accounts, new doctors) — treat it as a strong prior for matching,
not gospel. If a note clearly refers to a hospital/account not listed here,
ask Matan rather than inventing a new row/account silently.

## Cardio tracker
(`.../Selution 2026 Tracking/cardio/account activity tracker 2026.xlsx`)

| Account (as written in file) | Hebrew | Rep owner | Known doctors |
|---|---|---|---|
| Soroka Cardio | סורוקה, קרדיו | Noa & Matan | Dr. Aref, Dr. Moni (SH), Dr. Alaa, Dr. Kafri, Dr. Rosenstein |
| Kaplan Cardio | קפלן, קרדיו | Sigal & Matan | Dr. Poles (SH, retiring), Dr. Haberman (SH, successor), Dr. Gera, Dr. Sela, Dr. Yonash |
| Hilel Yafe Cardio | הלל יפה, קרדיו | Sigal & Matan | Prof. Rugin/Roguin (SH), Dr. Majdi, Prof. Abu-Fani |
| Sharei Zedek | שערי צדק, קרדיו | Matan & Noa | Dr. Juabeh, Dr. Mansra |
| Ichilov | איכילוב, קרדיו | Noa & Matan | Prof. Maayan, Dr. Bazan, Dr. Sekali/Skali |
| Carmel (cardio) | כרמל, קרדיו | Sigal & Matan | Dr. Zisman-Keren |

## Endo tracker
(`.../Selution 2026 Tracking/endo/account activity tracker 2026.xlsx`)

| Account (as written in file) | Hebrew | Rep owner | Known doctors |
|---|---|---|---|
| Meir | מאיר, אנדו | Noa & Matan | Dr. Meisam, Dr. Michail |
| Soroka (endo) | סורוקה, אנדו | Noa & Matan | Dr. Dima, Dr. Maxim, Dr. Anatoli, Dr. Greenberg, Dr. Nahel |
| Carmel (endo) | כרמל, אנדו | Sigal & Matan | Dr. Hashem, Dr. Nujidat/Nujeidat |

**Note:** Soroka and Carmel each have a separate row in *both* files (one per
department). If a note about Soroka or Carmel doesn't make clear whether it's
cardio or endo, ask.

Other hospitals appear in the internal mapping sheet without activity entries
yet: Sharei Zedek (מתן ונעה), Angio (Galia/Matan). If Matan mentions a hospital
from this set with no existing Activity row, flag it — appending still works
(the script only needs a matching Account-column value; it will error out
listing known accounts if nothing matches, which is your cue to check with
Matan before proceeding).

---

# Translation & style guide

Match the voice already used in the tracker so new entries blend in:

- **First person, past tense**, written from Matan/Noa/Sigal's perspective:
  "I met with...", "We had a meeting with...", "I gave a presentation on...".
- **Lead with the concrete fact**: who was met, on what date, in what format
  (meeting / presentation / call), before getting into opinions or analysis.
- **Dates** in `D.M` or `DD.M` format matching the file (e.g. `14.6`, `1.7`),
  not `June 14`.
- **Doctors** referred to as "Dr. [Name]" or "Prof. [Name]" — keep names
  transliterated the way they already appear in the tracker
  (`references/accounts.md`) rather than re-transliterating from Hebrew
  yourself, so the same doctor doesn't end up spelled two different ways.
- Separate distinct points with `*` bullet markers if the note covers several
  unrelated things (competitor mentions, action items, next steps) — this
  mirrors the existing multi-bullet entries in the file.
- Keep it a faithful, fairly literal translation of what Matan actually wrote
  — don't embellish, editorialize, or pad it out. If his note is three quick
  bullet points, the translation should be three quick bullet points, not a
  paragraph.
- If the note mentions competitor products, specific study names, or numbers,
  preserve them exactly (these are frequently referenced later).

### Example

**Hebrew input:**
> נפגשתי עם ד"ר בזן באיכילוב היום (7.7). הוא אמר שהוא מעדיף סירולימוס. קבענו
> הרצאה למחלקה ל-14.7.

**English entry written to the tracker:**
> [7.7] I met with Dr. Bazan at Ichilov today. He said he prefers Sirolimus.
> We scheduled a department presentation for 14.7.
