from pydantic import BaseModel

class ChurnRequest(BaseModel):
    tenure: int
    age: int
    address: int
    income: float
    ed: int
    employ: int
    equip: int
    callcard: int
    wireless: int
    longmon: float
    tollmon: float
    equipmon: float
    cardmon: float
    wiremon: float
    longten: float
    tollten: float
    cardten: float
    voice: int
    pager: int
    internet: int
    callwait: int
    confer: int
    ebill: int
    loglong: float
    logtoll: float
    lninc: float
    custcat: int

class ChurnResponse(BaseModel):
    churn: int
    probability: float
