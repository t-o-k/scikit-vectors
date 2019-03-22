# Functions to make n-dimensional vector classes:

[![Build Status](https://travis-ci.org/t-o-k/scikit-vectors.svg?branch=master)](https://travis-ci.org/t-o-k/scikit-vectors)

* create_class_Fundamental_Vector
* create_class_Simple_Vector
* create_class_Vector
* create_class_Cartesian_Vector
* create_class_Cartesian_2D_Vector
* create_class_Cartesian_3D_Vector
* create_class_Versatile_Vector
* create_class_Tolerant_Cartesian_Vector
* create_class_Tolerant_Cartesian_2D_Vector
* create_class_Tolerant_Cartesian_3D_Vector
* create_class_Tolerant_Versatile_Vector

## Project homepage:

https://github.com/t-o-k/scikit-vectors

## Project wiki:

https://github.com/t-o-k/scikit-vectors/wiki

## Installation:

scikit-vectors requires Python version 3.5 or higher.

```shell
pip install scikit-vectors
```

## Examples:

### Simple examples:

```python
>>> from skvectors import create_class_Cartesian_Vector
>>> V6D = create_class_Cartesian_Vector('V6D', [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth' ])
>>> u = V6D(3, 1, 0, -3, 4, 2)
>>> u
V6D(first=3, second=1, third=0, fourth=-3, fifth=4, sixth=2)
>>> v = V6D(2, 2, 1, 3, 1, 4)
>>> u * v + 10
V6D(first=16, second=12, third=10, fourth=1, fifth=14, sixth=18)
>>> 2 * (u - v)
V6D(first=2, second=-2, third=-2, fourth=-12, fifth=6, sixth=-4)
>>> u**v / 2
V6D(first=4.5, second=0.5, third=0.0, fourth=-13.5, fifth=2.0, sixth=8.0)
>>> u *= 2 / v
>>> u
V6D(first=3.0, second=1.0, third=0.0, fourth=-2.0, fifth=8.0, sixth=1.0)
>>> u.first
3.0
>>> (u + v).sixth
5.0
>>> u.fifth += 2
>>> u
V6D(first=3.0, second=1.0, third=0.0, fourth=-2.0, fifth=10.0, sixth=1.0)
>>> u.length()
10.723805294763608
>>> round((u - v).normalize(), 3)
V6D(first=0.092, second=-0.092, third=-0.092, fourth=-0.46, fifth=0.829, sixth=-0.276)
>>> (u + 2).dot(v)
42.0
>>> 
```

```python
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> 
>>> V3D = create_class_Cartesian_3D_Vector('V3D', 'xyz')
>>> V3D(-1, 2, 4).cross(V3D(0, 3, -2))
V3D(x=-16, y=-2, z=-3)
>>> 
```

### Not so simple example with NumPy:

```python
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> import numpy as np
>>> 
>>> NP3 = \
...     create_class_Cartesian_3D_Vector(
...         name = 'NP3',
...         component_names = [ chr(0x03b1)*2, chr(0x03b2)*2, chr(0x03b3)*2 ],
...         brackets = [ chr(0x2770)*2 + ' ', ' ' + chr(0x2771)*2 ],
...         sep = ', ',
...         cnull = np.array([ 0., 0., 0., 0., 0. ]),
...         cunit = np.array([ 1., 1., 1., 1., 1. ]),
...         functions = \
...             {
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
>>> v = \
...     NP3(
...         np.random.randint(0, 100, size=5),
...         np.random.randint(0, 100, size=5),
...         np.random.randint(0, 100, size=5)
...     )
>>> v
NP3(αα=array([30., 43., 71., 18., 61.]), ββ=array([98., 91., 76., 10., 92.]), γγ=array([23., 87., 76., 24., 68.]))
>>> str(v)
'❰❰ [30. 43. 71. 18. 61.], [98. 91. 76. 10. 92.], [23. 87. 76. 24. 68.] ❱❱'
>>> u = NP3(1, -1, 0)
>>> u
NP3(αα=array([1., 1., 1., 1., 1.]), ββ=array([-1., -1., -1., -1., -1.]), γγ=array([0., 0., 0., 0., 0.]))
>>> v.dot(u)
array([-68., -48.,  -5.,   8., -31.])
>>> v.axis_rotate(NP3(1, -2, 1), np.pi/4)
NP3(αα=array([-27.33663766, -48.63172697, -15.85742691,  -2.94129394,
       -25.36927154]), ββ=array([85.27843393, 56.72182696, 52.78489506,  3.1911334 , 68.40280694]), γγ=array([ 54.89350552, 110.07538089, 116.42721703,  31.32356074,
       107.17488542]))
>>> 
```

Also have a look at the examples at [scikit-vectors_examples](https://github.com/t-o-k/scikit-vectors_examples).

## Running the tests:

```shell
git clone https://github.com/t-o-k/scikit-vectors
cd scikit-vectors
python3 -m unittest discover
```
Here's more information:
https://travis-ci.org/t-o-k/scikit-vectors

## License information:

See the file LICENSE for information on terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

## Author:

Tor Olav Kristensen

http://subcube.com
