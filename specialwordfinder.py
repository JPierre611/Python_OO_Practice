"""Special Word Finder: finds random words from a dictionary."""

from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Finds a random word from a dictionary.
       When reading the file, ignore blank lines and lines starting with '#'.

    Assume you have a file at words.txt that looks like this:

    cat
    dog
    porcupine

    Working with this class should work like this:
    
    >>> wf = SpecialWordFinder("words.txt")
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

    def read_file(self, fname):
        """Reads a file containing a list of words and returns a list of those words."""
        file = open(fname, 'r')
        words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        file.close()
        return words
