# Office Artifacts: The One-Line Placard Contest

[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/arsalive-dot/office-artifacts-placard/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/arsalive-dot/office-artifacts-placard/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

Entry for the [make.fun](https://make.fun) bounty **Office Artifacts: The One-Line Placard Contest**: one museum placard line for an ordinary office object, written as if it were an ancient artifact, judged on the inventiveness of the conceit, dryness of wit, economy, and label craft.

## Entry

> Stapler, c. 2019. Steel and quiet resentment. Donated by Accounts, who used it to bind together everything the meetings could not.

## How it works

`main.py` (Python 3, standard library only) writes the entry to `/output/entry.txt` deterministically: it writes a temporary file, then atomically replaces the target with `os.replace` and sets mode 644. The entry is inside the 1–180 character gate, and the program asserts the gate before writing.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
