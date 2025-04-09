from fastapi import FastAPI
from pydantic import BaseModel #validation of data
from typing import List

from app.database.connection import connect_to_mongo,close_mongo_connection

app=FastAPI()

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    
@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
    
    

# class Tea(BaseModel):#schema
#     id:int
#     name:str
#     origin:str
    
# teas:List[Tea]=[]#local database

# app.include_router(auth)

#DECORATOR GIVE SUPER POWER TO FUNCTION
# @app.get("/")
# def read_root():
#     return{"message":"welcome to home route"}

# @app.get("/teas")
# def get_teas():
#     return teas

# @app.post("/teas")
# def add_tea(tea:Tea):
#     teas.append(tea)
#     return tea

# @app.put("/teas/{tea_id}")
# def update_tea(tea_id:int,updated_tea:Tea):
#     for index,tea in enumerate(teas):
#         if tea.id==tea_id:
#             teas[index]=update_tea
#             return update_tea
        
#     return {"error":"Tea not found"}

# @app.delete("/teas/{tea_id}")
# def delete_tea(tea_id:int):
#     for index,tea in enumerate(teas):
#         if tea.id==tea_id:
#             deleted=teas.pop(index)
#             return deleted
        
#     return {"error":"error not found"}