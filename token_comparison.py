"""
Token usage comparison across all 8 effort/thinking states for Claude Sonnet 4.6.

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."
    python token_comparison.py

Paste your test prompt inside TEST_PROMPT below, or pass it as a command-line argument:
    python token_comparison.py "Your prompt here"
"""

import anthropic
import sys
import time

# ── Configure your test prompt here ──────────────────────────────────────────
TEST_PROMPT = """
Explain the key differences between deductive and inductive reasoning,
give one concrete example of each, and identify a common logical fallacy
that can arise in each type of reasoning.
"""
# ─────────────────────────────────────────────────────────────────────────────

MODEL = "claude-sonnet-4-6"

# The 8 states: (label, effort, thinking_on)
STATES = [
    ("Low  / Thinking OFF", "low",    False),
    ("Low  / Thinking ON",  "low",    True),
    ("Med  / Thinking OFF", "medium", False),
    ("Med  / Thinking ON",  "medium", True),
    ("High / Thinking OFF", "high",   False),
    ("High / Thinking ON",  "high",   True),
    ("Max  / Thinking OFF", "max",    False),
    ("Max  / Thinking ON",  "max",    True),
]

# Delay between API calls to avoid rate-limit errors (seconds)
DELAY_BETWEEN_CALLS = 3


def run_state(client, prompt, effort, thinking_on):
    kwargs = {
        "model": MODEL,
        "max_tokens": 4096,
        "output_config": {"effort": effort},
        "messages": [{"role": "user", "content": prompt}],
    }

    if thinking_on:
        kwargs["thinking"] = {"type": "adaptive"}

    response = client.messages.create(**kwargs)
    usage = response.usage

    # thinking_tokens is only present when thinking actually ran
    thinking_tokens = getattr(usage, "thinking_input_tokens", 0) or 0

    # Some SDK versions surface thinking tokens differently
    # Try the content blocks as a fallback
    if thinking_tokens == 0 and thinking_on:
        for block in response.content:
            if getattr(block, "type", None) == "thinking":
                # Rough estimate: count characters / 4
                thinking_tokens = len(getattr(block, "thinking", "")) // 4
                break

    return {
        "input_tokens":    usage.input_tokens,
        "output_tokens":   usage.output_tokens,
        "thinking_tokens": thinking_tokens,
        "total_tokens":    usage.input_tokens + usage.output_tokens + thinking_tokens,
        "stop_reason":     response.stop_reason,
    }


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else TEST_PROMPT.strip()

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

    print(f"\nModel : {MODEL}")
    print(f"Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}\n")
    print(f"{'State':<24} {'Input':>7} {'Output':>7} {'Think':>7} {'Total':>7}  Stop")
    print("-" * 65)

    results = []

    for label, effort, thinking_on in STATES:
        try:
            data = run_state(client, prompt, effort, thinking_on)
            results.append((label, data))
            print(
                f"{label:<24} "
                f"{data['input_tokens']:>7} "
                f"{data['output_tokens']:>7} "
                f"{data['thinking_tokens']:>7} "
                f"{data['total_tokens']:>7}  "
                f"{data['stop_reason']}"
            )
        except anthropic.APIError as e:
            print(f"{label:<24} ERROR: {e}")
        except Exception as e:
            print(f"{label:<24} ERROR: {e}")

        time.sleep(DELAY_BETWEEN_CALLS)

    # Summary: relative cost multipliers vs Low/Thinking OFF baseline
    if results:
        baseline_total = results[0][1]["total_tokens"]
        print("\n── Relative token cost (multiplier vs Low/Thinking OFF) ──")
        for label, data in results:
            if baseline_total > 0:
                multiplier = data["total_tokens"] / baseline_total
                print(f"  {label:<24}  {multiplier:.2f}×")

    print("\nDone. All token counts are from the API usage object.")
    print("'Think' column is 0 when the model skipped reasoning at that effort level.")


if __name__ == "__main__":
    main()
