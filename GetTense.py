import nltk
import FindWord
from nltk.stem.wordnet import WordNetLemmatizer

Tense = []
SimplePresent = []
PresentPerfect = []
PresentProgressive = []
presentPerfectProgressive = []
PastPerfect = []
simplePast = []
PastProgressive = []
PastPerfectProgressive = []
future = []
futureProgressive = []
futurePerfect = []
futurePerfectProgressive = []
conditionalSimple = []
conditionalProgressive = []
conditionalPerfect = []
conditionalPerfectProgressive = []

def get(words) :
    try :

        levels = ["A1", "A2", "B1", "B2", "C"]
        for i in range(len(words) - 1):
            token = nltk.word_tokenize(words[i])
            TypeWord = (nltk.pos_tag(token))
            if TypeWord[0][1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:

                # Present Perfect
                if (TypeWord[0][1] in ["VBN", "VBD"]) and (words[i - 1] in ["have", "has", "haven't", "hasn't"]) and (
                        (nltk.pos_tag(nltk.word_tokenize(words[i - 2]))[0][1] != "MD")) and (
                        words[i - 3] not in ["wouldn't", "would", "will", "won't"]) and (
                        nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1]) != "VBG" or (
                        (TypeWord[0][1] in ["VBN", "VBD"]) and (
                        (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][1]) in ["PRP", "NN", "NNS", "NNP",
                                                                                   "NNPS"])) and (
                        words[i - 2] in ["have", "has", "haven't", "hasn't"]) and (
                        nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] != "VBG"):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Present Perfect')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    PresentPerfect.append(1)

                # Present Progressive
                elif (TypeWord[0][1] == "VBG") and (words[i - 1] in ["am", "are", "is", "isn't"]) and (
                        words[i + 1] != 'to') or (TypeWord[0][1] == "VBG") and (
                        words[i - 1] in ["am", "are", "is", ] and (words[i - 2] == "not")) and (
                        words[i + 1] != 'to') or (
                        (TypeWord[0][1] == "VBG") and (
                        (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][1]) in ["NN", "PRP"] and (
                        words[i + 1] != "to") and (words[i - 2]) in ["am", "is", "are"] and (
                                words[i - 2] not in ["was", "were"]))):

                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Present Progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    PresentProgressive.append(1)

                # S-Present
                elif ((TypeWord[0][1] in ["VBZ", "VBP", "VB"]) and (
                        words[i - 2] not in ["wouldn't", "would", "will", "did", "didn't"]) and (
                              words[i - 1] not in ["to", "will", "won't", "would", "wouldn't"]) and ((
                        (nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1]) not in ["VB", "VBD", "VBG", "VBN", "VBP",
                                                                                       "VBZ"])) and (
                              (nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1])) not in ["PRP", "NN"] and (
                              words[i + 1] != "not") or (
                              (TypeWord[0][1] == "VBZ" or "VBP") and (words[i - 1] in ["doesn't", "don't"]) and (
                              ((nltk.pos_tag(nltk.word_tokenize(words[i - 2]))[0][1])) in ["PRP", "NN"]) and ((
                              (nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1]) not in ["VB", "VBD", "VBG", "VBN",
                                                                                             "VBP", "VBZ"]))) or (
                              (TypeWord[0][1] == "VBZ" or "VBP") and (
                              (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][1]) in ["PRP", "NN"]) and (
                                      words[i - 2] in ["do", "does"]))):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Simple Present')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    SimplePresent.append(1)

                # present perfect progressive
                elif (TypeWord[0][1] == "VBG") and words[i - 1] == 'been' and (
                        words[i - 2] in ['have', 'has', "hasn't", "haven't"]) and (
                        words[i - 3] not in ["will", "won't", "would", "wouldn't"]) and (
                        words[i - 4] not in ["wouldn't", "would", "will", "won't"]) or (
                        (TypeWord[0][1] == "VBG") and (words[i - 1] == 'been') and ((nltk.pos_tag(
                    nltk.word_tokenize(words[i - 2]))[0][1]) == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 3] in ['has', 'have', "hasn't", "haven't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Present perfect progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    presentPerfectProgressive.append(1)

                    # Past perfect
                elif (TypeWord[0][1] in ["VBN", "VBD"]) and (words[i - 1] in ['had', "hadn't"]) and (
                        (nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1]) != "VBG") or ((
                                                                                                     TypeWord[0][1] in [
                                                                                                 "VBN", "VBD"] and ((
                                                                                                                            nltk.pos_tag(
                                                                                                                                nltk.word_tokenize(
                                                                                                                                    words[
                                                                                                                                        i - 1]))[
                                                                                                                                0][
                                                                                                                                1]) == "PRP" or "NN" or "NNS" or "NNP" or "NNPS")) and (
                                                                                                     (words[i - 2] in [
                                                                                                         'had',
                                                                                                         "hadn't"]) and (
                                                                                                     (
                                                                                                             nltk.pos_tag(
                                                                                                                 nltk.word_tokenize(
                                                                                                                     words[
                                                                                                                         i + 1]))[
                                                                                                                 0][
                                                                                                                 1] != "VBG")))):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Past perfect')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    PastPerfect.append(1)

                # simple past
                elif ((TypeWord[0][1] in ["VBN", "VBD"]) and (
                        (nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1]) not in ["NN", "PRP", "VBN", "VBD", "VB",
                                                                                       "VBG"]) and (
                              (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][1]) not in ["VBN", "VBD", "VB"]) and (
                              (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][1]) in ["NN", "PRP"]) and (
                              (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][1]) not in ["VBN", "VBD"]) or (
                              (TypeWord[0][1] == "VB") and (words[i - 1] == "didn't")) or (
                              (TypeWord[0][1] == "VB") and ((
                                                                    nltk.pos_tag(
                                                                        nltk.word_tokenize(
                                                                            words[
                                                                                i - 1]))[
                                                                        0][
                                                                        1]) == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                      words[i - 2] in [
                                  "didn't", 'did']))):

                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Simple Past')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    simplePast.append(1)


                # Past Progressive
                elif (TypeWord[0][1] == "VBG") and ((words[i - 1] in ["was", "were", "wasn't", "weren't"])) or (
                        (TypeWord[0][1] == "VBG") and (((nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][
                    1]) == "PRP" or "NN" or "NNS" or "NNP" or "NNPS"))) and (
                        (words[i - 2] in ["was", "were", "wasn't", "weren't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('past Progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    PastProgressive.append(1)


                # Past perfect progressive
                elif (TypeWord[0][1] == "VBG" and ((words[i - 2] in ['had', "hadn't"])) and (
                        words[i - 1] == 'been')) or (
                        (TypeWord[0][1] == 'VBG') and (words[i - 1] == 'been') and ((nltk.pos_tag(
                    nltk.word_tokenize(words[i - 2]))[0][1]) == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 3] in ['had', "hadn't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('Past perfect progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    PastPerfectProgressive.append(1)


                # will future
                elif ((TypeWord[0][1] in ["VBP", "VB", "VBZ"]) and (words[i - 1] in ['will', "won't"])) or ((
                        (TypeWord[0][1] == 'VB') and (nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][
                                                          1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 2] in ['will',
                                                 "won't"]) and (
                                (nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] not in ["VBG", "VBD", "VBN"])))):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('will future')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    future.append(1)



                # going to future
                elif ((TypeWord[0][1] == 'VB') and (words[i - 1] == 'to') and (words[i - 2] == 'going') and (
                        words[i - 3] == 'not') and (words[i - 4] in ['am', 'are', 'is'])) or (
                        (TypeWord[0][1] == 'VB') and (words[i - 1] == 'to') and (words[i - 2] == 'going') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i - 3]))[0][1] in ["PRP", "NN", "NNS", "NNP",
                                                                                 "NNPS"]) and (
                                words[i - 4] in ['am', "is", 'are', ])) or (
                        (TypeWord[0][1] == 'VB') and (words[i - 1] == 'to') and (words[i - 2] == 'going') and (
                        words[i - 3] in ['am', 'are', 'is'])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('going to future')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    future.append(1)


                # futer progressive
                elif ((TypeWord[0][1] == 'VBG') and (words[i - 1] == 'be') and (words[i - 2] in ['will', "won't"])) or (
                        (TypeWord[0][1] == 'VBG') and (words[i - 1] == 'be') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i - 2]))[0][
                            1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (words[i - 3] in ['will', "won't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('future progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    futureProgressive.append(1)


                # future perfect
                elif ((TypeWord[0][1] in ["VBN", "VBD"]) and (words[i - 1] == 'have') and (
                        words[i - 2] in ['will', "won't"]) and (
                              nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] != "VBG")) or (
                        (TypeWord[0][1] in ["VBN", "VBD"]) and (words[i - 1] == 'have') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] != "VBG") and (
                                nltk.pos_tag(nltk.word_tokenize(words[i - 2]))[0][
                                    1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 3] in ['will', "won't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('future perfect')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    futurePerfect.append(1)


                # fututre perfect progressive
                elif ((TypeWord[0][1] == 'VBG') and (words[i - 1] == 'been') and (words[i - 2] == 'have') and (
                        words[i - 3] in ['will', "won't", "'ll", 'will not'])) or (
                        (TypeWord[0][1] == 'VBG') and (words[i - 1] == 'been') and (words[i - 2] == 'have') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i - 3]))[0][
                            1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (words[i - 4] in ['will', "won't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('future perfect progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    futurePerfectProgressive.append(1)


                # conditional simple
                elif (TypeWord[0][1] == 'VB') and (words[i - 1] in ['would', "wouldn't"]) and (
                        nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] not in ["VBG", "VBD", "VBN"]) or (
                        (TypeWord[0][1] == 'VB') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] not in ["VBG", "VBN", "VBD"]) and (
                                nltk.pos_tag(nltk.word_tokenize(words[i - 1]))[0][
                                    1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 2] in ['would', "wouldn't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('conditional simple')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    conditionalSimple.append(1)

                # conditional progressive
                elif ((TypeWord[0][1] == 'VBG') and (words[i - 1] == 'be') and (
                        words[i - 2] in ['would', "wouldn't"])) or (
                        (TypeWord[0][1] == 'VBG') and (words[i - 1] == 'be') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i - 2]))[0][
                            1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 3] in ['would', "wouldn't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('conditional progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    conditionalProgressive.append(1)


                # conditional perfect
                elif ((TypeWord[0][1] in ['VBN', "VBD"]) and (words[i - 1] == 'have') and (
                        words[i - 2] in ['would', "wouldn't"]) and (
                              nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] != "VBG")) or (
                        (TypeWord[0][1] in ["VBN", "VBD"]) and (words[i - 1] == 'have') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i - 2]))[0][
                            1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 3] in ['would', "wouldn't"]) and (
                                nltk.pos_tag(nltk.word_tokenize(words[i + 1]))[0][1] != "VBG")):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('conditional perfect')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    conditionalPerfect.append(1)


                # conditional perfect progressive
                elif ((TypeWord[0][1] == 'VBG') and (words[i - 1] == 'been') and (words[i - 2] == 'have') and (
                        words[i - 3] in ['would', "wouldn't"])) or (
                        (TypeWord[0][1] == 'VBG') and (words[i - 1] == 'been') and (words[i - 2] == 'have') and (
                        nltk.pos_tag(nltk.word_tokenize(words[i - 3]))[0][
                            1] == "PRP" or "NN" or "NNS" or "NNP" or "NNPS") and (
                                words[i - 4] in ['would', "wouldn't"])):
                    a = TypeWord[0][0]
                    lemmatizer = WordNetLemmatizer()
                    x = lemmatizer.lemmatize(a, 'v')
                    WordLevel = FindWord.findWord(x)
                    TenseLevel = FindWord.findWord('conditional perfect progressive')
                    if levels.index(WordLevel) <= levels.index(TenseLevel):
                        Tense.append(TenseLevel)
                    else:
                        Tense.append(WordLevel)
                    conditionalPerfectProgressive.append(1)

        return Tense
    except :
        return Tense
