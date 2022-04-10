from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Subscribe to IZAK'S UNIVERSE - https://www.youtube.com/channel/UCj822eSJz7Ph-klb8Ls6QFw?sub_confirmation=1"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
