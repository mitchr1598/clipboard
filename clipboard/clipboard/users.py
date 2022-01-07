from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    """
    A class for users
    """
    id: int
    email: str
    payment: str
    frozen: bool
    firstName: str
    lastName: str
    mobileNumber: str
    isAdmin: bool
    isManager: bool
    employeeId: str
    wwccNumber: str
    wwccExpiryDate: str
    updatedDetails: bool
    activitiesPermissions: list
    departments: list
    unavailability: list
    role: str
