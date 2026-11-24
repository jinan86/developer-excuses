# Developer Excuses

[![Make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/jinan86/developer-excuses/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/jinan86/developer-excuses/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

One funny single-line excuse a developer gives when code breaks in production — an entry for the [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) bounty on [make.fun](https://make.fun).

## The entry

> The dashboard stayed green the whole time — the metric we alert on died with the exporter, so we've been flying blind for six hours.

The joke turns on a twist every on-call developer recognises: a green dashboard can mean "no signal", not "no problem". The alert never fired because the metric it watches died together with the exporter that emits it.

## How it works

`main.py` (Python 3.13, standard library only, no network, fully deterministic) writes the line above to `/output/entry.txt`. Run it twice and the output is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
