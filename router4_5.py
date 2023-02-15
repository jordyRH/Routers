from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class User(BaseModel):
    id:int
    Modelo: str
    Marca:str
    Precio:int
    Age:int 



users_list= [User(id=1,Modelo="Eco Sport", Marca="Dorado", Precio="50000", Age= "2015"),
             User(id=2,Modelo="Jetta", Marca="Plateado", Precio="60000", Age= "2000"),
             User(id=3,Modelo="Ranger", Marca="Negro onix", Precio="80000",Age= "2017"),  
             User(id=4,Modelo="Frontier", Marca="Verde", Precio="10000",Age= "2015"),
             User(id=5,Modelo="Versa", Marca="Gris", Precio="12000",Age= "2015")]
             

@router.get("/autos/")
async def usersclass():
    return (users_list)
