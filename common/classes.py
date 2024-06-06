from dataclasses import dataclass, asdict
from typing import List

@dataclass
class PostPendingRequest:
    Group_ID: str
    UserName: str
    Action: str
    Content: str
    KeyCheck: str
    
