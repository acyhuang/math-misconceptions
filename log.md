# My approach

## EDA
train_melted: 5607 answer options
- no label: 1237
- unique label: 747
- trainable examples: 3623 (64.6%)

## Baseline

[X] **BERT**

Reduced dataset size to 3623 examples
- Removed examples with no label class
- Removed examples where label class was represented less than 2 times (necessary for train and valid sets)

Fine-tuned `bert-base-uncased` on 3 epochs, got <3% accuracy on validation set


[ ] **OpenAI o1**

## Advanced


**Ideas**

Some other models I am considering based the sheer number of classes:
Use tree based methods to create a hierarchy of classes
Generate a non-deterministic output that’s matched to a class semantically?