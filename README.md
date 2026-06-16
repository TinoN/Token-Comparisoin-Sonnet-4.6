# Claude Sonnet 4.6 — Token Usage by Effort & Thinking State

**Model:** `claude-sonnet-4-6`  
**Date:** 2026-06-16  
**Runs:** 5  
**Test prompt:** *"Explain the key differences between deductive and inductive reasoning, give one concrete example of each, and identify a common logical fallacy that can arise in each type of reasoning."*

---

## Takeaway: Recommendation for Accuracy-Critical Use

**Use High / Thinking ON as your default.**

- Costs the same as High / Thinking OFF on average (both 1.57× baseline), but Thinking ON means the model runs a reasoning pass before responding — consistently 34–35 thinking tokens across all 5 runs, regardless of output variance
- The reasoning pass is modest at High effort, but it is real and stable; it is absent entirely at Low and Med
- High / Thinking OFF has slightly higher variance (stdev 99 vs 89), making High / Thinking ON marginally more predictable in addition to providing reasoning

**Switch to Max / Thinking ON for genuinely complex tasks** — multi-step logical problems, anything where you have previously noticed quality gaps. Accept that it costs ~3× the baseline with a wide variance (2.54–3.48×). It is the only state where extended reasoning is meaningfully active (avg 422 thinking tokens).

**Do not use Max / Thinking OFF.** It produces longer output without any reasoning — more words, not more rigor. At 1.40× average cost, it is nearly as expensive as High / Thinking ON while offering none of the reasoning benefit.

---

## Averaged Results (5 runs)

| State | Avg Output | Avg Think | Avg Total | Min | Max | Stdev |
|---|---:|---:|---:|---:|---:|---:|
| Low / Thinking OFF | 484 | 0 | 529 | 508 | 548 | 15 |
| Low / Thinking ON | 460 | 8 | 514 | 504 | 522 | 9 |
| Med / Thinking OFF | 660 | 0 | 705 | 634 | 768 | 52 |
| Med / Thinking ON | 585 | 26 | 656 | 598 | 719 | 50 |
| High / Thinking OFF | 784 | 0 | 829 | 665 | 915 | 99 |
| High / Thinking ON | 750 | 35 | 830 | 731 | 964 | 89 |
| Max / Thinking OFF | 696 | 0 | 741 | 671 | 855 | 69 |
| Max / Thinking ON | 1109 | 422 | **1576** | 1343 | 1812 | 210 |

---

## Relative Token Cost (5-run average, baseline = Low / Thinking OFF)

| State | Avg multiplier | Per-run range | Stdev (tokens) |
|---|---:|---|---:|
| Low / Thinking OFF | 1.00× | — | 15 |
| Low / Thinking ON | 0.97× | 0.92–1.03× | 9 |
| Med / Thinking OFF | 1.33× | 1.25–1.46× | 52 |
| Med / Thinking ON | 1.24× | 1.16–1.36× | 50 |
| High / Thinking OFF | 1.57× | 1.25–1.69× | 99 |
| High / Thinking ON | 1.57× | 1.44–1.83× | 89 |
| Max / Thinking OFF | 1.40× | 1.30–1.60× | 69 |
| Max / Thinking ON | **2.98×** | 2.54–3.48× | 210 |

### Per-run multipliers (each run's own Low/Thinking OFF as baseline)

| State | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
|---|---:|---:|---:|---:|---:|
| Low / Thinking OFF | 1.00× | 1.00× | 1.00× | 1.00× | 1.00× |
| Low / Thinking ON | 0.92× | 1.03× | 0.98× | 0.96× | 0.98× |
| Med / Thinking OFF | 1.29× | 1.25× | 1.39× | 1.46× | 1.27× |
| Med / Thinking ON | 1.16× | 1.18× | 1.36× | 1.21× | 1.30× |
| High / Thinking OFF | 1.67× | 1.61× | 1.69× | 1.63× | 1.25× |
| High / Thinking ON | 1.55× | 1.44× | 1.83× | 1.47× | 1.55× |
| Max / Thinking OFF | 1.30× | 1.32× | 1.40× | 1.38× | 1.60× |
| Max / Thinking ON | 2.56× | 3.48× | 2.54× | 2.96× | 3.39× |

---

## Raw Results

### Run 1

| State | Input | Output | Think | Total |
|---|---:|---:|---:|---:|
| Low / Thinking OFF | 45 | 503 | 0 | 548 |
| Low / Thinking ON | 45 | 452 | 8 | 505 |
| Med / Thinking OFF | 45 | 664 | 0 | 709 |
| Med / Thinking ON | 45 | 561 | 27 | 633 |
| High / Thinking OFF | 45 | 870 | 0 | 915 |
| High / Thinking ON | 45 | 773 | 34 | 852 |
| Max / Thinking OFF | 45 | 669 | 0 | 714 |
| Max / Thinking ON | 45 | 1003 | 357 | 1405 |

### Run 2

| State | Input | Output | Think | Total |
|---|---:|---:|---:|---:|
| Low / Thinking OFF | 45 | 463 | 0 | 508 |
| Low / Thinking ON | 45 | 469 | 8 | 522 |
| Med / Thinking OFF | 45 | 589 | 0 | 634 |
| Med / Thinking ON | 45 | 528 | 25 | 598 |
| High / Thinking OFF | 45 | 773 | 0 | 818 |
| High / Thinking ON | 45 | 651 | 35 | 731 |
| Max / Thinking OFF | 45 | 626 | 0 | 671 |
| Max / Thinking ON | 45 | 1271 | 453 | 1769 |

### Run 3

| State | Input | Output | Think | Total |
|---|---:|---:|---:|---:|
| Low / Thinking OFF | 45 | 483 | 0 | 528 |
| Low / Thinking ON | 45 | 463 | 8 | 516 |
| Med / Thinking OFF | 45 | 690 | 0 | 735 |
| Med / Thinking ON | 45 | 649 | 25 | 719 |
| High / Thinking OFF | 45 | 848 | 0 | 893 |
| High / Thinking ON | 45 | 884 | 35 | 964 |
| Max / Thinking OFF | 45 | 696 | 0 | 741 |
| Max / Thinking ON | 45 | 910 | 388 | 1343 |

### Run 4

| State | Input | Output | Think | Total |
|---|---:|---:|---:|---:|
| Low / Thinking OFF | 45 | 480 | 0 | 525 |
| Low / Thinking ON | 45 | 451 | 8 | 504 |
| Med / Thinking OFF | 45 | 723 | 0 | 768 |
| Med / Thinking ON | 45 | 564 | 25 | 634 |
| High / Thinking OFF | 45 | 809 | 0 | 854 |
| High / Thinking ON | 45 | 693 | 35 | 773 |
| Max / Thinking OFF | 45 | 678 | 0 | 723 |
| Max / Thinking ON | 45 | 1077 | 430 | 1552 |

### Run 5

| State | Input | Output | Think | Total |
|---|---:|---:|---:|---:|
| Low / Thinking OFF | 45 | 489 | 0 | 534 |
| Low / Thinking ON | 45 | 467 | 9 | 521 |
| Med / Thinking OFF | 45 | 633 | 0 | 678 |
| Med / Thinking ON | 45 | 622 | 28 | 695 |
| High / Thinking OFF | 45 | 620 | 0 | 665 |
| High / Thinking ON | 45 | 750 | 34 | 829 |
| Max / Thinking OFF | 45 | 810 | 0 | 855 |
| Max / Thinking ON | 45 | 1284 | 483 | 1812 |

*All token counts from the Anthropic API usage object. Think = 0 means the model skipped internal reasoning at that effort level. All runs returned `end_turn` as stop reason.*

---

## Observations

- **Low / Thinking OFF and ON are the most stable states** — by a wide margin. Stdev of 15 and 9 tokens respectively. Low / Thinking ON averaged 0.97× (3% cheaper), though it crossed above 1.00× in run 2. Over 5 runs the difference is negligible; treat them as equivalent in cost.

- **Thinking tokens are negligible except at Max.** Low averages 8 thinking tokens, Med 26, High 35 — stable across all 5 runs. Thinking token count at these levels is essentially fixed. Only Max / Thinking ON allocates a meaningful reasoning budget, averaging 422 tokens and ranging from 357 to 483.

- **High / Thinking OFF and High / Thinking ON converged to the same average** (both 1.57×, 829 and 830 tokens respectively). This is a meaningful result: enabling Thinking at High effort costs the same as disabling it, because the model compensates with shorter output. However, High / Thinking OFF has higher variance (stdev 99 vs 89), driven by run 5 producing only 665 total tokens — well below all other runs (818–915). Run 5 is a genuine outlier for this state.

- **Max / Thinking OFF showed an inverse anomaly in run 5** — 855 tokens vs 671–741 in all prior runs. High / Thinking OFF and Max / Thinking OFF effectively swapped positions in run 5, suggesting the model's output length for these two states is not reliably ordered. Over 5 runs, their averages (829 vs 741) reflect this instability.

- **Max / Thinking ON is the highest-cost and highest-variance state** (stdev 210, range 1343–1812). It is the only state where extended reasoning genuinely runs, but budget planning is difficult: any given session could cost anywhere from 2.54× to 3.48× of the Low baseline.

- **Med / Thinking ON is consistently cheaper than Med / Thinking OFF** across all 5 runs (1.24× vs 1.33× averaged). This held without exception and is the clearest efficiency finding: at Medium effort, enabling Thinking produces more concise output that more than offsets the small thinking token cost.

- **Practical takeaway:** If token predictability matters, use Low (either Thinking state). If you want reasoning depth at stable cost, High / Thinking ON and High / Thinking OFF are now statistically equivalent — choose based on output quality preference rather than token cost. Max / Thinking ON is the only state with active extended reasoning but requires accepting high cost variance.

> **Caveat:** These results are based on 5 runs of a single analytical prompt. Token counts are non-deterministic — run 5 produced a significant outlier for High / Thinking OFF (665 vs expected ~850) and Max / Thinking OFF (855 vs expected ~720), demonstrating that even 5 runs is insufficient to fully characterise variance at higher effort levels. Multipliers are directional for this prompt type and should not be extrapolated to other categories (creative writing, code generation, etc.) without separate testing.

---

## Method

Tested using the [Anthropic Python SDK](https://github.com/anthropic/anthropic-sdk-python) via direct API calls with `output_config: {effort: ...}` and `thinking: {type: "adaptive"}` where applicable. Each state was a fresh, independent API call with no conversation history. A 3-second delay was applied between calls to avoid rate limiting.

Script: [`token_comparison.py`](./token_comparison.py)
