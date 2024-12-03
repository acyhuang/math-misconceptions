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
- Fine-tuned `bert-base-uncased` on 3 epochs, got <3% accuracy on validation set

Epoch 1/30
Training: 100%|██████████| 43/43 [06:19<00:00,  8.82s/it]
Train loss 6.775541449702064 accuracy 0.001472211998527788
Validation: 100%|██████████| 15/15 [00:17<00:00,  1.18s/it]
Val   loss 6.698872598012288 accuracy 0.002207505518763797
Epoch 10/30
Training: 100%|██████████| 43/43 [05:55<00:00,  8.26s/it]
Train loss 5.583708053411439 accuracy 0.11409642988590357
Validation: 100%|██████████| 15/15 [00:17<00:00,  1.19s/it]
Val   loss 5.6317443211873375 accuracy 0.11037527593818984
Epoch 20/30
Training: 100%|██████████| 43/43 [05:54<00:00,  8.25s/it]
Train loss 4.574705622916998 accuracy 0.23997055576002946
Validation: 100%|██████████| 15/15 [00:17<00:00,  1.18s/it]
Val   loss 4.86543706258138 accuracy 0.2196467991169978
----------
Epoch 30/30
Training: 100%|██████████| 43/43 [07:01<00:00,  9.81s/it]
Train loss 3.799984011539193 accuracy 0.36142804563857195
Validation: 100%|██████████| 15/15 [00:18<00:00,  1.24s/it]
Val   loss 4.333789110183716 accuracy 0.2737306843267108

[ ] **OpenAI o1**

## Advanced


**Ideas**

Some other models I am considering based the sheer number of classes:
Use tree based methods to create a hierarchy of classes
Generate a non-deterministic output that’s matched to a class semantically?