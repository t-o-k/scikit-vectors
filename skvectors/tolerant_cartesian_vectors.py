"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import skvectors.helper_functions as hf
from skvectors.cartesian_vectors import create_class_Cartesian_Vector
from skvectors.make_tolerant import make_Cartesian_Vector_Tolerant


def create_class_Tolerant_Cartesian_Vector(name, component_names, *, brackets='<>', sep=', ', cnull=0, cunit=1, functions=None, abs_tol=1e-12, rel_tol=1e-9):
    """
    Function that creates a tolerant cartesian vector class
    The number of dimensions are determined by the number of component names
    """

    hf.verify_class_name(name)
    if functions is None:
        functions = { }
    CV = \
        create_class_Cartesian_Vector(
            name = 'CV_' + name,
            component_names = component_names,
            brackets = brackets,
            sep = sep,
            cnull = cnull,
            cunit = cunit,
            functions = functions
        )
    TCV = \
        make_Cartesian_Vector_Tolerant(
            cartesian_vector_class = CV,
            name = name,
            functions = functions,
            abs_tol = abs_tol,
            rel_tol = rel_tol
        )

    return TCV

