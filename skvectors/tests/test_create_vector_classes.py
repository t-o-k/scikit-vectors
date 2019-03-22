"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import unittest
import skvectors


class Test_Case_create_fundamental_vector_class(unittest.TestCase):

    dimensions = 1
    component_names = [ 't' ]
    create_vector_class = staticmethod(skvectors.create_class_Fundamental_Vector)


    @classmethod
    def setUpClass(cls):

        cls.fail_msg = \
            "Problem with function '{cls.create_vector_class.__name__}'" \
            .format_map(vars())


    @classmethod
    def tearDownClass(cls):

        del cls.fail_msg


    def test_create(self):

        fail_msg = self.fail_msg

        dimensions = self.dimensions
        component_names = self.component_names
        name = 'V'

        with self.assertRaises(TypeError, msg=fail_msg):
            V = self.create_vector_class()

        with self.assertRaises(TypeError, msg=fail_msg):
            V = self.create_vector_class(name)

        with self.assertRaises(TypeError, msg=fail_msg):
            V = self.create_vector_class(0, component_names)

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class('', component_names)

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class('0', component_names)

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, '')

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, '0'*dimensions)

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, '_'*dimensions)

        with self.assertRaises(ValueError, msg=fail_msg):
            V = \
                self.create_vector_class(
                    name,
                    [ cname + '_' for cname in component_names ]
                )

        with self.assertRaises(TypeError, msg=fail_msg):
            V = self.create_vector_class(name, component_names, '<>')

        V = \
            self.create_vector_class(
                name = name,
                component_names = component_names
            )
        s = V.__name__
        self.assertEqual(s, name, msg=fail_msg)
        s = V.__doc__
        self.assertIsInstance(s, str, msg=fail_msg)
        self.assertTrue('{} dimension'.format(dimensions) in s, msg=fail_msg)
        l = V.brackets
        self.assertListEqual(l, [ '<', '>' ], msg=fail_msg)
        l = V._cnames
        self.assertListEqual(l, component_names, msg=fail_msg)
        n = V._dimensions
        self.assertEqual(n, dimensions, msg=fail_msg)
        s = V.sep
        self.assertEqual(s, ', ', msg=fail_msg)

        V = \
            self.create_vector_class(
                name = name,
                component_names = component_names,
                brackets = [ '', '' ]
            )
        l = V.brackets
        self.assertListEqual(l, [ '', '' ], msg=fail_msg)

        V = \
            self.create_vector_class(
                name,
                component_names,
                brackets = [ ' { ', ' } ' ]
            )
        l = V.brackets
        self.assertListEqual(l, [ ' { ', ' } ' ], msg=fail_msg)

        with self.assertRaises(ValueError, msg=fail_msg):
            V = \
                self.create_vector_class(
                    name = name,
                    component_names = component_names,
                    brackets = '|'
                )

        with self.assertRaises(ValueError, msg=fail_msg):
            V = \
                self.create_vector_class(
                    name = name,
                    component_names = component_names,
                    brackets = [ '[', '|', ']' ]
                )

        V = \
            self.create_vector_class(
                name,
                component_names,
                brackets = '<>',
                sep = ''
            )
        s = V.sep
        self.assertEqual(s, '', msg=fail_msg)

        V = \
            self.create_vector_class(
                name,
                component_names,
                sep = ' _ '
            )
        s = V.sep
        self.assertEqual(s, ' _ ', msg=fail_msg)


    def test_five_dimensions(self):

        fail_msg = self.fail_msg

        dimensions = 5
        name = chr(0x039e)
        component_names = ''.join(chr(i) for i in range(0x03b1, 0x03b6))
        assert len(component_names) == dimensions
        brackets = chr(0x2770) + chr(0x2771)
        separator = chr(0x263a)
        V = \
            self.create_vector_class(
                name,
                component_names,
                brackets = brackets,
                sep = separator
            )
        s = V.__name__
        self.assertEqual(s, name, msg=fail_msg)
        l = V._cnames
        self.assertListEqual(l, list(component_names), msg=fail_msg)
        s = V.__doc__
        self.assertTrue(', '.join(l) in s, msg=fail_msg)
        self.assertTrue('{} dimensions'.format(dimensions) in s, msg=fail_msg)
        l = V.brackets
        self.assertListEqual(l, list(brackets), msg=fail_msg)
        s = V.sep
        self.assertEqual(s, separator, msg=fail_msg)


    def test_many_dimensions(self):

        fail_msg = self.fail_msg

        dimensions = 1000
        name = 'V_{}'.format(dimensions)
        component_names = [ 'c{}'.format(i) for i in range(dimensions) ]
        V = self.create_vector_class(name, component_names)
        s = V.__name__
        self.assertEqual(s, name, msg=fail_msg)
        l = V._cnames
        self.assertEqual(l, component_names, msg=fail_msg)
        s = V.__doc__
        self.assertTrue(', '.join(l) in s, msg=fail_msg)
        self.assertTrue('{} dimensions'.format(dimensions) in s, msg=fail_msg)
        n = V._dimensions
        self.assertEqual(n, dimensions, msg=fail_msg)


class Test_Case_create_simple_vector_class(Test_Case_create_fundamental_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Simple_Vector)

    # TODO:
    # Test dunder methods


class Test_Case_create_vector_class(Test_Case_create_simple_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Vector)

    # TODO:
    # Test dunder methods
    # Test cnull and cunit
    # Test internal functions
    # Test vector bases


class Test_Case_create_cartesian_vector_class(Test_Case_create_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Cartesian_Vector)

    # TODO: ?


class Test_Case_create_tolerant_cartesian_vector_class(Test_Case_create_cartesian_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_Vector)

    # TODO: ?


class Test_Case_create_cartesian_2d_vector_class(Test_Case_create_cartesian_vector_class):

    dimensions = 2
    component_names = [ 'u', 'v' ]
    create_vector_class = staticmethod(skvectors.create_class_Cartesian_2D_Vector)


    def test_two_dimensions(self):

        fail_msg = self.fail_msg

        dimensions = 2
        name = chr(0x039e)
        component_names = ''.join(chr(i) for i in range(0x03b1, 0x03b3))
        assert len(component_names) == dimensions
        brackets = chr(0x2770) + chr(0x2771)
        separator = chr(0x263a)
        V = \
            self.create_vector_class(
                name,
                component_names,
                brackets = brackets,
                sep = separator
            )
        s = V.__name__
        self.assertEqual(s, name, msg=fail_msg)
        l = V._cnames
        self.assertListEqual(l, list(component_names), msg=fail_msg)
        s = V.__doc__
        self.assertTrue(', '.join(l) in s, msg=fail_msg)
        self.assertTrue('{} dimensions'.format(dimensions) in s, msg=fail_msg)
        l = V.brackets
        self.assertListEqual(l, list(brackets), msg=fail_msg)
        s = V.sep
        self.assertEqual(s, separator, msg=fail_msg)


    def test_one_dimensions(self):

        fail_msg = self.fail_msg
        name = 'V'
        component_names = 't'

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, component_names)


    def test_three_dimensions(self):

        fail_msg = self.fail_msg
        name = 'V'
        component_names = 'xyz'

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, component_names)


    @unittest.skip("function can only create classes with 2 dimensions")
    def test_five_dimensions(self):

        pass


    @unittest.skip("function can only create classes with 2 dimensions")
    def test_many_dimensions(self):

        pass


    # TODO: ?


class Test_Case_create_cartesian_3d_vector_class(Test_Case_create_cartesian_vector_class):

    dimensions = 3
    component_names = [ 'u', 'v', 'w' ]
    create_vector_class = staticmethod(skvectors.create_class_Cartesian_3D_Vector)


    def test_three_dimensions(self):

        fail_msg = self.fail_msg

        dimensions = 3
        name = chr(0x039e)
        component_names = ''.join(chr(i) for i in range(0x03b1, 0x03b4))
        assert len(component_names) == dimensions
        brackets = chr(0x2770) + chr(0x2771)
        separator = chr(0x263a)
        V = \
            self.create_vector_class(
                name,
                component_names,
                brackets = brackets,
                sep = separator
            )
        s = V.__name__
        self.assertEqual(s, name, msg=fail_msg)
        l = V._cnames
        self.assertListEqual(l, list(component_names), msg=fail_msg)
        s = V.__doc__
        self.assertTrue(', '.join(l) in s, msg=fail_msg)
        self.assertTrue('{} dimensions'.format(dimensions) in s, msg=fail_msg)
        l = V.brackets
        self.assertListEqual(l, list(brackets), msg=fail_msg)
        s = V.sep
        self.assertEqual(s, separator, msg=fail_msg)


    def test_two_dimensions(self):

        fail_msg = self.fail_msg
        name = 'V'
        component_names = 'ab'

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, component_names)


    def test_four_dimensions(self):

        fail_msg = self.fail_msg
        name = 'V'
        component_names = 'abcd'

        with self.assertRaises(ValueError, msg=fail_msg):
            V = self.create_vector_class(name, component_names)


    @unittest.skip("function can only create classes with 3 dimensions")
    def test_five_dimensions(self):

        pass


    @unittest.skip("function can only create classes with 3 dimensions")
    def test_many_dimensions(self):

        pass


    # TODO: ?


class Test_Case_create_versatile_vector_class(Test_Case_create_fundamental_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Versatile_Vector)

    # TODO: ?


class Test_Case_create_tolerant_cartesian_2d_vector_class(Test_Case_create_cartesian_2d_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_2D_Vector)

    # TODO: ?


class Test_Case_create_tolerant_cartesian_3d_vector_class(Test_Case_create_cartesian_3d_vector_class):

    create_vector_class = staticmethod(skvectors.create_class_Tolerant_Cartesian_3D_Vector)

    # TODO: ?


if __name__ == "__main__":
    unittest.main()

