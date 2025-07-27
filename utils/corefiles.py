import json
import os
from typing import Dict, List, Optional
from config import DB_PATH

def readJson() -> Dict:
    try:
        with open(DB_PATH, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(data: Dict) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4, ensure_ascii=False)

import json
import os
from config import DB_PATH

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

        existing_data.update(data)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)

        return False
    except Exception as e:
        print("Error actualizando JSON:", e)
        return True

def deleteJson(path: List[str]) -> bool:
    data = readJson()
    if not data:
        return False

    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path and path[-1] in current:
        del current[path[-1]]
        writeJson(data)
        return True
    return False

def initializeJson(initialStructure: Dict) -> None:
    if not os.path.isfile(DB_PATH):
        writeJson(initialStructure)
    else:
        currentData = readJson()
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(currentData)