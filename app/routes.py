from flask import request, render_template
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%f %H:%M:%S")
    return {
        "ok": True, 
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/users")
def get_all_users():
     out = scan()
     out["ok"] = True 
     out["messsage"] = "Success"
     return out

@app.route("/users/<last_name>")
def get_one_user(last_name):
    out = read(last_name)
    out["ok"] = True
    out["message"] = "Success"
    return out

@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    new_user = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("job_title"),
    )

    return {"ok": True, "message": "Success", "new_user": new_user}

@app.route("/users/<last_name>", methods=["PUT"])
def update_user(last_name):
    user_data = request.json
    out = update(last_name, user_data)
    return {"ok": out, "message": "Updated"}


