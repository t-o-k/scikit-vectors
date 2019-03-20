"""
Copyright (c) 2017, 2019 Tor Olav Kristensen, http://subcube.com
https://github.com/t-o-k/scikit-vectors
Use of this source code is governed by a BSD-license that can be found in the LICENSE file.
"""

import skvectors.helper_functions as hf
from skvectors.cartesian_vectors import create_class_Cartesian_Vector


def create_class_Cartesian_3D_Vector(name, component_names, *, brackets='<>', sep=', ', cnull=0, cunit=1, functions=None):
    """Function that creates a cartesian vector class with 3 dimensions"""

    hf.verify_class_name(name)
    dimensions = 3
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


    def make_rotate_0_method(cls):


        def rotate_0(self, angle):
            """A vector rotated around the {axis_name}-axis by an angle in radians"""

            cnull = self._cnull
            cunit = self._cunit
            angle = cunit*angle
            cos = self.component_cos(angle)
            sin = self.component_sin(angle)
            vector = \
                self._mmult(
                    self._vector((cunit, cnull, cnull)),
                    self._vector((cnull,   cos,  -sin)),
                    self._vector((cnull,   sin,   cos))
                )

            return vector


        axis_name = cls._cnames[0]
        rotate_0.__doc__ = rotate_0.__doc__.format_map(vars())
        method_name = 'rotate_' + axis_name
        rotate_0.__name__ = method_name
        setattr(cls, method_name, rotate_0)


    def make_rotate_1_method(cls):


        def rotate_1(self, angle):
            """A vector rotated around the {axis_name}-axis by an angle in radians"""

            cnull = self._cnull
            cunit = self._cunit
            angle = cunit*angle
            cos = self.component_cos(angle)
            sin = self.component_sin(angle)
            vector = \
                self._mmult(
                    self._vector((  cos, cnull,   sin)),
                    self._vector((cnull, cunit, cnull)),
                    self._vector(( -sin, cnull,   cos))
                )

            return vector


        axis_name = cls._cnames[1]
        rotate_1.__doc__ = rotate_1.__doc__.format_map(vars())
        method_name = 'rotate_' + axis_name
        rotate_1.__name__ = method_name
        setattr(cls, method_name, rotate_1)


    def make_rotate_2_method(cls):


        def rotate_2(self, angle):
            """A vector rotated around the {axis_name}-axis by an angle in radians"""

            cnull = self._cnull
            cunit = self._cunit
            angle = cunit*angle
            cos = self.component_cos(angle)
            sin = self.component_sin(angle)
            vector = \
                self._mmult(
                    self._vector((  cos,  -sin, cnull)),
                    self._vector((  sin,   cos, cnull)),
                    self._vector((cnull, cnull, cunit))
                )

            return vector


        axis_name = cls._cnames[2]
        rotate_2.__doc__ = rotate_2.__doc__.format_map(vars())
        method_name = 'rotate_' + axis_name
        rotate_2.__name__ = method_name
        setattr(cls, method_name, rotate_2)


    def init_Cartesian_3D_Vector(cls):
        """Initialize class"""

        hf.setup_vector_class(cls=cls, name=name, functions=functions)
        make_rotate_0_method(cls)
        make_rotate_1_method(cls)
        make_rotate_2_method(cls)

        return cls


    @init_Cartesian_3D_Vector
    class Cartesian_3D_Vector(CV):
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
        def from_polar(cls, radius, azimuth, inclination):
            """A vector created from polar coordinates"""

### Add check for negative radius
            cunit = cls._cunit
            azimuth = cunit*azimuth
            cos_a = cls.component_cos(azimuth)
            sin_a = cls.component_sin(azimuth)
            inclination = cunit*inclination
            cos_i = cls.component_cos(inclination)
            sin_i = cls.component_sin(inclination)
            radius = cunit*radius
            vector = \
                cls(
                    radius*cos_i*cos_a,
                    radius*cos_i*sin_a,
                    radius*sin_i,
                    _internal = True
                )

            return vector


        @hf.ensure_other_is_vector
        def cross(self, other):
            """The cross product of two vectors"""

            cvs0, cvs1, cvs2 = self._cvalues
            cvo0, cvo1, cvo2 = other._cvalues
            vector = \
                self._vector(
                    (
                        cvs1*cvo2 - cvs2*cvo1,
                        cvs2*cvo0 - cvs0*cvo2,
                        cvs0*cvo1 - cvs1*cvo0
                    )
                )

            return vector


        @hf.ensure_others_are_vectors
        def stp(self, other, other_):
            """The scalar triple product of three vectors"""

            scalar = self.dot(other.cross(other_))

            return scalar


        @hf.ensure_others_are_vectors
        def vtp(self, other, other_):
            """The vector triple product of three vectors"""

            vector = self.cross(other.cross(other_))

            return vector


        @hf.ensure_other_is_vector
        def sin(self, other):
            """The sine of the angle between two vectors (from cnull to +cunit)"""

            ls = self.length()
            lo = other.length()
            lcr = self.cross(other).length()
            try:
                sine = lcr/(ls*lo)
            except ZeroDivisionError as err:
                msg = "One (or both) of the vectors is a zero vector"
                raise ZeroDivisionError(msg) from err
            cnull = self._cnull
            cunit = self._cunit
            sine = self.clip(sine, cnull, cunit)

            return sine


        def _axis_rot(self, *, axis, cos, sin):

            cunit = self._cunit
            la1 = axis.length()
            la2 = la1**2
            vcr1 = self.cross(axis)
            vcr2 = vcr1.cross(axis)
            vector = self + vcr2/la2*(cunit - cos) - vcr1/la1*sin

            return vector


        @hf.ensure_other_is_vector
        def axis_rotate(self, other, angle):
            """A vector rotated around another by an angle in radians"""

            cunit = self._cunit
            angle = cunit*angle
            cos = self.component_cos(angle)
            sin = self.component_sin(angle)
            try:
                vector = self._axis_rot(axis=other, cos=cos, sin=sin)
            except ZeroDivisionError as err:
                msg = "The axis vector is a zero vector"
                raise ZeroDivisionError(msg) from err

            return vector


        @hf.ensure_others_are_vectors
        def reorient(self, other, other_):
            """Reorient a vector from one direction to another direction"""

            axis = other.cross(other_)
            try:
                cos = other.cos(other_)
                sin = other.sin(other_)
            except ZeroDivisionError as err:
                msg = "One (or both) of the direction vectors is a zero vector"
                raise ZeroDivisionError(msg) from err
            try:
                vector = self._axis_rot(axis=axis, cos=cos, sin=sin)
            except ZeroDivisionError:
                parallel = True
            else:
                parallel = False
            if parallel:
                von = other.normalize()
                von_ = other_.normalize()
                dot = von.dot(von_)
                if self._equal_cunit(-dot):
                    msg = "The direction vectors are pointing in opposite directions"
                    raise ZeroDivisionError(msg)
                assert self._equal_cunit(dot)
                vector = self

            return vector


        @hf.ensure_other_is_vector
        def are_parallel(self, other):
            """Check if two vectors are parallel"""

            # vsn = self.normalize()
            # von = other.normalize()
            # cross = vsn.cross(von)
            cross = self.cross(other)
            parallel = cross.is_zero_vector()
### Are these needed with NumPy ?
#             parallel = self.component_or(parallel, self.is_zero_vector())
#             parallel = self.component_or(parallel, other.is_zero_vector())

            return parallel


        def polar_as_dict(self):
            """Polar coordinates of a vector as a dictionary"""

            result = \
                {
                    'radius': self.radius,
                    'azimuth': self.azimuth,
                    'inclination': self.inclination
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

            cvs0, cvs1, cvs2 = self._cvalues
            angle = self.component_atan2(cvs1, cvs0)

            return angle


        @property
        def inclination(self):
            """TODO"""

            cvs0, cvs1, cvs2 = self._cvalues
            r = (cvs0**(cunit*2) + cvs1**(cunit*2))**(cunit/2)
            angle = self.component_atan2(cvs2, r)

            return angle


    return Cartesian_3D_Vector

