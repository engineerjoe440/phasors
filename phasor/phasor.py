################################################################################
"""
Phasor - A means to measure complex values with magnitude and angle.

Built in Python for Electrical Engineers.
"""
################################################################################

from cmath import polar

from numpy import degrees, radians, sin, cos

class Phasor(complex):
    """
    Phasor Class - An extension of the Python complex type for scientific work.

    This class can be used in place of, or alongside the standard `complex` type
    in Python to represent complex numbers as phasors (magnitude and angle) for
    scientific computation and electrical engineering analysis.

    Examples
    --------
    >>> from phasor import Phasor
    >>> Phasor(67, 120) # 67 volts at angle 120 degrees
    Phasor(magnitude=67, angle=120)
    >>> volt = Phasor(67, 120)
    >>> print(volt)
    67 ∠ 120°

    Properties
    ----------
    mag:        float
                The phasor magnitude, also commonly known as its absolute value.
    ang:        float
                The phasor angle, expressed in degrees.
    real:       float
                The real component of the complex value.
    imag:       float
                The imaginary component of the complex value.
    complex:    complex
                The complex type-cast of the phasor.
    """

    _magnitude: float
    _angle: float

    def __init__(self, magnitude, angle=None):
        """
        Phasor Constructor.
        
        Parameters
        ----------
        magnitude:  float
                    The phasor magnitude to express.
        angle:      float
                    The phasor angle to express, in degrees.
        """
        # Handle Passing a Complex Type Directly to Phasor
        if isinstance(magnitude, complex):
            magnitude, ang_r = polar(magnitude)
            angle = degrees(ang_r)
        # Load the Internal Values
        self._magnitude = magnitude
        self._angle = angle

    @property
    def real(self):
        """Real ( RE{} ) evaluation."""
        return self._magnitude * cos(radians(self._angle))

    @property
    def imag(self):
        """Imaginary ( IM{} ) evaluation."""
        return self._magnitude * sin(radians(self._angle))

    @property
    def mag(self):
        """Phasor magnitude evaluation."""
        return self._magnitude

    @property
    def ang(self):
        """Phasor angle evaluation."""
        return self._angle

    @property
    def complex(self):
        """Phasor representation as complex."""
        return complex(self.real, self.imag)

    def __repr__(self):
        """Represent the Phasor."""
        return f"Phasor(magnitude={self._magnitude}, angle={self._angle})"

    def __gt__(self, __x):
        """Evaluate whether __x is greater than this."""
        # Compare Magnitudes for Phasor Types
        if isinstance(__x, Phasor):
            return self._magnitude.__gt__(__x._magnitude)
        # Compare Magnitudes after first Casting `complex` to Phasor
        if isinstance(__x, complex):
            return self.__gt__(Phasor(__x))
        return self._magnitude.__gt__(__x)

    def __lt__(self, __x):
        """Evaluate whether __x is less than this."""
        # Compare Magnitudes for Phasor Types
        if isinstance(__x, Phasor):
            return self._magnitude.__lt__(__x._magnitude)
        # Compare Magnitudes after first Casting `complex` to Phasor
        if isinstance(__x, complex):
            return self.__lt__(Phasor(__x))
        return self._magnitude.__lt__(__x)

    def __ge__(self, __x):
        """Evaluate whether __x is greater than or equal to this."""
        # Compare Magnitudes for Phasor Types
        if isinstance(__x, Phasor):
            return self._magnitude.__ge__(__x._magnitude)
        # Compare Magnitudes after first Casting `complex` to Phasor
        if isinstance(__x, complex):
            return self.__ge__(Phasor(__x))
        return self._magnitude.__ge__(__x)

    def __le__(self, __x):
        """Evaluate whether __x is less than or equal to this."""
        # Compare Magnitudes for Phasor Types
        if isinstance(__x, Phasor):
            return self._magnitude.__le__(__x._magnitude)
        # Compare Magnitudes after first Casting `complex` to Phasor
        if isinstance(__x, complex):
            return self.__le__(Phasor(__x))
        return self._magnitude.__le__(__x)

    def __str__(self):
        """Stringlify the Phasor."""
        return f"{self._magnitude} ∠ {self._angle}°"

    def __round__(self, ndigits=0):
        """Round the Phasor."""
        mag = self._magnitude
        ang = self._angle
        mag = round(mag, ndigits=ndigits)
        ang = round(ang, ndigits=ndigits)
        return Phasor(mag, ang)

    def __mul__(self, __x):
        """Return self*__x."""
        if isinstance(__x, Phasor):
            return self.complex.__mul__(__x.complex)
        else:
            return self.complex.__mul__(__x)

    def __truediv__(self, __x):
        """Return self/__x."""
        if isinstance(__x, Phasor):
            return self.complex.__mul__(__x.complex)
        else:
            return self.complex.__mul__(__x)

    def __abs__(self):
        """Return the absolute magnitude."""
        return self._magnitude

    @staticmethod
    def from_arraylike(arraylike) -> "Phasor" | list["Phasor"]:
        """
        Phasor Constructor for Casting from Array Like Object.
        
        Use this method to create a new Phasor object from a two-item (2) long
        arraylike object, (e.g., a `tuple`, `list`, or NumPy array).
        """
        if isinstance(arraylike[0], (list, tuple)):
            return [Phasor(*element) for element in arraylike]
        return Phasor(*arraylike)
