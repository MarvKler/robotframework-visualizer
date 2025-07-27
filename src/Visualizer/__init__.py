
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
    
    = Use Case =
    The initial idea of the library was to create diagrams with the date time series on the x-axis & the raw value on the y-axis.\n
    You can pass a CSV file or data-object & create one or multiple graphs within a diagram.
    First, you need to add data to a diagram & afterwards you can use ``Visualize`` keyword to create the diagram as png image.
    """

    def __init__(self):

        libraries = [
            Keywords()
        ]
        super().__init__(libraries)