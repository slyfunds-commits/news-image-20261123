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

- **Lead 1 — Nepal–India:** Nepal PM Balendra Shah meets PM Modi in New Delhi
  on his first India visit since taking office in March — talks at Hyderabad
  House, a joint press conference and a luncheon. Kathmandu asks for a $2bn
  aid package and three new air routes. (MEA / Deccan Herald, FORECAST)
- **Lead 2 — Markets:** Asia braces for another rout after Wall Street's
  sell-off — Tokyo shut for a holiday, MSCI's Asia gauge 18% below its June
  peak, the Nasdaq 100 coming off its worst week since March 2020.
  (Bloomberg / The Edge, CONFIRMED)
- **Lead 3 — Iran war:** Trump tells Fox News he is "inclined" to resume
  strikes on Iran if no deal is reached by the New Year, and calls Iran's
  negotiators "professional tap dancers". (Fox News / Times Now, REPORTED)

**38 stories in all:** 3 big illustrated leads, 10 small illustrated stories
(Saar condemns the West Bank settler attacks, the CENTCOM chief ends his
Middle East tour, Pezeshkian denies a government rift, Tehran's mine claims
in Hormuz, Jordan's search for a missing sailor, the Houthi shelling of
Taiz, Fonterra's 22-million-litre milk dump, the final day in Wellington,
Modi on AI and skilled jobs, the IFFI BRICS roundtable) and 25 one-line
briefs — plus a UTC timeline, a day-in-numbers strip, a world map with 8
pins, and a DATE CHECK footer naming what was left out.

## Date discipline

Every story happened, or was first reported, on Monday 23 November 2026, or
is a Monday event marked FORECAST (the Modi–Shah talks, the Wellington final
day, the market opens). No prior-day story is on the page. The DATE CHECK
footer names what was excluded: the COP31 collapse, the ATP final (Alcaraz
beat Zverev 6-2, 7-6(7)), BepiColombo reaching Mercury, the Sparta II fire,
the Cikande fire update, the Dymer strike, South Korea's education minister
resigning, the India–China talks concluding, the Trump–Kim report, and the
Lisbon march — all Sunday's (or Saturday's) news. Not yet known at press
time: the US market open, the Modi–Shah outcome, and the Wellington result.

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

`entry.png` is 1024×1024, under 1 MiB. This is the early edition, drawn in
the first hour of Monday 23 November 2026 (UTC); the day's full paper lands
in the final rebuild on Tuesday.

## Verification

- Rendered and viewed at full size and at 300px wide: the date, the three
  leads and the big numbers read at thumbnail size; every story has a picture.
- `main.ts` run twice locally; both runs wrote byte-identical `entry.png`.
- Region tally recomputed: Asia 18 + Middle East 12 + Europe 2 + Americas 3
  + Oceania 2 + Sport 1 = 38 stories.
- All facts checked against live reporting on 23 Nov 2026 (Bloomberg, The
  Edge, Deccan Herald, MEA, NDTV, RNZ, Times Now, Fox News, Cricinfo,
  Reuters, AFP, AP).
