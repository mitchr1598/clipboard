from dataclasses import dataclass


@dataclass(frozen=True)
class AgeGroup:
    """
    A Class for Age Group, eg. Junior, Middlle, etc. . Different to Year Group which is the grade of the student
    """
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
    sisCode: str = None
    optedInForLinking: bool = None
    department: Department = None


@dataclass(frozen=True)
class Team:
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
