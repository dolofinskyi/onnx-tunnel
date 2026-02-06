from typing import TypeVar, Generic

InputPipelineType = TypeVar('InputPipelineType')
InputModelDataType = TypeVar('InputModelDataType')
OutputModelDataType = TypeVar('OutputModelDataType')
OutputPipelineType = TypeVar('OutputPipelineType')


class BasePipeline(Generic[InputPipelineType, InputModelDataType, OutputModelDataType, OutputPipelineType]):

    @staticmethod
    def preprocess(data: InputPipelineType) -> InputModelDataType:
        raise NotImplementedError("Preprocess not implemented.")

    @staticmethod
    def postprocess(data: OutputModelDataType) -> OutputPipelineType:
        raise NotImplementedError("Postprocess not implemented.")