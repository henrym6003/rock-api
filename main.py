from flask import Flask, request, Response
from world import World, InvalidCharacterError
from rock_logger import RockLogger
import json
import time

app = Flask(__name__)
worlds = {}

rl = RockLogger("Main")
logger = rl.get_logger()


@app.route("/init-world", methods=["POST"])
def init_world():
    start = int(round(time.time() * 1000))
    print(request.data)
    if request.headers.get("Content-Type") != "text/plain":
        res = {
            "message": "'POST/init-world' only accepts Content-Type: text/plain"
        }
        logger.error(msg="world init failed, bad content-type", extra={"route": "/init-world", "status": 400})
        return build_response(res, "application/json"), 400

    new_world = World()
    try:
        new_world.add_rocks(request.data)

    except InvalidCharacterError as e:
        res = {
            "message": str(e)
        }
        logger.error(msg=str(e), extra={"route": "/init-world", "status": 400})
        return build_response(res, "application/json"), 400

    new_world.apply_gravity()
    worlds[new_world.uuid] = new_world
    res = {
        "message": "new world created successfully",
        "world_uuid": new_world.uuid
    }
    end = int(round(time.time() * 1000))

    logger.info(
        msg="new world created: {0}".format(new_world.uuid),
        extra={"route": "/init-world", "status": 201, "millis": (end - start)})
    return build_response(res, "application/json"), 201


@app.route("/world/<world_uuid>", methods=["GET"])
def world(world_uuid):
    start = int(round(time.time() * 1000))
    try:
        current_world: World = worlds[world_uuid]
    except KeyError:
        logger.error(msg="world not found", extra={"route": "/world/{0}".format(world_uuid), "status": 404})
        return build_response("world not found", "text/plain"), 404
    end = int(round(time.time() * 1000))
    logger.info(
        msg="",
        extra={"route": "/world/{0}".format(world_uuid), "status": 201, "millis": (end - start)})
    return build_response(current_world.get_graphical_world(), "text/plain"), 200


def build_response(data, content_type):
    response = Response()
    response.headers["Content-Type"] = content_type
    if content_type == "application/json":
        response.data = json.dumps(data)
    else:
        response.data = data
    return response

