from dataclasses import dataclass
from teams import Activity
from students import Student
from users import User
from teams import Team
from sessions import Session


@dataclass(frozen=True)
class Roll:
    id: int
    timeMarked: str
    markedByUser: User
    timeEdited: str


@dataclass(frozen=True)
class AttendanceRecords:
    id: int
    absent: bool
    explained: bool
    addedToRoll: bool
    attendanceFlags: list
    comment: str
    roll: Roll
    session: Session
    student: Student
    team: Team
    updatedTimestamp: str
    updatedByUser: User
