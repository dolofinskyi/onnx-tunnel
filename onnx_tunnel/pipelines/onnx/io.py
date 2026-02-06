from typing import TypedDict, List


class ONNXPipelineInput(TypedDict):
    inputs: List[List[float]]
    output_names: List[str]


class ONNXPipelineOutput(TypedDict):
    outputs: List[List[float]]