# PyBackport: Colors

`pybase_ext.colors` allows easy import and use color codes, commonly used in computer vision applications.

The following are the supported classes:
* _RGB_: Contains red-green-blue color codes as tuples of three ints.
* _BGR_: Contains blue-green-red color codes as tuples of three ints.

**Note**: Due to the existing of many color variations, the supported classes only contain the most common color codes.

```pycon
>>> from py_back import colors
>>> colors.RGB.RED
(255, 0, 0)
>>> colors.BGR.RED
(0, 0, 255)
>>> [c.name for c, _ in zip(colors.RGB, range(5))]
['BLACK', 'WHITE', 'RED', 'GREEN', 'BLUE']
>>> [c for c, _ in zip(colors.RGB, range(5))]
[(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
```
