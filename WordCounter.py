## Counts the number of times a word is used in a text file.
## dict.txt must be in same directory as this script.
##     Consists of unique words seperated by commas.
## sample.txt must be in same directory as this script.
##     Sample text file.
##
## Written by Will Fidrych. Spring 2016.
## Written in IDLE, tested on Python 3.5.1, Windows 7


# Specify removed characters in last maketrans arg. 
removals = str.maketrans("","",".,()")

## Create a list composed of [string,integer] pairs.
dictList = []
with open("dict.txt") as dict:
    text = dict.read()
    words = text.split(",")
    for i in range(len(words)):
        dictList.append([words[i],0])
dict.close()

## Read in the entire sample text file
with open("sample.txt") as sample:
    text = sample.read()
    words = text.split(" ")
    # Iterate through text.
    for i in range(len(words)):
        words[i] = words[i].lower()
        words[i] = words[i].translate(removals)
        # Iterate through dictionary for a match.
        for entry in dictList:
            if (entry[0] == words[i]):
                entry[1] = entry[1] + 1

## Print the resulting list of dictionary entries with non-zero count.
for entry in dictList:
    if (entry[1] > 0):
        print(entry[0] + ': ' + str(entry[1]))

