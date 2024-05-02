from typing import Tuple, List
"""3rd Optional Task"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """takes a tuple of integers and returns a list."""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
