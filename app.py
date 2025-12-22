"""

A simple FastAPI application.

"""

import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()


@app.get('/')
async def aio_sleep():
    await asyncio.sleep(1)
    return {'error': None}

@app.get("/health", response_class=HTMLResponse, tags=["Health"])
def health_check():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Check</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                text-align: center;
                padding-top: 50px;
            }}
            .status {{
                display: inline-block;
                padding: 20px 40px;
                background-color: #4CAF50;
                color: white;
                font-size: 24px;
                border-radius: 8px;
            }}
            .meta {{
                margin-top: 15px;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="status"> ✅ HEALTHY by Ayman 11111111</div>
        <div class="meta">
            <p>Service: FastAPI</p>
            <p>Time (UTC): {datetime.utcnow().isoformat()}</p>
        </div>
    </body>
    </html>
    """



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)