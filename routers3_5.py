from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Name: str
    Gr:int
    Precio:int


users_list= [User(id=1,Name="Parasetamol", Gr="35", Precio="100"),
             User(id=2,Name="Misoprosol", Gr="38", Precio="120"),
             User(id=3,Name="Next", Gr="30", Precio="56"),  
             User(id=4,Name="Tempra", Gr="50", Precio="66"),
             User(id=5,Name="Tapsin", Gr="25", Precio="88")]

@router.get("/medicamentos/")
async def usersclass():
    return (users_list)
