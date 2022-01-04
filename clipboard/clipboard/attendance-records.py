from dataclasses import dataclass


@dataclass(frozen=True)
class Activity:
    id: int
    name: str


@dataclass(frozen=True)
class Team:
    id: int
    name: str


@dataclass(frozen=True)
class YearGroup:
    id: int
    name: str


@dataclass(frozen=True)
class Student:
    id: int
    firstName: str
    legalFirstName: str
    lastName: str
    smsId: str
    yearGroup: YearGroup


@dataclass(frozen=True)
class Session:
    id: int
    title: str
    startDateTime: str
    endDateTime: str
    activity: Activity


@dataclass(frozen=True)
class MarkedByUser:
    id: int
    firstName: str
    lastName: str
    sisId: str


@dataclass(frozen=True)
class UpdatedByUser:
    id: int
    firstName: str
    lastName: str
    sisId: str


@dataclass(frozen=True)
class Roll:
    id: int
    timeMarked: str
    markedByUser: MarkedByUser
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
    updatedByUser: UpdatedByUser
