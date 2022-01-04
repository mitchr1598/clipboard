from dataclasses import dataclass


@dataclass(frozen=True)
class AgeGroup:
    id: int
    name: str


@dataclass(frozen=True)
class Category:
    id: int
    name: str


@dataclass(frozen=True)
class Department:
    id: int
    name: str
    optedInForLinking: bool


@dataclass(frozen=True)
class Activity:
    id: int
    name: str
    sisCode: str
    optedInForLinking: bool
    department: Department


@dataclass(frozen=True)
class Teams:
    id: int
    name: str
    playersRanked: bool
    category: Category
    ageGroup: AgeGroup
    activity: Activity
    assignedStaff: list
    hidden: bool
    students: list
    positions: list
    sortOrder: int
    studentSortType: str
