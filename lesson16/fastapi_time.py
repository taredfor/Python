from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from datetime import datetime
import pytz

app = FastAPI()


@app.get('/time', response_class=JSONResponse)
def read_root():
    fmt = '%d-%m-%Y %H:%M:%S'
    tz = pytz.timezone('Europe/London')
    current_time = datetime.now(tz).strftime(fmt)
    return current_time
