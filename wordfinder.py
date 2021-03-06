"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """Finds a random word from a dictionary.

    Assume you have a file at words.txt that looks like this:

    cat
    dog
    porcupine

    Working with this class should work like this:
    
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, filename):
        self.words = self.read_file(filename)
        print(f"{len(self.words)} words read.")

    def read_file(self, fname):
        """Reads a file containing a list of words and returns a list of those words."""
        file = open(fname, 'r')
        words = [line.rstrip() for line in file]
        file.close()
        return words

    def random(self):
        """Returns a random word from the list of words."""
        return choice(self.words)
