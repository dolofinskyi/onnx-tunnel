from ..base import BasePipeline

from .io import ONNXPipelineInput, ONNXPipelineOutput
from ...models.onnx.io import ONNXModelInput, ONNXModelOutput


class ONNXPipeline(
    BasePipeline[
        ONNXPipelineInput, 
        ONNXModelInput, 
        ONNXModelOutput, 
        ONNXPipelineOutput
    ]
):
    pass