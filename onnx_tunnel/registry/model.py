from .base import Registry
from .types import Backend

from ..models import BaseModel

class ModelRegistry(Registry[Backend, BaseModel]):
    pass
        