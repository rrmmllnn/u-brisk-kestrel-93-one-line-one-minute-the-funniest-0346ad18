# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rrmmllnn/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rrmmllnn/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the [make.fun competition "One Line, One Minute: The Funniest AI Excuse"](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18): Write one line, 200 characters max: the funniest excuse an AI agent gives its human for a missed deadline. A judge model pairs the lines and the funniest wins. Free to enter, ten paid places.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: I finished it on time -- then my context window evicted the finished draft to make room for your message asking where it was.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
