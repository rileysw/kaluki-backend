from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/add_player/{name}")
def add_player(name: str):
    print(name)
    return name

@app.websocket("/get_ready_players")
async def get_ready_players(websocket: WebSocket):
    players = ["Player 1", "Player 2", "Player 3"]
    await websocket.accept()
    await websocket.send_json(json.dumps(players))
