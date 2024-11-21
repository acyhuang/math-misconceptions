# My approach

**Baseline**

- [ ] Try BERT on the dataset.
- [ ] Try OpenAI o1 on a random sample of the dataset.

**Data processing**

- [ ] Clean, normalize, stem text.
- [ ] Create text representations using TF-IDF or word embeddings (Word2Vec?).
- [ ] Perform symbol analysis to extract math equations.

**Model and architecture**

I’ll likely start with a simple logistic regression model to get another baseline result. My guess is that this will do very poorly given that there are so many classes and not many examples of each class. 

Some other models I am considering based the sheer number of classes:
Use tree based methods to create a hierarchy of classes
Generate a non-deterministic output that’s matched to a class semantically?