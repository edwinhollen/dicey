from os import listdir, urandom
from os.path import isfile, join
from random import randint, seed
from sys import argv

wordListsPath = './wordlists/'

def main(words):
    seed(int.from_bytes(urandom(8), byteorder="big"))
    wordLists = getWordLists()
    phrase = ""
    for i in range(words):
        # dice rolls
        rolls = ''
        for i in range(5):
            rolls += str(randint(1, 6))
        phrase += str(wordLists[rolls][randint(0, len(wordLists[rolls])-1)]) + " "
    print(phrase)


def getWordListPaths():
    paths = []
    for name in listdir(wordListsPath):
        fullPath = join(wordListsPath, name)
        if isfile(fullPath):
            paths.append(fullPath)
    return paths

def getWordLists():
    words = {}
    for wordListPath in getWordListPaths():
        with open(wordListPath, "r") as wordList:
            for line in wordList:
                line = line.replace('\n', "")
                split = line.split("\t", 1)
                if split[0] not in words:
                    words[split[0]] = []
                words[split[0]].append(split[1])
    return words

if __name__ == "__main__":
    words = 5
    if len(argv) > 1:
        words = int(argv[1])
    main(words)