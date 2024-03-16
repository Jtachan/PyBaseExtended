![tests_badge](https://github.com/Jtachan/PyBackport/actions/workflows/unittests.yml/badge.svg)
[![PyPI Version](https://img.shields.io/pypi/v/pybase-ext)](https://pypi.org/project/pybase-ext/)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/downloads/) 
[![PyPI Downloads](https://img.shields.io/pypi/dm/pybase-ext)](https://pypi.org/project/pybase-ext/) 
[![MIT License](https://img.shields.io/github/license/will2dye4/labyrinth)](https://github.com/Jtachan/PyBackport/blob/master/LICENSE)

# Python Backport

The `py_back` modules serve three purposes:

* Enable the use of new base classes in older Python versions. For example, `enum.StrEnum` is new in Python 3.11, but `py_back` allows users on previous versions to use it too.
* Enable experimental classes not implemented in other modules. For example, `enum.TupleEnum` is not implemented in `enum`, but `py_back` allows users to create enumerations where its members are tuples.
* Provide of new classes containing commonly used constant values. For example, `py_back.colors` provides a wrapper to commonly used BGR color codes, like `BGR.WHITE` to use the color code `(255, 255, 255)`


## Setup

Install the package via pip.

```shell
pip install py-backport
```

The latest changes on develop can be installed via pip + git:
```shell
pip install git+https://github.com/Jtachan/PyBackport.git@develop
```

## 📖 Documentation

Documentation can be found at the [`docs`](https://github.com/Jtachan/PyBaseExtension/blob/main/docs/index.md) folder.

WIP: Sphinx documentation for further releases.
