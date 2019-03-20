"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import operator
import math
from copy import copy
from functools import reduce
import skvectors.helper_functions as hf
from skvectors.simple_vectors import create_class_Simple_Vector


def create_class_Vector(name, component_names, *, brackets='<>', sep=', ', cnull=None, cunit=None, functions=None):
    """
    Function that makes a creates class
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    if functions is None:
        functions = { }


    def verify_equal(eq, op_all):

        try:
            equal = op_all(eq)
        except TypeError:
            equal = None
        if equal is None:
            equal = bool(eq)
        if not equal:
            msg = "Invalid value(s) for cnull and/or cunit"
            raise ValueError(msg)


    def verify_equal_args(arg0, arg1):

        if functions is None:
            op_all = all
        else:
            op_all = functions.get('all', all)
        verify_equal(arg0 == arg1, op_all)
        verify_equal(arg1 == arg0, op_all)


    def verify_units(cnull, cunit):
        """Verify that some fundamental statements with cnull and cunit are true"""

        verify_equal_args(cnull, -cnull)  # ?
        verify_equal_args(cnull, +cnull)
        verify_equal_args(cnull, --cnull)
        verify_equal_args(cunit, --cunit)
        verify_equal_args(cunit, +cunit)
        verify_equal_args(cnull, cnull + cnull)
        verify_equal_args(cnull, cnull - cnull)
        verify_equal_args(cnull, +cnull - cnull)
        verify_equal_args(cnull, -cnull + cnull)
        verify_equal_args(cunit, cnull + cunit)
        verify_equal_args(cunit, cunit + cnull)
        verify_equal_args(cnull, +cunit - cunit)
        verify_equal_args(cnull, -cunit + cunit)
        verify_equal_args(cnull, cnull*cnull)
        verify_equal_args(cnull, cnull*cunit)
        verify_equal_args(cnull, cunit*cnull)
        verify_equal_args(cunit, cunit*cunit)
        verify_equal_args(cnull, cnull/cunit)
        verify_equal_args(cunit, cunit/cunit)
        verify_equal_args(cunit, cnull**cnull)  # ?
        verify_equal_args(cnull, cnull**cunit)
        verify_equal_args(cunit, cunit**cnull)
        verify_equal_args(cunit, cunit**cunit)
        # verify_equal_args(cunit, cunit**-cunit)  # Problem with Pandas
        verify_equal_args(cnull, cnull*0)
        verify_equal_args(cnull, 0*cnull)
        verify_equal_args(cnull, cnull*1)
        verify_equal_args(cnull, 1*cnull)
        verify_equal_args(cnull, cunit*0)
        verify_equal_args(cnull, 0*cunit)
        verify_equal_args(cunit, cunit*1)
        verify_equal_args(cunit, 1*cunit)
        verify_equal_args(cnull, cnull/1)
        verify_equal_args(cnull, 0/cunit)
        verify_equal_args(cunit, cunit/1)
        verify_equal_args(cunit, 1/cunit)
        verify_equal_args(cunit, cnull**0)  # ?
        verify_equal_args(cnull, cnull**1)
        verify_equal_args(cunit, cunit**0)
        verify_equal_args(cunit, cunit**1)
        # verify_equal_args(cunit, cunit**-1)  # Problem with Pandas
        verify_equal_args(cunit, 0**cnull)  # ?
        verify_equal_args(cnull, 0**cunit)
        verify_equal_args(cunit, 1**cnull)
        verify_equal_args(cunit, 1**cunit)
        # verify_equal_args(cunit, 1**-cunit)  # Problem with Pandas


    if (cnull is None) and (cunit is None):
        cnull = 0
        cunit = 1
    else:
        if (cnull is None) or (cunit is None):
            msg = \
                "If a value for either cnull or cunit is provided, " \
                "a value for the other must also be provided"
            raise TypeError(msg)
        cnull = copy(cnull)
        cunit = copy(cunit)
    verify_units(cnull, cunit)
    SV = \
        create_class_Simple_Vector(
            name = 'SV_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep
        )


    def make_zero_vector_method(cls):

        cnull = cls._cnull
        cvalues = [ cnull ]*cls._dimensions


        def zero(cls):
            """Vector with all components values set to 'cnull'"""

            return cls(*cvalues, _internal=True)


        cls.zero = classmethod(zero)


    def make_one_vector_method(cls):

        cunit = cls._cunit
        cvalues = [ cunit ]*cls._dimensions


        def one(cls):
            """Vector with all components values set to 'cunit'"""

            return cls(*cvalues, _internal=True)


        cls.one = classmethod(one)


    def setup_vector_bases(cls):


        class Basis:
            """Descriptor class for basis vectors"""


            def __init__(self, owner, index, cname, basis_name):

                self.method_name = basis_name
                self.cname = cname
                cnull = owner._cnull
                cunit = owner._cunit
                self.cvalues = \
                    [
                        cunit if (i == index) else cnull
                        for i in range(owner._dimensions)
                    ]


            def __set__(self, instance, value):

                owner = type(instance)
                msg = \
                    "'{owner.__name__}' object attribute '{self.method_name}' is read-only" \
                    .format_map(vars())
                raise AttributeError(msg)


            def __get__(self, instance, owner):


                def basis_vector():

                    vector = owner(*self.cvalues, _internal=True)

                    return vector


                basis_vector.__name__ = self.method_name
                basis_vector.__doc__ = \
                    "Basis vector, with length 'cunit' along the {self.cname}-axis" \
                    .format_map(vars())

                return basis_vector


        for index, cname in enumerate(cls._cnames):
            basis_name = 'basis_' + cname
            setattr(cls, basis_name, Basis(cls, index, cname, basis_name))


    def init_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)
        cls._cnull = cnull
        cls._cunit = cunit
        cls._true = cnull == cnull
        cls._false = cnull != cnull
        make_zero_vector_method(cls)
        make_one_vector_method(cls)
        setup_vector_bases(cls)
        hf.make_dunder_methods(
            cls,
            [
                (2, '', 'matmul', operator.matmul),
                (2, 'r', 'matmul', operator.matmul),
                # (2, 'i', 'matmul', operator.matmul)
            ]
        )

        return cls


    @init_Vector
    class Vector(SV):
        """
        A vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """

        _internal_functions = \
            [
                'and',
                'all',
                'floor',
                'ceil',
                'trunc'
            ]
        _component_operators = \
            {
                'arg1_n':
                    {
                        'abs': operator.abs,
                        'neg': operator.neg,
                        'pos': operator.pos,
                        'floor': math.floor,
                        'ceil': math.ceil,
                        'trunc': math.trunc
                    },
                'arg2_n':
                    {
                        'round': round,
                        'add': operator.add,
                        'sub': operator.sub,
                        'mul': operator.mul,
                        'pow': operator.pow,
                        'matmul': operator.matmul, # ?
                        'truediv': operator.truediv,
                        'floordiv': operator.floordiv,
                        'mod': operator.mod,
                    },
                'arg1_o':
                    {
                    },
                'arg2_o':
                    {
                    },
                'arg2_i':
                    {
                        'iadd': operator.iadd,
                        'isub': operator.isub,
                        'imul': operator.imul,
                        'ipow': operator.ipow,
                        'imatmul': operator.imatmul, # ?
                        'itruediv': operator.itruediv,
                        'ifloordiv': operator.ifloordiv,
                        'imod': operator.imod
                    }
            }


        @classmethod
        def component_null(cls):
            """Null value for vector components in class"""

            cnull = copy(cls._cnull)

            return cnull


        @classmethod
        def component_unit(cls):
            """Unit value for vector components in class"""

            cunit = copy(cls._cunit)

            return cunit


        @classmethod
        def repeat_cvalue(cls, value):
            """A vector with all component values set to value"""

            cunit = cls._cunit
            cvalues = \
                (
                    cunit*value
                    for _ in range(cls._dimensions)
                )
            vector = cls(*cvalues, _internal=True)

            return vector


        @classmethod
        def sum_of_vectors(cls, vectors):
            """The sum of several vectors"""

            vectors = cls._ensure_all_are_vectors(vectors)
            vector = reduce(operator.add, vectors, cls.zero())

            return vector


        @classmethod
        def prod_of_vectors(cls, vectors):
            """The product of several vectors"""

            vectors = cls._ensure_all_are_vectors(vectors)
            vector = reduce(operator.mul, vectors, cls.one())

            return vector


        def __init__(self, *cvalues, _internal=False, **named_cvalues):
            """TODO"""

            if _internal:
                self._cvalues = [ *cvalues ]
            else:
                self._check_arguments(cvalues, named_cvalues)
                cunit = self._cunit
                if len(named_cvalues) > 0:
                    self._cvalues = \
	                    [
	                        cunit*named_cvalues[cns]
	                        for cns in self._cnames
	                    ]
                else:
                    self._cvalues = \
                        [
                            cunit*cv
                            for cv in cvalues
                        ]


        def is_zero_vector(self):
            """Check if the vector is a zero vector"""

            cnull = self._cnull
            are_zeros = \
                (
                    cvs == cnull
                    for cvs in self._cvalues
                )
            is_zero = reduce(self.component_and, are_zeros)

            return is_zero


        def __setitem__(self, index, values):
            """Change vector component values by indexing"""

            cunit = self._cunit
            if isinstance(index, int):
                cvalues = cunit*values
            elif isinstance(index, slice):
                cvalues = \
                    [
                        cunit*cv
                        for cv in values
                    ]
                indices = range(*index.indices(self._dimensions))
                no_of_cvalues = len(cvalues)
                no_of_indices = len(indices)
                if no_of_cvalues != no_of_indices:
                    msg = \
                        "The number of given values ({no_of_cvalues}) does not match " \
                        "the number of components to be set ({no_of_indices})" \
                        .format_map(vars())
                    raise ValueError(msg)
            else:
                msg = \
                    "Vector index must be an integer or a slice, not {type_index.__name__}" \
                     .format(type_index=type(index))
                raise TypeError(msg)
            self._cvalues[index] = cvalues


        def __floor__(self):
            """Apply 'component_floor' to each of the vector component values"""

            vector = self._vector(map(self.component_floor, self._cvalues))

            return vector


        def __ceil__(self):
            """Apply 'component_ceil' to each of the vector component values"""

            vector = self._vector(map(self.component_ceil, self._cvalues))

            return vector


        def __trunc__(self):
            """Apply 'component_trunc' to each of the vector component values"""

            vector = self._vector(map(self.component_trunc, self._cvalues))

            return vector


        def __bool__(self):
            """Check if the vector is not a zero vector"""

            is_zero_vector = self.is_zero_vector()
            try:
                not_zero_vector = not self.component_all(is_zero_vector)
            except TypeError:
                not_zero_vector = None
            if not_zero_vector is None:
                not_zero_vector = not is_zero_vector

            return not_zero_vector


        def sum_of_components(self):
            """The sum of a vector's component values"""

            csum = self.component_null()
            for cvs in self._cvalues:
                csum += cvs

            return csum


        def prod_of_components(self):
            """The product of a vector's component values"""

            cprod = self.component_unit()
            for cvs in self._cvalues:
                cprod *= cvs

            return cprod


        @property
        def cnull(self):
            """Null value for vector components"""

            component_null = self.component_null()

            return component_null


        @property
        def cunit(self):
            """Unit value for vector components"""

            component_unit = self.component_unit()

            return component_unit


        @property
        def csum(self):
            """The sum of a vector's component values"""

            sum_of_components = self.sum_of_components()

            return sum_of_components


        @property
        def cprod(self):
            """The product of a vector's component values"""

            prod_of_components = self.prod_of_components()

            return prod_of_components


    return Vector

