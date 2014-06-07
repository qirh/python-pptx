# encoding: utf-8

"""
lxml custom element classes for DrawingML-related XML elements.
"""

from __future__ import absolute_import

from ...enum.dml import MSO_THEME_COLOR
from ..simpletypes import ST_Percentage
from ..xmlchemy import BaseOxmlElement, RequiredAttribute, ZeroOrOne


class _BaseColorElement(BaseOxmlElement):
    """
    Base class for <a:srgbClr> and <a:schemeClr> elements.
    """
    lumMod = ZeroOrOne('a:lumMod')
    lumOff = ZeroOrOne('a:lumOff')

    def add_lumMod(self, value):
        """
        Return a newly added <a:lumMod> child element.
        """
        lumMod = self._add_lumMod()
        lumMod.val = value
        return lumMod

    def add_lumOff(self, value):
        """
        Return a newly added <a:lumOff> child element.
        """
        lumOff = self._add_lumOff()
        lumOff.val = value
        return lumOff

    def clear_lum(self):
        """
        Return self after removing any <a:lumMod> and <a:lumOff> child
        elements.
        """
        self._remove_lumMod()
        self._remove_lumOff()
        return self

    @property
    def val(self):
        return self.get('val')

    @val.setter
    def val(self, value):
        self.set('val', value)


class CT_HslColor(_BaseColorElement):
    """
    Custom element class for <a:hslClr> element.
    """


class CT_Percentage(BaseOxmlElement):
    """
    Custom element class for <a:lumMod> and <a:lumOff> elements.
    """
    val = RequiredAttribute('val', ST_Percentage)


class CT_PresetColor(_BaseColorElement):
    """
    Custom element class for <a:prstClr> element.
    """


class CT_SchemeColor(_BaseColorElement):
    """
    Custom element class for <a:schemeClr> element.
    """
    @property
    def val(self):
        val = self.get('val')
        mso_theme_color_idx = MSO_THEME_COLOR.from_xml(val)
        return mso_theme_color_idx

    @val.setter
    def val(self, mso_theme_color_idx):
        val = MSO_THEME_COLOR.to_xml(mso_theme_color_idx)
        self.set('val', val)


class CT_ScRgbColor(_BaseColorElement):
    """
    Custom element class for <a:scrgbClr> element.
    """


class CT_SRgbColor(_BaseColorElement):
    """
    Custom element class for <a:srgbClr> element.
    """


class CT_SystemColor(_BaseColorElement):
    """
    Custom element class for <a:sysClr> element.
    """
