from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Name: str
    LastName:str
    Age:int


users_list= [User(id=1,Name="Owens", LastName="Harris", Age="22"),
            User(id=2,Name="Jhon", LastName="Bradley", Age="38"),
            User(id=3,Name="Laina", LastName="Heikkinen", Age="26")]

@router.get("/nombres/")
async def usersclass():
    return (users_list)
