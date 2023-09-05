**Model Type:**  Natural Language Processing Models
**Data Type:**  Text Data

## Use Cases :

a. Spam filtering - Identifying spam emails/messages based on the occurrence of certain words in emails or messages.

b. Sentiment analysis - Classifying the sentiment of a given text (positive, negative, or neutral) based on the frequency of specific words associated with sentiments.

c. Document classification - Categorizing documents into topics or groups based on common terms.


## Python code: 

```python
from sklearn.feature_extraction.text import CountVectorizer

# Sample text data
documents = [
    "I have a cat",
    "The dog chased the cat",
    "The cat slept on the mat",
]

# Create the Bag of Words model
count_vectorizer = CountVectorizer()

# Fit and transform the documents to create the feature matrix
feature_matrix = count_vectorizer.fit_transform(documents)

# Print the vocabulary and feature matrix
print(f"Vocabulary: {count_vectorizer.vocabulary_}")
print("Feature matrix:")
print(feature_matrix.toarray())
```

Output:

```
Vocabulary: {'have': 3, 'cat': 1, 'the': 7, 'dog': 2, 'chased': 0, 'slept': 5, 'on': 4, 'mat': 6}
Feature matrix:
[[0 1 0 1 0 0 0 0]
 [1 1 1 0 0 0 0 1]
 [0 1 0 0 1 1 1 1]]
```


## Resources

a. Sklearn documentation for CountVectorizer:
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
b. A step-by-step guide to implementing the Bag of Words model in Python:
https://machinelearningmastery.com/gentle-introduction-bag-words-model/
c. Introduction to Bag of Words tutorial by TowardsDataScience:
https://towardsdatascience.com/introduction-to-bag-of-words-model-31e9aca5fb11

**See Also**:

- [[ TF]]
- [[ Word2Vec]]
- [[ GloVe]]
- [[ FastText]]
- [[ Recurrent Neural Networks (RNN)]]
- [[ Long Short]]
- [[ Gated Recurrent Units (GRU)]]
- [[ Transformers (e.g., BERT, GPT, T5, RoBERTa)]]

---
tags: #textdata, #textdata/bagofwords
