"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import skvectors.helper_functions as hf
from skvectors.cartesian_2d_vectors import create_class_Cartesian_2D_Vector
from skvectors.make_tolerant import make_Cartesian_Vector_Tolerant


def create_class_Tolerant_Cartesian_2D_Vector(name, component_names, *, brackets='<>', sep=', ', cnull=0, cunit=1, functions=None, abs_tol=1e-12, rel_tol=1e-9):
    """
    Function that creates a tolerant cartesian vector class with 2 dimensions
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    if functions is None:
        functions = { }
    C2DV = \
        create_class_Cartesian_2D_Vector(
            name = 'C2DV_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep,
            cnull = cnull,
            cunit = cunit,
            functions = functions
        )
    TC2DV = \
        make_Cartesian_Vector_Tolerant(
            cartesian_vector_class = C2DV,
            name = name,
            functions = functions,
            abs_tol = abs_tol,
            rel_tol = rel_tol
        )


    @hf.ensure_other_is_vector
    def are_parallel(self, other):
        """Check if two vectors are parallel (within a calculated tolerance)"""

        try:
            vsn = self.normalize()
        except ZeroDivisionError:
            vsn = None
        try:
            von = other.normalize()
        except ZeroDivisionError:
            von = None
        if (vsn is None) or (von is None):
            parallel = self._true
        else:
            perp_dot = vsn.perp_dot(von)
            parallel = self._equal_cnull(perp_dot)
            parallel = self.component_or(parallel, self.is_zero_vector())
            parallel = self.component_or(parallel, other.is_zero_vector())

        return parallel


    TC2DV.are_parallel = are_parallel

    return TC2DV

