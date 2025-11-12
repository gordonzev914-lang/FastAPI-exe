
import uvicorn
from string_ops import reverse_str
import json
from fastapi import FastAPI, HTTPException



app=FastAPI()


@app.get("/reverse")
def string_reverse(text:str):
    rev=reverse_str(text)
    return rev








if __name__ == "__main__": 
    uvicorn.run(app, host="localhost", port=8000)