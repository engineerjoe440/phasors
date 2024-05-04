


# Phasors

*A means to measure complex values with magnitude and angle.*

[![pypi](https://img.shields.io/pypi/v/phasors.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/phasors/)
[![stars](https://pepy.tech/badge/phasors)](https://pepy.tech/project/phasors)
[![github](https://img.shields.io/github/stars/engineerjoe440/phasors?logo=github)](https://github.com/engineerjoe440/phasors/)
[![license](https://img.shields.io/pypi/l/phasors.svg?color=blue)](https://github.com/engineerjoe440/phasors/blob/master/LICENSE.txt)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/engineerjoe440)

The `phasors` package provides a means to work with complex numbers in their
polar coordinate form (with a magnitude and angle) allowing simple computation
for advanced electrical engineering or other phasor-based work.

## Installation

Installing is as simple as:

```shell
pip install phasors
```

## Usage

```python
from phasor import Phasor

voltage = Phasor(67, 120)

print(voltage)
# 67.0 ∠ 119.99999999999999°
```
