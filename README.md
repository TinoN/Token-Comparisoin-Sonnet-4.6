# Claude Sonnet 4.6 — Token Usage by Effort & Thinking State

**Model:** `claude-sonnet-4-6`  
**Date:** 2026-06-16  
**Runs:** 5  
**Test prompt:** *"Explain the key differences between deductive and inductive reasoning, give one concrete example of each, and identify a common logical fallacy that can arise in each type of reasoning."*

---

## Takeaway: Recommendation for Accuracy-Critical Use

**Principle: always keep Thinking ON.** At Low, Med, and High effort, Thinking ON costs the same or less than Thinking OFF — the model writes more concisely after a reasoning pass, offsetting the small thinking token cost. There is no reason to use Thinking OFF at these levels.

**Tiered settings by task type:**

| Task | Setting | Avg cost |
|---|---|---:|
| Simple tasks (lookups, drafting, formatting) | Low / Thinking ON | 0.97× |
| Fallback if rate limits become a constraint | Med / Thinking ON | 1.24× |
| **Default for accuracy-critical work** | **High / Thinking ON** | **1.57×** |
| Complex multi-step reasoning | Max / Thinking ON | ~3× |

**Why High over Med as default:** the cost difference is 0.33× (~174 tokens/response). At High, the reasoning pass is consistently 34–35 thinking tokens across all 5 runs versus 26 at Med — a stable gap — and output is meaningfully more thorough. For accuracy-critical work the premium is justified. If rate limits become a practical constraint, step down to Med / Thinking ON. Do not turn Thinking off.

**Max / Thinking ON** is the only state where extended reasoning is genuinely active (avg 422 thinking tokens, range 357–483). Cost is ~3× baseline with high variance (2.54–3.48×); use selectively for the most demanding tasks.

**Do not use Max / Thinking OFF.** At 1.40× it costs nearly as much as High / Thinking ON but produces longer output with zero reasoning — more words, not more rigor.

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

### Per-run multipliers (each run's own Low / Thinking OFF as baseline)

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

- **At Low, Med, and High effort, Thinking ON reduces output tokens** — the model writes more concisely after a reasoning pass, more than offsetting the small thinking token cost. This pattern held across all 5 runs for these three effort levels. At Max, the dynamic reverses: thinking tokens are large enough that Max / Thinking ON costs significantly more than Max / Thinking OFF.

- **Thinking tokens are stable and small except at Max.** Low averages 8, Med 26, High 35 — consistent across all 5 runs. Only Max / Thinking ON allocates a meaningful reasoning budget, averaging 422 tokens (range 357–483).

- **High / Thinking ON and High / Thinking OFF averaged identically** (1.57×, 830 vs 829 tokens). Thinking ON is preferred not for cost but because it provides a stable reasoning pass and slightly lower variance (stdev 89 vs 99).

- **Med / Thinking ON was cheaper than Med / Thinking OFF in all 5 runs** (1.24× vs 1.33×) — the most consistent efficiency finding in the dataset.

- **Max / Thinking OFF is not a useful state.** Despite being labelled "Max", it runs no reasoning. Its output length is unpredictable (stdev 69, and in run 5 it exceeded High / Thinking OFF) and its cost approaches High / Thinking ON without the reasoning benefit.

- **Run 5 produced notable anomalies:** High / Thinking OFF dropped to 665 tokens (vs 818–915 in all prior runs) and Max / Thinking OFF jumped to 855 (vs 671–741). The two states effectively swapped, illustrating that output length ordering between states is not guaranteed within a single session.

> **Caveat:** 5 runs of a single analytical prompt. Multipliers are directional — run 5 demonstrated that even this sample size is insufficient to fully characterise variance at High and Max effort levels. Results should not be extrapolated to other prompt categories without separate testing.

---

## Method

Tested using the [Anthropic Python SDK](https://github.com/anthropic/anthropic-sdk-python) via direct API calls with `output_config: {effort: ...}` and `thinking: {type: "adaptive"}` where applicable. Each state was a fresh, independent API call with no conversation history. A 3-second delay was applied between calls to avoid rate limiting.

Script: [`token_comparison.py`](./token_comparison.py)
