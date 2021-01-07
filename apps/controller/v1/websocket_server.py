# _*_ coding:utf-8 _*_
# @Time:2021/1/7 16:46
# @Author:Cadman
# @File websocket_server.py

from fastapi import  WebSocket, WebSocketDisconnect

from apps.service.websocket_service import ConnectionManager


async def websocket_endpoint(websocket: WebSocket, user: str):
    manager = ConnectionManager()
    await manager.connect(websocket)
    await manager.broadcast(f"用户{user}进入聊天室")

    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"你说了: {data}", websocket)
            await manager.broadcast(f"用户:{user} 说: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"用户-{user}-离开")