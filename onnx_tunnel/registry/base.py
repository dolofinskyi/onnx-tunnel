from typing import TypeVar, Generic, Dict, Type


KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')


class Registry(Generic[KeyType, ValueType]):
    _registry: Dict[KeyType, Type[ValueType]] = {}

    @classmethod
    def register(cls, key: KeyType, value: Type[ValueType]):
        cls._registry[key] = value
    
    @classmethod
    def register_all(cls):
        raise NotImplementedError("Registry must be registered")

    @classmethod
    def create(cls, key: KeyType, **kwargs) -> ValueType:
        if key not in cls._registry:
            raise ValueError(f"Key {key} not registered")
        return cls._registry[key](**kwargs)