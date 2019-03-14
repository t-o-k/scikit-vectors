"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import math
import unittest
import skvectors


class Test_Case_cartesian_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_Vector)


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


    def test_clip(self):

        fail_msg = "Problem with class method 'clip'"
        s = self.V3D.clip(5, 0, 10)
        self.assertEqual(s, 5, msg=fail_msg)
        s = self.V3D.clip(-5, 0, 10)
        self.assertEqual(s, 0, msg=fail_msg)
        s = self.V3D.clip(15, 0, 10)
        self.assertEqual(s, 10, msg=fail_msg)
        s = self.V3D.clip(-5, -10, 0)
        self.assertEqual(s, -5, msg=fail_msg)
        s = self.V3D.clip(5, -10, 0)
        self.assertEqual(s, 0, msg=fail_msg)
        s = self.V3D.clip(-15, -10, 0)
        self.assertEqual(s, -10, msg=fail_msg)
        s = self.V3D.clip(0.0, -3.0, 3.0)
        self.assertEqual(s, 0.0, msg=fail_msg)
        s = self.V3D.clip(-4.0, -3.0, 3.0)
        self.assertEqual(s, -3.0, msg=fail_msg)
        s = self.V3D.clip(4.0, -3.0, 3.0)
        self.assertEqual(s, 3.0, msg=fail_msg)
        s = self.V3D.clip(6.0, 3.5, 8.5)
        self.assertEqual(s, 6.0, msg=fail_msg)
        s = self.V3D.clip(3.0, 3.5, 8.5)
        self.assertEqual(s, 3.5, msg=fail_msg)
        s = self.V3D.clip(9.0, 3.5, 8.5)
        self.assertEqual(s, 8.5, msg=fail_msg)
        s = self.V3D.clip(-6.0, -8.5, -3.5)
        self.assertEqual(s, -6.0, msg=fail_msg)
        s = self.V3D.clip(-3.0, -8.5, -3.5)
        self.assertEqual(s, -3.5, msg=fail_msg)
        s = self.V3D.clip(-9.0, -8.5, -3.5)
        self.assertEqual(s, -8.5, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        s = v.clip(3.0, 1.5, 2.5)
        self.assertEqual(s, 2.5, msg=fail_msg)


    def test_is_zero_vector(self):

        fail_msg = "Problem with method 'is_zero_vector'"
        v = self.V3D(0.0, -1.0, 2.0)
        b = self.V3D.is_zero_vector(v)
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        b = self.V3D.is_zero_vector(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(1, 1, 1)
        b = v.is_zero_vector()
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0.0, 0.0, 0.0)
        b = v.is_zero_vector()
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0, 1, 0)
        b = v.is_zero_vector()
        self.assertFalse(b, msg=fail_msg)


    def test_is_unit_vector(self):

        fail_msg = "Problem with method 'is_unit_vector'"
        v = self.V3D(0, -1, 2)
        b = self.V3D.is_unit_vector(v)
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(1, 0, 0)
        b = self.V3D.is_unit_vector(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0.0, 0.8, -0.6)
        b = self.V3D.is_unit_vector(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0.6, 0.0, -0.8)
        b = v.is_unit_vector()
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(-0.8, -0.6, 0.0)
        b = v.is_unit_vector()
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        b = v.is_unit_vector()
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0.0, 0.0, -1.0)
        b = v.is_unit_vector()
        self.assertTrue(b, msg=fail_msg)


    def test_eq(self):

        fail_msg = "Problem with method '__eq__'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        b = self.V3D.__eq__(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(-3.5, -4.5, -5.5)
        b = self.V3D.__eq__(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(-3.5, 4.5, -5.5)
        b = u.__eq__(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(0.0, -1.0, 2.0)
        b = u == w
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, -2)
        b = u == w
        self.assertFalse(b, msg=fail_msg)


    def test_ne(self):

        fail_msg = "Problem with method '__ne__'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        b = self.V3D.__ne__(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(-3.5, -4.5, -5.5)
        b = self.V3D.__ne__(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(-3.5, 4.5, -5.5)
        b = u.__ne__(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0.0, -1.0, 2.0)
        w = self.V3D(0.0, -1.0, 2.0)
        b = u != w
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, -2)
        b = u != w
        self.assertTrue(b, msg=fail_msg)


    def test_are_orthogonal(self):

        fail_msg = "Problem with method 'are_orthogonal'"
        u = self.V3D(0.0, 0.0, 0.0)
        w = self.V3D(0.0, 0.0, 0.0)
        b = self.V3D.are_orthogonal(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 0, 0)
        b = self.V3D.are_orthogonal(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(-3, 4, -5)
        b = self.V3D.are_orthogonal(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        b = self.V3D.are_orthogonal(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(1.0, 0.0, 0.0)
        w = self.V3D(0.0, 1.0, 0.0)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0.0, 1.0, 0.0)
        w = self.V3D(0.0, 0.0, 1.0)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0.0, 0.0, 1.0)
        w = self.V3D(1.0, 0.0, 0.0)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-1, 0, 0)
        w = self.V3D(0, 2, 0)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, 3, 0)
        w = self.V3D(0, 0, -1)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, 0, -3)
        w = self.V3D(-2, 0, 0)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(3.0, 0, -5.0)
        w = self.V3D(2.5, 0, 1.5)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(2.5, -5.5, 0)
        w = self.V3D(-5.5, -2.5, 0)
        b = u.are_orthogonal(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, 1, 0)
        w = self.V3D(0, 1, 0)
        b = u.are_orthogonal(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0.0, 0.0, -1.0)
        w = self.V3D(0.0, 0.0, 1.0)
        b = u.are_orthogonal(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        b = u.are_orthogonal(0)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        b = u.are_orthogonal(-1)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(4.5, -3.0, -1.5)
        b = u.are_orthogonal(-3.0)
        self.assertTrue(b, msg=fail_msg)


    def test_equal_lengths(self):

        fail_msg = "Problem with method 'equal_lengths'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        b = self.V3D.equal_lengths(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(3.5, 4.5, 5.5)
        b = self.V3D.equal_lengths(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(5.0, 0.0, 0.0)
        w = self.V3D(0.0, 3.0, 4.0)
        b = u.equal_lengths(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -13, 0)
        w = self.V3D(-12, 0, 5)
        b = u.equal_lengths(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(1.0, 0.0, 1.0)
        w = self.V3D(0.0, 2.0, 0.0)
        b = u.equal_lengths(w)
        self.assertFalse(b, msg=fail_msg)


    def test_shorter(self):

        fail_msg = "Problem with method 'shorter'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        b = self.V3D.shorter(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0.0, 1.0, 0.0)
        w = self.V3D(0.0, 0.0, -2.0)
        b = self.V3D.shorter(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(1, 0, 1)
        w = self.V3D(0, 2, 0)
        b = u.shorter(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0.0, 0.0, -2.0)
        w = self.V3D(1.0, 1.0, 0.0)
        b = u.shorter(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.0, 4.5, -5.0)
        w = self.V3D(-4.0, -5.0, 3.0)
        b = u.shorter(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, -1, 2)
        b = u.shorter(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(2.0, 2.0, 2.0)
        b = u.shorter(2.0)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.0, 3.0, -3.0)
        b = u.shorter(2.0)
        self.assertFalse(b, msg=fail_msg)


    def test_longer(self):

        fail_msg = "Problem with method 'longer'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        b = self.V3D.longer(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0.0, 1.0, 0.0)
        w = self.V3D(0.0, 0.0, -2.0)
        b = self.V3D.longer(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(1, 0, 1)
        w = self.V3D(0, 2, 0)
        b = u.longer(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0.0, 0.0, -2.0)
        w = self.V3D(1.0, 1.0, 0.0)
        b = u.longer(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3.0, 4.5, -5.0)
        w = self.V3D(-4.0, -5.0, 3.0)
        b = u.longer(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, -1, 2)
        b = u.longer(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(2.0, 2.0, 2.0)
        b = u.longer(2.0)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.0, 3.0, -3.0)
        b = u.longer(2.0)
        self.assertTrue(b, msg=fail_msg)


    def test_dot(self):

        fail_msg = "Problem with method 'dot'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        s = self.V3D.dot(u, w)
        self.assertEqual(s, 0, msg=fail_msg)
        u = self.V3D(0.0, -1.0, 0.0)
        w = self.V3D(1.0, 0.0, 1.0)
        s = self.V3D.dot(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        s = u.dot(w)
        self.assertEqual(s, -14, msg=fail_msg)
        u = self.V3D(3.0,  4.5, 6.0)
        w = self.V3D(-3.5, 4.0, -5.5)
        s = u.dot(w)
        self.assertAlmostEqual(s, -25.5, msg=fail_msg)
        u = self.V3D(4.5, -3.0, -1.5)
        s = u.dot(-1.5)
        self.assertAlmostEqual(s, 0.0, msg=fail_msg)


    def test_length(self):

        fail_msg = "Problem with method 'length'"
        u = self.V3D(0.0, 0.0, 0.0)
        s = self.V3D.length(u)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(2.0, -1.0, -2.0)
        s = self.V3D.length(u)
        self.assertAlmostEqual(s, 3.0, msg=fail_msg)
        u = self.V3D(0.0, 3.0, 4.0)
        s = u.length()
        self.assertAlmostEqual(s, 5.0, msg=fail_msg)
        u = self.V3D(-0.6, -0.8, 0.0)
        s = u.length()
        self.assertAlmostEqual(s, 1.0, msg=fail_msg)


    def test_distance(self):

        fail_msg = "Problem with method 'distance'"
        u = self.V3D(-5.0, 0.0, 0.0)
        w = self.V3D(0.0, 12.0, 0.0)
        s = self.V3D.distance(u, w)
        self.assertAlmostEqual(s, 13.0, msg=fail_msg)
        u = self.V3D(0, 0, 0)
        s = self.V3D.distance(u, 0)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(-1.5, -1.5, 2.0)
        w = self.V3D(-1.5, 1.0, 2.0)
        s = u.distance(w)
        self.assertEqual(s, 2.5, msg=fail_msg)
        u = self.V3D(0.0, 0.0, 3.0)
        w = self.V3D(4.0, 0.0, 0.0)
        s = u.distance(w)
        self.assertAlmostEqual(s, 5.0, msg=fail_msg)
        u = self.V3D(2.0, 1.0, 2.0)
        s = u.distance(2.0)
        self.assertEqual(s, 1.0, msg=fail_msg)


    def test_normalize(self):

        fail_msg = "Problem with method 'normalize'"
        u = self.V3D(1, 0, 0)
        v = self.V3D.normalize(u)
        self.assertListEqual(v.component_values(), [ 1.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(0, -1, 0)
        v = self.V3D.normalize(u)
        self.assertListEqual(v.component_values(), [ 0.0, -1.0, 0.0 ], msg=fail_msg)
        u = self.V3D(0.0, 0.0, 4.0)
        v = self.V3D.normalize(u)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 1.0 ], msg=fail_msg)
        u = self.V3D(0.0, -3.0, 4.0)
        v = u.normalize()
        self.assertListEqual(v.component_values(), [ 0.0, -0.6, 0.8 ], msg=fail_msg)
        u = self.V3D(-1.5, -2.0, 0.0)
        v = u.normalize()
        self.assertListEqual(v.component_values(), [ -0.6, -0.8, 0.0 ], msg=fail_msg)
        u = self.V3D(1, 0, 0)
        id_u_before = id(u)
        v = u.normalize()
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.normalize()


    def test_project(self):

        fail_msg = "Problem with method 'project'"
        u = self.V3D(-2.0, 0.0, 0.0)
        w = self.V3D(1.0, 0.0, 0.0)
        v = self.V3D.project(u, w)
        self.assertListEqual(v.component_values(), [ -2.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D.project(u, 1.0)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(2.0, 0.0, -2.0)
        w = self.V3D(0.0, 0.0, 1.0)
        v = self.V3D.project(u, w)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, -2.0 ], msg=fail_msg)
        u = self.V3D(1.0, -1.0, 0.0)
        w = self.V3D(2.0, 2.0, 0.0)
        v = u.project(w)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, 5.0)
        w = self.V3D(1.0, 0.0, -1.0)
        v = u.project(w)
        self.assertListEqual(v.component_values(), [ -4.0, 0.0, 4.0 ], msg=fail_msg)
        u = self.V3D(5.0, -4.0, -3.0)
        w = self.V3D(-2.0, 2.0, 0.0)
        v = u.project(w)
        self.assertListEqual(v.component_values(), [ 4.5, -4.5, 0.0 ], msg=fail_msg)
        u = self.V3D(0.0, -3.0, 9.0)
        v = u.project(-2.0)
        self.assertAlmostEqual(v.x, 2.0, msg=fail_msg)
        self.assertAlmostEqual(v.y, 2.0, msg=fail_msg)
        self.assertAlmostEqual(v.z, 2.0, msg=fail_msg)
        u = self.V3D(1, 0, 0)
        id_u_before = id(u)
        w = self.V3D(1, 0, 0)
        v = u.project(w)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(1, 1, 1)
        w = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.project(w)


    def test_inv_project(self):

        fail_msg = "Problem with method 'inv_project'"
        u = self.V3D(0.0, 2.0, 0.0)
        w = self.V3D(0.0, -4.0, 0.0)
        v = self.V3D.inv_project(u, w)
        self.assertListEqual(v.component_values(), [ 0.0, 2.0, 0.0 ], msg=fail_msg)
        u = self.V3D(4.5, -4.5, 0.0)
        w = self.V3D(-10.0, 8.0, 6.0)
        v = u.inv_project(w)
        self.assertListEqual(v.component_values(), [ 5.0, -4.0, -3.0 ], msg=fail_msg)
        u = self.V3D(0.0, -1.0, 2.0)
        v = u.inv_project(-3.0)
        self.assertAlmostEqual(v.x, 5.0, msg=fail_msg)
        self.assertAlmostEqual(v.y, 5.0, msg=fail_msg)
        self.assertAlmostEqual(v.z, 5.0, msg=fail_msg)
        u = self.V3D(1, 0, 0)
        id_u_before = id(u)
        w = self.V3D(1, 0, 0)
        v = u.inv_project(w)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(1, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.inv_project(0)
        u = self.V3D(0, 0, 0)
        w = self.V3D(1, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.inv_project(w)


    def test_reject(self):

        fail_msg = "Problem with method 'reject'"

        u = self.V3D(-2.0, 0.0, 0.0)
        w = self.V3D(1.0, 0.0, 0.0)
        v = self.V3D.reject(u, w)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(0.0, 0.0, 0.0)
        v = self.V3D.reject(u, 1.0)
        self.assertListEqual(v.component_values(), [ 0.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(2.0, 0.0, -2.0)
        w = self.V3D(0.0, 0.0, 1.0)
        v = self.V3D.reject(u, w)
        self.assertListEqual(v.component_values(), [ 2.0, 0.0, 0.0 ], msg=fail_msg)
        u = self.V3D(1.0, -1.0, 0.0)
        w = self.V3D(2.0, 2.0, 0.0)
        v = u.reject(w)
        self.assertListEqual(v.component_values(), [ 1.0, -1.0, 0.0 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, 5.0)
        w = self.V3D(1.0, 0.0, -1.0)
        v = u.reject(w)
        self.assertListEqual(v.component_values(), [ 1.0, 4.0, 1.0 ], msg=fail_msg)
        u = self.V3D(5.0, -4.0, -3.0)
        w = self.V3D(-2.0, 2.0, 0.0)
        v = u.reject(w)
        self.assertListEqual(v.component_values(), [ 0.5, 0.5, -3.0 ], msg=fail_msg)
        u = self.V3D(3.0, 9.0, 0.0)
        v = u.reject(2.0)
        self.assertAlmostEqual(v.x, -1.0, msg=fail_msg)
        self.assertAlmostEqual(v.y, 5.0, msg=fail_msg)
        self.assertAlmostEqual(v.z, -4.0, msg=fail_msg)
        u = self.V3D(1, 0, 0)
        id_u_before = id(u)
        w = self.V3D(1, 0, 0)
        v = u.reject(w)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        u = self.V3D(1, 1, 1)
        w = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.reject(w)


    def test_scalar_project(self):

        fail_msg = "Problem with method 'scalar_project'"
        u = self.V3D(0.0, 0.0, 0.0)
        w = self.V3D(1.0, 0.0, 0.0)
        s = self.V3D.scalar_project(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        w = self.V3D(0.0, 0.0, 1.0)
        s = self.V3D.scalar_project(u, w)
        self.assertEqual(s, -5.0, msg=fail_msg)
        u = self.V3D(-3.0, 6.0, 0.0)
        w = self.V3D(2.0, -1.0, 2.0)
        s = u.scalar_project(w)
        self.assertEqual(s, -4.0, msg=fail_msg)
        u = self.V3D(-3.0, 4.0, 5.0)
        s = u.scalar_project(-2)
        self.assertAlmostEqual(s, -math.sqrt(12.0), msg=fail_msg)
        u = self.V3D(1, 1, 1)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            v = u.scalar_project(0)


    def test_angle(self):

        fail_msg = "Problem with method 'angle'"
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        s = self.V3D.angle(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, -2, 0)
        s = self.V3D.angle(u, w)
        self.assertEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(0, 0, -3)
        w = self.V3D(0, 0, 2)
        s = self.V3D.angle(u, w)
        self.assertAlmostEqual(s, math.pi, msg=fail_msg)
        u = self.V3D(3, 0, -3)
        w = self.V3D(-5, 0, 0)
        s = u.angle(w)
        self.assertAlmostEqual(s, math.pi*3/4, msg=fail_msg)
        u = self.V3D(0.0, -3.0, 0.0)
        w = self.V3D(0.0, -4.0, -4.0)
        s = u.angle(w)
        self.assertAlmostEqual(s, math.pi/4, msg=fail_msg)
        u = self.V3D(2.0, 0.0, 0.0)
        w = self.V3D(3.0, 0.0, -3.0)
        s = u.angle(w)
        self.assertAlmostEqual(s, math.pi/4, msg=fail_msg)
        u = self.V3D(4.5, -3.0, -1.5)
        s = u.angle(-3.0)
        self.assertAlmostEqual(s, math.pi/2, msg=fail_msg)
        u = self.V3D(4.5, -3.0, -1.5)
        s = u.angle(3.0)
        self.assertAlmostEqual(s, math.pi/2, msg=fail_msg)


    def test_cos(self):

        fail_msg = "Problem with method 'cos'"
        u = self.V3D(2, 0, 0)
        w = self.V3D(3, 0, 0)
        s = self.V3D.cos(u, w)
        self.assertAlmostEqual(s, 1.0, msg=fail_msg)
        u = self.V3D(0, -3, 0)
        w = self.V3D(0, 2, 0)
        s = self.V3D.cos(u, w)
        self.assertAlmostEqual(s, -1.0, msg=fail_msg)
        u = self.V3D(-3, -4, 0)
        w = self.V3D(4, -3, 0)
        s = u.cos(w)
        self.assertAlmostEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(4.5, -3.0, -1.5)
        s = u.cos(-3.0)
        self.assertAlmostEqual(s, 0.0, msg=fail_msg)
        u = self.V3D(2.0, 0.0, 0.0)
        w = self.V3D(3.0, 0.0, -3.0)
        s = u.cos(w)
        self.assertAlmostEqual(s, math.sqrt(2.0)/2.0, msg=fail_msg)
        u = self.V3D(0.0, 2.0, 0.0)
        w = self.V3D(0.0, -1.0, -math.sqrt(3.0))
        s = u.cos(w)
        self.assertAlmostEqual(s, -0.5, msg=fail_msg)
        u = self.V3D(0, 0, 0)
        w = self.V3D(0, 0, 0)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            s = u.cos(w)
        u = self.V3D(0, 0, 0)
        w = self.V3D(-3, 4, -5)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            s = u.cos(w)
        u = self.V3D(0, -1, 2)
        with self.assertRaises(ZeroDivisionError, msg=fail_msg):
            s = u.cos(0)

### TODO ?:
#     def test_imatmul(self):
#
#         fail_msg = "Problem with method '__imatmul__'"


class Test_Case_tolerant_cartesian_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_Vector)


class Test_Case_cartesian_3d_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_3D_Vector)


class Test_Case_tolerant_cartesian_3d_vector(Test_Case_cartesian_3d_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_3D_Vector)


if __name__ == "__main__":
    unittest.main()

