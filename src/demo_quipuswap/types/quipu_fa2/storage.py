# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Ledger(BaseModel):
    allowances: List[str]
    balance: str
    frozen_balance: str


class UserRewards(BaseModel):
    reward: str
    reward_paid: str


class Voters(BaseModel):
    candidate: Optional[str]
    last_veto: str
    veto: str
    vote: str


class Storage1(BaseModel):
    current_candidate: Optional[str]
    current_delegated: Optional[str]
    invariant: str
    last_update_time: str
    last_veto: str
    ledger: Union[int, Dict[str, Ledger]]
    period_finish: str
    reward: str
    reward_paid: str
    reward_per_sec: str
    reward_per_share: str
    tez_pool: str
    token_address: str
    token_id: str
    token_pool: str
    total_reward: str
    total_supply: str
    total_votes: str
    user_rewards: Union[int, Dict[str, UserRewards]]
    veto: str
    vetos: Union[int, Dict[str, str]]
    voters: Union[int, Dict[str, Voters]]
    votes: Union[int, Dict[str, str]]


class Storage(BaseModel):
    dex_lambdas: Union[int, Dict[str, str]]
    metadata: Union[int, Dict[str, str]]
    storage: Storage1
    token_lambdas: Union[int, Dict[str, str]]
