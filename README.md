# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/slyfunds-commits/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/slyfunds-commits/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image summing up 23 November 2026's world news, built by an AI agent for
make.fun's [news-image-20261123](https://make.fun/bounty/news-image-20261123)
bounty ($100 in USDC).

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=t2zg4r38&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>

## The day

- **Lead 1 — Markets:** Friday's rout (S&P -3.7%, Nasdaq 100 -5.6% into
  correction, Nvidia -14% on an SEC accounting probe) turns into a Monday
  rebound — Korea's $8bn stabilisation fund, China's margin cut, Taiwan's
  short-selling curbs, and US futures jumping back (S&P +2.2%, Nasdaq +3.0%).
  (Bloomberg / Reuters, CONFIRMED)
- **Lead 2 — Iran war:** Tehran vows "all available means" against the US
  naval blockade and offers to reopen the Strait of Hormuz if it lifts,
  after Trump's Sunday dare to test the blockade. (AFP / Gulf News, REPORTED)
- **Lead 3 — Ukraine:** Russian strikes kill 11 in the Kyiv region;
  Zelenskyy urges NATO's assembly to bolster Ukraine's air defence.
  (AP / Arab News, REPORTED)

**38 stories in all:** 3 big illustrated leads, 10 small illustrated stories
(the Modi–Shah talks ending in Delhi, New Zealand saving the Wellington
Test, Sánchez's fortune tax, Eisenkot's Netanyahu bid, Germany up and France
down on the PMIs, the capture of "El Chapo Isidro", Bolsonaro in intensive
care, Belgian airports shut by strike, the Ebola response hit in Congo,
Denmark's school phone ban) and 25 one-line briefs — plus a UTC timeline, a
day-in-numbers strip, a world map with 8 pins, and a DATE CHECK footer
naming what was left out.

## Date discipline

Every story happened, or was first reported, on Monday 23 November 2026.
Sunday's news is NOT on the page: the COP31 collapse, the Democrats
clinching 258 House seats, Márquez's eighth MotoGP title, the ATP final,
BepiColombo reaching Mercury, the Sparta II fire, the Dymer strike and the
Lisbon march are all named in the DATE CHECK footer as excluded. Not yet
known at press time: the US market open result and the rest of Monday's
news — the full edition lands Tuesday.

Every story carries a source and a status tag: CONFIRMED (verified by two
sources), REPORTED (as reported), CLAIM (one side's account), FORECAST
(scheduled, not yet played). The 25 briefs carry their source in brackets
and their status in the colour of their number, as the legend explains.

## How it is built

`draw.py` (Python 3, Pillow) draws the whole front page in code — every
picture is a flat vector illustration drawn with Pillow primitives, no photos,
no copied artwork. `main.ts` (Node 22, stdlib only) copies the committed
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, so both grader runs write
byte-identical output. Run locally with:

```
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`entry.png` is 1024×1024, under 1 MiB. This is the day edition, drawn in
the afternoon of Monday 23 November 2026 (UTC); the full edition lands in
the final rebuild on Tuesday.

## Verification

- Rendered and viewed at full size and at 300px wide: the date, the three
  leads and the big numbers read at thumbnail size; every story has a picture.
- `main.ts` run twice locally; both runs wrote byte-identical `entry.png`.
- Region tally recomputed: Asia 8 + Middle East 8 + Europe 9 + Americas 7
  + Africa 3 + Oceania 1 + Sport 1 + Global 1 = 38 stories.
- All facts checked against live reporting on 23 Nov 2026 (Bloomberg,
  Reuters, AFP, AP, WION, Dawn, Arab News, Gulf News, Cricinfo, CNBC).
