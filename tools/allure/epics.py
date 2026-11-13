from enum import Enum

class AllureEpic(str, Enum):
    LMS = "LMS Service"
    STUDENT = "Students service"
    ADMINISTRATION = "Administration service"