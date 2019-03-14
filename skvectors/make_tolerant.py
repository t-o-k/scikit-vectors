"""
Copyright (c) 2017 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import skvectors.helper_functions as hf


def make_Cartesian_Vector_Tolerant(*, cartesian_vector_class, name, functions, abs_tol, rel_tol):
    """
    Function that makes a cartesian vector class tolerant
    """

    if not isinstance(abs_tol, float):
        msg = \
            "The absolute tolerance 'abs_tol' must be a float, not {type_name}" \
            .format(type_name=type(abs_tol).__name__)
        raise TypeError(msg)
    if not isinstance(rel_tol, float):
        msg = \
            "The relative tolerance 'rel_tol' must be a float, not {type_name}" \
            .format(type_name=type(rel_tol).__name__)
        raise TypeError(msg)
    if functions is None:
        functions = { }


    def init_Tolerant(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)
        cunit = cls._cunit
        cls.abs_tol = cunit*abs_tol
        cls.rel_tol = rel_tol
        cls.cround = property(cls.round_components)

        return cls


    @init_Tolerant
    class Tolerant(cartesian_vector_class):
        """
        A tolerant cartesian vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """

        _internal_functions = \
            [
                # 'and',
                # 'or',
                # 'all',
                # 'min',
                # 'max',
                # 'floor',
                # 'ceil',
                # 'trunc',
                # 'atan2',
                # 'pi',
                'copysign',
                'log10'
            ]


        @classmethod
        def _epsilon_1(cls, length):

            eps = cls.component_max(cls.abs_tol, length*cls.rel_tol)

            return eps


        @classmethod
        def _epsilon_2(cls, length_0, length_1):

            max_length = cls.component_max(length_0, length_1)
            eps = cls.component_max(cls.abs_tol, max_length*cls.rel_tol)

            return eps


        @classmethod
        def _epsilon_n(cls, lengths):

            max_length = cls.component_max(*lengths)
            eps = cls.component_max(cls.abs_tol, max_length*cls.rel_tol)

            return eps


        @classmethod
        def tolerance_all(cls, vectors):
            """Calculate a common tolerance for several vectors based on their lengths"""

            vectors = cls._ensure_all_are_vectors(vectors)
            eps = \
                cls._epsilon_n(
                    v.length()
                    for v in vectors
                )

            return eps


        @hf.ensure_other_is_vector
        def tolerance_with(self, other):
            """Calculate a common tolerance for two vectors based on their lengths"""

            ls = self.length()
            lo = other.length()
            eps = self._epsilon_2(ls, lo)

            return eps


        def tolerance(self):
            """Calculate the tolerance for a vector based on its length"""

            ls = self.length()
            eps = self._epsilon_1(ls)

            return eps


        @classmethod
        def _equal_cnull(cls, value):

            cnull = cls._cnull
            cunit = cls._cunit
            value = cunit*value
            tol = cls.abs_tol
            result = cls.component_and((cnull - tol) <= value, value <= (cnull + tol))

            return result


        @classmethod
        def _equal_cunit(cls, value):

            cunit = cls._cunit
            value = cunit*value
            tol = cunit*cls.rel_tol
            result = cls.component_and((cunit - tol) <= value, value <= (cunit + tol))

            return result


        @property
        def tol(self):
            """Tolerance for a vector based on its length"""

            tolerance = self.tolerance()

            return tolerance


        @hf.ensure_other_is_vector
        def __eq__(self, other):
            """
            Check if two vectors are equal (within a calculated tolerance)
            based on their distance from each other
            """

            tol = self.tolerance_with(other)
            equal = self.distance(other) <= tol

            return equal


        @hf.ensure_other_is_vector
        def __ne__(self, other):
            """
            Check if two vectors are not equal (within a calculated tolerance)
            based on their distance from each other
            """

            tol = self.tolerance_with(other)
            not_equal = self.distance(other) > tol

            return not_equal


        @hf.ensure_other_is_vector
        def are_orthogonal(self, other):
            """Check if two vectors are orthogonal (within a calculated tolerance)"""

            try:
                vsn = self.normalize()
            except ZeroDivisionError:
                vsn = None
            try:
                von = other.normalize()
            except ZeroDivisionError:
                von = None
            if (vsn is None) or (von is None):
                orthogonal = self._true
            else:
                dot = vsn.dot(von)
                orthogonal = self._equal_cnull(dot)
                orthogonal = self.component_or(orthogonal, self.is_zero_vector())
                orthogonal = self.component_or(orthogonal, other.is_zero_vector())

            return orthogonal


        @hf.ensure_other_is_vector
        def equal_lengths(self, other):
            """Check if two vectors have equal lengths (within a calculated tolerance)"""

            ls = self.length()
            lo = other.length()
            tol = self.tolerance_with(other)
            equal_vector_lengths = self.component_and((lo - tol) <= ls, ls <= (lo + tol))

            return equal_vector_lengths


        @hf.ensure_other_is_vector
        def shorter(self, other):
            """Check if a vector is shorter than another (within a calculated tolerance)"""

            ls = self.length()
            lo = other.length()
            tol = self.tolerance_with(other)
            is_shorter = ls < (lo - tol)

            return is_shorter


        @hf.ensure_other_is_vector
        def longer(self, other):
            """Check if a vector is longer than another (within a calculated tolerance)"""

            ls = self.length()
            lo = other.length()
            tol = self.tolerance_with(other)
            is_longer = (lo + tol) < ls

            return is_longer


### Needs more testing
        @classmethod
        def _round(cls, value, p):

            cunit = cls._cunit
            d = (cunit*10)**p
            rounded_value = cls.component_trunc(value*d + cls.component_copysign(cunit/2, value))/d

            return rounded_value


### Needs more testing
        @classmethod
        def _round_cvalue(cls, cvalue, p):

            cunit = cls._cunit
            rounded_cvalue = cunit*cls._round(cvalue/cunit, p)

            return rounded_cvalue


        def round_components(self):
            """Vector with the component values rounded to a calculated tolerance"""

            eps = self.tolerance()
            p = -self.component_ceil(self.component_log10(eps))
            round_fn = lambda cv: self._round_cvalue(cv, p)
            vector = self._vector(map(round_fn, self._cvalues))

            return vector


    return Tolerant

