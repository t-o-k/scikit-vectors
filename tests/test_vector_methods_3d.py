"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import unittest
import skvectors


class Test_Case_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Vector)


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


    def test_component_null(self):

        fail_msg = "Problem with class method 'component_null'"
        s = self.V3D.component_null()
        self.assertEqual(s, 0, msg=fail_msg)
        v = self.V3D(-3, 4, 5)
        s = v.component_null()
        self.assertEqual(s, 0, msg=fail_msg)


    def test_component_unit(self):

        fail_msg = "Problem with class method 'component_unit'"
        s = self.V3D.component_unit()
        self.assertEqual(s, 1, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        s = v.component_unit()
        self.assertEqual(s, 1, msg=fail_msg)


    def test_basis_x(self):

        fail_msg = "Problem with class method 'basis_x'"
        v = self.V3D.basis_x()
        self.assertListEqual(v.component_values(), [ 1, 0, 0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u.basis_x()
        self.assertListEqual(v.component_values(), [ 1, 0, 0 ], msg=fail_msg)
        u = self.V3D(1, 0, 0)
        id_u_before = id(u)
        v = u.basis_x()
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_basis_y(self):

        fail_msg = "Problem with class method 'basis_y'"
        v = self.V3D.basis_y()
        self.assertListEqual(v.component_values(), [ 0, 1, 0 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u.basis_y()
        self.assertListEqual(v.component_values(), [ 0, 1, 0 ], msg=fail_msg)
        u = self.V3D(0, 1, 0)
        id_u_before = id(u)
        v = u.basis_y()
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_basis_z(self):

        fail_msg = "Problem with class method 'basis_z'"
        v = self.V3D.basis_z()
        self.assertListEqual(v.component_values(), [ 0, 0, 1 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u.basis_z()
        self.assertListEqual(v.component_values(), [ 0, 0, 1 ], msg=fail_msg)
        u = self.V3D(0, 0, 1)
        id_u_before = id(u)
        v = u.basis_z()
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_repeat_cvalue(self):

        fail_msg = "Problem with class method 'repeat_cvalue'"
        v = self.V3D.repeat_cvalue(0)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        v = self.V3D.repeat_cvalue(-3)
        self.assertListEqual(v.component_values(), [ -3, -3, -3 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u.repeat_cvalue(2.5)
        self.assertListEqual(v.component_values(), [ 2.5, 2.5, 2.5 ], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        id_u_before = id(u)
        v = u.repeat_cvalue(0)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_sum_of_vectors(self):

        fail_msg = "Problem with class method 'sum_of_vectors'"
        vectors = [ ]
        v = self.V3D.sum_of_vectors(vectors)
        self.assertListEqual(v.component_values(), [ 0, 0, 0 ], msg=fail_msg)
        vectors = \
            [
                self.V3D(0, -1, 2),
                self.V3D(-3, 4, -5),
                self.V3D(6, -7, 0)
            ]
        v = self.V3D.sum_of_vectors(vectors)
        self.assertListEqual(v.component_values(), [ 3, -4, -3 ], msg=fail_msg)
        u = self.V3D(2, -1, 3)
        vectors = \
            [
                self.V3D(0, -1, 2),
                self.V3D(-3, 4, -5),
            ]
        v = u.sum_of_vectors(vectors)
        self.assertListEqual(v.component_values(), [ -3, 3, -3 ], msg=fail_msg)
        u = self.V3D(0, 0, 0)
        id_u_before = id(u)
        vectors = [ u ]
        v = self.V3D.sum_of_vectors(vectors)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_prod_of_vectors(self):

        fail_msg = "Problem with class method 'prod_of_vectors'"
        vectors = [ ]
        v = self.V3D.prod_of_vectors(vectors)
        self.assertListEqual(v.component_values(), [ 1, 1, 1 ], msg=fail_msg)
        vectors = \
            [
                self.V3D(0, -1, 2),
                self.V3D(-3, 4, -5),
                self.V3D(6, -7, 0)
            ]
        v = self.V3D.prod_of_vectors(vectors)
        self.assertListEqual(v.component_values(), [ 0, 28, 0 ], msg=fail_msg)
        u = self.V3D(2, -1, 3)
        vectors = \
            [
                self.V3D(0, -1, 2),
                self.V3D(-3, 4, -5),
            ]
        v = u.prod_of_vectors(vectors)
        self.assertListEqual(v.component_values(), [ 0, -4, -10 ], msg=fail_msg)
        id_u_before = id(u)
        vectors = [ u ]
        v = self.V3D.prod_of_vectors(vectors)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_is_zero_vector(self):

        fail_msg = "Problem with method 'is_zero_vector'"
        v = self.V3D(0, 0, 0)
        b = self.V3D.is_zero_vector(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        b = v.is_zero_vector()
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(2, 0, 0)
        b = v.is_zero_vector()
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0, -1, 0)
        b = v.is_zero_vector()
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0, 0, 1)
        b = v.is_zero_vector()
        self.assertFalse(b, msg=fail_msg)


    def test_bool(self):

        fail_msg = "Problem with method '__bool__'"
        v = self.V3D(0, 0, 0)
        b = self.V3D.__bool__(v)
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0, 0, 0)
        b = bool(v)
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(2, 0, 0)
        b = bool(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0, -1, 0)
        b = bool(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0, 0, 1)
        b = bool(v)
        self.assertTrue(b, msg=fail_msg)


    def test_sum_of_components(self):

        fail_msg = "Problem with method 'sum_of_components'"
        v = self.V3D(0, 0, 0)
        s = self.V3D.sum_of_components(v)
        self.assertEqual(s, 0, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        s = v.sum_of_components()
        self.assertEqual(s, 1, msg=fail_msg)
        v = self.V3D(-3.5, 4.5, -5.5)
        s = v.sum_of_components()
        self.assertEqual(s, -4.5, msg=fail_msg)


    def test_prod_of_components(self):

        fail_msg = "Problem with method 'prod_of_components'"
        v = self.V3D(0, 0, 0)
        s = self.V3D.prod_of_components(v)
        self.assertEqual(s, 0, msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        s = v.prod_of_components()
        self.assertEqual(s, 60, msg=fail_msg)
        v = self.V3D(1.5, -2.0, 3.5)
        s = v.prod_of_components()
        self.assertEqual(s, -10.5, msg=fail_msg)


    def test_cnull(self):

        fail_msg = "Problem with property method 'cnull'"
        v = self.V3D(-3, 4, -5)
        s = v.cnull
        self.assertEqual(s, 0, msg=fail_msg)


    def test_cunit(self):

        fail_msg = "Problem with property method 'cunit'"
        v = self.V3D(-3, 4, -5)
        s = v.cunit
        self.assertEqual(s, 1, msg=fail_msg)


    def test_csum(self):

        fail_msg = "Problem with property method 'csum'"
        v = self.V3D(0, 0, 0)
        s = v.csum
        self.assertEqual(s, 0, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        s = v.csum
        self.assertEqual(s, 1, msg=fail_msg)
        v = self.V3D(0.5, -1.0, 0)
        s = v.csum
        self.assertEqual(s, -0.5, msg=fail_msg)
        v = self.V3D(-3.5, 4.5, -5.5)
        s = v.csum
        self.assertEqual(s, -4.5, msg=fail_msg)


    def test_cprod(self):

        fail_msg = "Problem with property method 'cprod'"
        v = self.V3D(0, 0, 0)
        s = v.cprod
        self.assertEqual(s, 0, msg=fail_msg)
        v = self.V3D(0, -1, -2)
        s = v.cprod
        self.assertEqual(s, 0, msg=fail_msg)
        v = self.V3D(-3.0, 4.5, 0.0)
        s = v.cprod
        self.assertEqual(s, 0.0, msg=fail_msg)
        v = self.V3D(1.5, -2.0, 3.5)
        s = v.cprod
        self.assertEqual(s, -10.5, msg=fail_msg)


class Test_Case_cartesian_vector(Test_Case_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_Vector)


    def test_is_zero_vector(self):

        fail_msg = "Problem with method 'is_zero_vector'"
        v = self.V3D(0, 0, 0)
        b = self.V3D.is_zero_vector(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0.0, 1.0, -1.0)
        b = v.is_zero_vector()
        self.assertFalse(b, msg=fail_msg)


class Test_Case_tolerant_cartesian_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_Vector)


class Test_Case_cartesian_3d_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_3D_Vector)


class Test_Case_tolerant_cartesian_3d_vector(Test_Case_cartesian_3d_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_3D_Vector)


if __name__ == "__main__":
    unittest.main()

