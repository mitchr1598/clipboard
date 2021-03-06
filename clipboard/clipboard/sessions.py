from dataclasses import dataclass


@dataclass(frozen=True)
class LocationOwner:
    id: int
    name: str
    acronym: str
    shortName: str
    state: str


@dataclass(frozen=True)
class Location:
    id: int
    name: str
    address: str
    latitude: float
    longitude: float
    owner: LocationOwner


@dataclass(frozen=True)
class Department:
    id: int
    name: str


@dataclass(frozen=True)
class Activity:
    id: int
    name: str
    department: Department
    colour: int
    hexColor: str


@dataclass(frozen=True)
class OpponentOrganisation:
    id: int
    name: str


@dataclass(frozen=True)
class OpponentTeam:
    id: int
    name: str
    activityName: str


@dataclass(frozen=True)
class Session:
    activity: Activity
    feedback: list
    assignedStaff: list
    locationData: Location
    location: str
    result: str
    activityColour: int
    bye: bool
    cancelled: bool
    creatorUserId: int
    endDateTime: str
    hexColor: str
    id: int
    notes: str
    opponentScore: str
    organisationScore: str
    remindStaff: bool
    scored: bool
    seriesId: int
    startDateTime: str
    status: str
    studentParentNotes: str
    title: str
    opponent: str
    opponentOrganisation: OpponentOrganisation
    opponentTeam: OpponentTeam
    teams: list
    students: list


