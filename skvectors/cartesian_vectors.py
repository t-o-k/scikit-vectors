"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import skvectors.helper_functions as hf
from skvectors.vectors import create_class_Vector


def create_class_Cartesian_Vector(name, component_names, *, brackets='<>', sep=', ', cnull=None, cunit=None, functions=None):
    """
    Function that creates a cartesian vector class
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    if functions is None:
        functions = { }
    V = \
        create_class_Vector(
            name = 'V_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep,
            cnull = cnull,
            cunit = cunit,
            functions = functions
        )


    def init_Cartesian_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)
        cls.__abs__ = cls.length
        cls.__matmul__ = cls.dot
        cls.__rmatmul__ = cls.dot

        return cls


    @init_Cartesian_Vector
    class Cartesian_Vector(V):
        """
        A cartesian vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """

        _internal_functions = \
            [
                # 'and',
                'or',
                # 'all',
                'min',
                'max',
                # 'floor',
                # 'ceil',
                # 'trunc',
                'pi',
                'atan2'
            ]


        @classmethod
        def clip(cls, value, min_value, max_value):
            """Limits a value so that it lies between two values"""

            cunit = cls._cunit
            value = cunit*value
            min_value = cunit*min_value
            max_value = cunit*max_value
            clipped_value = cls.component_max(min_value, cls.component_min(value, max_value))

            return clipped_value


        @classmethod
        def _equal_cnull(cls, value):

            cnull = cls._cnull
            cunit = cls._cunit
            value = cunit*value
            result = value == cnull

            return result


        @classmethod
        def _equal_cunit(cls, value):

            cunit = cls._cunit
            value = cunit*value
            result = value == cunit

            return result


        def is_zero_vector(self):
            """Check if the length of a vector is equal to cnull"""

            ls = self.length()
            result = self._equal_cnull(ls)

            return result


        def is_unit_vector(self):
            """Check if the length of a vector is equal to cunit"""

            ls = self.length()
            result = self._equal_cunit(ls)

            return result


        @hf.ensure_other_is_vector
        def __eq__(self, other):
            """
            Check if two vectors are equal
            based on their distance from each other
            """

            cnull = self._cnull
            equal = self.distance(other) == cnull

            return equal


        @hf.ensure_other_is_vector
        def __ne__(self, other):
            """
            Check if two vectors are not equal
            based on their distance from each other
            """

            cnull = self._cnull
            not_equal = self.distance(other) != cnull

            return not_equal


        @hf.ensure_other_is_vector
        def are_orthogonal(self, other):
            """Check if two vectors are orthogonal"""

            dot = self.dot(other)
            orthogonal = self._equal_cnull(dot)
                ### Perhaps these are needed with numpy:
                # orthogonal = self.component_or(orthogonal, self.is_zero_vector())
                # orthogonal = self.component_or(orthogonal, other.is_zero_vector())

            return orthogonal


        @hf.ensure_other_is_vector
        def equal_lengths(self, other):
            """Check if two vectors have equal lengths"""

            ls = self.length()
            lo = other.length()
            equal_vector_lengths = ls == lo

            return equal_vector_lengths


        @hf.ensure_other_is_vector
        def shorter(self, other):
            """Check if a vector is shorter than another"""

            ls = self.length()
            lo = other.length()
            is_shorter = ls < lo

            return is_shorter


        @hf.ensure_other_is_vector
        def longer(self, other):
            """Check if a vector is longer than another"""

            ls = self.length()
            lo = other.length()
            is_longer = lo < ls

            return is_longer


        @hf.ensure_other_is_vector
        def dot(self, other):
            """The dot product (inner product) of two vectors"""

            scalar = (self*other).sum_of_components()

            return scalar


        def length(self):
            """The length (norm) of a vector"""

            cunit = self._cunit
            length_of_vector = (self**(cunit*2)).sum_of_components()**(cunit/2)

            return length_of_vector


        @hf.ensure_other_is_vector
        def distance(self, other):
            """The distance between two vectors"""

            length_between = (other - self).length()

            return length_between


        def normalize(self):
            """Vector scaled so that its length is cunit"""

            ls = self.length()
            try:
                vector = self/ls
            except ZeroDivisionError as err:
                msg = "The length of the vector is zero"
                raise ZeroDivisionError(msg) from err

            return vector


        @hf.ensure_other_is_vector
        def project(self, other):
            """Projection of a vector onto another"""

            num = self.dot(other)
            den = other.dot(other)
            try:
                s = num/den
            except ZeroDivisionError as err:
                msg = "The length of the vector to project onto is zero"
                raise ZeroDivisionError(msg) from err
            vector = other*s

            return vector


        @hf.ensure_other_is_vector
        def inv_project(self, other):
            """Inverse projection of a vector from another"""

            num = self.dot(self)
            den = self.dot(other)
            try:
                s = num/den
            except ZeroDivisionError as err:
                msg = "The vectors are orthogonal to each other"
                raise ZeroDivisionError(msg) from err
            vector = other*s

            return vector


        @hf.ensure_other_is_vector
        def reject(self, other):
            """Rejection of a vector from another"""

            num = self.dot(other)
            den = other.dot(other)
            try:
                s = num/den
            except ZeroDivisionError as err:
                msg = "The length of the vector to reject from is zero"
                raise ZeroDivisionError(msg) from err
            vector = self - other*s

            return vector


        @hf.ensure_other_is_vector
        def scalar_project(self, other):
            """Scalar projection of a vector onto another vector"""

            try:
                von = other.normalize()
            except ZeroDivisionError as err:
                msg = "The length of the vector to project onto is zero"
                raise ZeroDivisionError(msg) from err
            scalar = self.dot(von)

            return scalar


        @hf.ensure_other_is_vector
        def angle(self, other):
            """The smallest angle in radians (from cnull to +cunit*pi) between two vectors"""

            ls = self.length()
            lo = other.length()
            vs = self*lo
            vo = other*ls
            ln = (vs - vo).length()
            ld = (vs + vo).length()
            angle_between = self.component_atan2(ln, ld)*2

            return angle_between


        @hf.ensure_other_is_vector
        def cos(self, other):
            """The cosine of the angle between two vectors (from -cunit to +cunit)"""

            ls = self.length()
            lo = other.length()
            dot = self.dot(other)
            try:
                cosine = dot/(ls*lo)
            except ZeroDivisionError as err:
                msg = "One (or both) of the vectors is a zero vector"
                raise ZeroDivisionError(msg) from err
            cunit = self._cunit
            cosine = self.clip(cosine, -cunit, cunit)

            return cosine


        def _mmult(self, *others):

            assert len(others) == self._dimensions
            vector = self._vector(map(self.dot, others))

            return vector


### Consider if this should be added
#         def __imatmul__(self, other):
#             """TODO"""
#
#             self = self*self.dot(other)
#
#             return self


    return Cartesian_Vector

