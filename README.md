# Functions to make n-dimensional vector classes:

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

### Simple examples:

```python
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> 
>>> V3D = create_class_Cartesian_3D_Vector('V3D', 'xyz')
>>> V3D(-1, 2, 4).cross(V3D(0, 3, -2))
V3D(x=-16, y=-2, z=-3)
>>> 
```

```python
>>> from skvectors import create_class_Cartesian_Vector
>>> 
>>> V6D = create_class_Cartesian_Vector('V6D', [ 'first', 'second', 'third', 'fourth', 'fifth', 'sixth' ])
>>> v = V6D(3.2, 1.1, 0.5, -2.9, 4.7, 2.4)
>>> v.sixth = 9.9
>>> v
V6D(first=3.2, second=1.1, third=0.5, fourth=-2.9, fifth=4.7, sixth=9.9)
>>> v.length()
11.841030360572512
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

More to come soon...

Tor Olav Kristensen
