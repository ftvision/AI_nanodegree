import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    for ind, word in enumerate(test_set.wordlist):
        X, lengths = test_set.get_item_Xlengths(ind)
        word_guess = {}
        for guess_word, model in models.items():
            try:
                logL = model.score(X, lengths)
            except:
                logL = float("-inf")
            word_guess[guess_word] = logL
        probabilities.append(word_guess)
        guesses.append(max(word_guess.keys(), key=lambda w:word_guess[w]))

    return probabilities, guesses
