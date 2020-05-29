# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-5-26 上午10:04

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket
import uvicorn
import asyncio
import time

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


html1 = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws/new");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
# @app.get("/")告诉FastAPI如何去处理请求
# 路径 /
# 使用get操作
x = 1
@app.get("/")
async def get():
    # 返回表单信息
    global x
    x += 1
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # time.sleep(1)
    # x = 1
    while True:
        # data = await websocket.receive_text()
        await asyncio.sleep(1)
        await websocket.send_text(f"Message text was: {str(x)}")

@app.get("/new")
async def get():
    # 返回表单信息
    global x
    x += 1
    return HTMLResponse(html1)

@app.websocket("/ws/new")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # time.sleep(1)
    # x = 1
    while True:
        # data = await websocket.receive_text()
        await asyncio.sleep(1)
        await websocket.send_text(f"Message text was: {str(x)}")


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)