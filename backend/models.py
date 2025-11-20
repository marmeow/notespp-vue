from datetime import datetime  # noqa: INP001
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, computed_field


class Tag(StrEnum):
    PERSONAL = "Personal"
    PROJECT = "Project"
    OTHER = "Other"


class TaskUpdate(BaseModel):
    is_done: Optional[bool] = None  # noqa: UP045


class Task(BaseModel):
    titol: str
    is_done: bool
    tipus: str | None
    deadline: datetime | None
    reminder: datetime | None

    @computed_field(return_type=str | None)
    @property
    def deadline_formatted(self) -> str | None:
        if self.deadline is None:
            return None
        return self.deadline.strftime("%d %b")

    @computed_field(return_type=str | None)
    @property
    def reminder_formatted(self) -> str | None:
        if self.reminder is None:
            return None
        date = self.reminder.strftime("%d %b")
        time = self.reminder.strftime("%I:%M %p")
        return f"{date}, {time}"


class Nota(BaseModel):
    titol: str
    contingut: str
    link: str | None
    num_links: int
    tags: list[Tag] | None
    time: str
    notebook: str
    has_alarm: bool
    is_shared: bool
    tasks_id: list[int]
    last_edit: str
    images: list[str] | None
