"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        self.start = start
        self.next = self.start

    def generate(self):
        """Returns the next sequential number."""
        self.current = self.next
        self.next += 1
        return self.current

    def reset(self):
        """Resets the next number back to the original start number."""
        self.next = self.start