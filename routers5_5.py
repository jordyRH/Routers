from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Modelo: str
    Marca:str
    Precio:int
   



users_list= [User(id=1,Modelo="Iphone ", Marca="Apple", Precio="50000"),
             User(id=2,Modelo="Galaxy ", Marca="Samsung", Precio="60000"),
             User(id=3,Modelo="Galaxy", Marca="Samsung", Precio="80000"),  
             User(id=4,Modelo="Iphone ", Marca="Apple", Precio="10000"),
             User(id=5,Modelo="Mate ", Marca="Huawei", Precio="12000")]
             

@router.get("/celulares/")
async def usersclass():
    return (users_list)
