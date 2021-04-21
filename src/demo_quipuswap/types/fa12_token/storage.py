# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict, Union

from pydantic import BaseModel


class Balances(BaseModel):
    approvals: Dict[str, str]
    balance: str


class TokenMetadata(BaseModel):
    nat: str
    map: Dict[str, str]


class Storage(BaseModel):
    administrator: str
    balances: Union[int, Dict[str, Balances]]
    debtCeiling: str
    governorContractAddress: str
    metadata: Union[int, Dict[str, str]]
    paused: bool
    token_metadata: Union[int, Dict[str, TokenMetadata]]
    totalSupply: str
