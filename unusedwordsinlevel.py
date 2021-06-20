import createListOfWords
import readBook
import FindWord
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

list=createListOfWords.l

levelsList=['A1','A2','B1','B2','C']
usedwords = readBook.readedList

def unusedIteminLevel (level):

    if level != 'C' :
        firstelement = level
        lastelement = levelsList[levelsList.index(level) + 1]
        totalWords = list[list.index(firstelement) + 1:list.index(lastelement)]
    elif level == 'C' :
        firstelement = level
        totalWords = list[list.index(firstelement) + 1:]

    for i in usedwords :
        a = FindWord.findWord(i)
        if a == level:
            try:
                totalWords.remove(i)
            except ValueError:
                totalWords=totalWords
    for i in usedwords :
        token = nltk.word_tokenize(i)
        TypeWord = (nltk.pos_tag(token))
        if TypeWord[0][1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"] :
            a = TypeWord[0][0]
            lemmatizer = WordNetLemmatizer()
            x = lemmatizer.lemmatize(a, 'v')
            try:
                totalWords.remove(x)
            except ValueError:
                totalWords=totalWords

    return totalWords



if __name__ == "__main__":
   print( unusedIteminLevel('C') )


