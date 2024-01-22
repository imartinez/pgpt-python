# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .open_ai_choice import OpenAiChoice
from .open_ai_completion_object import OpenAiCompletionObject

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OpenAiCompletion(pydantic.BaseModel):
    """
    Clone of OpenAI Completion model.

    For more information see: https://platform.openai.com/docs/api-reference/chat/object
    """

    id: str
    object: typing.Optional[OpenAiCompletionObject]
    created: int
    model: typing.Any
    choices: typing.List[OpenAiChoice]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
