Info from [Kaggle listing](https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics/overview)

# Overview

## Description

A Diagnostic Question is a multiple-choice question with four options: one correct answer and three distractors (incorrect answers). Each distractor is carefully crafted to capture a specific misconception. For example:

5 * 4 + 6 / 2

A: 23
B: 13
C: 25
D: 35

If a student selects the distractor "13," they may have the misconception "Carries out operations from left to right regardless of priority order."

Tagging distractors with appropriate misconceptions is essential but time-consuming, and it is difficult to maintain consistency across multiple human labellers. Misconceptions vary significantly in terms of description granularity, and new misconceptions are often discovered as human labellers tag distractors in new topic areas.

Initial efforts to use pre-trained language models have not been successful, likely due to the complexity of the mathematical content in the questions. Therefore, a more efficient and consistent approach is needed to streamline the tagging process and enhance the overall quality.

This competition challenges you to develop a Natural Language Processing (NLP) model driven by Machine L18
On Eedi, students answer Diagnostic Questions (DQs), which are multiple-choice questions featuring one correct answer and three incorrect answers, known as distractors. Each question targets a specific construct (also referred to as a skill), representing the most granular level of knowledge relevant to the question. Each distractor is designed to correspond with a potential misconception. Below is an example of a DQ:

In the diagram, AN : NB = 3 : 5.
AB = 48.
What is the distance AN?

A: 16
B: 30
C: 6
D: 18

In this example, the options for the question are labeled with misconceptions as follows:

A: Divides total amount by each side of the ratio instead of dividing by the sum of the parts
B: Mixes up sides of a ratio
C: Finds one part of a ratio but doesn't multiply that by the number of parts needed
D: Correct answer

The Diagnostic Questions were originally presented in image format, and the text, including mathematical content, has been extracted using a human-in-the-loop OCR process.

File and Field Information: 
- **\[train/test].csv**
  - `QuestionId` - Unique question identifier (int).
  - `ConstructId` - Unique construct identifier (int) .
  - `ConstructName` - Most granular level of knowledge related to question (str).
  - `CorrectAnswer` - A, B, C or D (char).
  - `SubjectId` - Unique subject identifier (int).
  - `SubjectName` - More general context than the construct (str).
  - `QuestionText` - Question text extracted from the question image using human-in-the-loop OCR (str) .
  - `Answer[A/B/C/D]Text` - Answer option A text extracted from the question image using human-in-the-loop OCR (str).
  - `Misconception[A/B/C/D]Id` - Unique misconception identifier (int). Ground truth labels in train.csv; your task is to predict these labels for test.csv.
- **misconception_mapping.csv** - maps MisconceptionId to its MisconceptionName
- **sample_submission.csv** - A submission file in the correct format.
  - `QuestionId_Answer` - Each question has three incorrect answers for which need you predict the MisconceptionId.
  - `MisconceptionId` - You can predict up to 25 values, space delimited.

## Evaluation

Submissions are evaluated according to the Mean Average Precision @ 25 (MAP@25):

\[
\text{MAP}@25 = \frac{1}{U} \sum_{u=1}^{U} \sum_{k=1}^{\min(n, 25)} P(k) \times \text{rel}(k)
\]

where 𝑈 is the number of observations, 𝑃(𝑘) is the precision at cutoff 𝑘, 𝑛 is the number predictions submitted per observation, and 𝑟𝑒𝑙(𝑘) is an indicator function equaling 1 if the item at rank 𝑘 is a relevant (correct) label, zero otherwise.

Once a correct label has been scored for an observation, that label is no longer considered relevant for that observation, and additional predictions of that label are skipped in the calculation. For example, if the correct label is A for an observation, the following predictions all score an average precision of 1.0.

[A, B, C, D, E]
[A, A, A, A, A]
[A, B, A, C, A]
There is only one correct label per observation (hence no divisor term in front of the inner summation.)

## Submission File

For each QuestionId_Answer row in the test set, you must predict the corresponding MisconceptionId. You can predict up to 25 MisconceptionId values per row, and these should be space-delimited. The file should contain a header and have the following format:

QuestionId_Answer,MisconceptionId
1869_A,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
1869_B,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
1869_C,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
1870_B,1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
...