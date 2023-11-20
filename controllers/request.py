from dataclasses import dataclass


@dataclass
class DeleteGroupsRequest:
    uids: list

@dataclass
class AddGroupRequest:
    uid: str
    name: str
    approve_key: str
    decline_key: str