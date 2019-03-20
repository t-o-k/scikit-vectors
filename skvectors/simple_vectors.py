"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import operator
import math
from copy import copy
import skvectors.helper_functions as hf
from skvectors.fundamental_vectors import create_class_Fundamental_Vector


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


def create_class_Simple_Vector(name, component_names, *, brackets='<>', sep=', '):
    """
    Function that creates a simple vector class
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    FV = \
        create_class_Fundamental_Vector(
            name = 'FV_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep
        )


    def init_Simple_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=None)
        hf.make_dunder_methods(
            cls,
            [
                (1, '', 'abs', operator.abs),
                (1, '', 'neg', operator.neg),
                (1, '', 'pos', operator.pos),
                (2, '', 'add', operator.add),
                (2, '', 'sub', operator.sub),
                (2, '', 'mul', operator.mul),
                (2, '', 'pow', operator.pow),
                (2, '', 'truediv', operator.truediv),
                (2, '', 'floordiv', operator.floordiv),
                (2, '', 'mod', operator.mod),
                (2, 'r', 'add', operator.add),
                (2, 'r', 'sub', operator.sub),
                (2, 'r', 'mul', operator.mul),
                (2, 'r', 'pow', operator.pow),
                (2, 'r', 'truediv', operator.truediv),
                (2, 'r', 'floordiv', operator.floordiv),
                (2, 'r', 'mod', operator.mod),
                (2, 'i', 'add', operator.add),
                (2, 'i', 'sub', operator.sub),
                (2, 'i', 'mul', operator.mul),
                (2, 'i', 'pow', operator.pow),
                (2, 'i', 'truediv', operator.truediv),
                (2, 'i', 'floordiv', operator.floordiv),
                (2, 'i', 'mod', operator.mod)
            ]
        )

        return cls


    @init_Simple_Vector
    class Simple_Vector(FV):
        """
        A simple vector class with {dimensions} dimensions and the component names '{cs_cnames}'
        """

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
                        'itruediv': operator.itruediv,
                        'ifloordiv': operator.ifloordiv,
                        'imod': operator.imod
                    }
            }


        def _cvalues_present(self, cnames):

            cnames_present = \
                (
                    cns in cnames
                    for cns in self._cnames
                )
            result = zip(self._cvalues, cnames_present)

            return result


        def _apply_operator_arg1_n(self, op, cnames):

            cvalues_present = self._cvalues_present(cnames)


            def apply_op_arg1_n():

                vector = \
                    self._vector(
                        op(cvs) if present else cvs
                        for cvs, present in cvalues_present
                    )

                return vector


            return apply_op_arg1_n


        def _apply_operator_arg2_n(self, op, cnames):

            cvalues_present = self._cvalues_present(cnames)


            def apply_op_arg2_n(value):

                vector = \
                    self._vector(
                        op(cvs, value) if present else cvs
                        for cvs, present in cvalues_present
                    )

                return vector


            return apply_op_arg2_n


        def _apply_operator_arg1_o(self, op, cnames):

            cvalues_present = self._cvalues_present(cnames)


            def apply_op(cvs, value):
	
                cvs = copy(cvs)
                op(cvs, value)

                return cvs


            def apply_op_arg1_o(value):

                vector = \
                    self._vector(
                        apply_op(cvs, value) if present else cvs
                        for cvs, present in cvalues_present
                    )

                return vector


            return apply_op_arg1_o


        def _apply_operator_arg2_o(self, op, cnames):

            cvalues_present = self._cvalues_present(cnames)


            def apply_op(cvs, value0, value1):

                cvs = copy(cvs)
                op(cvs, value0, value1)

                return cvs


            def apply_op_arg2_o(value0, value1):

                vector = \
                    self._vector(
                        apply_op(cvs, value0, value1) if present else cvs
                        for cvs, present in cvalues_present
                    )

                return vector


            return apply_op_arg2_o


        def _apply_operator_arg2_i(self, op, cnames):

            cvalues_present = self._cvalues_present(cnames)


            def apply_op_arg2_i(value):

                self._cvalues = \
                    [
                        op(cvs, value) if present else cvs
                        for cvs, present in cvalues_present
                    ]


            return apply_op_arg2_i


        def __round__(self, ndigits=0):
            """Round each component value to a given precision in decimal digits"""

            vector = \
                self._vector(
                    round(cvs, ndigits)
                    for cvs in self._cvalues
                )

            return vector


        def __floor__(self):
            """Apply math.floor to each of the vector component values"""

            vector = self._vector(map(math.floor, self._cvalues))

            return vector


        def __ceil__(self):
            """Apply math.ceil to each of the vector component values"""

            vector = self._vector(map(math.ceil, self._cvalues))

            return vector


        def __trunc__(self):
            """Apply math.trunc to each of the vector component values"""

            vector = self._vector(map(math.trunc, self._cvalues))

            return vector


        def _decode_attr_name(self, attr_name):

            if attr_name.startswith('c_'):
                attr_name = attr_name[2:]
                method_name, *decoded_cnames = attr_name.split('_')
                for op_type, operator_names in self._component_operators.items():
                    if method_name in operator_names:
                        break
                else:
                    op_type = None
                if len(decoded_cnames) == 0:
                    bar = False
                else:
                    bar = decoded_cnames[0] == 'bar'
                    if bar:
                        del decoded_cnames[0]
                if verify_names(chk_names=decoded_cnames, ref_names=self._cnames):
                    if bar:
                        decoded_cnames = \
                            [
                                cns
                                for cns in self._cnames
                                if cns not in decoded_cnames
                            ]
                else:
                    decoded_cnames = None
            else:
                method_name, op_type, decoded_cnames = None, None, None

            return method_name, op_type, decoded_cnames


        def __setattr__(self, attr_name, value):
            """TODO"""

            decoded_attr_name = self._decode_attr_name(attr_name)
            if any(val is None for val in decoded_attr_name):
                super().__setattr__(attr_name, value)
            else:
                cls = type(self)
                msg = "'{cls.__name__}' object attribute '{attr_name}' is read-only"
                raise AttributeError(msg.format_map(vars()))


        def __getattr__(self, attr_name):
            """TODO"""

            try:
                attr = super().__getattribute__(attr_name)
            except AttributeError:
                attr = None
            if attr is None:
                decoded_attr_name = self._decode_attr_name(attr_name)
                if any(val is None for val in decoded_attr_name):
                    cls = type(self)
                    msg = "'{cls.__name__}' object has no attribute '{attr_name}'"
                    raise AttributeError(msg.format_map(vars()))
                else:
                    method_name, op_type, cnames = decoded_attr_name
                    op = self._component_operators[op_type][method_name]
                    methods_apply_op = \
                        {
                            'arg1_n': self._apply_operator_arg1_n,
                            'arg2_n': self._apply_operator_arg2_n,
                            'arg1_o': self._apply_operator_arg1_o,
                            'arg2_o': self._apply_operator_arg2_o,
                            'arg2_i': self._apply_operator_arg2_i
                        }
                    method = methods_apply_op[op_type]
                    attr = method(op, cnames)
                    attr.__name__ = attr_name
                    attr.__doc__ = \
                        "Applies operator '{method_name}' to these vector components: {component_names}" \
                        .format(method_name=method_name, component_names=', '.join(cnames))

            return attr


    return Simple_Vector

