from typing import Union
from fastapi import FastAPI

import mook
import re

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data{data}")
def read_root():
    return {"tutelas": data}

@app.get("/api/v1/search?tipo_tutela=salud")
def read_root():
    def find_decreto(keyword):
    result = []
    for tutela in tutelas:
        if re.search(keyword, tutela["titulo"] + " " + tutela["resumen"], re.IGNORECASE):
            result.append(tutela)
    return result

return find_decreto(tipo_tutela)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
  
