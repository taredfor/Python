from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from datetime import datetime
import pytz

app = FastAPI()


@app.get('/time', response_class=JSONResponse)
def read_root():
    fmt = '%d-%m-%Y %H:%M:%S'
    current_time = datetime.utcnow().strftime(fmt)
    return current_time
