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
pip3 install scikit-vectors
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

### Example with SymPy

```python
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> import sympy
>>> sympy_functions = \
...     {
...         'eq': sympy.Eq,
...         'ne': sympy.Ne,
...         'and': sympy.And,
...         'or': sympy.Or,
...         'min': sympy.functions.Min,
...         'max': sympy.functions.Max,
...         'cos': sympy.functions.cos,
...         'sin': sympy.functions.sin,
...         'atan2': sympy.functions.atan2
...     }
>>> V3 = \
...     create_class_Cartesian_3D_Vector(
...         'V3',
...         'αβγ',
...         cnull = sympy.sympify(0),
...         cunit = sympy.sympify(1),
...         functions = sympy_functions
...     )
>>> V3.basis_α(), V3.basis_β(), V3.basis_γ()
(V3(α=1, β=0, γ=0), V3(α=0, β=1, γ=0), V3(α=0, β=0, γ=1))
>>> x, y, z = sympy.symbols('x y z')
>>> a, b, c = sympy.symbols('a b c')
>>> d, e, f = sympy.symbols('d e f')
>>> u = V3(x, y, z)
>>> u.contains(2)
Eq(2, x) | Eq(2, y) | Eq(2, z)
>>> u = V3(x, y, z)
>>> u.normalize()
V3(α=x/sqrt(x**2 + y**2 + z**2), β=y/sqrt(x**2 + y**2 + z**2), γ=z/sqrt(x**2 + y**2 + z**2))
>>> u = V3(a, b, c)
>>> v = V3(d, e, f)
>>> u.are_parallel(v)
Eq(sqrt((a*e - b*d)**2 + (-a*f + c*d)**2 + (b*f - c*e)**2), 0)
>>> u = V3(a, b, c)
>>> v = V3(d, e, f)
>>> u.project(v)
V3(α=d*(a*d + b*e + c*f)/(d**2 + e**2 + f**2), β=e*(a*d + b*e + c*f)/(d**2 + e**2 + f**2), γ=f*(a*d + b*e + c*f)/(d**2 + e**2 + f**2))
>>> u = V3(a, b, c)
>>> v = V3(d, e, f)
>>> u.sin(v)
sqrt((a*e - b*d)**2 + (-a*f + c*d)**2 + (b*f - c*e)**2)/(sqrt(a**2 + b**2 + c**2)*sqrt(d**2 + e**2 + f**2))
>>> u = V3(x, y, z)
>>> u.rotate_α(angle=e)
(V3(α=x, β=y*cos(e) - z*sin(e), γ=y*sin(e) + z*cos(e))
>>> u = V3(x, y, z)
>>> u(lambda s: a + s * b)
V3(α=a + b*x, β=a + b*y, γ=a + b*z)
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
...         np.random.randint(-10, 10, size=4),
...         np.random.randint(-10, 10, size=4),
...         np.random.randint(-10, 10, size=4)
...     )
>>> u
NP3(αα=array([ 7., -8.,  5.,  7.]), ββ=array([-1., -4.,  7., -4.]), γγ=array([ 1.,  6., -2.,  8.]))
>>> u /= 10
>>> u
NP3(αα=array([ 0.7, -0.8,  0.5,  0.7]), ββ=array([-0.1, -0.4,  0.7, -0.4]), γγ=array([ 0.1,  0.6, -0.2,  0.8]))
>>> v = \
...     NP3(
...         np.array([ -3,  5, -1,  2 ]),
...         np.array([  0, 12,  0, -1 ]),
...         np.array([  4,  0,  0,  2 ])
...     )
>>> str(v)
'❰❰ [-3.  5. -1.  2.], [  0.  12.   0.  -1.], [ 4.  0.  0.  2.] ❱❱'
>>> v.length()
array([  5.,  13.,   1.,   3.])
>>> v.contains(np.array([ 4.0, 2.0, -1.0, 3.0 ]))
array([ True, False,  True, False], dtype=bool)
>>> (u - v) * 10
NP3(αα=array([ 37., -58.,  15., -13.]), ββ=array([  -1., -124.,    7.,    6.]), γγ=array([-39.,   6.,  -2., -12.]))
>>> w = NP3(1, -1, 0)
>>> w
NP3(αα=array([ 1.,  1.,  1.,  1.]), ββ=array([-1., -1., -1., -1.]), γγ=array([ 0.,  0.,  0.,  0.]))
>>> u.reorient(v, w)
NP3(αα=array([ 0.1771821 , -0.0652714 , -0.84852814,  0.76479998]), ββ=array([ 0.65801471,  0.8920424 , -0.14142136, -0.83797539]), γγ=array([-0.21359575,  0.6       , -0.2       ,  0.05364919]))
>>> u.axis_rotate(NP3(1, -2, 1), np.pi/4)
NP3(αα=array([ 0.51492277, -0.76733621,  0.21325376,  0.26084032]), ββ=array([ 0.00486333, -0.74556654,  0.80444152, -0.53626169]), γγ=array([ 0.49480389, -0.12379688,  0.29562928,  0.96663629]))
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
