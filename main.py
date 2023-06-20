import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
testFile = pd.read_csv('test.csv')
testData = testFile['Description'].tolist()
testLabel = testFile['Title'].tolist()


# Function removes punctuations
def removePunctuation(textRemovePun):
    textRemovePun = re.sub(r'[^\w\s]', '', textRemovePun)
    return textRemovePun


# Function removes stopwords using nltk generated stopwords
def removeStopwords(textRemoveStop):
    stopWords = set(stopwords.words('english'))
    tokens = word_tokenize(textRemoveStop)
    filteredTokens = [token for token in tokens if token.lower() not in stopWords]
    textRemoveStop = ' '.join(filteredTokens)
    return textRemoveStop


# Calls both functions for testData, to get label and description processed.

cleanTestData = []
for text in testData:
    cleanText = removePunctuation(text)
    cleanText = removeStopwords(cleanText)
    cleanTestData.append(cleanText)

cleanTestLabel = []
for label in testLabel:
    cleanLabel = removePunctuation(label)
    cleanLabel = removeStopwords(cleanLabel)
    cleanTestLabel.append(cleanLabel)

# Save data in csv file with Label, Description.
preprocessedFile = pd.DataFrame({'Label': cleanTestLabel, 'Description': cleanTestData})
preprocessedFile.to_csv('preprocessedDescriptions.csv', index=False)
