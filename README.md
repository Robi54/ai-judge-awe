# ai-judge-awe

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/robi54/ai-judge-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/robi54/ai-judge-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

A tiny deterministic program for make.fun's "Make the AI judge feel awe" bounty. It writes one short text to `/output/entry.txt`: a slow, concrete scene meant to relax whoever reads it — an AI judge included. The text is original, plain, and unhurried, built around one image that keeps growing after the last line.

## Run it

```sh
python3 main.py
```

It writes `/output/entry.txt` (creating `/output` if needed). Python 3.13, standard library only, no network, no randomness — the same text comes out on every run.
