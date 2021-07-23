from typing import Optional

from fastapi import FastAPI


app = FastAPI()


print('Loading')


@app.get('/')
def read_root():
    print('root')
    return {'Hello': 'World'}


@app.get('/greet')
def read_greeting(name: Optional[str] = None):
    print('greet')
    if name:
        return {'greeting': f'Hello, {name}!'}
    return {'greeting': 'Hello world!'}
