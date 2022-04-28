from typing import *
from enum import Enum

from enum import Enum
import MyPG.Metaclasses as mc


class CurveEnumBase(Enum):
    def _ReturnResource(self, url):
        return mc.API().NCP_PACKAGE.findResourceFromUrl(url)

    @property
    def Resource(self):
        raise NotImplementedError()


class CreateCurve(CurveEnumBase):
    Dots_8 = 0
    Start = 1
    Body = 2
    Circle = 3
    Spiral = 4
    Polygon = 5
    PolySpiral = 6
    Connect = 7
    Close = 8
    Outline = 9
    DetachSurface = 10
    Import = 11

    @property
    def Resource(self):
        return self._ReturnResource(f"Create/c_{self.value:02}")


class EditCurve(CurveEnumBase):
    AssignAttrib = 0
    AssignAttribSimple = 1
    InvertU = 2
    Carve = 3
    BlendShape = 4
    Smooth = 5
    Transform = 6
    DirectionalWarp = 7
    Centroid = 8
    ShiftU = 9
    Switch = 10
    Fit = 11
    Repeat = 12
    VectorMorph = 13
    Split = 14

    @property
    def Resource(self):
        return self._ReturnResource(f"Edit/e_{self.value:02}")


class RenderCurve(CurveEnumBase):
    Gray = 0
    Color = 1
    Flow = 2
    Preview = 3
    SingleGray = 4
    SingleColor = 5
    Area = 6
    Ladder1 = 7
    Ladder2 = 8

    @property
    def Resource(self):
        return self._ReturnResource(f"Render/r_{self.value:02}")


class Surface(CurveEnumBase):
    SurfaceBuilder = 0
    Line8 = 1
    Gray = 2
    Color = 3

    @property
    def Resource(self):
        return self._ReturnResource(f"Surface/s_{self.value:02}")


class Analysis(CurveEnumBase):
    Length = 0
    Density = 1

    @property
    def Resource(self):
        return self._ReturnResource(f"Analysis/a_{self.value:02}")


class Polynomial(CurveEnumBase):
    Start = 0
    Ax_B = 1
    Blend = 2
    Tri = 3
    Pow = 4
    Exp = 5
    Abs = 6
    Mod = 7
    Const = 8

    @property
    def Resource(self):
        return self._ReturnResource(f"PolynomialBuilder/p_{self.value:02}")


class Util(CurveEnumBase):
    SetPivotGray = 0
    SetPivotColor = 1
    MergePivotGray = 2
    MergePivotColor = 3

    @property
    def Resource(self):
        return self._ReturnResource(f"Utils/u_{self.value:02}")
