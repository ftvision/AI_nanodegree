import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        best_num_components = None
        best_score = None
        for n_components in range(self.min_n_components, self.max_n_components + 1):
            try:
                model = self.base_model(n_components)
                logL = model.score(self.X, self.lengths)
                n_datapoint = sum(self.lengths)
                BIC_score = - 2 * logL + n_components * np.log(n_datapoint)
                if self.verbose:
                    print("model created for {} with {} states, its BIC_score is {}".format(self.this_word, n_components, BIC_score))
                if best_num_components is None or BIC_score < best_score:
                    best_num_components = n_components
                    best_score = BIC_score
            except:
                continue

        if self.verbose:
            print("Best model for {} with {} states, its BIC score is {}".format(self.this_word, best_num_components, best_score))
        return self.base_model(best_num_components)

class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on DIC scores

        M = len(self.words)
        best_num_components = None
        best_score = None
        for n_components in range(self.min_n_components, self.max_n_components + 1):
            try:
                model = self.base_model(n_components)
                logL = model.score(self.X, self.lengths)
                logL_other = 0
                for word in self.words:
                    if word != self.this_word:
                        other_X, other_lengths = self.hwords[word]
                        logL_other += model.score(other_X, other_lengths)
                DIC = logL -  1 / (M - 1) * logL_other

                if best_num_components is None or DIC > best_score:
                    best_num_components = n_components
                    best_score = DIC
            except:
                continue
        return self.base_model(best_num_components)

class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection using CV
        if len(self.sequences) == 1:
            minimal_num_component = 2
            return self.base_model(minimal_num_component)

        best_num_components = None
        best_score = None
        split_method = KFold(n_splits = min(3, len(self.sequences)))
        for n_components in range(self.min_n_components, self.max_n_components + 1):
            log_scores = []
            for cv_train_idx, cv_test_idx in split_method.split(self.sequences):
                train_X, train_lengths = combine_sequences(cv_train_idx, self.sequences)
                test_X, test_lengths = combine_sequences(cv_test_idx, self.sequences)
                try:
                    model = GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=1000,
                                        random_state=self.random_state, verbose=False).fit(train_X, train_lengths)
                    logL = model.score(test_X, test_lengths)
                    log_scores.append(logL)
                except:
                    continue

            mean_score = np.mean(log_scores)
            if self.verbose:
                print("model created for {} with {} states, its mean logL is {}".format(self.this_word, n_components, mean_score))
            if best_num_components is None or mean_score > best_score:
                best_score = mean_score
                best_num_components = n_components

        if self.verbose:
            print("Best model for {} with {} states, its mean logL is {}".format(self.this_word, best_num_components, best_score))
        return self.base_model(best_num_components)

class SelectorCV2(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds
        Selector CV algorithm from reviewer
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        mean_scores = []

        # Save reference to 'KFold' in variable as shown in notebook
        split_method = KFold()
        try:
            for n_component in range(self.min_n_components, self.max_n_components + 1):
                model = self.base_model(n_component)
                # Fold and calculate model mean scores
                fold_scores = []
                for _, test_idx in split_method.split(self.sequences):
                    # Get test sequences
                    test_X, test_length = combine_sequences(test_idx, self.sequences)
                    # Record each model score
                    fold_scores.append(model.score(test_X, test_length))

                # Compute mean of all fold scores
                mean_scores.append(np.mean(fold_scores))
        except Exception as e:
            pass

        num_components = range(self.min_n_components, self.max_n_components + 1)
        states = num_components[np.argmax(mean_scores)] if mean_scores else self.n_constant
        return self.base_model(states)
