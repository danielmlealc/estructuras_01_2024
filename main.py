from typing import Union
from fastapi import FastAPI, Query

import mook
import re

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data")
def read_item(data: str | None = Query(None, min_length=3)):
    return {"tutelas": data}

@app.get("/api/v1/search?tipo_tutela=salud")
def read_root():
    result = []
    for tutela in tutelas:
        if re.search(tipo_tutela, tutela["titulo"] + " " + tutela["resumen"], re.IGNORECASE):
            result.append(tutela)
    return result

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
  
