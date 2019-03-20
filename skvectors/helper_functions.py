"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import keyword
import operator
import math
from functools import wraps
from pydoc import render_doc, plaintext


def ensure_other_is_vector(method):


    @wraps(method)
    def wrapper(self, other, *args, **kwargs):

        if not self.is_vector(other):
            other = self.repeat_cvalue(other)

        return method(self, other, *args, **kwargs)


    return wrapper


def ensure_others_are_vectors(method):


    @wraps(method)
    def wrapper(self, other, other_, *args, **kwargs):

        if not self.is_vector(other):
            other = self.repeat_cvalue(other)
        if not self.is_vector(other_):
            other_ = self.repeat_cvalue(other_)

        return method(self, other, other_, *args, **kwargs)


    return wrapper


def setup_internal_functions(cls, functions):


    def and_(a, b):
        """Return True if both a and b evaluates to True, else return False"""

        return bool(a and b)


    def or_(a, b):
        """Return True if either a or b evaluates to True, else return False"""

        return bool(a or b)


    if functions is not None:
        functions = dict(functions)
        default_functions = \
            {
                'and': and_,
                'or': or_,
                'all': all,
                'any': any,
                'min': min,
                'max': max,
                'abs': abs,
                'not': operator.not_, # ?
                'trunc': math.trunc,
                'floor': math.floor,
                'ceil': math.ceil,
                'pi': math.pi,
                'atan2': math.atan2,
                'cos': math.cos,
                'sin': math.sin,
                'copysign': math.copysign,
                'log10': math.log10
            }
        internal_functions = getattr(cls, '_internal_functions', { })
        for fname in internal_functions:
            if fname in functions:
                fn = functions[fname]
            else:
                fn = default_functions[fname]
            cfname = 'component_' + fname
            if fname == 'pi':
                setattr(cls, cfname, fn)
                # cunit = cls._cunit
                # setattr(cls, cfname, cunit*fn)
            else:
                method = staticmethod(fn)
                setattr(cls, cfname, method)


def verify_class_name(name):

    if not isinstance(name, str):
        msg = "The class name is not a string"
        raise TypeError(msg)
    if keyword.iskeyword(name):
        msg = "The class name is a built in keyword"
        raise ValueError(msg)
    if not name.isidentifier():
        msg = "The class name is not a valid identifier"
        raise ValueError(msg)


def setup_vector_class(*, cls, name, functions):

    cls.__name__ = name
    cls.__doc__ = \
        cls.__doc__.format(
            dimensions = cls._dimensions,
            cs_cnames = ', '.join(cls._cnames)
        )
    setup_internal_functions(cls, functions)


def make_method_arg1(name, function):
    """TODO"""


    def method(self):

        vector = self._vector(map(function, self._cvalues))

        return vector


    method.__name__ = name
    function_doc = render_doc(function, title='%s', renderer=plaintext)
    doc = "Apply this function component-wise to a vector:\n\n"
    doc += function_doc
    method.__doc__ = doc

    return method


def make_method_arg2(name, function):
    """TODO"""


    @ensure_other_is_vector
    def method(self, other):

        vector = self._vector(map(function, self._cvalues, other._cvalues))

        return vector


    method.__name__ = name
    function_doc = render_doc(function, title='%s', renderer=plaintext)
    doc = "Apply this function component-wise to two vectors:\n\n"
    doc += function_doc
    method.__doc__ = doc

    return method


def make_method_arg2_r(name, function):
    """TODO"""


    @ensure_other_is_vector
    def method(self, other):

        vector = self._vector(map(function, other._cvalues, self._cvalues))

        return vector


    method.__name__ = name
    function_doc = render_doc(function, title='%s', renderer=plaintext)
    doc = "Apply this right-side function component-wise to two vectors:\n\n"
    doc += function_doc
    method.__doc__ = doc

    return method


def make_method_arg2_i(name, function):
    """TODO"""


    @ensure_other_is_vector
    def method(self, other):

        self._cvalues = [ *map(function, self._cvalues, other._cvalues) ]

        return self


    method.__name__ = name
    function_doc = render_doc(function, title='%s', renderer=plaintext)
    doc = "Apply this in-place function component-wise to two vectors:\n\n"
    doc += function_doc
    method.__doc__ = doc

    return method


def make_method_arg3(name, function):
    """TODO"""


    @ensure_others_are_vectors
    def method(self, other, other_):

        vector = self._vector(map(function, self._cvalues, other._cvalues, other_._cvalues))

        return vector


    method.__name__ = name
    function_doc = render_doc(function, title='%s', renderer=plaintext)
    doc = "Apply this function component-wise to three vectors:\n\n"
    doc += function_doc
    method.__doc__ = doc

    return method


def make_dunder_methods(cls, functions):
    """Make double-under methods"""

    for no_of_args, prefix, name, fn in functions:
        make_methods = \
            {
                '1': make_method_arg1,
                '2': make_method_arg2,
                '2r': make_method_arg2_r,
                '2i': make_method_arg2_i
            }
        make_method = make_methods[str(no_of_args) + prefix]
        method_name = '__' + prefix + name + '__'
        method = make_method(method_name, fn)
        setattr(cls, method_name, method)

