from fastapi import WebSocket
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_json(self, websocket: WebSocket, obj: dict):
        await websocket.send_json(json.dumps(obj))

    async def broadcast(self, obj: dict):
        for connection in self.active_connections:
            await connection.send_json(json.dumps(obj))
