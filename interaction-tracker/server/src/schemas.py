from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, field_validator

class EventType(str, Enum):
    click = "click"
    page_view = "page_view"
    form_submit = "form_submit"

class InteractionCreate(BaseModel):
    user_id: str = Field(..., min_length=1, max_length=255)
    event_type: EventType
    metadata: Optional[Dict[str, Any]] = Field(default=None)

    @field_validator("metadata")
    @classmethod
    def metadata_must_be_object(cls, v):
        if v is not None and not isinstance(v, dict):
            raise ValueError("metadata must be an object")
        return v