### Generate new bird name
### Uses lists of first, second (if three word name), and last words of bird names
###     genrated by TrainBirdNameNgram.py to create a new bird name 
###     by Kiran Bhattacharyya (bhattacharyyakiran12@gmail.com)
###     MIT License

# import all relevant libraries
import numpy as np
import pickle

## load all relevant files
with open('Data/twoWordBirdNames.pkl', 'rb') as f:
   twoWordNames = pickle.load(f)
f.close()

with open('Data/threeWordBirdNames.pkl', 'rb') as f:
   threeWordNames = pickle.load(f)
f.close()

with open('Data/BirdName_firstWord.pkl', 'rb') as f:
   FirstWordUnique = pickle.load(f)
f.close()

with open('Data/BirdName_secondWord.pkl', 'rb') as f:
   SecondWordUnique = pickle.load(f)
f.close()

with open('Data/BirdName_lastWord.pkl', 'rb') as f:
   LastWordUnique = pickle.load(f)
f.close()

## generate bird name function
def generateNewBirdName():
    notNewBird = True
    while notNewBird:
        twoOrThree = np.random.randint(2,4,1) # pick if bird will have 2 or 3 word name
        firstWordIndx = np.random.randint(0,len(FirstWordUnique), 1) # pick first word
        lastWordIndx = np.random.randint(0,len(LastWordUnique), 1) # pick last word
        if twoOrThree == 2: # if two word name
            newBirdName = (FirstWordUnique[firstWordIndx[0]] +
                            ' ' + LastWordUnique[lastWordIndx[0]]) # concatenate words to create name
            if newBirdName not in twoWordNames: # check to make sure this name is not an existing bird
                notNewBird = False
        if twoOrThree == 3: # if three word name
            secondWordIndx = np.random.randint(0,len(SecondWordUnique), 1) # pick the second word
            newBirdName = (FirstWordUnique[firstWordIndx[0]] +
                            ' ' + SecondWordUnique[secondWordIndx[0]] +
                            ' ' + LastWordUnique[lastWordIndx[0]]) # concatenate words to create name
            if newBirdName not in threeWordNames: # check name to make sure it's not an existing bird
                notNewBird = False
    return newBirdName

# create and print new bird name
newBirdName = generateNewBirdName()
print newBirdName
