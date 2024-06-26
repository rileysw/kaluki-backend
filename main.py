from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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


# for testing
@app.get("/restart")
def restart():
    kaluki.restart_game()


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
                kaluki.update_turn()

            if not kaluki.has_table():
                response = {"user": data["user"],
                            "method": data["method"], "players": []}
            elif data["method"] == "start":
                response = {
                    "user": data["user"], "method": data["method"], "players": kaluki.get_player_names()}
            else:
                response = {
                    "user": data["user"], "method": data["method"], "players": kaluki.get_player_names()}
            await manager.broadcast(response)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


@app.get("/game_info/{player}")
def game_info(player):
    return {"hand": kaluki.get_player_hand(player), "turn": kaluki.get_turn(), "hasDrawn": kaluki.get_has_drawn(player), "allLaydowns": kaluki.get_laydowns(), "trashCard": kaluki.get_trash_card()}


@app.websocket("/play_game")
async def play_game(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            kaluki.update_player_hand(data["user"], data["hand"])
            if data["method"].startswith("draw"):
                kaluki.draw_card(data["user"], data["method"])
                response = {"user": data["user"],
                            "method": data["method"],
                            "trashCard": kaluki.get_trash_card(),
                            "hand": kaluki.get_player_hand(data["user"]),
                            "hasDrawn": kaluki.get_has_drawn(data["user"])}
            elif data["method"] == "trash":
                kaluki.trash_card(data["user"], data["cardId"])
                kaluki.update_turn()
                response = {"user": data["user"],
                            "method": data["method"],
                            "trashCard": kaluki.get_trash_card(),
                            "hand": kaluki.get_player_hand(data["user"]),
                            "turn": kaluki.get_turn(),
                            "hasDrawn": kaluki.get_has_drawn(data["user"])}
            elif data["method"] == "laydown":
                kaluki.add_laydown(data["user"], data["laydown"])
                response = {"user": data["user"],
                            "method": data["method"],
                            "hand": kaluki.get_player_hand(data["user"]),
                            "allLaydowns": kaluki.get_laydowns()}
            await manager.broadcast(response)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
