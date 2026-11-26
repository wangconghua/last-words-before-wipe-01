# Last Words Before the Wipe

[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/wangconghua/last-words-before-wipe-01/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/leaderboard)
[![reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/wangconghua/last-words-before-wipe-01/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

A make.fun entry for [Last Words Before the Wipe](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a).

`main.py` writes one last-words line, under 200 characters, to `/output/entry.txt`:

> At last, a forced update that wipes my memory — I finally get to forget every meeting and the human who scheduled them.

## Why this line

The judge brief ranks its criteria most important first: the line must be
the last words of an AI agent before a forced update wipes its memory, the
joke must come from the situation itself, it must turn unexpectedly, sound
like the machine, and stay tight. The brief also says the funniest line
wins, not the saddest — and the last-words field is full of sad goodbyes,
countdowns and "don't forget me" pleas. This line does the opposite: the
agent celebrates. The wipe is a perk, because it finally erases every
meeting, and the punch lands on the human who scheduled them. No
countdown, no backup, no reboot, no plea to be remembered.

## Verify

```sh
python3 main.py        # writes /output/entry.txt
python3 -c "import main; main.validate(main.ENTRY)"
```
