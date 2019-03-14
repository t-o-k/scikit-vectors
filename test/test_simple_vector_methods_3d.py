"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

from math import floor, ceil, trunc
import itertools
import unittest
import skvectors


class Test_Case_simple_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Simple_Vector)


    @classmethod
    def setUpClass(cls):

        cls.V3D = \
            cls.create_vector_class(
                name = 'V3D',
                component_names = 'xyz',
                brackets = '<>',
                sep = ', '
            )


    @classmethod
    def tearDownClass(cls):

        del cls.V3D


    def test_round(self):

        fail_msg = "Problem with method '__round__'"
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = self.V3D.__round__(u)
        self.assertListEqual(v.component_values(), [ -556.0, -333.0, 556.0 ], msg=fail_msg)
        u = self.V3D(x=555.555, y=333.333, z=-555.555)
        v = u.__round__(ndigits=0)
        self.assertListEqual(v.component_values(), [ 556.0, 333.0, -556.0 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = round(u)
        self.assertListEqual(v.component_values(), [ -556.0, -333.0, 556.0 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = round(u, 0)
        self.assertListEqual(v.component_values(), [ -556.0, -333.0, 556.0 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = round(u, ndigits=2)
        self.assertListEqual(v.component_values(), [ -555.55, -333.33, 555.55 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = round(u, ndigits=-2)
        self.assertListEqual(v.component_values(), [ -600.0, -300.0, 600.0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = round(u)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_floor(self):

        fail_msg = "Problem with method '__floor__'"
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = self.V3D.__floor__(u)
        self.assertListEqual(v.component_values(), [ -556.0, -334.0, 555.0 ], msg=fail_msg)
        u = self.V3D(x=555.555, y=333.333, z=-555.555)
        v = u.__floor__()
        self.assertListEqual(v.component_values(), [ 555.0, 333.0, -556.0 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = floor(u)
        self.assertListEqual(v.component_values(), [ -556.0, -334.0, 555.0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = floor(u)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_ceil(self):

        fail_msg = "Problem with method '__ceil__'"
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = self.V3D.__ceil__(u)
        self.assertListEqual(v.component_values(), [ -555.0, -333.0, 556.0 ], msg=fail_msg)
        u = self.V3D(x=555.555, y=333.333, z=-555.555)
        v = u.__ceil__()
        self.assertListEqual(v.component_values(), [ 556.0, 334.0, -555.0 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = ceil(u)
        self.assertListEqual(v.component_values(), [ -555.0, -333.0, 556.0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = ceil(u)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_trunc(self):

        fail_msg = "Problem with method '__trunc__'"
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = self.V3D.__trunc__(u)
        self.assertListEqual(v.component_values(), [ -555.0, -333.0, 555.0 ], msg=fail_msg)
        u = self.V3D(x=555.555, y=333.333, z=-555.555)
        v = u.__trunc__()
        self.assertListEqual(v.component_values(), [ 555.0, 333.0, -555.0 ], msg=fail_msg)
        u = self.V3D(x=-555.555, y=-333.333, z=555.555)
        v = trunc(u)
        self.assertListEqual(v.component_values(), [ -555.0, -333.0, 555.0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = trunc(u)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_abs(self):

        fail_msg = "Problem with method '__abs__'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.__abs__(u)
        self.assertListEqual(v.component_values(), [ 0, 1, 2 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.__abs__()
        self.assertListEqual(v.component_values(), [ 3.5, 4.5, 5.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = abs(u)
        self.assertListEqual(v.component_values(), [ 0, 1, 2 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = abs(u)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_neg(self):

        fail_msg = "Problem with method '__neg__'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.__neg__(u)
        self.assertListEqual(v.component_values(), [ 0, 1, -2 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.__neg__()
        self.assertListEqual(v.component_values(), [ 3.5, -4.5, 5.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = -u
        self.assertListEqual(v.component_values(), [ 0, 1, -2 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = -u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_pos(self):

        fail_msg = "Problem with method '__pos__'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.__pos__(u)
        self.assertListEqual(v.component_values(), [ 0, -1, 2 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.__pos__()
        self.assertListEqual(v.component_values(), [ -3.5, 4.5, -5.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = +u
        self.assertListEqual(v.component_values(), [ 0, -1, 2 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = +u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_add(self):

        fail_msg = "Problem with method '__add__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__add__(u, w)
        self.assertListEqual(v.component_values(), [ -3, 3, -3 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u.__add__(3.5)
        self.assertListEqual(v.component_values(), [ 0.5, 7.5, -1.5 ], msg=fail_msg)
        u = self.V3D(0, 1, -2)
        w = self.V3D(-3, 4, -5)
        v = u + w
        self.assertListEqual(v.component_values(), [ -3, 5, -7 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u + 4.5
        self.assertListEqual(v.component_values(), [ 4.5, 3.5, 6.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u + (-3)
        self.assertListEqual(v.component_values(), [ -3, -4, -1 ], msg=fail_msg)
        u = self.V3D(0, 1, -2)
        w = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        v = u + w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_sub(self):

        fail_msg = "Problem with method '__sub__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__sub__(u, w)
        self.assertListEqual(v.component_values(), [ 3, -5, 7 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u.__sub__(3.5)
        self.assertListEqual(v.component_values(), [ -6.5, 0.5, -8.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = u - w
        self.assertListEqual(v.component_values(), [ 3, -5, 7 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u - 4.5
        self.assertListEqual(v.component_values(), [ -4.5, -5.5, -2.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u - (-3)
        self.assertListEqual(v.component_values(), [ 3, 2, 5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        v = u - w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_mul(self):

        fail_msg = "Problem with method '__mul__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__mul__(u, w)
        self.assertListEqual(v.component_values(), [ 0, -4, -10 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u.__mul__(1.5)
        self.assertListEqual(v.component_values(), [ -4.5, 6.0, -7.5 ], msg=fail_msg)
        u = self.V3D(0, 1, -2)
        w = self.V3D(-3, 4, -5)
        v = u * w
        self.assertListEqual(v.component_values(), [ 0, 4, 10 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u * 4.5
        self.assertListEqual(v.component_values(), [ 0.0, -4.5, 9.0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u * -3
        self.assertListEqual(v.component_values(), [ 9, -12, 15 ], msg=fail_msg)
        u = self.V3D(0, 1, -2)
        w = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        v = u * w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_pow(self):

        fail_msg = "Problem with method '__pow__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(2, 0, 1)
        v = self.V3D.__pow__(u, w)
        self.assertListEqual(v.component_values(), [ 0, 1, 2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(2, 1, 0)
        v = u.__pow__(w)
        self.assertListEqual(v.component_values(), [ 9, 4, 1 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(2, 1, 0)
        v = u**w
        self.assertListEqual(v.component_values(), [ 0, -1, 1 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 2, 1)
        v = u**w
        self.assertListEqual(v.component_values(), [ 1, 1, 2 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u**3
        self.assertListEqual(v.component_values(), [ 0, -1, 8 ], msg=fail_msg)
        u = self.V3D(-2, 4, -5)
        v = u**-1
        self.assertListEqual(v.component_values(), [ -0.5, 0.25, -0.2 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(2, 1, 0)
        id_u_before = id(u)
        v = u**w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(-1, 0, 2)
        w = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u**w
        u = self.V3D(-1, 0, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u**-1


    def test_truediv(self):

        fail_msg = "Problem with method '__truediv__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 5, -4)
        v = self.V3D.__truediv__(u, w)
        self.assertListEqual(v.component_values(), [ 0.0, -0.2, -0.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u.__truediv__(5)
        self.assertListEqual(v.component_values(), [ 0.0, -0.2, 0.4 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = u / w
        self.assertListEqual(v.component_values(), [ 0.0, -0.25, -0.4 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u / 4
        self.assertListEqual(v.component_values(), [ 0.0, -0.25, 0.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u / -2
        self.assertListEqual(v.component_values(), [ 0.0, 0.5, -1 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -2.0)
        v = 6.0 / u
        self.assertListEqual(v.component_values(), [ -2.0, 1.5, -3.0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        w = self.V3D(-3, 4, -5)
        v = u / w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u / w
        u = self.V3D(0, -1, 2)
        w = self.V3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u / w
        u = self.V3D(0, -1, 2)
        w = self.V3D(1, 1, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u / w
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v / 0


    def test_floordiv(self):

        fail_msg = "Problem with method '__floordiv__'"
        u = self.V3D(3, 2, -5)
        w = self.V3D(1, -2, -4)
        v = self.V3D.__floordiv__(u, w)
        self.assertListEqual(v.component_values(), [ 3, -1, 1 ], msg=fail_msg)
        u = self.V3D(-3, 4, 0)
        v = u.__floordiv__(5)
        self.assertListEqual(v.component_values(), [ -1, 0, 0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        v = u // w
        self.assertListEqual(v.component_values(), [ 3, 2, -2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u // 4
        self.assertListEqual(v.component_values(), [ -1, 1, -2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u // -3
        self.assertListEqual(v.component_values(), [ 1, -2, 1 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        w = self.V3D(-1, 2, 4)
        v = u // w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u // w
        u = self.V3D(0, -1, 2)
        w = self.V3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u // w
        u = self.V3D(0, -1, 2)
        w = self.V3D(1, 1, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u // w
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v // 0


    def test_mod(self):

        fail_msg = "Problem with method '__mod__'"
        u = self.V3D(-3, 4, -5)
        w = self.V3D(2, -4, 3)
        v = self.V3D.__mod__(u, w)
        self.assertListEqual(v.component_values(), [ 1, 0, 1 ], msg=fail_msg)
        u = self.V3D(3, -4, 5)
        v = u.__mod__(3)
        self.assertListEqual(v.component_values(), [ 0, 2, 2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        v = u % w
        self.assertListEqual(v.component_values(), [ 0, 0, 3 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u % 4
        self.assertListEqual(v.component_values(), [ 1, 0, 3 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u % -3
        self.assertListEqual(v.component_values(), [ 0, -2, -2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        id_u_before = id(u)
        v = u % w
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u % w
        u = self.V3D(0, -1, 2)
        w = self.V3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u % w
        u = self.V3D(0, -1, 2)
        w = self.V3D(1, 1, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            u % w
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v % 0


    def test_radd(self):

        fail_msg = "Problem with method '__radd__'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.__radd__(u, -2)
        self.assertListEqual(v.component_values(), [ -2, -3, 0 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.__radd__(3.5)
        self.assertListEqual(v.component_values(), [ 0.5, 7.5, -1.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = 4 + u
        self.assertListEqual(v.component_values(), [ 4, 3, 6 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = -2.0 + u
        self.assertListEqual(v.component_values(), [ -5.5, 2.5, -7.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = 4 + u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_rsub(self):

        fail_msg = "Problem with method '__rsub__'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.__rsub__(u, -2)
        self.assertListEqual(v.component_values(), [ -2, -1, -4 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.__rsub__(3.5)
        self.assertListEqual(v.component_values(), [ 6.5, -0.5, 8.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = 4 - u
        self.assertListEqual(v.component_values(), [ 4, 5, 2 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = -2 - u
        self.assertListEqual(v.component_values(), [ 1.5, -6.5, 3.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = 4 - u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_rmul(self):

        fail_msg = "Problem with method '__rmul__'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.__rmul__(u, -2)
        self.assertListEqual(v.component_values(), [ 0, 2, -4 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.__rmul__(1.5)
        self.assertListEqual(v.component_values(), [ -4.5, 6.0, -7.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = 4 * u
        self.assertListEqual(v.component_values(), [ 0, -4, 8 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = (-3.0) * u
        self.assertListEqual(v.component_values(), [ 10.5, -13.5, 16.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = 4 * u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_rpow(self):

        fail_msg = "Problem with method '__rpow__'"
        u = self.V3D(0, 1, 2)
        v = self.V3D.__rpow__(u, 3)
        self.assertListEqual(v.component_values(), [ 1, 3, 9 ], msg=fail_msg)
        u = self.V3D(1.0, 2.0, -1.0)
        v = u.__rpow__(2.5)
        self.assertListEqual(v.component_values(), [ 2.5, 6.25, 0.4 ], msg=fail_msg)
        u = self.V3D(0, 1, 2)
        v = (-3)**u
        self.assertListEqual(v.component_values(), [ 1, -3, 9 ], msg=fail_msg)
        u = self.V3D(0, 1, 2)
        id_u_before = id(u)
        v = (-3)**u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        v = self.V3D(-1, 0, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            0**v


    def test_rtruediv(self):

        fail_msg = "Problem with method '__rtruediv__'"
        u = self.V3D(-1, 4, -5)
        v = self.V3D.__rtruediv__(u, 2)
        self.assertListEqual(v.component_values(), [ -2.0, 0.5, -0.4 ], msg=fail_msg)
        u = self.V3D(2.0, 5.0, -4.0)
        v = u.__rtruediv__(-1.0)
        self.assertListEqual(v.component_values(), [ -0.5, -0.2, 0.25 ], msg=fail_msg)
        u = self.V3D(2.0, -4.0, 5.0)
        v = 4.0 / u
        self.assertListEqual(v.component_values(), [ 2.0, -1.0, 0.8 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
        id_u_before = id(u)
        v = 4 / u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            0 / v


    def test_rfloordiv(self):

        fail_msg = "Problem with method '__rfloordiv__'"
### TODO: Change values
        u = self.V3D(2, -4, 5)
        v = self.V3D.__rfloordiv__(u, 4)
        self.assertListEqual(v.component_values(), [ 2, -1, 0 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
### TODO: Change value
        v = u.__rfloordiv__(4)
        self.assertListEqual(v.component_values(), [ 2, -1, 0 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
        v = 4 // u
        self.assertListEqual(v.component_values(), [ 2, -1, 0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -2)
        v = -6 // u
        self.assertListEqual(v.component_values(), [ 2, -2, 3 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
        id_u_before = id(u)
        v = 4 // u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            0 // v


    def test_rmod(self):

        fail_msg = "Problem with method '__rmod__'"
### TODO: Change values
        u = self.V3D(2, -4, 5)
        v = self.V3D.__rmod__(u, 4)
        self.assertListEqual(v.component_values(), [ 0, 0, 4 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
### TODO: Change value
        v = u.__rmod__(4)
        self.assertListEqual(v.component_values(), [ 0, 0, 4 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
        v = 4 % u
        self.assertListEqual(v.component_values(), [ 0, 0, 4 ], msg=fail_msg)
        u = self.V3D(2, -4, 5)
        id_u_before = id(u)
        v = 4 % u
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            0 % v


    def test_iadd(self):

        fail_msg = "Problem with method '__iadd__'"
### TODO: Change values
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__iadd__(v, w)
        self.assertListEqual(v.component_values(), [ -3, 3, -3 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
### TODO: Change value
        v = v.__iadd__(3)
        self.assertListEqual(v.component_values(), [ 3, 2, 5 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v += w
        self.assertListEqual(v.component_values(), [ -3, 3, -3 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        v += 4
        self.assertListEqual(v.component_values(), [ 4, 3, 6 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        id_v_before = id(v)
        v += w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)


    def test_isub(self):

        fail_msg = "Problem with method '__isub__'"
### TODO: Change values
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__isub__(v, w)
        self.assertListEqual(v.component_values(), [ 3, -5, 7 ], msg=fail_msg)
### TODO: Change values
        v = self.V3D(0, -1, 2)
        v = v.__isub__(3)
        self.assertListEqual(v.component_values(), [ -3, -4, -1 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v -= w
        self.assertListEqual(v.component_values(), [ 3, -5, 7 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        v -= 4
        self.assertListEqual(v.component_values(), [ -4, -5, -2 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        id_v_before = id(v)
        v -= w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)


    def test_imul(self):

        fail_msg = "Problem with method '__imul__'"
### TODO: Change values
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__imul__(v, w)
        self.assertListEqual(v.component_values(), [ 0, -4, -10 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
### TODO: Change value
        v = v.__imul__(3)
        self.assertListEqual(v.component_values(), [ 0, -3, 6 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v *= w
        self.assertListEqual(v.component_values(), [ 0, -4, -10 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        v *= 4
        self.assertListEqual(v.component_values(), [ 0, -4, 8 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        id_v_before = id(v)
        v *= w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)


    def test_ipow(self):

        fail_msg = "Problem with method '__ipow__'"
### TODO: Change values
        v = self.V3D(0, -1, 2)
        w = self.V3D(2, 1, 0)
        v = self.V3D.__ipow__(v, w)
        self.assertListEqual(v.component_values(), [ 0, -1, 1 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
### TODO: Change value
        v = v.__ipow__(3)
        self.assertListEqual(v.component_values(), [ 0, -1, 8 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(2, 1, 0)
        v **= w
        self.assertListEqual(v.component_values(), [ 0, -1, 1 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(0, 2, 1)
        v **= w
        self.assertListEqual(v.component_values(), [ 1, 1, 2 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        v **= 3
        self.assertListEqual(v.component_values(), [ 0, -1, 8 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(0, 2, 1)
        id_v_before = id(v)
        v **= w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v **= -1


    def test_itruediv(self):

        fail_msg = "Problem with method '__itruediv__'"
### TODO: Change values
        v = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        v = self.V3D.__itruediv__(v, w)
        self.assertListEqual(v.component_values(), [ 0.0, -0.25, -0.4 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
### TODO: Change value
        v = v.__itruediv__(4)
        self.assertListEqual(v.component_values(), [ 0.0, -0.25, 0.5 ], msg=fail_msg)
        v = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(-3.0, 4.0, -5.0)
        v /= w
        self.assertListEqual(v.component_values(), [ 0.0, -0.25, -0.4 ], msg=fail_msg)
        v = self.V3D(0.0, -1.0, 2.0)
        v /= 4.0
        self.assertListEqual(v.component_values(), [ 0.0, -0.25, 0.5 ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        id_v_before = id(v)
        v /= w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v /= w
        v = self.V3D(0, -1, 2)
        w = self.V3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v /= w
        v = self.V3D(0, -1, 2)
        w = self.V3D(1, 1, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v /= w
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v /= 0


    def test_ifloordiv(self):

        fail_msg = "Problem with method '__ifloordiv__'"
### TODO: Change values
        v = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        v = self.V3D.__ifloordiv__(v, w)
        self.assertListEqual(v.component_values(), [ 3, 2, -2 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
### TODO: Change value
        v = v.__ifloordiv__(3)
        self.assertListEqual(v.component_values(), [ -1, 1, -2 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        v //= w
        self.assertListEqual(v.component_values(), [ 3, 2, -2 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        v //= 4
        self.assertListEqual(v.component_values(), [ -1, 1, -2 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        id_v_before = id(v)
        v //= w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v //= w
        v = self.V3D(0, -1, 2)
        w = self.V3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v //= w
        v = self.V3D(0, -1, 2)
        w = self.V3D(1, 1, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v //= w
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v //= 0


    def test_imod(self):

        fail_msg = "Problem with method '__imod__'"
### TODO: Change values
        v = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        v = self.V3D.__imod__(v, w)
        self.assertListEqual(v.component_values(), [ 0, 0, 3 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
### TODO: Change value
        v = v.__imod__(3)
        self.assertListEqual(v.component_values(), [ 0, 1, 1 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        v %= w
        self.assertListEqual(v.component_values(), [ 0, 0, 3 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        v %= 4
        self.assertListEqual(v.component_values(), [ 1, 0, 3 ], msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        w = self.V3D(-1, 2, 4)
        id_v_before = id(v)
        v %= w
        id_v_after = id(v)
        self.assertEqual(id_v_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v %= w
        v = self.V3D(0, -1, 2)
        w = self.V3D(1, 0, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v %= w
        v = self.V3D(0, -1, 2)
        w = self.V3D(1, 1, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v %= w
        v = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v %= 0


    def test_getattr(self):

        fail_msg = "Problem with method '__getattr__'"


        def verify_attributes(test_vector, test_data):

            for attr_name, arg, result in test_data:
                function = getattr(test_vector, attr_name)
                v = function(*arg)
                with self.subTest(v=test_vector, operator=attr_name, expected_result=result):
                    self.assertListEqual(v.component_values(), result, msg=fail_msg)


        def verify_attributes_i(test_vector, test_data):

            for attr_name, arg, result in test_data:
                v = test_vector.copy()
                function = getattr(v, attr_name)
                function(*arg)
                with self.subTest(v=v, operator=attr_name, expected_result=result):
                    self.assertListEqual(v.component_values(), result, msg=fail_msg)


        def verify_attribute_names(test_vector, test_operators):

            invalid_elements = [ 'a' ]
            # invalid_elements = [ '', 'a' ]
            valid_elements = [ 'bar' ] + test_vector.cnames
            for test_op in test_operators:
                valid_attr_names = test_vector.cnames
                for i in range(len(valid_elements)+2):
                    valid_attr_names += \
                        [
                            '_'.join(['c', test_op] + list(comb))
                            for comb in set(itertools.combinations(valid_elements, i))
                        ]
                for i in range(len(valid_elements + invalid_elements)+1):
                    elements = [ test_op ] + valid_elements * i + invalid_elements
                    for perm in set(itertools.permutations(elements, i)):
                        attr_name = 'c_' + '_'.join(perm)
                        with self.subTest(v=test_vector, attr=attr_name):
                            if attr_name in valid_attr_names:
                                self.assertTrue(hasattr(test_vector, attr_name), msg=fail_msg)
                            else:
                                self.assertFalse(hasattr(test_vector, attr_name), msg=fail_msg)
                elements = [ 'c', test_op, 'bar' ]
                elements += [ '' ] * 4
                elements += [ '_' ] * 3  # NB: 4 or more will generate __pos__ etc.
                elements += test_vector.cnames[0:1]
                attribute_names = \
                    set(
                        ''.join(perm)
                        for i in range(8)
                        for perm in set(itertools.permutations(elements, i))
                    )
                for attr_name in attribute_names:
                    with self.subTest(v=test_vector, attr=attr_name):
                        if attr_name in valid_attr_names:
                            self.assertTrue(hasattr(test_vector, attr_name), msg=fail_msg)
                        else:
                            self.assertFalse(hasattr(test_vector, attr_name), msg=fail_msg)


        verify_attributes(
            self.V3D(-3, -4, -5),
            [
                ('c_abs'          , [ ], [ -3, -4, -5 ]),
                ('c_abs_bar_x_y_z', [ ], [ -3, -4, -5 ]),
                ('c_abs_x'        , [ ], [  3, -4, -5 ]),
                ('c_abs_bar_y_z'  , [ ], [  3, -4, -5 ]),
                ('c_abs_y'        , [ ], [ -3,  4, -5 ]),
                ('c_abs_bar_x_z'  , [ ], [ -3,  4, -5 ]),
                ('c_abs_z'        , [ ], [ -3, -4,  5 ]),
                ('c_abs_bar_x_y'  , [ ], [ -3, -4,  5 ]),
                ('c_abs_x_y'      , [ ], [  3,  4, -5 ]),
                ('c_abs_bar_z'    , [ ], [  3,  4, -5 ]),
                ('c_abs_y_z'      , [ ], [ -3,  4,  5 ]),
                ('c_abs_bar_x'    , [ ], [ -3,  4,  5 ]),
                ('c_abs_x_z'      , [ ], [  3, -4,  5 ]),
                ('c_abs_bar_y'    , [ ], [  3, -4,  5 ]),
                ('c_abs_x_y_z'    , [ ], [  3,  4,  5 ]),
                ('c_abs_bar'      , [ ], [  3,  4,  5 ])
            ]
        )
        verify_attributes(
            self.V3D(-3.5, 4.5, -5.5),
            [
                ('c_neg_y'    , [ ], [ -3.5, -4.5, -5.5 ]),
                ('c_neg_x_z'  , [ ], [  3.5,  4.5,  5.5 ]),
                ('c_pos_y'    , [ ], [ -3.5,  4.5, -5.5 ]),
                ('c_pos_x_z'  , [ ], [ -3.5,  4.5, -5.5 ]),
                ('c_floor_y'  , [ ], [ -3.5,  4  , -5.5 ]),
                ('c_floor_x_z', [ ], [ -4  ,  4.5, -6   ]),
                ('c_ceil_y'   , [ ], [ -3.5,  5  , -5.5 ]),
                ('c_ceil_x_z' , [ ], [ -3  ,  4.5, -5   ]),
                ('c_trunc_y'  , [ ], [ -3.5,  4  , -5.5 ]),
                ('c_trunc_x_z', [ ], [ -3  ,  4.5, -5   ])
            ]
        )
        verify_attributes(
            self.V3D(-2.5, 3.5, -1.5),
            [
                ('c_add_y'       , [ 2 ], [ -2.5 ,  5.5 , -1.5  ]),
                ('c_add_x_z'     , [ 2 ], [ -0.5 ,  3.5 ,  0.5  ]),
                ('c_sub_y'       , [ 2 ], [ -2.5 ,  1.5 , -1.5  ]),
                ('c_sub_x_z'     , [ 2 ], [ -4.5 ,  3.5 , -3.5  ]),
                ('c_mul_y'       , [ 2 ], [ -2.5 ,  7.0 , -1.5  ]),
                ('c_mul_x_z'     , [ 2 ], [ -5.0 ,  3.5 , -3.0  ]),
                ('c_pow_y'       , [ 2 ], [ -2.5 , 12.25, -1.5  ]),
                ('c_pow_x_z'     , [ 2 ], [  6.25,  3.5 ,  2.25 ]),
                ('c_truediv_y'   , [ 2 ], [ -2.5 ,  1.75, -1.5  ]),
                ('c_truediv_x_z' , [ 2 ], [ -1.25,  3.5 , -0.75 ]),
                ('c_floordiv_y'  , [ 2 ], [ -2.5 ,  1.0 , -1.5  ]),
                ('c_floordiv_x_z', [ 2 ], [ -2.0 ,  3.5 , -1.0  ]),
                ('c_mod_y'       , [ 2 ], [ -2.5 ,  1.5 , -1.5  ]),
                ('c_mod_x_z'     , [ 2 ], [  1.5 ,  3.5 ,  0.5  ])
            ]
        )
### TODO:
# Test division by zero
# Verify that c_radd etc. does not exist (?)

        verify_attributes_i(
            self.V3D(-2.5, 3.5, -1.5),
            [
                ('c_iadd_y'       , [ 2 ], [ -2.5 ,  5.5 , -1.5  ]),
                ('c_iadd_x_z'     , [ 2 ], [ -0.5 ,  3.5 ,  0.5  ]),
                ('c_isub_y'       , [ 2 ], [ -2.5 ,  1.5 , -1.5  ]),
                ('c_isub_x_z'     , [ 2 ], [ -4.5 ,  3.5 , -3.5  ]),
                ('c_imul_y'       , [ 2 ], [ -2.5 ,  7.0 , -1.5  ]),
                ('c_imul_x_z'     , [ 2 ], [ -5.0 ,  3.5 , -3.0  ]),
                ('c_ipow_y'       , [ 2 ], [ -2.5 , 12.25, -1.5  ]),
                ('c_ipow_x_z'     , [ 2 ], [  6.25,  3.5 ,  2.25 ]),
                ('c_itruediv_y'   , [ 2 ], [ -2.5 ,  1.75, -1.5  ]),
                ('c_itruediv_x_z' , [ 2 ], [ -1.25,  3.5 , -0.75 ]),
                ('c_ifloordiv_y'  , [ 2 ], [ -2.5 ,  1.0 , -1.5  ]),
                ('c_ifloordiv_x_z', [ 2 ], [ -2.0 ,  3.5 , -1.0  ]),
                ('c_imod_y'       , [ 2 ], [ -2.5 ,  1.5 , -1.5  ]),
                ('c_imod_x_z'     , [ 2 ], [  1.5 ,  3.5 ,  0.5  ]),
            ]
        )
### TODO:
# Test division by zero
# Test with non existing operators
# Test with non existing components

        verify_attribute_names(
            self.V3D(-2.5, 3.5, -1.5),
            [
                # 'abs',
                # 'neg',
                'pos',
                # 'floor',
                # 'ceil',
                # 'trunc',
                # 'add',
                # 'sub',
                # 'mul',
                # 'pow',
                # 'truediv',
                # 'floordiv',
                # 'mod'
            ]
        )


### TODO:
#     def test_setattr(self):
#
#         fail_msg = "Problem with method '__setattr__'"


class Test_Case_vector(Test_Case_simple_vector):

    create_vector_class = staticmethod(skvectors.create_class_Vector)


class Test_Case_cartesian_vector(Test_Case_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_Vector)


    def test_abs(self):

        fail_msg = "Problem with method '__abs__'"
        u = self.V3D(0, -4.0, 3.0)
        s = self.V3D.__abs__(u)
        self.assertAlmostEqual(s, 5.0, msg=fail_msg)
        u = self.V3D(-12.0, -5.0, 0.0)
        s = u.__abs__()
        self.assertAlmostEqual(s, 13.0, msg=fail_msg)
        u = self.V3D(0.0, 0.0, 0.0)
        s = abs(u)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(0.0, 0.0, -3.0)
        s = abs(u)
        self.assertAlmostEqual(s, 3.0, msg=fail_msg)
        u = self.V3D(-3.0, 0.0, 4.0)
        s = abs(u)
        self.assertAlmostEqual(s, 5.0, msg=fail_msg)
        u = self.V3D(5.0, 12.0, 0.0)
        s = abs(u)
        self.assertAlmostEqual(s, 13.0, msg=fail_msg)
        u = self.V3D(-2.0, -1.0, -2.0)
        s = abs(u)
        self.assertAlmostEqual(s, 3.0, msg=fail_msg)


class Test_Case_tolerant_cartesian_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_Vector)


class Test_Case_cartesian_3d_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_3D_Vector)


class Test_Case_tolerant_cartesian_3d_vector(Test_Case_cartesian_3d_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_3D_Vector)


if __name__ == "__main__":
    unittest.main()

