from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from connection_manager import ConnectionManager
from kaluki import Kaluki

kaluki = Kaluki()
manager = ConnectionManager()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/setup_game")
async def update_players(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            if data["method"] == "add":
                kaluki.add_player(data["user"])
            elif data["method"] == "remove":
                kaluki.remove_player(data["user"])
            elif data["method"] == "start":
                kaluki.start_game()

            if not kaluki.has_table():
                response = {"user": data["user"], "method": data["method"], "players": []}
            else:
                response = {"user": data["user"], "method": data["method"], "players": kaluki.get_player_names()}
            await manager.broadcast(response)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/player_hand/{player}")
def player_hand(player):
    return kaluki.get_player_hand(player)
