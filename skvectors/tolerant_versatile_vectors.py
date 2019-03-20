"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

from functools import reduce

import skvectors.helper_functions as hf
from skvectors.versatile_vectors import create_class_Versatile_Vector


### Consider if this solution should be used:
# cls.component_max = np.maximum
# cls.component_abs = np.abs
# If so, then perhaps abs_tol should be multiplied by cls._cunit

def epsilon(*, abs_tol, rel_tol, values):
    """Calculates a common tolerance value (epsilon) for all the values"""


    def absolutes(values):

        yield abs_tol/rel_tol
        yield from map(abs, values)


    abs_values = absolutes(values)
    eps = max(abs_values)*rel_tol

    return eps


def create_class_Tolerant_Versatile_Vector(name, component_names, *, brackets='<>', sep=', ', functions=None, abs_tol=1e-12, rel_tol=1e-9):
    """
    Function that creates a tolerant versatile vector class
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    if functions is None:
        functions = { }
    VV = \
        create_class_Versatile_Vector(
            name = 'VV_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep,
            functions = functions
        )


    def init_Tolerant_Versatile_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)


        def prepare_tolerances(name, tolerances, dimensions):

            try:
                all_tolerances = [ *tolerances ]
            except TypeError:
                all_tolerances = None
            if all_tolerances is None:
                all_tolerances = [ tolerances ]*dimensions
            else:
                if len(all_tolerances) != dimensions:
                    msg = "The number of tolerances in {name} does not match the number of dimensions"
                    raise ValueError(msg.format_map(vars()))
            result = \
                [
                    float(tol)
                    for tol in all_tolerances
                ]

            return result


        cls.abs_tolerances = prepare_tolerances('abs_tol', abs_tol, cls._dimensions)
        cls.rel_tolerances = prepare_tolerances('rel_tol', rel_tol, cls._dimensions)
        compare_methods = \
            {
                'eq': \
                    "Check if the corresponding component values of " \
                    "two vectors are equal (within calculated tolerances)",
                'ne': \
                    "Check if the corresponding component values of " \
                    "two vectors are not equal (within calculated tolerances)",
                'lt': \
                    "TODO",
                'gt': \
                    "TODO",
                'le': \
                    "TODO",
                'ge':
                    "TODO"
            }
        for comp_type, method_doc in compare_methods.items():


            def compare_method(self, other, _comp_type=comp_type):

                vector = self._vector(self._compare_cvalues(other, _comp_type))

                return vector


            method_name = comp_type
            compare_method.__name__ = method_name
            compare_method.__doc__ = method_doc
            setattr(cls, method_name, compare_method)
        dunder_compare_methods = \
            {
                'eq': \
                    "Check if all corresponding component values of " \
                    "two vectors are equal (within calculated tolerances)",
                'ne': \
                    "Check if all corresponding component values of " \
                    "two vectors are not equal (within calculated tolerances)",
                'lt': \
                    "TODO",
                'gt': \
                    "TODO",
                'le': \
                    "TODO",
                'ge':
                    "TODO"
            }
        for comp_type, method_doc in dunder_compare_methods.items():


            def dunder_compare_method(self, other, _comp_type=comp_type):

                compare_results = self._compare_cvalues(other, _comp_type)
                cmp = reduce(self.component_and, compare_results)
                try:
                    result = self.component_all(cmp)
                except TypeError:
                    result = None
                if result is None:
                    result = bool(cmp)

                return result


            method_name = '__' + comp_type + '__'
            dunder_compare_method.__name__ = method_name
            dunder_compare_method.__doc__ = method_doc
            setattr(cls, method_name, dunder_compare_method)

        return cls


    @init_Tolerant_Versatile_Vector
    class Tolerant_Versatile_Vector(VV):
        """
        A tolerant versatile vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """

        _internal_functions = \
            [
                'and',
                'or',
                # 'any',
                'max',
                'abs'
            ]


### Needs more testing
        @classmethod
        def _epsilon_1(cls, cvalues):

            eps = \
                (
                    cls.component_max(
                        cls.abs_tolerances[i],
                        cvalues[i]*cls.rel_tolerances[i]
                    )
                    for i in range(cls._dimensions)
                )

            return eps


### Needs more testing
        @classmethod
        def _epsilon_2(cls, cvalues_1, cvalues_2):

            eps = \
                (
                    cls.component_max(
                        cls.abs_tolerances[i],
                        cls.component_max(cvalues_1[i], cvalues_2[i])*cls.rel_tolerances[i]
                    )
                    for i in range(cls._dimensions)
                )

            return eps


### Needs more testing
        @classmethod
        def _epsilon_n(cls, cvalues_n, i):
            """Calculates a common tolerance value (epsilon) for all the values"""

            abs_tol = cls.abs_tolerances[i]
            rel_tol = cls.rel_tolerances[i]
            eps = \
                cls.component_max(
                    abs_tol,
                    cls.component_max(
                        cls.component_abs(cv)
                        for cv in cvalues_n
                    )*rel_tol  ### This does not always work
                )

            return eps


        @classmethod
        def _component_from_vectors(cls, vectors, index):

            vectors = cls._ensure_all_are_vectors(vectors)
            result = \
                (
                    v._cvalues[index]
                    for v in vectors
                )

            return result


### Needs more testing
        @classmethod
        def tolerance_all(cls, vectors):
            """Calculate a tolerance for each of the components of several vectors"""  ###

            vectors = tuple(cls._ensure_all_are_vectors(vectors))
            cvalues = \
                (
                    cls._epsilon_n(cls._component_from_vectors(vectors, i), i)
                    for i in range(cls._dimensions)
                )
            vector = cls(*cvalues, _internal=True)

            return vector


### TODO
#         def tolerance_with(self, other):
#             """Calculate a common tolerance for two vectors based on their lengths"""
#
#             return


        @hf.ensure_other_is_vector
        def _compare_cvalues(self, other, comp_type):

            compare_fn = \
                {
                    'eq': lambda s, o, t: self.component_and((o - t) <= s, s <= (o + t)),
                    'ne': lambda s, o, t: self.component_or(s < (o - t), (o + t) < s),
                    'lt': lambda s, o, t: s < (o - t),
                    'gt': lambda s, o, t: (o + t) < s,
                    'le': lambda s, o, t: s <= (o + t),
                    'ge': lambda s, o, t: (o - t) <= s
                }
            fn = compare_fn[comp_type]
            csot = \
                zip(
                    self._cvalues,
                    other._cvalues,
                    self.tolerance_with(other)._cvalues
                )
            result = \
                (
                    fn(cvs, cvo, cvt)
                    for cvs, cvo, cvt in csot
                )

            return result


    return Tolerant_Versatile_Vector

