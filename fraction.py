import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if (type(numerator) or type(denominator)) is not int:
            raise TypeError('Value must be integer.')
        if denominator == 0:
            self.denominator = 0
            if numerator == 0:
                self.numerator = 0
            else:
                self.numerator = int(numerator / math.gcd(abs(numerator), abs(denominator)))
        else:
            self.numerator = int(numerator/math.gcd(abs(numerator), abs(denominator)))
            self.denominator = int(denominator/math.gcd(abs(numerator), abs(denominator)))
            if self.denominator < 0:
                self.numerator = -1 * self.numerator
                self.denominator = abs(self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = (self.numerator*frac.denominator) + (self.denominator*frac.numerator)
        denominator = self.denominator*frac.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, frac):
        numerator = self.numerator*frac.numerator
        denominator = self.denominator*frac.denominator
        return Fraction(numerator, denominator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return '{}/{}'.format(self.numerator, self.denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator

