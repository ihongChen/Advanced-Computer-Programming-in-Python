# count vowels
from collections import defaultdict
words = 'supercalifragilisticexpialidocious'

words_dict = defaultdict(int)
for e in words:
    if e in ['a', 'e', 'i', 'o', 'u']:
        words_dict[e] += 1

print(words_dict)
