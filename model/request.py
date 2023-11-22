from dataclasses import dataclass, field
from typing import Dict


@dataclass
class InsertRequest:
    table: str
    data: list

@dataclass
class DeleteRequest:
    table: str
    column: str
    values_list: list

@dataclass
class SelectRequest:
    table: str
    columns: str = '*'
    conditions: str = ''
    parameters: Dict[str, str] = field(default_factory=dict)

@dataclass
class UpdateRequest:
    table: str
    data: Dict[str, str] = field(default_factory=dict)
    expressions: Dict[str, str] = field(default_factory=dict)
    conditions: str = ''
    parameters: Dict[str, str] = field(default_factory=dict)