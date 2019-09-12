from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import Home
from schemas import HomeSchema

# "postgres://username:password@server:port/db_name"
url = "postgres://postgres:postgres@localhost:5432/homes"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    homes = Home.query.all()
    for home in homes:
        print(
            "",
            home.age,
            " years ",
            home.acres,
            " of house with ",
            home.bath,
            " bathroom(s) ",
            home.rooms,
            " rooms, ",
            home.beds,
            " beds selling at total of $",
            home.sell,
            "k with tax: ",
            home.taxes,
        )

    json_homes = HomeSchema(many=True).dump(homes)
    return jsonify(json_homes)


@app.route("/searchbyroom")
def gethomebyroom(room):
    room = request.args.get("room")

    query = Home.query

    if room is not None:
        query = query.filter(Home.rooms == room)

    homes = query.all()
    json_homes = HomeSchema(many=True).dump(homes)
    return jsonify(json_homes)

