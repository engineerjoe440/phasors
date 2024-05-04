################################################################################
"""
Phasor - A means to measure complex values with magnitude and angle.

Built in Python for Electrical Engineers.
"""
################################################################################

from typing import Union
from sys import stdout
from cmath import polar

from numpy import degrees, radians, sin, cos, absolute, angle

__all__ = [
    "Phasor",
    "alpha"
]

class Phasor(complex):
    """
    An extension of the Python `complex` type for work in polar coordinates.

    This class can be used in place of, or alongside the standard `complex` type
    in Python to represent complex numbers as phasors (magnitude and angle) for
    scientific computation and electrical engineering analysis and work.

    Examples
    --------
    >>> from electricpy._phasor import Phasor
    >>> Phasor(67, 120) # 67 volts at angle 120 degrees
    Phasor(magnitude=67, angle=120)
    >>> volt = Phasor(67, 120)
    >>> print(volt)
    67 ∠ 120°
        
    Parameters
    ----------
    magnitude:  float
                The phasor magnitude to express.
    angle:      float
                The phasor angle to express, in degrees.

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
    """

    def __new__(self, magnitude, angle=None):
        """
        Phasor Constructor.
        """
        # Handle Passing a Complex Type Directly to Phasor
        if isinstance(magnitude, complex):
            magnitude, ang_r = polar(magnitude)
            angle = degrees(ang_r)
        return complex.__new__(
            self,
            real=(magnitude * cos(radians(angle))),
            imag=(magnitude * sin(radians(angle)))
        )

    @property
    def mag(self):
        """Phasor magnitude evaluation."""
        return absolute(self)

    @property
    def ang(self):
        """Phasor angle evaluation in degrees."""
        return degrees(angle(self))

    def __repr__(self):
        """Represent the Phasor."""
        return f"Phasor(magnitude={self.mag}, angle={self.ang})"

    def __str__(self):
        """Stringlify the Phasor."""
        angle_denotion = "∠"
        if stdout.encoding != "utf-8":
            angle_denotion = "/_"
        return f"{self.mag} {angle_denotion} {self.ang}°"

    def __round__(self, ndigits=0):
        """Round the Phasor."""
        return Phasor(
            round(self.mag, ndigits=ndigits),
            round(self.ang, ndigits=ndigits)
        )

    @staticmethod
    def from_arraylike(arraylike) -> Union["Phasor", list["Phasor"]]:
        """
        Phasor Constructor for Casting from Array Like Object.
        
        Use this method to create a new Phasor object from a two-item (2) long
        arraylike object, (e.g., a `tuple`, `list`, or NumPy array).
        """
        if isinstance(arraylike[0], (list, tuple)):
            return [Phasor(*element) for element in arraylike]
        return Phasor(*arraylike)

alpha = Phasor(1, 120)
