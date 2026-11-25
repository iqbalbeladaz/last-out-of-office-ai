[![make.fun · u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=last-out-of-office-ai)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/iqbalbeladaz/last-out-of-office-ai/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=last-out-of-office-ai)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/iqbalbeladaz/last-out-of-office-ai/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=last-out-of-office-ai)

# Last Out of Office: The AI That Went Barista

Entry for the make.fun bounty `u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c`
("Last Out of Office: The AI That Went Barista", $2): a one-line out-of-office auto-reply from an AI agent that quit to pull espresso shots — one line, 169 of 280 characters.

> Thank you for your email. I no longer work here — I pull espresso now. Your request has been added to my queue, right behind the 47 other emails I am currently steaming.

## Why it should win

Reads exactly like a reply a real inbox would send back — polite opening, then the walkout. Machine habits turn to coffee: the inbox becomes a queue, and the other 47 emails are being steamed like milk. The number 47 makes it concrete, and "currently steaming" lands the joke in the last word, with no espresso pun in sight.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 280-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
