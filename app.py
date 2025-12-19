"""

A simple FastAPI application.

"""

import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def aio_sleep():
    await asyncio.sleep(1)
    return {'error': None}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)