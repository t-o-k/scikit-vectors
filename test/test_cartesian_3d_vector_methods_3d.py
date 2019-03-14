"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import math
import unittest
import skvectors


class Test_Case_cartesian_3d_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_3D_Vector)

    pi_1_4 = math.pi/4.0
    pi_1_2 = math.pi/2.0
    pi_3_4 = math.pi*3.0/4.0
    pi_1_1 = math.pi
    sqrt_2 = math.sqrt(2.0)
    sqrt_3 = math.sqrt(3.0)
    sqrt_6 = math.sqrt(6.0)
    sqrt_8 = math.sqrt(8.0)
    polar_to_cartesian = \
        [
            ((0.0,  pi_1_4,     0.0), (    0.0,     0.0,     0.0)),
            ((0.0,     0.0, -pi_1_4), (    0.0,     0.0,     0.0)),
            ((2.0,     0.0,     0.0), (    2.0,     0.0,     0.0)),
            ((2.0, -pi_1_1,     0.0), (   -2.0,     0.0,     0.0)),
            ((2.0,  pi_1_1,     0.0), (   -2.0,     0.0,     0.0)),
            ((2.0,     0.0, -pi_1_1), (   -2.0,     0.0,     0.0)),
            ((2.0,     0.0,  pi_1_1), (   -2.0,     0.0,     0.0)),
            ((2.0, -pi_1_1, -pi_1_1), (    2.0,     0.0,     0.0)),
            ((2.0, -pi_1_1,  pi_1_1), (    2.0,     0.0,     0.0)),
            ((2.0,  pi_1_1, -pi_1_1), (    2.0,     0.0,     0.0)),
            ((2.0,  pi_1_1,  pi_1_1), (    2.0,     0.0,     0.0)),
            ((2.0, -pi_1_2,     0.0), (    0.0,    -2.0,     0.0)),
            ((2.0,  pi_1_2,     0.0), (    0.0,     2.0,     0.0)),
            ((2.0,     0.0, -pi_1_2), (    0.0,     0.0,    -2.0)),
            ((2.0,     0.0,  pi_1_2), (    0.0,     0.0,     2.0)),
            ((2.0, -pi_1_2, -pi_1_2), (    0.0,     0.0,    -2.0)),
            ((2.0, -pi_1_2,  pi_1_2), (    0.0,     0.0,     2.0)),
            ((2.0,  pi_1_2, -pi_1_2), (    0.0,     0.0,    -2.0)),
            ((2.0,  pi_1_2,  pi_1_2), (    0.0,     0.0,     2.0)),
            ((2.0, -pi_1_4,     0.0), ( sqrt_2, -sqrt_2,     0.0)),
            ((2.0,  pi_1_4,     0.0), ( sqrt_2,  sqrt_2,     0.0)),
            ((2.0,     0.0, -pi_1_4), ( sqrt_2,     0.0, -sqrt_2)),
            ((2.0,     0.0,  pi_1_4), ( sqrt_2,     0.0,  sqrt_2)),
            ((2.0, -pi_1_4, -pi_1_4), (    1.0,    -1.0, -sqrt_2)),
            ((2.0, -pi_1_4,  pi_1_4), (    1.0,    -1.0,  sqrt_2)),
            ((2.0,  pi_1_4, -pi_1_4), (    1.0,     1.0, -sqrt_2)),
            ((2.0,  pi_1_4,  pi_1_4), (    1.0,     1.0,  sqrt_2)),
            ((2.0, -pi_1_2, -pi_1_4), (    0.0, -sqrt_2, -sqrt_2)),
            ((2.0, -pi_1_2,  pi_1_4), (    0.0, -sqrt_2,  sqrt_2)),
            ((2.0,  pi_1_2, -pi_1_4), (    0.0,  sqrt_2, -sqrt_2)),
            ((2.0,  pi_1_2,  pi_1_4), (    0.0,  sqrt_2,  sqrt_2)),
            ((2.0, -pi_1_4, -pi_1_2), (    0.0,     0.0,    -2.0)),
            ((2.0, -pi_1_4,  pi_1_2), (    0.0,     0.0,     2.0)),
            ((2.0,  pi_1_4, -pi_1_2), (    0.0,     0.0,    -2.0)),
            ((2.0,  pi_1_4,  pi_1_2), (    0.0,     0.0,     2.0)),
            ((5.0, math.atan2(-4.0, -3.0), 0.0), (-3.0, -4.0,  0.0)),
            ((5.0, math.atan2(-4.0,  3.0), 0.0), ( 3.0, -4.0,  0.0)),
            ((5.0, math.atan2( 4.0, -3.0), 0.0), (-3.0,  4.0,  0.0)),
            ((5.0, math.atan2( 4.0,  3.0), 0.0), ( 3.0,  4.0,  0.0)),
            ((13.0, 0.0, math.atan2(-5.0, -12.0)), (-12.0,  0.0, -5.0)),
            ((13.0, 0.0, math.atan2(-5.0,  12.0)), ( 12.0,  0.0, -5.0)),
            ((13.0, 0.0, math.atan2( 5.0, -12.0)), (-12.0,  0.0,  5.0)),
            ((13.0, 0.0, math.atan2( 5.0,  12.0)), ( 12.0,  0.0,  5.0))
        ]
    cartesian_to_polar = \
        [
            (( 0.0,  0.0,  0.0), (   0.0,     0.0,     0.0)),
            ((-2.0,  0.0,  0.0), (   2.0,  pi_1_1,     0.0)),
            (( 2.0,  0.0,  0.0), (   2.0,     0.0,     0.0)),
            (( 0.0, -2.0,  0.0), (   2.0, -pi_1_2,     0.0)),
            (( 0.0,  2.0,  0.0), (   2.0,  pi_1_2,     0.0)),
            (( 0.0,  0.0, -2.0), (   2.0,     0.0, -pi_1_2)),
            (( 0.0,  0.0,  2.0), (   2.0,     0.0,  pi_1_2)),
            ((-2.0, -2.0,  0.0), (sqrt_8, -pi_3_4,     0.0)),
            ((-2.0,  2.0,  0.0), (sqrt_8,  pi_3_4,     0.0)),
            (( 2.0, -2.0,  0.0), (sqrt_8, -pi_1_4,     0.0)),
            (( 2.0,  2.0,  0.0), (sqrt_8,  pi_1_4,     0.0)),
            ((-2.0,  0.0, -2.0), (sqrt_8,  pi_1_1, -pi_1_4)),
            ((-2.0,  0.0,  2.0), (sqrt_8,  pi_1_1,  pi_1_4)),
            (( 2.0,  0.0, -2.0), (sqrt_8,     0.0, -pi_1_4)),
            (( 2.0,  0.0,  2.0), (sqrt_8,     0.0,  pi_1_4)),
            (( 0.0, -2.0, -2.0), (sqrt_8, -pi_1_2, -pi_1_4)),
            (( 0.0, -2.0,  2.0), (sqrt_8, -pi_1_2,  pi_1_4)),
            (( 0.0,  2.0, -2.0), (sqrt_8,  pi_1_2, -pi_1_4)),
            (( 0.0,  2.0,  2.0), (sqrt_8,  pi_1_2,  pi_1_4))
        ]


    @classmethod
    def setUpClass(cls):

        cls.V3D = \
            cls.create_vector_class(
                name = 'V3D',
                component_names = 'xyz',
                brackets = '<>',
                sep = ', ',
                cnull = 0,
                cunit = 1,
                functions = None
            )


    @classmethod
    def tearDownClass(cls):

        del cls.V3D


    def test_from_polar(self):

        fail_msg = "Problem with class method 'from_polar'"
        v = \
            self.V3D.from_polar(
                radius = 5.0,
                azimuth = math.atan2(-4.0,  3.0),
                inclination = -math.pi/4.0
            )
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, math.sqrt(4.5), msg=fail_msg)
        self.assertAlmostEqual(y, -math.sqrt(8.0), msg=fail_msg)
        self.assertAlmostEqual(z, -math.sqrt(12.5), msg=fail_msg)


        def verify_from_polar(test_data):

            for polar_coord, cartesian_coord in test_data:
                expected_x, expected_y, expected_z = cartesian_coord
                v = self.V3D.from_polar(*polar_coord)
                x, y, z = v.component_values()
                with self.subTest(polar_coord=polar_coord, cartesian_coord=cartesian_coord):
                    self.assertAlmostEqual(x, expected_x, msg=fail_msg)
                    self.assertAlmostEqual(y, expected_y, msg=fail_msg)
                    self.assertAlmostEqual(z, expected_z, msg=fail_msg)


        verify_from_polar(self.polar_to_cartesian)

### TODO: Add test with negative radius. Should fail.


    def test_cross(self):

        fail_msg = "Problem with method 'cross'"
        u = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(-3.0, 4.0, -5.0)
        v = self.V3D.cross(u, w)
        self.assertListEqual(v.component_values(), [ -3.0, -6.0, -3.0 ], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        v = self.V3D.cross(u, w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, -1, 2)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(0, 0, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(-1, 0, 0)
        w = self.V3D(3, 0, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(0, 2, 0)
        w = self.V3D(0, 1, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(0, 0, 2)
        w = self.V3D(0, 0, -3)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(2, 0, 0)
        w = self.V3D(0, 3, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, 6 ], msg=fail_msg)
        u = self.V3D(0, -3, 0)
        w = self.V3D(-2, 0, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, 0, -6 ], msg=fail_msg)
        u = self.V3D(0, -2, 0)
        w = self.V3D(0, 0, 3)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ -6, 0, 0 ], msg=fail_msg)
        u = self.V3D(0, 0, 3)
        w = self.V3D(0, 2, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ -6, 0, 0 ], msg=fail_msg)
        u = self.V3D(0, 0, -3)
        w = self.V3D(2, 0, 0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, -6, 0 ], msg=fail_msg)
        u = self.V3D(-3, 0, 0)
        w = self.V3D(0, 0, -2)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 0, -6, 0 ], msg=fail_msg)
        u = self.V3D(-2.0, -3.0, -5.0)
        w = self.V3D(7.0, 13.0, 11.0)
        v = u.cross(w)
        self.assertListEqual(v.component_values(), [ 32.0, -13.0, -5.0 ], msg=fail_msg)
        u = self.V3D(-2.0, -3.0, -5.0)
        v = u.cross(-1.5)
        self.assertListEqual(v.component_values(), [ -3.0, 4.5, -1.5 ], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        id_u_before = id(u)
        w = self.V3D(0, 0, 0)
        v = u.cross(w)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_stp(self):

        fail_msg = "Problem with method 'stp'"
        u = self.V3D(0, 0, 0)
        v = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        r = self.V3D.stp(u, v, w)
        self.assertEqual(r, 0, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = self.V3D(-3, 4, -5)
        w = self.V3D(3, 1, 2)
        r = self.V3D.stp(u, v, w)
        self.assertEqual(r, -21, msg=fail_msg)
        u = self.V3D(3, 1, 2)
        v = self.V3D(0, 0, 0)
        w = self.V3D(-3, 4, -5)
        r = u.stp(v, w)
        self.assertEqual(r, 0, msg=fail_msg)
        u = self.V3D(3.0, 1.0, 2.0)
        v = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(0.0, 0.0, 0.0)
        r = u.stp(v, w)
        self.assertEqual(r, 0.0, msg=fail_msg)
        u = self.V3D(2.0, 1.0, 3.0)
        v = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(0.0, 0.0, 0.0)
        r = u.stp(v, w)
        self.assertEqual(r, 0.0, msg=fail_msg)
        u = self.V3D(3.0, 1.0, 2.0)
        v = self.V3D(-3.5, 4.5, -5.0)
        w = self.V3D(0.0, 1.0, -2.5)
        r = u.stp(v, w)
        self.assertEqual(r, -34.5, msg=fail_msg)
        u = self.V3D(3.0, 1.0, 2.0)
        v = self.V3D(-3.5, 4.5, -5.0)
        r = u.stp(-2.0, v)
        self.assertEqual(r, 22.0, msg=fail_msg)
        u = self.V3D(3.0, 1.0, 2.0)
        v = self.V3D(-3.5, 4.5, -5.0)
        r = u.stp(v, 3.0)
        self.assertEqual(r, 33.0, msg=fail_msg)


    def test_vtp(self):

        fail_msg = "Problem with method 'vtp'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        v = self.V3D.vtp(u, w, self.V3D(0, 0, 0))
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(3, 1, 2)
        v = self.V3D.vtp(u, w, self.V3D(0, -1, 2))
        self.assertListEqual(v.component_values(), [-42, -29, 2], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, 5)
        v = self.V3D.vtp(u, w, self.V3D(3, 1, 2))
        self.assertListEqual(v.component_values(), [ -27, 6, 3 ], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(-3, 4, -5)
        v = self.V3D(3, 1, 2).vtp(u, w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D(3.0, 1.0, 2.0).vtp(u, w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D(2.0, 1.0, 3.0).vtp(u, w)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.0)
        w = self.V3D(0.0, 1.0, -2.5)
        v = self.V3D(3.0, 1.0, 2.0).vtp(u, w)
        self.assertListEqual(v.component_values(), [14.0, -2.0, -20.0], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.0)
        w = self.V3D(3.0, 1.0, 2.0)
        v = u.vtp(2.5, w)
        self.assertListEqual(v.component_values(), [-10.0, -30.0, -20.0], msg=fail_msg)
        u = self.V3D(3.0, 1.0, 2.0)
        w = self.V3D(-3.5, 4.5, 5.0)
        v = u.vtp(w, -3.0)
        self.assertListEqual(v.component_values(), [75.0, -69.0, -78.0], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        id_u_before = id(u)
        w = self.V3D(0, 0, 0)
        v = u.vtp(w, self.V3D(0, 0, 0))
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_sin(self):

        fail_msg = "Problem with method 'sin'"
        u = self.V3D(2, 0, 0)
        w = self.V3D(3, 0, 0)
        r = self.V3D.sin(u, w)
        self.assertAlmostEqual(r, 0.0, msg=fail_msg)
        u = self.V3D(0, -3, 0)
        w = self.V3D(0, 2, 0)
        r = self.V3D.sin(u, w)
        self.assertAlmostEqual(r, 0.0, msg=fail_msg)
        u = self.V3D(-3, -4, 0)
        w = self.V3D(4, -3, 0)
        r = u.sin(w)
        self.assertAlmostEqual(r, 1.0, msg=fail_msg)
        u = self.V3D(4.5, -3.0, -1.5)
        r = u.sin(-3.0)
        self.assertAlmostEqual(r, 1.0, msg=fail_msg)
        u = self.V3D(2.0, 0.0, 0.0)
        w = self.V3D(3.0, 0.0, -3.0)
        r = u.sin(w)
        self.assertAlmostEqual(r, math.sqrt(2.0)/2.0, msg=fail_msg)
        u = self.V3D(0.0, 2.0, 0.0)
        w = self.V3D(0.0, -1.0, -math.sqrt(3.0))
        r = u.sin(w)
        self.assertAlmostEqual(r, math.sqrt(3.0)/2, msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            r = u.sin(w)
        u = self.V3D(0, 0, 0)
        w = self.V3D(-3, 4, -5)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            r = u.sin(w)
        u = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            r = u.sin(0)


    def test_rotate_x(self):

        fail_msg = "Problem with method 'rotate_x'"
        u = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D.rotate_x(u, 2*math.pi)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.rotate_x(3*math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, -3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -4.0, msg=fail_msg)
        self.assertAlmostEqual(z, 5.0, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.rotate_x(-5*math.pi/2)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, -3.5, msg=fail_msg)
        self.assertAlmostEqual(y, -5.5, msg=fail_msg)
        self.assertAlmostEqual(z, -4.5, msg=fail_msg)
### TODO: Add more tests


    def test_rotate_y(self):

        fail_msg = "Problem with method 'rotate_y'"
        u = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D.rotate_y(u, 2*math.pi)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.rotate_y(3*math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, 4.0, msg=fail_msg)
        self.assertAlmostEqual(z, 5.0, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.rotate_y(-5*math.pi/2)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 5.5, msg=fail_msg)
        self.assertAlmostEqual(y, 4.5, msg=fail_msg)
        self.assertAlmostEqual(z, -3.5, msg=fail_msg)
### TODO: Add more tests


    def test_rotate_z(self):

        fail_msg = "Problem with method 'rotate_z'"
        u = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D.rotate_z(u, 2*math.pi)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.rotate_z(3*math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -4.0, msg=fail_msg)
        self.assertAlmostEqual(z, -5.0, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.rotate_z(-5*math.pi/2)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 4.5, msg=fail_msg)
        self.assertAlmostEqual(y, 3.5, msg=fail_msg)
        self.assertAlmostEqual(z, -5.5, msg=fail_msg)
### TODO: Add more tests


    def test_axis_rotate(self):

        fail_msg = "Problem with method 'axis_rotate'"
        u = self.V3D(0.0, 0.0, 0.0)
        w = self.V3D(0.0, 1.0, 0.0)
        v = self.V3D.axis_rotate(u, w, 0.0)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(2.0, 0.0, 0.0)
        w = self.V3D(0.0, -3.0, 0.0)
        v = self.V3D.axis_rotate(u, w, math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, -2.0, msg=fail_msg)
        self.assertAlmostEqual(y, 0.0, msg=fail_msg)
        self.assertAlmostEqual(z, 0.0, msg=fail_msg)
        u = self.V3D(0.0, 0.0, 3.0)
        w = self.V3D(-2.0, 0.0, 0.0)
        v = u.axis_rotate(w, -math.pi/2)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 0.0, msg=fail_msg)
        self.assertAlmostEqual(y, -3.0, msg=fail_msg)
        self.assertAlmostEqual(z, 0.0, msg=fail_msg)
        u = self.V3D(-2.0, 3.0, 0.0)
        w = self.V3D(0.0, 0.0, 5.0)
        v = u.axis_rotate(w, math.pi/2)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, -3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -2.0, msg=fail_msg)
        self.assertAlmostEqual(z, 0.0, msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        w = self.V3D(0.0, -1.0, 2.0)
        v = u.axis_rotate(w, math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, 1.6, msg=fail_msg)
        self.assertAlmostEqual(z, -6.2, msg=fail_msg)
        u = self.V3D(3.0, -4.0, 5.0)
        w = self.V3D(0.0, 2.5, 2.0)
        v = u.axis_rotate(w, 4*math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -4.0, msg=fail_msg)
        self.assertAlmostEqual(z, 5.0, msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        w = self.V3D(0.0, -2.5, -2.0)
        v = u.axis_rotate(w, -3*math.pi)
        x, y, z = v.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -4.0, msg=fail_msg)
        self.assertAlmostEqual(z, 5.0, msg=fail_msg)
### TODO: Add more tests
        u = self.V3D(0.0, 0.0, 0.0)
        id_u_before = id(u)
        w = self.V3D(0.0, 1.0, 0.0)
        v = u.axis_rotate(w, 0.0)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(0.0, 0.0, 0.0)
        w = self.V3D(0.0, 0.0, 0.0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.axis_rotate(w, 0.0)


    def test_reorient(self):

        fail_msg = "Problem with method 'reorient'"
### TODO: Add tests


    def test_are_parallel(self):

        fail_msg = "Problem with method 'are_parallel'"
### TODO: Add tests


    def test_polar_as_dict(self):

        fail_msg = "Problem with method 'polar_as_dict'"
        v = self.V3D(math.sqrt(4.5), -math.sqrt(8.0), -math.sqrt(12.5))
        polar = v.polar_as_dict()
        radius = polar['radius']
        azimuth = polar['azimuth']
        inclination = polar['inclination']
        self.assertAlmostEqual(radius, 5.0, msg=fail_msg)
        self.assertAlmostEqual(azimuth, math.atan2(-4.0,  3.0), msg=fail_msg)
        self.assertAlmostEqual(inclination, -math.pi/4, msg=fail_msg)


        def verify_polar_as_dict(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_radius, expected_azimuth, expected_inclination = polar_coord
                v = self.V3D(*cartesian_coord)
                polar = v.polar_as_dict()
                radius = polar['radius']
                azimuth = polar['azimuth']
                inclination = polar['inclination']
                with self.subTest(cartesian_coord=cartesian_coord, polar_coord=polar_coord):
                    self.assertAlmostEqual(radius, expected_radius, msg=fail_msg)
                    self.assertAlmostEqual(azimuth, expected_azimuth, msg=fail_msg)
                    self.assertAlmostEqual(inclination, expected_inclination, msg=fail_msg)


        verify_polar_as_dict(self.cartesian_to_polar)


    def test_radius(self):

        fail_msg = "Problem with property method 'radius'"
        v = self.V3D(-3.0, 0.0, 4.0)
        r = v.radius
        self.assertAlmostEqual(r, 5.0, msg=fail_msg)
        v = self.V3D(1.0, -1.0, 2.0)
        r = v.radius
        self.assertAlmostEqual(r, math.sqrt(6.0), msg=fail_msg)
        v = self.V3D(math.sqrt(4.5), -math.sqrt(8.0), -math.sqrt(12.5))
        r = v.radius
        self.assertAlmostEqual(r, 5.0, msg=fail_msg)


        def verify_radius(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_radius = polar_coord[0]
                v = self.V3D(*cartesian_coord)
                radius = v.radius
                with self.subTest(cartesian_coord=cartesian_coord, radius=expected_radius):
                    self.assertAlmostEqual(radius, expected_radius, msg=fail_msg)


        verify_radius(self.cartesian_to_polar)


    def test_azimuth(self):

        fail_msg = "Problem with property method 'azimuth'"
        v = self.V3D(1.0, -1.0, 2.0)
        r = v.azimuth
        self.assertAlmostEqual(r, -math.pi/4, msg=fail_msg)
        v = self.V3D(math.sqrt(4.5), -math.sqrt(8.0), -math.sqrt(12.5))
        r = v.azimuth
        self.assertAlmostEqual(r, math.atan2(-4.0,  3.0), msg=fail_msg)


        def verify_azimuth(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_azimuth = polar_coord[1]
                v = self.V3D(*cartesian_coord)
                azimuth = v.azimuth
                with self.subTest(cartesian_coord=cartesian_coord, azimuth=expected_azimuth):
                    self.assertAlmostEqual(azimuth, expected_azimuth, msg=fail_msg)


        verify_azimuth(self.cartesian_to_polar)


    def test_inclination(self):

        fail_msg = "Problem with property method 'inclination'"
        v = self.V3D(1.0, -1.0, 2.0)
        r = v.inclination
        self.assertAlmostEqual(r, math.atan2(2, math.sqrt(2)), msg=fail_msg)
        v = self.V3D(math.sqrt(4.5), -math.sqrt(8.0), -math.sqrt(12.5))
        r = v.inclination
        self.assertAlmostEqual(r, -math.pi/4, msg=fail_msg)


        def verify_inclination(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_inclination = polar_coord[2]
                v = self.V3D(*cartesian_coord)
                inclination = v.inclination
                with self.subTest(cartesian_coord=cartesian_coord, inclination=expected_inclination):
                    self.assertAlmostEqual(inclination, expected_inclination, msg=fail_msg)


        verify_inclination(self.cartesian_to_polar)


class Test_Case_tolerant_cartesian_3d_vector(Test_Case_cartesian_3d_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_3D_Vector)

### TODO: Add test methods


if __name__ == "__main__":
    unittest.main()

