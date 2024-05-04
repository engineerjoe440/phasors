# Test Phasor Package

import numpy as np
from numpy.testing import assert_almost_equal

from phasors import *

def test_phasor():
    """Test Basic Performance of the Phasor Class."""
    magnitude = 10
    # basic angles test case 0
    z1 = Phasor(magnitude, 0)
    z2 = Phasor(magnitude, 30)
    z3 = Phasor(magnitude, 45)
    z4 = Phasor(magnitude, 60)
    z5 = Phasor(magnitude, 90)

    assert_almost_equal(z1, complex(magnitude, 0))
    assert_almost_equal(z2, complex(magnitude * np.sqrt(3) / 2, magnitude / 2))
    assert_almost_equal(z3, complex(magnitude / np.sqrt(2), magnitude / np.sqrt(2)))
    assert_almost_equal(z4, complex(magnitude / 2, magnitude * np.sqrt(3) / 2))
    assert_almost_equal(z5, complex(0, magnitude))

    # z(theta) = z(theta+360) test case 1
    theta = np.random.randint(360)
    assert_almost_equal(Phasor(magnitude, theta), Phasor(magnitude, theta + 360))

    # z(-theta)*z(theta) == abs(z)^2 test case 2.
    z0 = Phasor(magnitude, theta)
    z1 = Phasor(magnitude, -theta)
    assert_almost_equal(z0 * z1, np.power(abs(z0), 2))

    # z(theta+180) = -1*Z(theta)
    z0 = Phasor(magnitude, theta)
    z1 = Phasor(magnitude, 180 + theta)
    assert_almost_equal(z0, -1 * z1)

def test_alpha():
    """Test the Alpha Constant."""
    assert alpha == Phasor(1, 120)
    a_phase = Phasor(5, 0)
    b_phase = Phasor(5, 120)
    assert a_phase * alpha == b_phase
    