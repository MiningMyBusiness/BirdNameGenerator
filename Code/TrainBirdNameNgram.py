### Train Bird Name Ngram model
### Uses wikipedia list of common names (not scienctific) of birds from around the world
###     to extract data about the first, second (if three word name), and last words in
###     bird names.
###     by Kiran Bhattacharyya (bhattacharyyakiran12@gmail.com)
###     MIT License


# import all relevant libraries
import wikipedia
import nltk
import numpy as np
import matplotlib.pyplot as plt
import pickle

## get data from wikipedia page of birds
wikiPage = wikipedia.page("List of birds by common name")

## grab content from page
content = wikiPage.content

## split content by new line character
contentSplit = content.split("\n")

## grab bird names and avoid other page content
birdNames = contentSplit[7:5352]

## filter bird names to not include empty slots or list headings
birdNames_filt = list()
for name in birdNames:
    if "==" not in name and len(name) > 0:
        birdNames_filt.append(name)

## get length of names in words
nameLengths = list()
for name in birdNames_filt:
    name = name.lower()
    wordList = nltk.word_tokenize(name)
    nameLengths.append(len(wordList))

## names that 2 - 3 words long are most common
## uncomment the following lines to find out for yourself
## nameArray = np.array(nameLengths)
## plt.hist(nameArray)
## plt.show()

## break bird names into two word and three word names
twoWordNames = list()
threeWordNames = list()
for name in birdNames_filt:
    name = name.lower()
    wordList = nltk.word_tokenize(name)
    if len(wordList) == 2:
        twoWordNames.append(name)
    if len(wordList) == 3:
        threeWordNames.append(name)

## get words by order
firstWord = list() # for both two and three word names
threeWord_2ndWord = list()
lastWord = list()
for name in twoWordNames:
    wordList = nltk.word_tokenize(name)
    firstWord.append(wordList[0])
    lastWord.append(wordList[1])
for name in threeWordNames:
    wordList = nltk.word_tokenize(name)
    firstWord.append(wordList[0])
    threeWord_2ndWord.append(wordList[1])
    lastWord.append(wordList[2])

## reduce list to only unique words
FirstWordUnique = list()
SecondWordUnique = list()
LastWordUnique = list()
for word in firstWord:
    if word not in FirstWordUnique:
        FirstWordUnique.append(word)
for word in threeWord_2ndWord:
    if word not in SecondWordUnique:
        SecondWordUnique.append(word)
for word in lastWord:
    if word not in LastWordUnique:
        LastWordUnique.append(word)

## save all lists to file
with open('Data/twoWordBirdNames.pkl', 'wb') as f:
   pickle.dump(twoWordNames, f)
f.close()

with open('Data/threeWordBirdNames.pkl', 'wb') as f:
   pickle.dump(threeWordNames, f)
f.close()

with open('Data/BirdName_firstWord.pkl', 'wb') as f:
   pickle.dump(FirstWordUnique, f)
f.close()

with open('Data/BirdName_secondWord.pkl', 'wb') as f:
   pickle.dump(SecondWordUnique, f)
f.close()

with open('Data/BirdName_lastWord.pkl', 'wb') as f:
   pickle.dump(LastWordUnique, f)
f.close()
