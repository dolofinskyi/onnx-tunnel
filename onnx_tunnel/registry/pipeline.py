from .base import Registry
from .types import Backend

from ..pipelines import BasePipeline

class PipelineRegistry(Registry[Backend, BasePipeline]):
    pass
        