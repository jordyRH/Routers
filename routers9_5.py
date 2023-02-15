from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    nombre: str
    calorias:int
   



users_list= [User(id=1,nombre="Manzana ", calorias="15"),
             User(id=2,nombre="Espinacas ", calorias="55"),
             User(id=3,nombre="Uvas", calorias="20"),  
             User(id=4,nombre="Camote ", calorias="90"),
             User(id=5,nombre="Cerezas", calorias="80")]
             

@router.get("/alimentos/")
async def usersclass():
    return (users_list)