# code that should find syllables in a word. found on stackoverflow.
# does not currently work because apparently my computer doesn't
# feel like installing the data for nltk

from nltk.corpus import cmudict
d = cmudict.dict()
def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]] 