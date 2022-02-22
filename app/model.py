from ipaddress import IPv4Address
from typing import Optional

from pydantic import BaseModel


class Server(BaseModel):
    ip: IPv4Address
    name: str


class Result(BaseModel):
    server: Server
    result: Optional[int]
