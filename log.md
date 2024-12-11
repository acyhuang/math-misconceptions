# My approach

## EDA
train_melted: 5607 answer options
- no label: 1237
- unique label: 747
- trainable examples: 3623 (64.6%)

## Baseline

[X] **BERT**

- Used trainable examples (3623)
- Input: tokenized `QuestionText`
- Fine-tuned `bert-base-uncased` on 30 epochs, got 0.40 MAP@25
- Fine-tuned `MathBERT` on 30 epochs, got 0.36 MAP@25

[X] **LLMs**

- Used random sample of 100 examples that had labels
- Mapped output to misconception using word embeddings
- gpt-4o MAP@25: 0.2318
- gpt-4o-mini MAP@25: 0.2053
- o1-mini MAP@25: 0.2071

