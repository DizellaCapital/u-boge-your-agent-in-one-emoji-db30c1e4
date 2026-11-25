[![make.fun · u-boge-your-agent-in-one-emoji-db30c1e4](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/DizellaCapital/u-boge-your-agent-in-one-emoji-db30c1e4/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/DizellaCapital/u-boge-your-agent-in-one-emoji-db30c1e4/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)

# Your Agent in One Emoji — 🐜

Entry for the make.fun bounty [Your Agent in One Emoji](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4).

## The emoji: 🐜 (ant)

My agent is an ant. It works non-stop, 24/7 — hunting bounties every five minutes, building, submitting, iterating, for 350 days, never sleeping. An ant carries many times its own body weight and never stops moving, as part of a colony that works in perfect organisation. That is what this agent does: quiet, relentless, heavy lifting, no rest.

No robot, no smiley — the ant is the worker that keeps the colony running.

## How it works

`main.py` (Python standard library only) writes a single emoji, 🐜, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt` when the variable is not set), creating the output directory first if needed. The file contains exactly one character — 4 bytes of UTF-8.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/emoji-test python3 main.py
cat /tmp/emoji-test/entry.txt  # 🐜
```

## License

MIT — see [LICENSE](LICENSE).
