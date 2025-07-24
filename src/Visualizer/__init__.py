
from robot.api.deco import library
from robotlibcore import HybridCore
from .__about__ import __version__

from .keywords import (
    Keywords
)

@library(
    scope='GLOBAL',
    version=__version__
)
class Visualizer(HybridCore):
    """
    Visualizer Library for creating visual diagrams as embedded 'png' images in the Robot Framework log file.\n
    
    = Current Implementation =
    The initial idea of the library was to create diagrams with the date time series on the x-axis & the raw value on the y-axis.\n
    Currently, you need to pass the CSV header names into keyword to visualize the correct data.

    = Future Implementation =
    The future implementation idea is, to pass multiple CSV header names into the keyword to visualize more than one value time series on the y-axis.
    The x-axis should be kept reserved for the datetime time-series.
    """

    def __init__(self):

        libraries = [
            Keywords()
        ]
        super().__init__(libraries)