from flask import Flask, render_template
import datetime
import socket

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def index():
    message = f"Application déployée depuis le conteneur {socket.gethostname()}"
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template(
        "index.html",
        version=APP_VERSION,
        message=message,
        current_time=current_time,
    )


@app.route("/health")
def health():
    return {"status": "ok", "version": APP_VERSION}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)