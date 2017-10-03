import re

class EuclidDict:

	"""A dictionary containing phrases sorted by their euclidian distances 
	"""

	# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
	__english_letter_freq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

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
			euclidian_sum += (self.__english_letter_freq[key] - phrase_letter_freq[key])**2
		euclidian_dist = euclidian_sum**0.5
		return euclidian_dist


	def add_phrase(self, phrase):

		self.__euclid_dict[phrase] = self._euclidian_distance(phrase)


	def get_top_phrases(self, num, regex=None):

		if not regex:
			return (sorted(self.__euclid_dict, key=self.__euclid_dict.__getitem__))[:num]
		pattern = re.compile(str(regex))
		print "filtering!"
		filtered_dict = {key: self.__euclid_dict[key] for key in self.__euclid_dict.keys() if pattern.match(key)}
		return (sorted(filtered_dict, key=filtered_dict.__getitem__))[:num]
