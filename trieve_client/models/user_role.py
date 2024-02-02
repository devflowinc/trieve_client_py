from enum import Enum


class UserRole(str, Enum):
    ADMIN = "Admin"
    OWNER = "Owner"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
