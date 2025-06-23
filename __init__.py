"""
EDU-AIgent Core Module

The EDU Formula: EDU(A,X) = (A/255·π), (406.4/X)
Discovered by Eduard Terre (ASCII-EDU), Offenburg, Germany, 2024

This module provides the core implementation of the EDU Formula
and fundamental algorithms for universal signal processing.
"""

from .edu_formula import EDUFormula, EDUConstants

__version__ = "1.0.0"
__author__ = "Eduard Terre (ASCII-EDU)"
__location__ = "Offenburg, Germany"
__year__ = "2024"

__all__ = [
    "EDUFormula",
    "EDUConstants"
]