from typing import Annotated
from pydantic import BaseModel
import  logging
class User(BaseModel):
    id:int
    name:str ="Dinesh"
external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}
user = User(**external_data) 
print(user.id)
