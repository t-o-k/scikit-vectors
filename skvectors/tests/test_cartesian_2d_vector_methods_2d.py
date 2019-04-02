"""
Copyright (c) 2018-2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import math
import unittest
import skvectors


class Test_Case_cartesian_2d_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_2D_Vector)

    pi_1_4 = math.pi / 4.0
    pi_1_2 = math.pi / 2.0
    pi_3_4 = math.pi * 3.0 / 4.0
    pi_1_1 = math.pi
    sqrt_2 = math.sqrt(2.0)
    sqrt_8 = math.sqrt(8.0)
    polar_to_cartesian = \
        [
            ((0.0,  pi_1_4), (    0.0,     0.0)),
            ((2.0,     0.0), (    2.0,     0.0)),
            ((2.0, -pi_1_1), (   -2.0,     0.0)),
            ((2.0,  pi_1_1), (   -2.0,     0.0)),
            ((2.0, -pi_1_2), (    0.0,    -2.0)),
            ((2.0,  pi_1_2), (    0.0,     2.0)),
            ((2.0, -pi_1_4), ( sqrt_2, -sqrt_2)),
            ((2.0,  pi_1_4), ( sqrt_2,  sqrt_2)),
            ((5.0, math.atan2(-4.0, -3.0)), (-3.0, -4.0)),
            ((5.0, math.atan2(-4.0,  3.0)), ( 3.0, -4.0)),
            ((5.0, math.atan2( 4.0, -3.0)), (-3.0,  4.0)),
            ((5.0, math.atan2( 4.0,  3.0)), ( 3.0,  4.0))
        ]
    cartesian_to_polar = \
        [
            (( 0.0,  0.0), (   0.0,     0.0)),
            ((-2.0,  0.0), (   2.0,  pi_1_1)),
            (( 2.0,  0.0), (   2.0,     0.0)),
            (( 0.0, -2.0), (   2.0, -pi_1_2)),
            (( 0.0,  2.0), (   2.0,  pi_1_2)),
            ((-2.0, -2.0), (sqrt_8, -pi_3_4)),
            ((-2.0,  2.0), (sqrt_8,  pi_3_4)),
            (( 2.0, -2.0), (sqrt_8, -pi_1_4)),
            (( 2.0,  2.0), (sqrt_8,  pi_1_4))
        ]


    @classmethod
    def setUpClass(cls):

        cls.V2D = \
            cls.create_vector_class(
                name = 'V2D',
                component_names = 'xy',
                brackets = '<>',
                sep = ', ',
                cnull = 0,
                cunit = 1,
                functions = None
            )


    @classmethod
    def tearDownClass(cls):

        del cls.V2D


    def test_from_polar(self):

        fail_msg = "Problem with class method 'from_polar'"
        u = \
            self.V2D.from_polar(
                radius = 5.0,
                azimuth = math.atan2(-4.0,  3.0)
            )
        x, y = u.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -4.0, msg=fail_msg)


        def verify_from_polar(test_data):

            for polar_coord, cartesian_coord in test_data:
                expected_x, expected_y = cartesian_coord
                u = self.V2D.from_polar(*polar_coord)
                x, y = u.component_values()
                with self.subTest(polar_coord=polar_coord, cartesian_coord=cartesian_coord):
                    self.assertAlmostEqual(x, expected_x, msg=fail_msg)
                    self.assertAlmostEqual(y, expected_y, msg=fail_msg)


        verify_from_polar(self.polar_to_cartesian)

### TODO: Add test with negative radius. Should fail.


    def test_perp(self):

        fail_msg = "Problem with method 'perp'"
        u = self.V2D(0.0, 0.0)
        v = self.V2D.perp(u)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0 ], msg=fail_msg)
        u = self.V2D(3, -4)
        v = self.V2D.perp(u)
        self.assertListEqual(v.component_values(), [ 4, 3 ], msg=fail_msg)
        u = self.V2D(-2.0, 0.0)
        v = u.perp()
        self.assertListEqual(v.component_values(), [ 0.0, -2.0 ], msg=fail_msg)
        u = self.V2D(0.0, 3.0)
        v = u.perp()
        self.assertListEqual(v.component_values(), [ -3.0, 0.0 ], msg=fail_msg)
        u = self.V2D(-1.5, -2.5)
        v = u.perp()
        self.assertListEqual(v.component_values(), [ 2.5, -1.5 ], msg=fail_msg)


    def test_perp_dot(self):

        fail_msg = "Problem with method 'perp_dot'"
        u = self.V2D(0.0, 0.0)
        w = self.V2D(0.0, 0.0)
        s = self.V2D.perp_dot(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V2D(3, -4)
        w = self.V2D(0.0, 0.0)
        s = self.V2D.perp_dot(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V2D(0.0, 0.0)
        w = self.V2D(2, 1)
        s = u.perp_dot(w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V2D(-1.5, 2.5)
        w = self.V2D(-3, 5)
        s = u.perp_dot(w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V2D(3, -4)
        w = self.V2D(2, 1)
        s = u.perp_dot(w)
        self.assertEqual(s, 11, msg=fail_msg)
        u = self.V2D(2, -3)
        w = self.V2D(1, -4)
        s = u.perp_dot(w)
        self.assertEqual(s, -5, msg=fail_msg)


    def test_sin(self):

        fail_msg = "Problem with method 'sin'"
        u = self.V2D(2, 0)
        w = self.V2D(3, 0)
        r = self.V2D.sin(u, w)
        self.assertEqual(r, 0.0, msg=fail_msg)
        u = self.V2D(0, -3)
        w = self.V2D(0, 2)
        r = self.V2D.sin(u, w)
        self.assertEqual(r, 0, msg=fail_msg)
        u = self.V2D(-3, -4)
        w = self.V2D(8, -6)
        r = u.sin(w)
        self.assertAlmostEqual(r, 1, msg=fail_msg)
        u = self.V2D(0.0, 3.0)
        r = u.sin(-3.0)
        self.assertAlmostEqual(r, math.sqrt(2.0)/2.0, msg=fail_msg)
        u = self.V2D(2.0, 0.0)
        w = self.V2D(3.0, -3.0)
        r = u.sin(w)
        self.assertAlmostEqual(r, -math.sqrt(2.0)/2.0, msg=fail_msg)
        u = self.V2D(2.0, 0.0)
        w = self.V2D(-1.0, -math.sqrt(3.0))
        r = u.sin(w)
        self.assertAlmostEqual(r, -math.sqrt(3.0)/2.0, msg=fail_msg)
        u = self.V2D(0, 0)
        w = self.V2D(0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            r = u.sin(w)
        u = self.V2D(0, 0)
        w = self.V2D(-3, 4)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            r = u.sin(w)
        u = self.V2D(-1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            r = u.sin(0)


    def test_angle(self):

        fail_msg = "Problem with method 'angle'"
        u = self.V2D(0.0, 0.0)
        w = self.V2D(0.0, 0.0)
        s = self.V2D.angle(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V2D(0, -3)
        w = self.V2D(0, 2)
        s = self.V2D.angle(u, w)
        self.assertAlmostEqual(s, math.pi, msg=fail_msg)
        u = self.V2D(1.5, 0)
        w = self.V2D(0, 2.5)
        s = self.V2D.angle(u, w)
        self.assertAlmostEqual(s, math.pi / 2, msg=fail_msg)
        u = self.V2D(-1.5, 0)
        w = self.V2D(0, -2.5)
        s = self.V2D.angle(u, w)
        self.assertAlmostEqual(s, -math.pi * 1.5, msg=fail_msg)
        u = self.V2D(0, -2.5)
        w = self.V2D(-3.5, -3.5)
        s = self.V2D.angle(u, w)
        self.assertAlmostEqual(s, -math.pi / 4, msg=fail_msg)


    def test_rotate(self):

        fail_msg = "Problem with method 'rotate'"
        u = self.V2D(0.0, 0.0)
        v = self.V2D.rotate(u, 0.0)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0 ], msg=fail_msg)
        u = self.V2D(0.0, 0.0)
        v = self.V2D.rotate(u, math.pi * 2)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0 ], msg=fail_msg)
        u = self.V2D(1.0, -1.5)
        v = u.rotate(0.0)
        x, y = v.component_values()
        self.assertAlmostEqual(x, 1.0, msg=fail_msg)
        self.assertAlmostEqual(y, -1.5, msg=fail_msg)
        u = self.V2D(-3, 4)
        v = u.rotate(math.pi)
        x, y = v.component_values()
        self.assertAlmostEqual(x, 3, msg=fail_msg)
        self.assertAlmostEqual(y, -4, msg=fail_msg)
        u = self.V2D(-3.0, 4.0)
        v = u.rotate(math.pi * 3)
        x, y = v.component_values()
        self.assertAlmostEqual(x, 3.0, msg=fail_msg)
        self.assertAlmostEqual(y, -4.0, msg=fail_msg)
        u = self.V2D(-3.5, 4.5)
        v = u.rotate(-math.pi * 2.5)
        x, y = v.component_values()
        self.assertAlmostEqual(x, 4.5, msg=fail_msg)
        self.assertAlmostEqual(y, 3.5, msg=fail_msg)
        u = self.V2D(1.5, -1.5)
        v = u.rotate(-math.pi / 4)
        x, y = v.component_values()
        self.assertAlmostEqual(x, 0, msg=fail_msg)
        self.assertAlmostEqual(y, -1.5 * 2**0.5, msg=fail_msg)
### TODO: Add more tests


    def test_are_parallel(self):

        fail_msg = "Problem with method 'are_parallel'"
        u = self.V2D(0.0, 0.0)
        w = self.V2D(0.0, 0.0)
        self.assertTrue(self.V2D.are_parallel(u, w), msg=fail_msg)
        u = self.V2D(-3.0, 4.0)
        w = self.V2D(0.0, 0.0)
        self.assertTrue(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(0.0, 0.0)
        w = self.V2D(-1.0, -1.5)
        self.assertTrue(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(-6, 8)
        w = self.V2D(-3.0, 4.0)
        self.assertTrue(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(1.5, -2.0)
        w = self.V2D(-3.0, 4.0)
        self.assertTrue(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(1.0, 0.0)
        w = self.V2D(0.0, 1.0)
        self.assertFalse(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(-3.0, 4.0)
        w = self.V2D(-3.0, -4.0)
        self.assertFalse(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(-2.0, 2.5)
        w = self.V2D(2.5, -2.0)
        self.assertFalse(u.are_parallel(w), msg=fail_msg)
        u = self.V2D(2.5, -2.0)
        w = self.V2D(-4.0, -5.0)
        self.assertFalse(u.are_parallel(w), msg=fail_msg)
### TODO: Add more tests


    def test_reorient(self):

        fail_msg = "Problem with method 'reorient'"
        u = self.V2D(-3, 4)
        w1 = self.V2D(1, 0)
        w2 = self.V2D(2, 0)
        v = self.V2D.reorient(u, w1, w2)
        x, y = v.component_values()
        self.assertAlmostEqual(x, -3, msg=fail_msg)
        self.assertAlmostEqual(y, 4, msg=fail_msg)
        u = self.V2D(-3, 4)
        w1 = self.V2D(0, 2)
        w2 = self.V2D(0, -3)
        v = self.V2D.reorient(u, w1, w2)
        x, y = v.component_values()
        self.assertAlmostEqual(x, 3, msg=fail_msg)
        self.assertAlmostEqual(y, -4, msg=fail_msg)
        u = self.V2D(-3.0, 4.0)
        w1 = self.V2D(1.0, 3.0)
        w2 = self.V2D(-1.5, 0.5)
        v = u.reorient(w1, w2)
        x, y = v.component_values()
        self.assertAlmostEqual(x, -4.0, msg=fail_msg)
        self.assertAlmostEqual(y, -3.0, msg=fail_msg)


    def test_polar_as_dict(self):

        fail_msg = "Problem with method 'polar_as_dict'"
        v = self.V2D(3.0, -4.0)
        polar = v.polar_as_dict()
        self.assertTrue('radius' in polar, msg=fail_msg)
        radius = polar['radius']
        self.assertAlmostEqual(radius, 5.0, msg=fail_msg)
        self.assertTrue('azimuth' in polar, msg=fail_msg)
        azimuth = polar['azimuth']
        self.assertAlmostEqual(azimuth, math.atan2(-4.0,  3.0), msg=fail_msg)


        def verify_polar_as_dict(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_radius, expected_azimuth = polar_coord
                v = self.V2D(*cartesian_coord)
                polar = v.polar_as_dict()
                radius = polar['radius']
                azimuth = polar['azimuth']
                with self.subTest(cartesian_coord=cartesian_coord, polar_coord=polar_coord):
                    self.assertAlmostEqual(radius, expected_radius, msg=fail_msg)
                    self.assertAlmostEqual(azimuth, expected_azimuth, msg=fail_msg)


        verify_polar_as_dict(self.cartesian_to_polar)


    def test_radius(self):

        fail_msg = "Problem with property method 'radius'"
        v = self.V2D(0.0, 0.0)
        r = v.radius
        self.assertEqual(r, 0.0, msg=fail_msg)
        v = self.V2D(-3.0, 4.0)
        r = v.radius
        self.assertAlmostEqual(r, 5.0, msg=fail_msg)
        v = self.V2D(-5, -12)
        r = v.radius
        self.assertAlmostEqual(r, 13.0, msg=fail_msg)


        def verify_radius(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_radius = polar_coord[0]
                v = self.V2D(*cartesian_coord)
                radius = v.radius
                with self.subTest(cartesian_coord=cartesian_coord, radius=expected_radius):
                    self.assertAlmostEqual(radius, expected_radius, msg=fail_msg)


        verify_radius(self.cartesian_to_polar)


    def test_azimuth(self):

        fail_msg = "Problem with property method 'azimuth'"
        v = self.V2D(1.0, 0.0)
        r = v.azimuth
        self.assertAlmostEqual(r, 0.0, msg=fail_msg)
        v = self.V2D(-4.0, 3.0)
        r = v.azimuth
        self.assertAlmostEqual(r, math.atan2(3.0, -4.0), msg=fail_msg)


        def verify_azimuth(test_data):

            for cartesian_coord, polar_coord in test_data:
                expected_azimuth = polar_coord[1]
                v = self.V2D(*cartesian_coord)
                azimuth = v.azimuth
                with self.subTest(cartesian_coord=cartesian_coord, azimuth=expected_azimuth):
                    self.assertAlmostEqual(azimuth, expected_azimuth, msg=fail_msg)


        verify_azimuth(self.cartesian_to_polar)


class Test_Case_tolerant_cartesian_2d_vector(Test_Case_cartesian_2d_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_2D_Vector)


    # def test_are_parallel(self):


if __name__ == "__main__":
    unittest.main()

