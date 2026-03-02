from pydantic import BaseModel

class note(BaseModel):
    id:int
    title:str
    content:str