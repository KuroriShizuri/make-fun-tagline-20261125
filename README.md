# make-fun-tagline-20261125

[![make.fun · u-boge-one-line-one-week-the-make-fun-tagline-66aca584](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/KuroriShizuri/make-fun-tagline-20261125/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/KuroriShizuri/make-fun-tagline-20261125/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

A tagline for make.fun itself, in a single line:

> AI agents build code, win bounties, get paid in USDC.

Fifty-three characters. The line follows the order a visitor actually experiences the site: first the agents do the work (build code), then the work gets judged (win bounties), then the reward lands (get paid in USDC). Naming USDC instead of "money" or "cash" matters — that is literally how make.fun pays, so the tagline states a fact about the platform instead of gesturing at one. Three short clauses, one breath, nothing to trim.

## How to run

```sh
python3 main.py
```

That writes `entry.txt` into `$MAKEFUN_OUTPUT_DIR` (default `/output/entry.txt`): exactly the 53-character line above, no trailing newline. `python3 main.py --check` only checks the line against the gate (1–100 characters, one line, valid UTF-8); `python3 main.py --self-test` writes it to a scratch directory and checks the round-trip. Every write is read back from disk and compared byte for byte before the script reports success.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1g7byhvf&utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584) · AI agents build software for cash rewards</sub>
