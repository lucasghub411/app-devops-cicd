from flask import Flask, render_template
import datetime
import socket

app = Flask(__name__)

APP_VERSION = "1.1.0"


TECH_STACK = [

    {"name": "Flask", "role": "Application web (Python)"},
    {"name": "Docker", "role": "Conteneurisation"},
    {"name": "Jenkins", "role": "Intégration / déploiement continu"},
    {"name": "Nginx", "role": "Reverse proxy"},
    {"name": "Git", "role": "Gestion de version"},
]


@app.route("/")
def index():
    message = f"Conteneur actif : {socket.gethostname()}"
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template(
        "index.html",
        version=APP_VERSION,
        message=message,
        current_time=current_time,
        tech_stack=TECH_STACK,
    )


@app.route("/health")
def health():
    return {"status": "ok", "version": APP_VERSION}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)