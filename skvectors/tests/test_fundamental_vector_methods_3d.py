"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import unittest
import skvectors


class Test_Case_fundamental_vector(unittest.TestCase):

    create_vector_class = staticmethod(skvectors.create_class_Fundamental_Vector)


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


    def test_init(self):

        fail_msg = "Problem with method '__init__'"
        v = self.V3D(x=-3.0, y=4.0, z=-5.0)
        self.assertEqual(v._cvalues, [-3.0, 4.0, -5.0], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        self.assertEqual(v._cvalues, [0, -1, 2], msg=fail_msg)
        # with self.assertRaises(TypeError, msg=fail_msg):
        #     v = self.V3D(x='a', y='b', z='c')
        with self.assertRaises(TypeError, msg=fail_msg):
            v = self.V3D()
        with self.assertRaises(TypeError, msg=fail_msg):
            v = self.V3D([1, 2, 3])
        with self.assertRaises(TypeError, msg=fail_msg):
            v = self.V3D(x=1, y=2)
        with self.assertRaises(TypeError, msg=fail_msg):
            v = self.V3D(1, 2, 3, 4)
        with self.assertRaises(TypeError, msg=fail_msg):
            v = self.V3D(1, y=2, z=3)
        with self.assertRaises(ValueError, msg=fail_msg):
            v = self.V3D(X=1, Y=2, Z=3)


    def test_dimensions(self):

        fail_msg = "Problem with class method 'dimension'"
        n = self.V3D.dimensions()
        self.assertEqual(n, 3, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        n = v.dimensions()
        self.assertEqual(n, 3, msg=fail_msg)


    def test_len(self):

        fail_msg = "Problem with method '__len__'"
        v = self.V3D(0, -1, 2)
        n = self.V3D.__len__(v)
        self.assertEqual(n, 3, msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        n = v.__len__()
        self.assertEqual(n, 3, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        n = len(v)
        self.assertEqual(n, 3, msg=fail_msg)


    def test_component_names(self):

        fail_msg = "Problem with class method 'component_names'"
        l = self.V3D.component_names()
        self.assertListEqual(l, [ 'x', 'y', 'z' ], msg=fail_msg)
        v = self.V3D(0, -1, 2)
        l = v.component_names()
        self.assertListEqual(l, [ 'x', 'y', 'z' ], msg=fail_msg)


    def test_cnames(self):

        fail_msg = "Problem with property method 'cnames'"
        v = self.V3D(0, -1, 2)
        l = v.cnames
        self.assertListEqual(l, [ 'x', 'y', 'z' ], msg=fail_msg)


    def test_component_values(self):

        fail_msg = "Problem with method 'component_values'"
        v = self.V3D(0, -1, 2)
        l = self.V3D.component_values(v)
        self.assertListEqual(l, [ 0, -1, 2 ], msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        l = v.component_values()
        self.assertListEqual(l, [ -3.0, 4.0, -5.0 ], msg=fail_msg)


    def test_cvalues(self):

        fail_msg = "Problem with property method 'cvalues'"
        v = self.V3D(0, -1, 2)
        l = v.cvalues
        self.assertListEqual(l, [ 0, -1, 2 ], msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        l = v.cvalues
        self.assertListEqual(l, [ -3.0, 4.0, -5.0 ], msg=fail_msg)


    def test_x(self):

        fail_msg = "Problem with property method 'x'"
        v = self.V3D(0, -1, 2)
        self.assertEqual(v.x, 0, msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        self.assertEqual(v.x, -3.0, msg=fail_msg)


    def test_y(self):

        fail_msg = "Problem with property method 'y'"
        v = self.V3D(0, -1, 2)
        self.assertEqual(v.y, -1, msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        self.assertEqual(v.y, 4.0, msg=fail_msg)


    def test_z(self):

        fail_msg = "Problem with property method 'Z'"
        v = self.V3D(0, -1, 2)
        self.assertEqual(v.z, 2, msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        self.assertEqual(v.z, -5.0, msg=fail_msg)


    def test_repeat_cvalue(self):

        fail_msg = "Problem with class method 'repeat_cvalue'"
        v = self.V3D.repeat_cvalue(-1)
        l = v.component_values()
        self.assertListEqual(l, [ -1, -1, -1 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u.repeat_cvalue(3.5)
        l = v.component_values()
        self.assertListEqual(l, [ 3.5, 3.5, 3.5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        id_u_before = id(u)
        v = u.repeat_cvalue(1)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_is_vector(self):

        fail_msg = "Problem with class method 'is_vector'"
        v = self.V3D(0, -1, 2)
        b = self.V3D.is_vector(v)
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        b = self.V3D.is_vector(v)
        self.assertTrue(b, msg=fail_msg)
        d = { 'x': -3, 'y': 4, 'z': -5 }
        b = self.V3D.is_vector(d)
        self.assertFalse(b, msg=fail_msg)
        l = [ 0, -1, 2 ]
        b = self.V3D.is_vector(l)
        self.assertFalse(b, msg=fail_msg)
        t = (-3, 4, -5)
        b = self.V3D.is_vector(t)
        self.assertFalse(b, msg=fail_msg)
        r = { 0, -1, 2 }
        b = self.V3D.is_vector(r)
        self.assertFalse(b, msg=fail_msg)


### TODO: Consider if this test should be made more thorough
    def test_copy(self):

        fail_msg = "Problem with method 'copy'"
        u = self.V3D(0, -1, 2)
        v = self.V3D.copy(u)
        l = v.component_values()
        self.assertListEqual(l, [ 0, -1, 2 ], msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        v = u.copy()
        l = v.component_values()
        self.assertListEqual(l, [ -3.0, 4.0, -5.0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        v = u.copy()
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)


    def test_as_dict(self):

        fail_msg = "Problem with property method 'as_dict'"
        v = self.V3D(0, -1, 2)
        d = self.V3D.as_dict(v)
        self.assertDictEqual(d, { 'x': 0, 'y': -1, 'z': 2 }, msg=fail_msg)
        v = self.V3D(-3.5, 4.5, -5.5)
        d = v.as_dict()
        self.assertDictEqual(d, { 'x': -3.5, 'y': 4.5, 'z': -5.5 }, msg=fail_msg)


    def test_str(self):

        fail_msg = "Problem with method '__str__'"
        v = self.V3D(-3, 4, -5)
        st = self.V3D.__str__(v)
        self.assertEqual(st, '<-3, 4, -5>', msg=fail_msg)
        v = self.V3D(0, -1, 2)
        st = v.__str__()
        self.assertEqual(st, '<0, -1, 2>', msg=fail_msg)
        v = self.V3D(-3.5, 4.5, -5.5)
        st = str(v)
        self.assertEqual(st, '<-3.5, 4.5, -5.5>', msg=fail_msg)


    def test_repr(self):

        fail_msg = "Problem with method '__repr__'"
        v = self.V3D(-3.5, 4.5, -5.5)
        st = self.V3D.__repr__(v)
        self.assertEqual(st, 'V3D(x=-3.5, y=4.5, z=-5.5)', msg=fail_msg)
        v = self.V3D(0, -1, 2)
        st = v.__repr__()
        self.assertEqual(st, 'V3D(x=0, y=-1, z=2)', msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        st = repr(v)
        self.assertEqual(st, 'V3D(x=-3.0, y=4.0, z=-5.0)', msg=fail_msg)


    def test_format(self):

        fail_msg = "Problem with method '__format__'"
        v = self.V3D(0, -1, 2)
        st = self.V3D.__format__(v)
        self.assertEqual(st, str(v), msg=fail_msg)  ### ?
        v = self.V3D(0, -1, 2)
        st = v.__format__('.1f')
        self.assertEqual(st, '<0.0, -1.0, 2.0>', msg=fail_msg)
        v = self.V3D(-3.0, 4.0, -5.0)
        st = format(v)
        self.assertEqual(st, str(v), msg=fail_msg)  ### ?
        v = self.V3D(0, -1, 2)
        st = '{!s:}'.format(v)
        self.assertEqual(st, str(v), msg=fail_msg)
        v = self.V3D(0, -1, 2)
        st = '{!r:}'.format(v)
        self.assertEqual(st, repr(v), msg=fail_msg)
        v = self.V3D(0.0, -1.0, 2.0)
        st = format(v)
        self.assertEqual(st, str(v), msg=fail_msg)  ### ?
        v = self.V3D(0.0, -1.0, 2.0)
        st = format(v, '.2e')
        self.assertEqual(st, '<0.00e+00, -1.00e+00, 2.00e+00>', msg=fail_msg)
        v = self.V3D(-4.444, 5.555, -6.666)
        st = '{:.2e}'.format(v)
        self.assertEqual(st, '<-4.44e+00, 5.55e+00, -6.67e+00>', msg=fail_msg)


    def test_iter(self):

        fail_msg = "Problem with method '__iter__'"
        u = self.V3D(0, -1, 2)
        i = self.V3D.__iter__(u)
        l = [ next(i), next(i), next(i) ]
        self.assertListEqual(l, [ 0, -1, 2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        i = u.__iter__()
        l = [ next(i), next(i), next(i) ]
        self.assertListEqual(l, [ -3, 4, -5 ], msg=fail_msg)
        u = self.V3D(0.5, -1.5, 2.5)
        i = iter(u)
        l = [ next(i), next(i), next(i) ]
        self.assertListEqual(l, [ 0.5, -1.5, 2.5 ], msg=fail_msg)
        with self.assertRaises(StopIteration, msg=fail_msg):
            next(i)


    def test_getitem(self):

        fail_msg = "Problem with method '__getitem__'"
        v = self.V3D(-3, 4, -5)
        s = self.V3D.__getitem__(v, 2)
        self.assertEqual(s, -5, msg=fail_msg)
        v = self.V3D(0.5, -1.5, 2.5)
        s = v.__getitem__(1)
        self.assertEqual(s, -1.5, msg=fail_msg)
        test_data = \
            [
                ( 0,  0        ),
                ( 1,     -1    ),
                ( 2,          2),
                (-1,          2),
                (-2,     -1    ),
                (-3,  0        )
            ]
        for index, result in test_data:
            v = self.V3D(0, -1, 2)
            s = v[index]
            with self.subTest(v=v, index=index, expected_result=result):
                self.assertEqual(s, result, msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        v = u[::]
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        with self.assertRaises(IndexError, msg=fail_msg):
            v[3]
        v = self.V3D(-3, 4, -5)
        with self.assertRaises(IndexError, msg=fail_msg):
            v[-4]
        v = self.V3D(0, -1, 2)
        with self.assertRaises(TypeError, msg=fail_msg):
            v[0.0]
        v = self.V3D(-3, 4, -5)
        with self.assertRaises(TypeError, msg=fail_msg):
            v['0']
        test_data = \
            [
                (slice(   0,    0,    1), [            ]),
                (slice(   1,    1,    1), [            ]),
                (slice(   2,    2,    1), [            ]),
                (slice(   0,    1,    1), [  0         ]),
                (slice(   1,    2,    1), [     -1     ]),
                (slice(   2,    3,    1), [          2 ]),
                (slice(   0,    2,    1), [  0, -1     ]),
                (slice(   1,    3,    1), [     -1,  2 ]),
                (slice(   0,    3,    1), [  0, -1,  2 ]),
                (slice(   0,    3,   -1), [            ]),
                (slice(   0,    3,   -2), [            ]),
                (slice(   0,    3,   -3), [            ]),
                (slice(   0,    0, None), [            ]),
                (slice(   1,    1, None), [            ]),
                (slice(   2,    2, None), [            ]),
                (slice(   0,    1, None), [  0         ]),
                (slice(   1,    2, None), [     -1     ]),
                (slice(   2,    3, None), [          2 ]),
                (slice(   0,    2, None), [  0, -1     ]),
                (slice(   1,    3, None), [     -1,  2 ]),
                (slice(   0,    3, None), [  0, -1,  2 ]),
                (slice(   0, None, None), [  0, -1,  2 ]),
                (slice(   1, None, None), [     -1,  2 ]),
                (slice(   2, None, None), [          2 ]),
                (slice(  -1, None, None), [          2 ]),
                (slice(  -2, None, None), [     -1,  2 ]),
                (slice(  -3, None, None), [  0, -1,  2 ]),
                (slice(None,    0, None), [            ]),
                (slice(None,    1, None), [  0         ]),
                (slice(None,    2, None), [  0, -1     ]),
                (slice(None,    3, None), [  0, -1,  2 ]),
                (slice(None,   -1, None), [  0, -1     ]),
                (slice(None,   -2, None), [  0         ]),
                (slice(None,   -3, None), [            ]),
                (slice(None, None,    1), [  0, -1,  2 ]),
                (slice(None, None,    2), [  0,      2 ]),
                (slice(None, None,    3), [  0         ]),
                (slice(None, None,   -1), [  2, -1,  0 ]),
                (slice(None, None,   -2), [  2,      0 ]),
                (slice(None, None,   -3), [  2         ]),
                (slice(None, None, None), [  0, -1,  2 ])
            ]
        for slice_, result in test_data:
            v = self.V3D(0, -1, 2)
            l = v[slice_]
            with self.subTest(v=v, slice=slice_, expected_result=result):
                self.assertListEqual(l, result, msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        with self.assertRaises(ValueError, msg=fail_msg):
            v[::0]
        v = self.V3D(0, -1, 2)
        with self.assertRaises(TypeError, msg=fail_msg):
            v[::, ::]


    def test_setitem(self):

        fail_msg = "Problem with method '__setitem__'"
        v = self.V3D(0, -1, 2)
        self.V3D.__setitem__(v, 0, 2)
        l = v.component_values()
        self.assertListEqual(l, [ 2, -1, 2 ], msg=fail_msg)
        v = self.V3D(-3.5, 4.5, -5.5)
        v.__setitem__(1, -2.0)
        l = v.component_values()
        self.assertListEqual(l, [ -3.5, -2.0, -5.5 ], msg=fail_msg)
        test_data = \
            [
                ( 0, -3        , [ -3, -1,  2 ]),
                ( 1,      4    , [  0,  4,  2 ]),
                ( 2,         -5, [  0, -1, -5 ]),
                (-1,         -5, [  0, -1, -5 ]),
                (-2,      4    , [  0,  4,  2 ]),
                (-3, -3        , [ -3, -1,  2 ])
            ]
        for index, values, result in test_data:
            v = self.V3D(0, -1, 2)
            v[index] = values
            l = v.component_values()
            with self.subTest(v=v, index=index, values=values, expected_result=result):
                self.assertListEqual(l, result, msg=fail_msg)
        v = self.V3D(-3, 4, -5)
        with self.assertRaises(IndexError, msg=fail_msg):
            v[3] = 0
        v = self.V3D(0, -1, 2)
        with self.assertRaises(IndexError, msg=fail_msg):
            v[-4] = 0
        v = self.V3D(-3, 4, -5)
        with self.assertRaises(TypeError, msg=fail_msg):
            v[0.0] = 0
        v = self.V3D(0, 0, 0)
        with self.assertRaises(TypeError, msg=fail_msg):
            v['0'] = 0
        test_data = \
            [
                (slice(   0,    0,    1), [            ], [  0, -1,  2 ]),
                (slice(   1,    1,    1), [            ], [  0, -1,  2 ]),
                (slice(   2,    2,    1), [            ], [  0, -1,  2 ]),
                (slice(   0,    1,    1), [ -3         ], [ -3, -1,  2 ]),
                (slice(   1,    2,    1), [      4     ], [  0,  4,  2 ]),
                (slice(   2,    3,    1), [         -5 ], [  0, -1, -5 ]),
                (slice(   0,    2,    1), [ -3,  4     ], [ -3,  4,  2 ]),
                (slice(   1,    3,    1), [      4, -5 ], [  0,  4, -5 ]),
                (slice(   0,    3,    1), [ -3,  4, -5 ], [ -3,  4, -5 ]),
                (slice(   0,    3,   -1), [            ], [  0, -1,  2 ]),
                (slice(   0,    3,   -2), [            ], [  0, -1,  2 ]),
                (slice(   0,    3,   -3), [            ], [  0, -1,  2 ]),
                (slice(   0,    0, None), [            ], [  0, -1,  2 ]),
                (slice(   1,    1, None), [            ], [  0, -1,  2 ]),
                (slice(   2,    2, None), [            ], [  0, -1,  2 ]),
                (slice(   0,    1, None), [ -3         ], [ -3, -1,  2 ]),
                (slice(   1,    2, None), [      4     ], [  0,  4,  2 ]),
                (slice(   2,    3, None), [         -5 ], [  0, -1, -5 ]),
                (slice(   0,    2, None), [ -3,  4     ], [ -3,  4,  2 ]),
                (slice(   1,    3, None), [      4, -5 ], [  0,  4, -5 ]),
                (slice(   0,    3, None), [ -3,  4, -5 ], [ -3,  4, -5 ]),
                (slice(   0, None, None), [ -3,  4, -5 ], [ -3,  4, -5 ]),
                (slice(   1, None, None), [      4, -5 ], [  0,  4, -5 ]),
                (slice(   2, None, None), [         -5 ], [  0, -1, -5 ]),
                (slice(  -1, None, None), [         -5 ], [  0, -1, -5 ]),
                (slice(  -2, None, None), [      4, -5 ], [  0,  4, -5 ]),
                (slice(  -3, None, None), [ -3,  4, -5 ], [ -3,  4, -5 ]),
                (slice(None,    0, None), [            ], [  0, -1,  2 ]),
                (slice(None,    1, None), [ -3         ], [ -3, -1,  2 ]),
                (slice(None,    2, None), [ -3,  4     ], [ -3,  4,  2 ]),
                (slice(None,    3, None), [ -3,  4, -5 ], [ -3,  4, -5 ]),
                (slice(None,   -1, None), [ -3,  4     ], [ -3,  4,  2 ]),
                (slice(None,   -2, None), [ -3         ], [ -3, -1,  2 ]),
                (slice(None,   -3, None), [            ], [  0, -1,  2 ]),
                (slice(None, None,    1), [ -3,  4, -5 ], [ -3,  4, -5 ]),
                (slice(None, None,    2), [ -3,     -5 ], [ -3, -1, -5 ]),
                (slice(None, None,    3), [ -3         ], [ -3, -1,  2 ]),
                (slice(None, None,   -1), [ -3,  4, -5 ], [ -5,  4, -3 ]),
                (slice(None, None,   -2), [ -3,     -5 ], [ -5, -1, -3 ]),
                (slice(None, None,   -3), [ -3,        ], [  0, -1, -3 ]),
                (slice(None, None, None), [ -3,  4, -5 ], [ -3,  4, -5 ])
            ]
        for slice_, values, result in test_data:
            v = self.V3D(0, -1, 2)
            v[slice_] = values
            l = v.component_values()
            with self.subTest(v=v, slice=slice_, values=values, expected_result=result):
                self.assertListEqual(l, result, msg=fail_msg)


    def test_eq(self):

        fail_msg = "Problem with method '__eq__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, -1, 2)
        b = self.V3D.__eq__(u, w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        w = self.V3D(-3.5, 4.5, -5.5)
        b = u.__eq__(w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(-3.5, 4.5, -5.5)
        b = u == w
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        w = self.V3D(-3, 4, -5)
        b = u == w
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(2, -1, 0)
        b = u == w
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 2)
        b = u == w
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        b = u == w
        self.assertFalse(b, msg=fail_msg)


    def test_ne(self):

        fail_msg = "Problem with method '__ne__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, -1, 2)
        b = self.V3D.__ne__(u, w)
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(-3.0, 4.0, -5.0)
        w = self.V3D(-3.5, 4.5, -5.5)
        b = u.__ne__(w)
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        w = self.V3D(-3.5, 4.5, -5.5)
        b = u != w
        self.assertFalse(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(2, -1, 0)
        b = u != w
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 1, 2)
        b = u != w
        self.assertTrue(b, msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, 4, -5)
        b = u != w
        self.assertTrue(b, msg=fail_msg)


    def test_contains(self):

        fail_msg = "Problem with method '__contains__'"
        v = self.V3D(0, -1, 2)
        b = 0 in v
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        b = -1 in v
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0.5, -1.5, 2.5)
        b = 2.5 in v
        self.assertTrue(b, msg=fail_msg)
        v = self.V3D(0.5, -1.5, 2.5)
        b = -1.0 in v
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        b = 1 in v
        self.assertFalse(b, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        b = 3 in v
        self.assertFalse(b, msg=fail_msg)


    def test_call(self):

        fail_msg = "Problem with method '__call__'"
        u = self.V3D(-3.0, 4.5, -5.5)
        v = self.V3D.__call__(u, abs, needs_index=False)
        l = v.component_values()
        self.assertListEqual(l, [ 3.0, 4.5, 5.5 ], msg=fail_msg)
        u = self.V3D(0.1, -1.5, 2.5)
        v = u.__call__(int)
        l = v.component_values()
        self.assertListEqual(l, [ 0, -1, 2 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        v = u(abs, False)
        l = v.component_values()
        self.assertListEqual(l, [ 3, 4, 5 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        fn = lambda cvs, i, dim: cvs + i - dim
        v = u(fn, needs_index=True)
        l = v.component_values()
        self.assertListEqual(l, [ -3, -3, 1 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        fn = lambda cvs, i, dim: cvs*i + dim
        v = u(fn, True)
        l = v.component_values()
        self.assertListEqual(l, [ 3, 7, -7 ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = u(lambda a: 5.5*a)
        l = v.component_values()
        self.assertListEqual(l, [ 0.0, -5.5, 11.0 ], msg=fail_msg)
        u = self.V3D(-3, 4, -5)
        id_u_before = id(u)
        v = u(abs)
        id_v_after = id(v)
        self.assertNotEqual(id_u_before, id_v_after, msg=fail_msg)
        v = self.V3D(0, -1, 2)
        with self.assertRaises(TypeError, msg=fail_msg):
            v(lambda : 0)
        v = self.V3D(0, -1, 2)
        with self.assertRaises(TypeError, msg=fail_msg):
            v(lambda a, b: 0)
        v = self.V3D(0, -1, 2)
        with self.assertRaises(TypeError, msg=fail_msg):
            v(0)


    def test_create_vector_method_arg1(self):


        def double(s):

            return s + s


        fail_msg = "Problem with method 'create_vector_method_arg1'"
        self.V3D.create_vector_method_arg1('double', function=double)
        self.assertTrue(hasattr(self.V3D, 'vector_double'), msg=fail_msg)
        u = self.V3D(0, -1, 2)
        v = self.V3D.vector_double(u)
        l = v.component_values()
        self.assertListEqual(l, [ 0, -2, 4 ], msg=fail_msg)
        u = self.V3D(-3.5, 4.5, -5.5)
        v = u.vector_double()
        l = v.component_values()
        self.assertListEqual(l, [ -7.0, 9.0, -11.0 ], msg=fail_msg)
        doc = self.V3D.vector_double.__doc__
        self.assertIsNotNone(doc, msg=fail_msg)


    def test_create_vector_method_arg2(self):


        def power(b, e):

            return b**e


        fail_msg = "Problem with method 'create_vector_method_arg2'"
        self.V3D.create_vector_method_arg2('power', function=power)
        self.assertTrue(hasattr(self.V3D, 'vector_power'), msg=fail_msg)
        u = self.V3D(1, 2, -3)
        w = self.V3D(0, 1, 2)
        v = self.V3D.vector_power(u, w)
        l = v.component_values()
        self.assertListEqual(l, [ 1, 2, 9 ], msg=fail_msg)
        u = self.V3D(-1, 2, 3)
        w = self.V3D(0, 2, 1)
        v = u.vector_power(w)
        l = v.component_values()
        self.assertListEqual(l, [ 1, 4, 3 ], msg=fail_msg)
        doc = self.V3D.vector_power.__doc__
        self.assertIsNotNone(doc, msg=fail_msg)


    def test_create_vector_method_arg3(self):


        def sum_3(a, b, c):

            return a + b + c


        fail_msg = "Problem with method 'create_vector_method_arg3'"
        self.V3D.create_vector_method_arg3('sum_3', function=sum_3)
        self.assertTrue(hasattr(self.V3D, 'vector_sum_3'), msg=fail_msg)
        u0 = self.V3D(-1, 2, 3)
        u1 = self.V3D(0, 2, 1)
        u2 = self.V3D(4, -2, 0)
        v = self.V3D.vector_sum_3(u0, u1, u2)
        self.assertEqual(v.component_values(), [ 3, 2, 4 ], msg=fail_msg)
        u0 = self.V3D(1.5, 0.0, -3.5)
        u1 = self.V3D(-3.5, 2.0, 1.0)
        u2 = self.V3D(0.0, -3.5, 2.5)
        v = u0.vector_sum_3(u1, u2)
        self.assertEqual(v.component_values(), [ -2.0, -1.5, 0.0 ], msg=fail_msg)
        doc = self.V3D.vector_sum_3.__doc__
        self.assertIsNotNone(doc, msg=fail_msg)


class Test_Case_simple_vector(Test_Case_fundamental_vector):

    create_vector_class = staticmethod(skvectors.create_class_Simple_Vector)


class Test_Case_vector(Test_Case_simple_vector):

    create_vector_class = staticmethod(skvectors.create_class_Vector)


class Test_Case_cartesian_vector(Test_Case_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_Vector)


class Test_Case_tolerant_cartesian_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_Vector)


class Test_Case_cartesian_3d_vector(Test_Case_cartesian_vector):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_3D_Vector)


class Test_Case_versatile_vector(Test_Case_fundamental_vector):

    create_vector_class = staticmethod(skvectors.create_class_Versatile_Vector)


    def test_eq(self):

        fail_msg = "Problem with method '__eq__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, -1, -5)
        v = u == w
        self.assertListEqual(v.component_values(), [ False, True, False ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 4, 2)
        v = u == w
        self.assertListEqual(v.component_values(), [ True, False, True ], msg=fail_msg)


    def test_ne(self):

        fail_msg = "Problem with method '__ne__'"
        u = self.V3D(0, -1, 2)
        w = self.V3D(-3, -1, -5)
        v = u != w
        self.assertListEqual(v.component_values(), [ True, False, True ], msg=fail_msg)
        u = self.V3D(0, -1, 2)
        w = self.V3D(0, 4, 2)
        v = u != w
        self.assertListEqual(v.component_values(), [ False, True, False ], msg=fail_msg)


class Test_Case_tolerant_cartesian_3d_vector(Test_Case_cartesian_3d_vector):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_3D_Vector)

### TODO: Add methods test_eq and test_ne


if __name__ == "__main__":
    unittest.main()

