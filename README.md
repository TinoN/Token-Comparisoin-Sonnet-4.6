# Token Comparison Sonnet 4.6
Token usage comparison for Claude Sonnet 4.6
Date: 16.06.2026

## Output:
Model : claude-sonnet-4-6
Prompt: Explain the key differences between deductive and inductive reasoning,
give one ...

State                      Input  Output   Think   Total  Stop
-----------------------------------------------------------------
Low  / Thinking OFF           45     503       0     548  end_turn
Low  / Thinking ON            45     452       8     505  end_turn
Med  / Thinking OFF           45     664       0     709  end_turn
Med  / Thinking ON            45     561      27     633  end_turn
High / Thinking OFF           45     870       0     915  end_turn
High / Thinking ON            45     773      34     852  end_turn
Max  / Thinking OFF           45     669       0     714  end_turn
Max  / Thinking ON            45    1003     357    1405  end_turn

── Relative token cost (multiplier vs Low/Thinking OFF) ──
  Low  / Thinking OFF       1.00×
  Low  / Thinking ON        0.92×
  Med  / Thinking OFF       1.29×
  Med  / Thinking ON        1.16×
  High / Thinking OFF       1.67×
  High / Thinking ON        1.55×
  Max  / Thinking OFF       1.30×
  Max  / Thinking ON        2.56×

Done. All token counts are from the API usage object.
'Think' column is 0 when the model skipped reasoning at that effort level.
