from dataclasses import dataclass
from typing import Optional

@dataclass
class Employee:
    id: Optional[str]
    first_name: str
    last_name: str
    salary: float
