from dataclasses import dataclass


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
