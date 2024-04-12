from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from models import Hand
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

@app.post("/draw_card")
def draw_card(req: Hand):
    kaluki.update_player_hand(req.user, req.hand)
    kaluki.draw_card(req.user)
    return kaluki.get_player_hand(req.user)

@app.websocket("/play_game")
async def play_game(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            if data["method"] == "trash":
                kaluki.update_player_hand(data["user"], data["hand"])
                trash_card = kaluki.trash_card(data["user"], data["index"])
                response = {"user": data["user"],
                            "method": data["method"],
                            "card": trash_card,
                            "hand": kaluki.get_player_hand(data["user"])}
            await manager.broadcast(response)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
