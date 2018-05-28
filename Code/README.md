# Code files overview 

### TrainBirdNameNgram.py
Pulls content for [list of birds by common name](https://en.wikipedia.org/wiki/List_of_birds_by_common_name) and parses names to create two lists of two- and three-word names of birds. These lists are then parsed to create three new lists of first, second (if three-word name), and last words for names. All lists are save as data files in the [Data](https://github.com/MiningMyBusiness/BirdNameGenerator/tree/master/Data) directory of the repo.

### birdNameGenerator.py
Loads in data files saved of two- and three-word names of birds alond with the first, second (if three-word name), and last words for names. Uses a monte-carlo method to generate a new name and checks to make sure this name doesn't already exist. 
