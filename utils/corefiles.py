import json
import os
from typing import Dict, List
from config import DB_PATH

def readJson(name: str) -> dict:
    try:
        with open(os.path.join(DB_PATH, f"{name}.json"), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(name: str, data: dict) -> None:
    with open(os.path.join(DB_PATH, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def updateJson(data, json_file_key):
    try:
        file_name = json_file_key[0] + ".json"
        file_path = os.path.join(DB_PATH, file_name)
        os.makedirs(DB_PATH, exist_ok=True)

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}

        key_root = json_file_key[0]
        if key_root not in existing_data or not isinstance(existing_data[key_root], dict):
            existing_data[key_root] = {}

        existing_data[key_root].update(data)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)

        return False
    except Exception as e:
        print("Error actualizando JSON:", e)
        return True

def deleteJson(path: List[str]) -> bool:
    data = readJson(path[0])
    if not data:
        return False

    current = data
    for key in path[1:-1]:
        if key not in current:
            return False
        current = current[key]

    if path[-1] in current:
        del current[path[-1]]
        writeJson(path[0], data)
        return True
    return False

def initializeJson(initialStructure: Dict) -> None:
    file_path = os.path.join(DB_PATH, "equipos.json")
    if not os.path.isfile(file_path):
        writeJson("equipos", initialStructure)
    else:
        currentData = readJson("equipos")
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson("equipos", currentData)