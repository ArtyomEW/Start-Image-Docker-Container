from starlette.responses import PlainTextResponse
from fastapi import FastAPI

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
def get():
    return "Hello world"
