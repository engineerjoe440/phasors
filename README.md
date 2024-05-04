


# Phasor

*A means to measure complex values with magnitude and angle.*

The `phasor` package provides a means to work with complex numbers in their
polar coordinate form (with a magnitude and angle) allowing simple computation
for advanced electrical engineering or other phasor-based work.

## Installation

```
pip install phasor
```

## Usage

```python
from phasor import Phasor

voltage = Phasor(67, 120)

print(voltage)
# 67 ∠ 120°
```