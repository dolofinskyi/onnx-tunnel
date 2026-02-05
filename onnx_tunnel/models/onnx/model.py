from ..base import BaseModel

from .io import ONNXInput, ONNXOutput

import onnxruntime as ort


class ONNXModel(BaseModel[ONNXInput, ONNXOutput]):
    def __init__(self, model_path: str):
        super().__init__(model_path)
        self.session = ort.InferenceSession(model_path)

    def predict(self, data: ONNXInput) -> ONNXOutput:
        return self.session.run(data["outputs"], data["inputs"])