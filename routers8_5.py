from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    pais: str
    poblacion:int
    idioma:str
   



users_list= [User(id=1,pais="Mexico ", poblacion="150000", idioma="Español"),
             User(id=2,pais="España ", poblacion="2000000", idioma="Español"),
             User(id=3,pais="Uruguay", poblacion="500000", idioma="Español"),  
             User(id=4,pais="Chile ", poblacion="250000", idioma="Español"),
             User(id=5,pais="Canada", poblacion="1500000", idioma="Ingles")]
             

@router.get("/paises/")
async def usersclass():
    return (users_list)