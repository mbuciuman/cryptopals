import re
from operator import attrgetter


class EuclidDict:

    """A dictionary containing phrases sorted by their euclidian distances 
    """

    # frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
    __english_letter_freq = {'E': .1270, 'T': .0906, 'A': .0817, 'O': .0751, 'I': .0697, 'N': .0675, 'S': .0633, 'H': .0609, 'R': .0599, 'D': .0425, 'L': .0403, 'C': .0278,
                             'U': .0276, 'M': .0241, 'W': .0236, 'F': .0223, 'G': .0202, 'Y': .0197, 'P': .0193, 'B': .0129, 'V': .0098, 'K': .0077, 'J': .0015, 'X': .0015, 'Q': .0010, 'Z': .0007}

    def __init__(self):

        self._euclid_dict = {}

    def _euclidian_distance(self, phrase):

        phrase_letter_freq = dict.fromkeys(self.__english_letter_freq.keys())
        for key in phrase_letter_freq:
            phrase_letter_freq[key] = 0
        for char in phrase:
            if phrase_letter_freq.has_key(char.upper()):
                phrase_letter_freq[char.upper()] += 1
        euclidian_sum = float(0)
        for key in phrase_letter_freq:
            phrase_letter_freq[key] /= float(len(phrase))
            euclidian_sum += (self.__english_letter_freq[
                              key] - phrase_letter_freq[key])**2
        euclidian_dist = euclidian_sum**0.5
        return euclidian_dist

    def add_phrase(self, phrase, encryption_key=None):

        self._euclid_dict[phrase] = EuclidEntry(phrase, self._euclidian_distance(phrase), encryption_key)

    def get_top_phrases(self, num, regex=None):

        if not regex:
            return (sorted(self._euclid_dict.keys(), key=lambda phrase: self._euclid_dict[phrase].get_euclid_dist()))[:num]
        pattern = re.compile(str(regex))
        filtered_dict = {key: self._euclid_dict[
            key] for key in self._euclid_dict.keys() if pattern.match(key)}
        return (sorted(filtered_dict, key=lambda phrase: self._euclid_dict[phrase].get_euclid_dist()))[:num]

    def get_top_items(self, num, regex=None):

        if not regex:
            sorted_keys = (sorted(self._euclid_dict.keys(),
                                  key=lambda phrase: self._euclid_dict[phrase].get_euclid_dist()))[:num]
            return {key: self._euclid_dict[key] for key in sorted_keys}
        pattern = re.compile(str(regex))
        filtered_dict = {key: self._euclid_dict[
            key] for key in self._euclid_dict.keys() if pattern.match(key)}
        sorted_keys = (
            sorted(filtered_dict.keys(), key=lambda phrase: self._euclid_dict[phrase].get_euclid_dist()))[:num]
        return {key: self._euclid_dict[key] for key in sorted_keys}

    def get_size(self):
        return len(self._euclid_dict)


class EuclidEntry:

    def __init__(self, phrase, euclid_dist, encryption_key):
        self.phrase = phrase
        self.euclid_dist = euclid_dist
        self.encryption_key = encryption_key

    def get_phrase(self):
        return self.phrase

    def get_euclid_dist(self):
        return self.euclid_dist

    def get_encryption_key(self):
        return self.encryption_key
