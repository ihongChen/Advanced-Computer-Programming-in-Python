###  palindrom detection
from collections import deque

class Word:

    def __init__(self, word=None):
        self.word = word
        self.characters = deque(word)

    
    def is_palindrom(self):
        if len(self.characters) > 1:
            return self.characters.popleft() == self.characters.pop() \
                and Word(''.join(self.characters)).is_palindrom()
        else:
            return True

if __name__ == '__main__':
    p1 = Word('radar')
    p2 = Word('level')
    p3 = Word('structure')
    print(p1.is_palindrom())
    print(p2.is_palindrom())
    print(p3.is_palindrom())