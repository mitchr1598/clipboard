from dataclasses import dataclass


@dataclass(frozen=True)
class Activity:
    id: int
    name: str


@dataclass(frozen=True)
class Student:
    id: int
    smsId: str
    fullName: str


@dataclass(frozen=True)
class Team:
    id: int
    name: str
    activity: Activity


@dataclass(frozen=True)
class StudentTeams:
    id: int
    student: Student
    team: Team
    startDateTime: str
    endDateTime: str
