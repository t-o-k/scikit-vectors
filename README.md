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

Simple example:

```python
>>> from skvectors import create_class_Cartesian_3D_Vector
>>> V3D = create_class_Cartesian_3D_Vector('V3D', 'xyz')
>>> V3D(-1, 2, 4).cross(V3D(0, 3, -2))
V3D(x=-16, y=-2, z=-3)
>>> 
```

More to come soon...

Tor Olav
