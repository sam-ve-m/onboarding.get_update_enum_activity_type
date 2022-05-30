from abc import ABC, abstractmethod
from typing import List, Any


class IActivityTypeEnumRepository(ABC):
    @abstractmethod
    def get_activity_type_enum(self) -> List[Any]:
        pass

    @abstractmethod
    def _get_activity_type_cached_enum(self, query: str) -> List[Any]:
        pass
