from dataclasses import dataclass

@dataclass
class EventLog:
    """Class for storing user event logs
    
    Attributes:
        date (str): date of the user event
        event (str): name of the user event
        user (str): name of the user
        status (str): status of the user event
    """

    date: str = ""
    event: str = ""
    user: str = ""
    status: str = ""