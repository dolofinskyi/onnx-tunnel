from typing import Any, List, TypedDict

import numpy as np


class ONNXInput(TypedDict):
    inputs: List[np.ndarray]
    outputs: List[np.ndarray]

ONNXOutput = Any