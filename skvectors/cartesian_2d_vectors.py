"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import skvectors.helper_functions as hf
from skvectors.cartesian_vectors import create_class_Cartesian_Vector


def create_class_Cartesian_2D_Vector(name, component_names, *, brackets='<>', sep=', ', cnull=0, cunit=1, functions=None):
    """
    Function that creates a cartesian vector class with 2 dimensions
    """

    hf.verify_class_name(name)
    dimensions = 2
    component_names = [ *component_names ]
    if len(component_names) != dimensions:
        msg = "The number of component names must be {dimensions}"
        raise ValueError(msg.format_map(vars()))
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


    def init_Cartesian_2D_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)

        return cls


    @init_Cartesian_2D_Vector
    class Cartesian_2D_Vector(CV):
        """
        A cartesian vector class with {dimensions} dimensions and the component names '{cs_cnames}'
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
                # 'pi',
                # 'atan2',
                'cos',
                'sin'
            ]


        @classmethod
        def from_polar(cls, radius, azimuth):
            """A vector created from polar coordinates"""

            cunit = cls._cunit
            azimuth = cunit*azimuth
            cos_a = cls.component_cos(azimuth)
            sin_a = cls.component_sin(azimuth)
            radius = cunit*radius
            vector = \
                cls(
                    radius*cos_a,
                    radius*sin_a,
                    _internal = True
                )

            return vector


        def perp(self):
            """A vector that is perpendicular to a vector"""

            cvs0, cvs1 = self._cvalues
            vector = self._vector((-cvs1, cvs0))

            return vector


        def perp_dot(self, other):
            """The dot product of a vector that is perpendicular to a vector and another vector"""

            scalar = self.perp().dot(other)

            return scalar


        @hf.ensure_other_is_vector
        def sin(self, other):
            """The sine of the angle between two vectors (from -cunit to +cunit)"""

            ls = self.length()
            lo = other.length()
            pd = self.perp_dot(other)
            try:
                sine = pd/(ls*lo)
            except ZeroDivisionError as err:
                msg = "One (or both) of the vectors is a zero vector"
                raise ZeroDivisionError(msg) from err
            cunit = self._cunit
            sine = self.clip(sine, -cunit, cunit)

            return sine


        @hf.ensure_other_is_vector
        def angle(self, other):
            """The angle in radians (from -cunit*pi to +cunit*pi) between two vectors"""  ### Verify

            cvs0, cvs1 = self._cvalues
            cvo0, cvo1 = other._cvalues
            angle_s = self.component_atan2(cvs1, cvs0)
            angle_o = other.component_atan2(cvo1, cvo0)
            angle_between = angle_o - angle_s
            # angle_between = self._angle_to_minus_plus_pi(angle_between)

            return angle_between


        def rotate(self, angle):
            """The vector rotated by an angle in radiands"""

            cunit = self._cunit
            angle = cunit*angle
            cos = self.component_cos(angle)
            sin = self.component_sin(angle)
            vector = \
                self._mmult(
                    self._vector(( cos, -sin)),
                    self._vector(( sin,  cos))
                )

            return vector


        @hf.ensure_other_is_vector
        def are_parallel(self, other):
            """Check if two vectors are parallel"""

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


        @hf.ensure_others_are_vectors
        def reorient(self, other, other_):
            """Reorient a vector from one direction to another direction"""

            angle = other.angle(other_)
            vector = self.rotate(angle)

            return vector


        def polar_as_dict(self):
            """Polar coordinates of a vector as a dictionary"""

            result = \
                {
                    'radius': self.radius,
                    'azimuth': self.azimuth
                }

            return result


        @property
        def radius(self):
            """TODO"""

            length = self.length()

            return length


        @property
        def azimuth(self):
            """TODO"""

            cvs0, cvs1 = self._cvalues
            angle = self.component_atan2(cvs1, cvs0)
            # angle = self._angle_to_minus_plus_pi(angle)

            return angle


    return Cartesian_2D_Vector

