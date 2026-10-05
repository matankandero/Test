# Memory — Matan (Selution/DEB rep)

## Fixed cath-lab days per hospital (for weekly scheduling)

Use these when building Matan's weekly schedule (לוז). Israeli work week: Sunday–Thursday.

| Hospital / Dept | Doctor | Cath day |
|---|---|---|
| Hillel Yaffe Cardio | Dr. Majdi | Monday |
| Kaplan Cardio | Dr. Haberman | Tuesday |
| Ichilov Cardio | Dr. Arbel | Tuesday |
| Carmel Endo | Dr. Nujidat / Dr. Hashem | Sunday |
| Meir Endo | Dr. Michail | Sunday / Monday |
| Shaarei Zedek Cardio | Dr. Juabeh | Wednesday |

Known constraint: Dr. Haberman is at the Kupat Holim clinic on Mondays (not at Kaplan).

### Cath days still unknown — find out and add above
- Dr. Zisman-Keren — Carmel Cardio
- Dr. Sheinman — Hillel Yaffe Cardio
- Dr. Alexei — Angio, Assaf Harofeh (Shamir)
- Dr. Saar Minha — Assaf Harofeh (Shamir) Cardio

## Upcoming commitments
- 9.9.2026 — presentation at Hadassah vascular (כלי דם). Task: improve the deck + prepare (run hospital-meeting-prep closer to the date). Same visit: collect Hadassah expired stock (all 3 items expired by then).
- Carmel visit of Sunday 16.8 was skipped — rolled to Sunday 23.8 (procedures Nujidat/Hashem, Cordis 6F answer, first Selution case push, collect 3 expired items).

## Notes
- Carmel Cardio: joining procedures in the cath lab is NOT possible (insurance/access issue, unresolvable) — follow cases from the control room only.

## Standing rule — expired stock collection (פגי תוקף)
Matan gets a consignment-stock expiry report (xlsx, per-warehouse: מחסן / product / qty / lot / expiry date).
1. IMPORTANT: items can only be collected AFTER their expiry date has passed — never suggest collecting an item before it expires. "Collect at visit" applies only to items already expired as of the visit date.
2. Every time a weekly schedule is built, for each location Matan visits add a task: collect the items at that site that will already be expired by the visit date (list them specifically from the latest expiry report).
3. For sites holding already-expired stock with no upcoming visit, and for items about to expire where no visit is planned shortly after the expiry date — raise an alert so Matan can plan a visit after the expiry or arrange things differently.
4. Ask for a fresh expiry report if the last one is more than ~2 weeks old.

### Expiry snapshot (from report `/matan kandero/פגי_תוקף_קונסיגנציה_2026-09.csv`, generated ~30.9.2026)
Source xlsx was uploaded to chat on 5.10.2026; a CSV copy was written to the private Dropbox
folder under the standard name so future runs find it. Covers expiries up to 31.3.2027.
Totals: 161 lines, 228 units. **Expired as of 5.10.2026: 34 lines, 50 units, ~58,000 ILS.**

Expired stock by site (units / ILS / oldest expiry):
- **איכילוב D06 (השאלות, לא קונסיגנציה)** — 25 units / ~31,900 ILS / oldest 25.7 — by far the largest pile
- סורוקה צנתורים — 5 / ~6,940 / 11.9
- כרמל ח.נ כלי דם — 2 / ~3,019 / **4.1.2026 (9 months)**
- לניאדו אנגיו — 2 / ~2,773 / 19.9
- רבקה זיו צנתורים — 2 / ~2,576 / 25.4
- נהריה צנתורים — 2 / ~2,466 / 8.8
- מאיר אנגיו — 2 / ~1,710 / 31.7
- לניאדו כלי דם — 1 / ~1,569 / **4.1.2026**
- הדסה ח.נ כלי דם — 1 / ~1,479 / 19.6
- העמק צנתורים — 1 / ~1,139 / 25.7
- הלל יפה ח.נ כלי דם — 3 / ~1,074 / 31.5
- העמק אנגיו — 1 / ~371 / 31.7
- כרמל צנתורים — 1 / ~351 / 31.8
- מאיר ח.נ כלי דם — 1 / ~346 / 30.9
- בלינסון כלי דם — 1 / ~269 / 30.9

Clean (nothing expired): **שערי צדק** (all 4 units collected 30.9 — verified against this report), קפלן צנתורים, הלל יפה צנתורים, בני ציון.

Data-quality flags in this report:
- **Negative quantity**: `D06` איכילוב, `SC14225030` lot `L93732`, exp 15.8, qty **-1**. A stock-count error — raise with logistics.
- **מאיר**: `STENT SMART CONTROL 7X40` lot `18356548` (exp 31.7) is still listed although it was
  reported collected on 23.9. Either it was not actually collected or the warehouse record was
  never updated. Verify before telling anyone it is closed.
- **כרמל**: the 3 expired items that the 23.8 visit was supposed to collect are all still listed.
