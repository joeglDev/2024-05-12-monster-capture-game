import uvicorn
from fastapi import FastAPI

from server.helpers.get_codemon_info_helper import get_codemon_info_helper
from server.helpers.get_codemon_stats_helper import get_codemon_stats_helper

app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "success"}


@app.get("/codemon/info/{codemon_id}")
def get_codemon_info(codemon_id: int):
    res = get_codemon_info_helper(codemon_id=codemon_id)

    return {"CodemonInfo", res}


@app.get("/codemon/stats/{codemon_id}")
def get_codemon_stats(codemon_id: int):
    res = get_codemon_stats_helper(codemon_id=codemon_id)

    return res


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
