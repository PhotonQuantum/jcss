from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Optional


class Status(IntEnum):
    success: auto()
    fail: auto()
    error: auto()


@dataclass(frozen=True)
class Result:
    status: Status
    data: Optional[dict] = None
    message: Optional[str] = None

    def dict(self):
        resp = {"status": self.status.name}
        if self.data:
            resp["data"] = self.data
        if self.message:
            resp["message"] = self.message
        return resp
