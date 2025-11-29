import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

def read_config():
    config = configparser.ConfigParser()
    result = {}

    try:
        config.read("config.ini")

        # Read Database section
        result["Database"] = {
            "host": config.get("Database", "host"),
            "port": config.get("Database", "port"),
            "username": config.get("Database", "username"),
            "password": config.get("Database", "password")
        }

        # Read Server section
        result["Server"] = {
            "address": config.get("Server", "address"),
            "port": config.get("Server", "port")
        }

        # Save as JSON
        with open("output.json", "w") as f:
            json.dump(result, f, indent=4)

        return result

    except Exception as e:
        print("Error reading config:", e)
        return {}


@app.route("/get-config")
def get_config():
    try:
        with open("output.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({"error": "Unable to read file"})


if __name__ == "__main__":
    data = read_config()
    print("Config Data:")
    print(json.dumps(data, indent=4))
    app.run()