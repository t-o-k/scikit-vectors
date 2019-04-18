[![Build Status](https://travis-ci.org/t-o-k/scikit-vectors.svg?branch=master)](https://travis-ci.org/t-o-k/scikit-vectors)

# Functions to create n-dimensional vector classes

This is a Python library with functions that create vector classes with 2, 3 or an arbitrary number of dimensions.

The name of the classes to be created, and the names of their vector components are set when calling the functions. The brackets for the vectors and the seperators for their components can also be given as arguments to these functions.

There are 11 functions that create vector classes. Each of them creates vector classes with a certain functionality. 8 of the functions create vector classes with a cartesian coordinate system and 4 of the functions create vector classes with tolerances for comparing vectors.

Created vector classes can be extended with extra functionality for processing their vector instances and ther component values.

Some of the vector classes are suitable for using e.g. NumPy's ndarrays, Pandas Series or SymPy's algebraic expressions as component values.

## Project homepage

https://github.com/t-o-k/scikit-vectors

## Project wiki

https://github.com/t-o-k/scikit-vectors/wiki

The wiki has links to documents that shows how created vector classes can be used.

## Installation

scikit-vectors requires Python version 3.5 or higher.

```shell
pip install scikit-vectors
```

## Examples

In addition to the short examples below, there are some more elaborate ones here:

https://github.com/t-o-k/scikit-vectors_examples

### Simple examples

```python
>>> from math import pi
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> CV3D = create_class_Cartesian_3D_Vector('CV3D', 'xyz', brackets=[ '<< ', ' >>' ])
>>> u = CV3D(3, 0, -4)
>>> print(u)
<< 3, 0, -4 >>
>>> v = CV3D(1, -2, 3) * 2
>>> repr(v)
'CV3D(x=2, y=-4, z=6)'
>>> u.normalize()
CV3D(x=0.6, y=0.0, z=-0.8)
>>> u.dot(v)
-18
>>> u.cross(v)
CV3D(x=-16, y=-26, z=-12)
>>> u = CV3D(4.5, -3.0, -1.5)
>>> v = CV3D(-3, -3, -3)
>>> u.angle(v) / pi
0.49999999999999994
>>> u = CV3D(5, -4, -3)
>>> v = CV3D(-2, 0, 2)
>>> u.project(v)
CV3D(x=4.0, y=-0.0, z=-4.0)
>>> u = CV3D(-5, 0, 0)
>>> v = CV3D(0, 12, 0)
>>> (u - v).length()
13.0
>>> u = CV3D(-3, 4, -5)
>>> u.rotate_x(pi)
CV3D(x=-3, y=-3.9999999999999996, z=5.000000000000001)
>>> u = CV3D(-3, 4, -5)
>>> v = CV3D(0, -10, -8)
>>> u.axis_rotate(v, -pi)
CV3D(x=2.999999999999999, y=-4.0, z=5.0)
>>> u = CV3D(-3, 4, -5)
>>> v = CV3D(-6, 0, 0)
>>> w = CV3D(0, 0, 7)
>>> u.reorient(v, w)
CV3D(x=-5.0, y=4.0, z=3.0)
>>> u = CV3D(0, -1, 2)
>>> v = CV3D(-3, 4, -5)
>>> w = CV3D(3, 1, 2)
>>> u.stp(v, w)
-21
>>> 
```

```python
>>> from skvectors import create_class_Simple_Vector
>>> SV = create_class_Simple_Vector('SV', [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth' ])
>>> u = SV(3, 1, -2, -3, 4, 2)
>>> u
SV(first=3, second=1, third=-2, fourth=-3, fifth=4, sixth=2)
>>> v = SV(2, -2, 1, 3, 1, 4)
>>> u * v + 10
SV(first=16, second=8, third=8, fourth=1, fifth=14, sixth=18)
>>> 2 * (u - v)
SV(first=2, second=6, third=-6, fourth=-12, fifth=6, sixth=-4)
>>> u**v / 2
SV(first=4.5, second=0.5, third=-1.0, fourth=-13.5, fifth=2.0, sixth=8.0)
>>> u *= 2 / v
>>> u
SV(first=3.0, second=-1.0, third=-4.0, fourth=-2.0, fifth=8.0, sixth=1.0)
>>> u.first
3.0
>>> (u + v).sixth
5.0
>>> u.fifth += 20
>>> u
SV(first=3.0, second=-1.0, third=-4.0, fourth=-2.0, fifth=28.0, sixth=1.0)
>>> u.c_add_third(24)
SV(first=3.0, second=-1.0, third=20.0, fourth=-2.0, fifth=28.0, sixth=1.0)
>>> u.c_imul_bar_second(1000)
>>> u
SV(first=3000.0, second=-1.0, third=-4000.0, fourth=-2000.0, fifth=28000.0, sixth=1000.0)
>>> v = SV(0, 1, 2, 3, 4, 5) / 6
>>> round(v, 3)
SV(first=0.0, second=0.167, third=0.333, fourth=0.5, fifth=0.667, sixth=0.833)
>>> 
```

### Not so simple example with NumPy

```python
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> import numpy as np
>>> NP3 = \
...     create_class_Cartesian_3D_Vector(
...         name = 'NP3',
...         component_names = [ chr(0x03b1)*2, chr(0x03b2)*2, chr(0x03b3)*2 ],
...         brackets = [ chr(0x2770)*2 + ' ', ' ' + chr(0x2771)*2 ],
...         sep = ', ',
...         cnull = np.array([ 0., 0., 0., 0. ]),
...         cunit = np.array([ 1., 1., 1., 1. ]),
...         functions = \
...             {
...                 'eq': np.equal,
...                 'ne': np.not_equal,
...                 'not': np.logical_not,
...                 'and': np.logical_and,
...                 'or': np.logical_or,
...                 'all': np.all,
...                 'any': np.any,
...                 'min': np.minimum,
...                 'max': np.maximum,
...                 'abs': np.absolute,
...                 'int': np.rint,
...                 'ceil': np.ceil,
...                 'copysign': np.copysign,
...                 'log10': np.log10,
...                 'cos': np.cos,
...                 'sin': np.sin,
...                 'atan2': np.arctan2,
...                 'pi': np.pi
...             }
...     )
>>> NP3.component_names()
['αα', 'ββ', 'γγ']
>>> u = \
...     NP3(
...         np.random.randint(0, 100, size=4),
...         np.random.randint(0, 100, size=4),
...         np.random.randint(0, 100, size=4)
...     )
>>> u
NP3(αα=array([ 55.,   5.,  89.,  17.]), ββ=array([ 31.,  80.,  79.,   9.]), γγ=array([ 72.,  98.,  82.,  30.]))
>>> v = \
...     NP3(
...         np.array([ -3,  5, -1,  2 ]),
...         np.array([  0, 12,  0, -1 ]),
...         np.array([  4,  0,  0,  2 ])
...     )
>>> str(v)
'❰❰ [-3.  5. -1.  2.], [  0.  12.   0.  -1.], [ 4.  0.  0.  2.] ❱❱'
>>> v.contains(np.array([ 4.0, 2.0, -1.0, 3.0 ]))
array([ True, False,  True, False], dtype=bool)
>>> v.length()
array([  5.,  13.,   1.,   3.])
>>> w = NP3(1, -1, 0)
>>> w
NP3(αα=array([ 1.,  1.,  1.,  1.]), ββ=array([-1., -1., -1., -1.]), γγ=array([ 0.,  0.,  0.,  0.]))
>>> u.reorient(v, w)
NP3(αα=array([  82.05609225,   72.07049885, -118.79393924,   29.71619365]), ββ=array([ 47.26643861, -35.08337491,   7.07106781, -10.35319062]), γγ=array([ 14.23662552,  98.        ,  82.        ,  16.72600607]))
>>> u.axis_rotate(NP3(1, -2, 1), np.pi/4)
NP3(αα=array([ -8.45426572, -78.92128882,  -6.58095221,  -6.48211845]), ββ=array([ 10.66681319,  35.28672614,  56.61295771,  -0.22011683]), γγ=array([  94.78789209,   92.49474109,  132.80686762,   35.04188478]))
>>> 
```

## Running the tests

```shell
git clone https://github.com/t-o-k/scikit-vectors
cd scikit-vectors
python3 -m unittest discover
```
Here's more information:
https://travis-ci.org/t-o-k/scikit-vectors

## License information

See the file LICENSE for information on terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

## Author

Tor Olav Kristensen

http://subcube.com
