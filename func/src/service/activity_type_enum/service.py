from etria_logger import Gladsheim

from src.core.interfaces.service.activity_type_enum.interface import IActivityTypeEnumService
from src.domain.response.model import ResponseModel
from src.domain.response.status_code.enums import StatusCode
from src.repository.activity_type_enum.repository import ActivityTypeEnumRepository


class ActivityTypeEnumService(IActivityTypeEnumService):
    @classmethod
    def get_response(cls):
        service_response = []

        enums = ActivityTypeEnumRepository.get_activity_type_enum()
        for code, value in enums:
            service_response.append({"code": code, "value": value})

        service_response = ResponseModel.build_response(
            success=True, code=StatusCode.SUCCESS, message=None, result=service_response
        )
        return service_response
