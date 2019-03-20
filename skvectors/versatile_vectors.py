"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import operator
import math
import skvectors.helper_functions as hf
from skvectors.simple_vectors import create_class_Simple_Vector


def create_class_Versatile_Vector(name, component_names, *, brackets='<>', sep=', ', functions=None):
    """
    Function that creates a versatile vector class
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    if functions is None:
        functions = { }

    SV = \
        create_class_Simple_Vector(
            name = 'SV_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep
        )


    def init_Versatile_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)
        hf.make_dunder_methods(
            cls,
            [
                (1, '', 'not', operator.not_),
                (1, '', 'index', operator.index),
                (1, '', 'inv', operator.inv),
                (1, '', 'invert', operator.invert),
                (2, '', 'matmul', operator.matmul),
                (2, '', 'eq', operator.eq),
                (2, '', 'ne', operator.ne),
                (2, '', 'lt', operator.lt),
                (2, '', 'gt', operator.gt),
                (2, '', 'le', operator.le),
                (2, '', 'ge', operator.ge),
                (2, '', 'and', operator.and_),
                (2, '', 'or', operator.or_),
                (2, '', 'xor', operator.xor),
                (2, '', 'lshift', operator.lshift),
                (2, '', 'rshift', operator.rshift),
                (2, 'r', 'matmul', operator.matmul),
                (2, 'r', 'and', operator.and_),
                (2, 'r', 'or', operator.or_),
                (2, 'r', 'xor', operator.xor),
                (2, 'r', 'lshift', operator.lshift),
                (2, 'r', 'rshift', operator.rshift),
                (2, 'i', 'matmul', operator.matmul),
                (2, 'i', 'and', operator.and_),
                (2, 'i', 'or', operator.or_),
                (2, 'i', 'xor', operator.xor),
                (2, 'i', 'lshift', operator.lshift),
                (2, 'i', 'rshift', operator.rshift)
            ]
        )

        return cls


    @init_Versatile_Vector
    class Versatile_Vector(SV):
        """
        A versatile vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """

        _internal_functions = \
            [
                'any'
            ]
        _component_operators = \
            {
                'arg1_n':
                    {
                        'not': operator.not_,
                        'truth': operator.truth,
                        'abs': operator.abs,
                        'neg': operator.neg,
                        'pos': operator.pos,
                        'index': operator.index,
                        'inv': operator.inv,
                        'invert': operator.invert,
                        'floor': math.floor,
                        'ceil': math.ceil,
                        'trunc': math.trunc
                    },
                'arg2_n':
                    {
                        'round': round,
                        'and': operator.and_,
                        'or': operator.or_,
                        'xor': operator.xor,
                        'eq': operator.eq,
                        'ne': operator.ne,
                        'lt': operator.lt,
                        'gt': operator.gt,
                        'le': operator.le,
                        'ge': operator.ge,
                        'add': operator.add,
                        'sub': operator.sub,
                        'mul': operator.mul,
                        'pow': operator.pow,
                        'matmul': operator.matmul,
                        'truediv': operator.truediv,
                        'floordiv': operator.floordiv,
                        'mod': operator.mod,
                        'lshift': operator.lshift,
                        'rshift': operator.rshift,
                        'is': operator.is_,
                        'isnot': operator.is_not,
                        'concat': operator.concat,
                        'contains': operator.contains,
                        'countof': operator.countOf,
                        'indexof': operator.indexOf,
                        'getitem': operator.getitem
                    },
                'arg1_o':
                    {
                        'delitem': operator.delitem
                    },
                'arg2_o':
                    {
                        'setitem': operator.setitem
                    },
                'arg2_i':
                    {
                        'iand': operator.iand,
                        'ior': operator.ior,
                        'ixor': operator.ixor,
                        'iadd': operator.iadd,
                        'isub': operator.isub,
                        'imul': operator.imul,
                        'ipow': operator.ipow,
                        'imatmul': operator.imatmul,
                        'itruediv': operator.itruediv,
                        'ifloordiv': operator.ifloordiv,
                        'imod': operator.imod,
                        'ilshift': operator.ilshift,
                        'irshift': operator.irshift
                    }
            }


    return Versatile_Vector

