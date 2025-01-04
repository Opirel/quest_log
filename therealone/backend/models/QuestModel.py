from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from enum import Enum


class CharactersENUM(Enum):
    Urthor = 1,
    Aelin=2,
    Brol=3,
    Leonard=4,
    Levy=5,
    Raamses=6,
    Rexona=7

class QuestMD(BaseModel):
    QuestName: str
    QuestDescription: str
    QuestReward: str
    CharactersInvolved: List[str]
    QuestCompleted: bool