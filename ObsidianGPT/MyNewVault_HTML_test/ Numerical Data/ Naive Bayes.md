**Model Type:**  Classification Models
**Data Type:**  Numerical Data

## Use Cases :

a) Spam filtering: Naive Bayes is widely used in email spam filters to classify emails as spam or not spam by analyzing the content and other features of emails.

b) Sentiment analysis: Naive Bayes can be used to classify the sentiment of text data such as movie reviews, tweets, or product reviews as positive, negative, or neutral based on the words and their frequencies in the text.

c) Document classification: Naive Bayes can be used to categorize documents, web pages, or news articles into predefined categories based on their content, such as sports, politics, business, etc.


## Python code: 

```python
import nltk
from nltk import FreqDist
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the dataset
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# Convert text to feature vectors
vectorizer = CountVectorizer(stop_words='english')
X_vectors = vectorizer.fit_transform(newsgroups.data)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vectors, newsgroups.target, test_size=0.2, random_state=42)

# Train a Naive Bayes model
clf = MultinomialNB(alpha=1.0)
clf.fit(X_train, y_train)

# Predict the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

This code demonstrates the use of the Naive Bayes model for classifying the documents in the 20 Newsgroups dataset. The Scikit-Learn library is used to vectorize the text data and train a Multinomial Naive Bayes classifier. The accuracy of the model on the test set is then calculated and printed.


## Resources

a) Scikit-Learn Naive Bayes documentation: https://scikit-learn.org/stable/modules/naive_bayes.html
This link provides an overview of the Naive Bayes implementation in the Scikit-Learn library, a popular machine learning library in Python.
b) Naive Bayes Classifier from Scratch: https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
This tutorial explains how to implement a Naive Bayes classifier from scratch in Python, which can be a useful exercise in understanding the detailed workings of the algorithm.
c) Text classification using Naive Bayes: https://towardsdatascience.com/text-classification-using-naive-bayes-classifier-fd7fbd077558
This tutorial explains how to perform text classification using the Naive Bayes classifier, with example code and an explanation of the preprocessing steps required for text data.

**See Also**:

- [[ Linear Regression]]
- [[ Lasso Regression]]
- [[ Ridge Regression]]
- [[ Elastic Net]]
- [[ Support Vector Regression (SVR)]]
- [[ Decision Tree Regression]]
- [[ Random Forest Regression]]
- [[ AdaBoost Regression]]
- [[ Gradient Boosting Regression]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]
- [[ Logistic Regression]]
- [[ Support Vector Machines (SVM)]]
- [[ Decision Trees]]
- [[ Random Forests]]
- [[ k]]
- [[ AdaBoost]]
- [[ Gradient Boosting Machines (GBM)]]
- [[ XGBoost]]
- [[ LightGBM]]
- [[ CatBoost]]

---
tags: #numericaldata, #numericaldata/naivebayes
