"""Stub file for divider.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Divider(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, orientation: Optional[Union[Var[str], str]] = None, variant: Optional[Union[Var[str], str]] = None, **props) -> "Divider": ...  # type: ignore
