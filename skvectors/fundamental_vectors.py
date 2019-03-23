"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

from copy import copy
from inspect import getfullargspec, isfunction, ismethod  # isbuiltin
# import functools
import skvectors.helper_functions as hf


def check_identifier(identifier):
    """Check if identifier is a valid name for a vector component"""

    valid_chars = \
        ''.join(
            (
                'abcdefghijklmnopqrstuvwxyz',  # latin lc
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ',  # latin uc
                ''.join(chr(i) for i in range(0x03b1, 0x03ca)),  # greek lc
                ''.join(chr(i) for i in range(0x0391, 0x03aa))   # greek uc
            )
        )
    decimal_digits = '0123456789'
    first_char, *remaining_chars = identifier
    valid_first_char = first_char in valid_chars
    valid_remaining_chars = \
        all(
            char in (valid_chars + decimal_digits)
            for char in remaining_chars
        )

    return valid_first_char and valid_remaining_chars


def verify_names(*, chk_names, ref_names):
    """
    Verifies that all names in chk_names also are in ref_names and in the same order.
    Names that appear multiple times in chk_names should appear the same number of times in ref_names.
    """

    i_chk = iter(chk_names)
    i_ref = iter(ref_names)
    chk = next(i_chk, None)
    ref = next(i_ref, None)
    while (chk is not None) and (ref is not None):
        if chk == ref:
            chk = next(i_chk, None)
        ref = next(i_ref, None)
    names_ok = chk is None

    return names_ok


def create_class_Fundamental_Vector(name, component_names, *, brackets='<>', sep=', '):
    """
    Function that creates a fundamental vector class
    The number of dimensions are determined by the number of component names
    """


    def verify_arguments(component_names, dimensions, brackets):

        if len(component_names) != dimensions:
            msg = "Some of the component names are not unique"
            raise ValueError(msg)
        if dimensions == 0:
            msg = "The number of component names is 0"
            raise ValueError(msg)
        for cname in component_names:
            if not isinstance(cname, str):
                msg = "One (or more) of the component names is not a string"
                raise TypeError(msg)
            if not check_identifier(cname):
                msg = \
                    "All characters in the component names must be either " \
                    "a latin letter, a greek letter or a decimal digit, except " \
                    "for the first character which should not be a digit"
                raise ValueError(msg)
        if len(brackets) != 2:
            msg = "The number of characters (or strings) for the brackets is not 2"
            raise ValueError(msg)


    hf.verify_class_name(name)
    component_names = [ *component_names ]
    dimensions = len(set(component_names))
    brackets = [ str(br) for br in brackets ]
    sep = str(sep)
    verify_arguments(component_names, dimensions, brackets)


    def setup_components_access(cls):

        for index, cname in enumerate(cls._cnames):


            def cget(self, _index=index):

                value = copy(self._cvalues[_index])

                return value


            def cset(self, value, _index=index):

                self._cvalues[_index] = copy(value)


            cdoc = \
                "Value of {cname}-component of vector (component no. {index})" \
                .format_map(vars())
            setattr(cls, cname, property(fget=cget, fset=cset, doc=cdoc))


    def init_Fundamental_Vector(cls):
        """Initialize class"""

        cls._dimensions = dimensions
        cls._cnames = component_names
        cls.brackets = brackets
        cls.sep = sep
        hf.setup_vector_class(cls=cls, name=name, functions=None)
        setup_components_access(cls)

        return cls


    @init_Fundamental_Vector
    class Fundamental_Vector:
        """
        A fundamental vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """


        @classmethod
        def dimensions(cls):
            """Number of dimensions for vectors in the class"""

            dim = cls._dimensions

            return dim


        @classmethod
        def component_names(cls):
            """List of component names for vectors in the class"""

            cnames = cls._cnames.copy()

            return cnames


        @classmethod
        def is_vector(cls, va):
            """Check if something is a vector"""

            result = isinstance(va, cls)

            return result


        @classmethod
        def repeat_cvalue(cls, value):
            """A vector with all component values set to value"""

            cvalues = \
                (
                    copy(value)
                    for _ in range(cls._dimensions)
                )
            vector = cls(*cvalues, _internal=True)

            return vector


        @classmethod
        def _ensure_all_are_vectors(cls, vectors):

            vectors = \
                (
                    v if cls.is_vector(v) else cls.repeat_cvalue(v)
                    for v in vectors
                )

            return vectors


        def __init__(self, *cvalues, _internal=False, **named_cvalues):
            """TODO"""

            if _internal:
                self._cvalues = [ *cvalues ]
            else:
                self._check_arguments(cvalues, named_cvalues)
                if len(named_cvalues) > 0:
                    self._cvalues = \
	                [
	                    copy(named_cvalues[cns])
	                    for cns in self._cnames
	                ]
                else:
                    self._cvalues = \
                        [
                            copy(cv)
                            for cv in cvalues
                        ]


        def _check_arguments(self, cvalues, named_cvalues):

            no_of_cvalues = len(cvalues)
            no_of_named_cvalues = len(named_cvalues)
            cls = type(self)
            if (no_of_cvalues == self._dimensions) and (no_of_named_cvalues == 0):
                pass
            elif (no_of_cvalues == 0) and (no_of_named_cvalues == self._dimensions):
                if set(named_cvalues) == set(self._cnames):
                    pass
                else:
                    msg = "One or more keyword argument to {cls.__name__}() was given with wrong name)"
                    raise ValueError(msg.format_map(vars()))
            else:
                if no_of_cvalues == 0:
                    if no_of_named_cvalues == 0:
                        msg = "{cls.__name__}() takes {self._dimensions} argument(s) (0 was given)"
                    else:
                        msg = "{cls.__name__}() takes {self._dimensions} argument(s) ({no_of_named_cvalues} was given)"
                else:
                    if no_of_named_cvalues == 0:
                        msg = "{cls.__name__}() takes {self._dimensions} argument(s) ({no_of_cvalues} was given)"
                    else:
                        msg = "Arguments to {cls.__name__}() must either be given with or without keywords (both was given)"
                raise TypeError(msg.format_map(vars()))


        def component_values(self):
            """List of a vector's component values"""

            cvalues = \
                [
                    copy(cvs)
                    for cvs in self._cvalues
                ]

            return cvalues


        def _vector(self, cvalues):

            cls = type(self)
            vector = cls(*cvalues, _internal=True)

            return vector


        def copy(self):
            """Copy of vector"""

            vector = self._vector(map(copy, self._cvalues))

            return vector


        @property
        def cnames(self):
            """List of a vector's component names"""

            component_names = self.component_names()

            return component_names


        @property
        def cvalues(self):
            """List of a vector's component values"""

            component_values = self.component_values()

            return component_values


        def as_dict(self):
            """A vector's component names and values in a dictionary"""

            result = \
                dict(
                    zip(
                        self.component_names(),
                        self.component_values()
                    )
                )

            return result


        def __len__(self):
            """Number of dimensions for vector"""

            dimensions = self._dimensions

            return dimensions


        def __str__(self):
            """Apply str() to each component value"""

            csv = self.sep.join(map(str, self._cvalues))
            string = csv.join(self.brackets)

            return string


        def __repr__(self):
            """Apply repr() to each component value"""

            csv = \
                self.sep.join(
                    cns + '=' + repr(cvs)
                    for cns, cvs in zip(self._cnames, self._cvalues)
                )
            cls = type(self)
            string = cls.__name__ + '(' + csv + ')'

            return string


        def __format__(self, format_spec=''):
            """Apply format() to each component value"""

            csv = \
                self.sep.join(
                    format(cvs, format_spec)
                    for cvs in self._cvalues
                )
            string = csv.join(self.brackets)

            return string


        def __iter__(self):
            """Iterable for iterating over the vector component values"""

            yield from map(copy, self._cvalues)


        def __getitem__(self, index):
            """Retrive vector component values by indexing"""

            cvalues = self.component_values()

            return cvalues[index]


        def __setitem__(self, index, values):
            """Change vector component values by indexing"""

            if isinstance(index, int):
                cvalues = copy(values)
            elif isinstance(index, slice):
                cvalues = \
                    [
                        copy(cv)
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
                    "Vector indices must be integers or slices, not {type_index.__name__}" \
                    .format(type_index=type(index))
                raise TypeError(msg)
            self._cvalues[index] = cvalues


        @hf.ensure_other_is_vector
        def __eq__(self, other):

            for cvs, cvo in zip(self._cvalues, other._cvalues):
                if cvs != cvo:
                    equal = False
                    break
            else:
                equal = True

            return equal


        @hf.ensure_other_is_vector
        def __ne__(self, other):

            for cvs, cvo in zip(self._cvalues, other._cvalues):
                if cvs != cvo:
                    not_equal = True
                    break
            else:
                not_equal = False

            return not_equal


        def __contains__(self, value):
            """Check if a value is equal to any of the vector component values"""

            contains = value in self._cvalues

            return contains


        def __call__(self, function, needs_index=False):
            """Apply a function to each of the vector component values"""

            if needs_index:
                dimensions = self._dimensions
                vector = \
                    self._vector(
                        function(cvs, index, dimensions)
                        for index, cvs in enumerate(self._cvalues)
                    )
            else:
                vector = self._vector(map(function, self._cvalues))

            return vector


        @classmethod
        def _verify_function(cls, name, function, no_of_arguments):

            if function is None:
                method_name = 'component_' + name
                if not hasattr(cls, method_name):
                    msg = \
                        "class {cls.__name__} has no method named '{method_name}'" \
                        .format_map(vars())
                    raise AttributeError(msg)
            else:
                # function_types = \
                #     (
                #         types.FunctionType,
                #         types.BuiltinFunctionType,
                #         functools.partial
                #     )
                # if not isinstance(function, function_types):
                function_name = getattr(function, '__name__', str(function))
                if not (isfunction(function) or ismethod(function)):
                    msg = \
                        "{function_name} can not be used here" \
                        .format_map(vars())
                    raise TypeError(msg)
                msg = \
                    "{function_name} can not be called with {n} argument{s}" \
                    .format(
                        function_name = function_name,
                        n = no_of_arguments,
                        s = '' if no_of_arguments == 1 else 's'
                    )
                argspec = getfullargspec(function)
                arg_count = len(argspec.args)
                if argspec.defaults is not None:
                    arg_count -= len(argspec.defaults)
                if arg_count > no_of_arguments:
                    raise TypeError(msg)
                if arg_count < no_of_arguments and argspec.varargs is None:
                    raise TypeError(msg)
                kwonly_arg_count = len(argspec.kwonlyargs)
                if argspec.defaults is not None:
                    kwonly_arg_count -= len(argspec.kwonly_defaults)
                if kwonly_arg_count > 0:
                    raise TypeError(msg)


        @classmethod
        def create_vector_method_arg1(cls, name, function=None):
            """TODO"""

            cls._verify_function(name, function, 1)
            if function is None:
                function = getattr(cls, 'component_' + name)
            name = 'vector_' + name
            vector_function = hf.make_method_arg1(name, function)
            setattr(cls, name, vector_function)


        @classmethod
        def create_vector_method_arg2(cls, name, function=None):
            """TODO"""

            cls._verify_function(name, function, 2)
            if function is None:
                function = getattr(cls, 'component_' + name)
            name = 'vector_' + name
            vector_function = hf.make_method_arg2(name, function)
            setattr(cls, name, vector_function)


        @classmethod
        def create_vector_method_arg3(cls, name, function=None):
            """TODO"""

            cls._verify_function(name, function, 3)
            if function is None:
                function = getattr(cls, 'component_' + name)
            name = 'vector_' + name
            vector_function = hf.make_method_arg3(name, function)
            setattr(cls, name, vector_function)


    return Fundamental_Vector

