import re


class EuclidDict:

    """A dictionary containing phrases sorted by their euclidian distances 
    """

    # frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
    __english_letter_freq = {'E': .1270, 'T': .0906, 'A': .0817, 'O': .0751, 'I': .0697, 'N': .0675, 'S': .0633, 'H': .0609, 'R': .0599, 'D': .0425, 'L': .0403, 'C': .0278,
                             'U': .0276, 'M': .0241, 'W': .0236, 'F': .0223, 'G': .0202, 'Y': .0197, 'P': .0193, 'B': .0129, 'V': .0098, 'K': .0077, 'J': .0015, 'X': .0015, 'Q': .0010, 'Z': .0007}

    def __init__(self):

        self.__euclid_dict = {}

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

    def add_phrase(self, phrase):

        self.__euclid_dict[phrase] = self._euclidian_distance(phrase)

    def get_top_phrases(self, num, regex=None):

        if not regex:
            return (sorted(self.__euclid_dict, key=self.__euclid_dict.__getitem__))[:num]
        pattern = re.compile(str(regex))
        filtered_dict = {key: self.__euclid_dict[
            key] for key in self.__euclid_dict.keys() if pattern.match(key)}
        return (sorted(filtered_dict, key=filtered_dict.__getitem__))[:num]

    def get_top_phrases_and_dists(self, num, regex=None):
        if not regex:
            sorted_keys = (sorted(self.__euclid_dict,
                                  key=self.__euclid_dict.__getitem__))[:num]
            return {key: __euclid_dict[key] for key in sorted_keys}
        pattern = re.compile(str(regex))
        filtered_dict = {key: self.__euclid_dict[
            key] for key in self.__euclid_dict.keys() if pattern.match(key)}
        sorted_keys = (
            sorted(filtered_dict, key=filtered_dict.__getitem__))[:num]
        return {key: __euclid_dict[key] for key in sorted_keys}
