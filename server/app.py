import uvicorn
from fastapi import FastAPI

from server.get_codemon_info import get_codemon_info_helper

app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "success"}


@app.get("/codemon_info/{codemon_id}")
def get_codemon_info(codemon_id: int):
    res = get_codemon_info_helper(codemon_id=codemon_id)

    return {"CodemonInfo", res}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
