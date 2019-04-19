"""
Copyright (c) 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import math
import unittest
import skvectors


class Test_Case_tolerant_cartesian_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_Vector)
    abs_tol = 1e-12
    rel_tol = 1e-9

    @classmethod
    def setUpClass(cls):

        cls.V4D = \
            cls.create_vector_class(
                name = 'V4D',
                component_names = 'abcd',
                brackets = '<>',
                sep = ', ',
                cnull = 0,
                cunit = 1,
                functions = None,
                abs_tol = cls.abs_tol,
                rel_tol = cls.rel_tol
            )


    @classmethod
    def tearDownClass(cls):

        del cls.V4D


    def test_tolerance_all(self):

        fail_msg = "Problem with method 'tolerance_all'"
        r = self.V4D.tolerance_all([ ])
        self.assertEqual(r, self.abs_tol, msg=fail_msg)
        u = self.V4D(0.0, 0.0, 0.0, 0.0)
        r = self.V4D.tolerance_all([ u ])
        self.assertEqual(r, self.abs_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, 0.8, -0.4)
        r = self.V4D.tolerance_all([ u ])
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, 0.0, 0.0, 0.0)
        v = self.V4D(0.0, 0.0, 0.0, 0.0)
        r = self.V4D.tolerance_all([ u, v ])
        self.assertEqual(r, self.abs_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, 0.8, -0.4)
        v = self.V4D(0.0, 0.6, -0.8, 0.0)
        r = self.V4D.tolerance_all([ u, v ])
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, 0.8, -0.4)
        v = self.V4D(1.0, -2.0, -4.0, 2.0)
        r = self.V4D.tolerance_all([ u, v ])
        self.assertEqual(r, self.rel_tol * 5, msg=fail_msg)
        u = self.V4D(-1.0, 2.0, -4.0, 2.0)
        v = self.V4D(0.2, -0.4, 0.8, -0.4)
        r = self.V4D.tolerance_all([ u, v ])
        self.assertEqual(r, self.rel_tol * 5, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, 0.8, -0.4)
        v = self.V4D(0.0, 0.6, -0.8, 0.0)
        w = self.V4D(-1.0, 2.0, -4.0, 2.0)
        r = self.V4D.tolerance_all([ u, v, w ])
        self.assertEqual(r, self.rel_tol * 5, msg=fail_msg)


    def test_tolerance_with(self):

        fail_msg = "Problem with method 'tolerance_with'"
        u = self.V4D(0.0, 0.0, 0.0, 0.0)
        v = self.V4D(0.0, 0.0, 0.0, 0.0)
        r = self.V4D.tolerance_with(u, v)
        self.assertEqual(r, self.abs_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, 0.8, -0.4)
        v = self.V4D(0.0, 0.6, -0.8, 0.0)
        r = u.tolerance_with(v)
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, 0.8, -0.4)
        v = self.V4D(1.0, -2.0, -4.0, 2.0)
        r = u.tolerance_with(v)
        self.assertEqual(r, self.rel_tol * 5, msg=fail_msg)
        u = self.V4D(-1.0, 2.0, -4.0, 2.0)
        v = self.V4D(0.2, -0.4, 0.8, -0.4)
        r = u.tolerance_with(v)
        self.assertEqual(r, self.rel_tol * 5, msg=fail_msg)


    def test_tolerance(self):

        fail_msg = "Problem with method 'tolerance'"
        u = self.V4D(0.0, 0.0, 0.0, 0.0)
        r = self.V4D.tolerance(u)
        self.assertEqual(r, self.abs_tol, msg=fail_msg)
        u = self.V4D(1.0, 0.0, 0.0, 0.0)
        r = u.tolerance()
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, -1.0, 0.0, 0.0)
        r = u.tolerance()
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, 0.0, 1.0, 0.0)
        r = u.tolerance()
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, 0.0, 0.0, -1.0)
        r = u.tolerance()
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, -0.8, 0.4)
        r = u.tolerance()
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(200, 400, 800, 400)
        r = u.tolerance()
        self.assertEqual(r, self.rel_tol * 1000, msg=fail_msg)
        u = self.V4D(-0.0002, -0.0004, -0.0008, -0.0004)
        r = u.tolerance()
        self.assertAlmostEqual(r, self.rel_tol / 1000, msg=fail_msg)


    def test_tol(self):

        fail_msg = "Problem with property method 'tol'"
        u = self.V4D(0.0, 0.0, 0.0, 0.0)
        r = u.tol
        self.assertEqual(r, self.abs_tol, msg=fail_msg)
        u = self.V4D(-1.0, 0.0, 0.0, 0.0)
        r = u.tol
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, 1.0, 0.0, 0.0)
        r = u.tol
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, 0.0, -1.0, 0.0)
        r = u.tol
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(0.0, 0.0, 0.0, 1.0)
        r = u.tol
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(-0.2, 0.4, -0.8, 0.4)
        r = u.tol
        self.assertEqual(r, self.rel_tol, msg=fail_msg)
        u = self.V4D(-200, -400, -800, -400)
        r = u.tol
        self.assertEqual(r, self.rel_tol * 1000, msg=fail_msg)
        u = self.V4D(0.0002, 0.0004, 0.0008, 0.0004)
        r = u.tol
        self.assertAlmostEqual(r, self.rel_tol / 1000, msg=fail_msg)


    # def test_eq(self):
    # 
    #     fail_msg = "Problem with method '__eq__'"


    # def test_ne(self):
    # 
    #     fail_msg = "Problem with method '__ne__'"


    # def test_are_orthogonal(self):
    # 
    #     fail_msg = "Problem with method 'are_orthogonal'"


    # def test_equal_lengths(self):
    # 
    #     fail_msg = "Problem with method 'equal_lengths'"


    # def test_shorter(self):
    # 
    #     fail_msg = "Problem with method 'shorter'"


    # def test_longer(self):
    # 
    #     fail_msg = "Problem with method 'longer'"


    # def test_round_components(self):
    # 
    #     fail_msg = "Problem with method 'round_components'"

