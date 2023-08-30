import requests
import json
import os
import string
import random
import pytest
from requests.exceptions import JSONDecodeError

base_url = "https://b2btesterscom.s1.my.looru.ai/api"
headers_value = "sessionid=.eJxdkE1LxDAQhv9LzqZr2ubLmwdhF0GFBRUvYZJMbLG20KRsrfjfbVTU3dMMwzwvD-876XFO5IJs8tyQMxKhwxiG0SEdYEpNaWKChOvL0-NunJZ9ef92vbNz_9D717Rdbtr5cKjutsvVCptMmCniaFq_IpX3KqB0tK4Up3Vtz6m2ylOwnjPBai5BH2MW3Av2mY2Da6Ezbhix-LnG4s-u2P-ut5fZ8zingdisIZoD06KsvEAMAqQtXWAsMGe95pahZRB05YRk2tZeKAFK-CzNpEMOIhfy7fEV3UFMphue2_6_6Glj5OMTpqNztw:1qWcbC:cfipsDkPJ4eTeg3OhFLtp0EZg4AZ23ZiJg2vEpOV2TI;base_url=https://b2btesterscom.s1.my.looru.ai"
headers = {"cookie": headers_value}


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "testdata_sf_workflows")


def readwrite_json_from_file(filename):
    file_path = os.path.join(TEST_DATA_DIR, filename)
    print("File path:", file_path)
    try:
        with open(file_path, "r") as json_file:
            payload = json.load(json_file)

        # Update the payload with a random name
            payload["name"] = generate_random_name()

        # Write the updated payload back to the file
        with open(file_path, "w") as json_file:
            json.dump(payload, json_file, indent=4)

        return payload
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        return None


def read_json_from_file(filename):
    file_path = os.path.join(TEST_DATA_DIR, filename)
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        return None


def generate_random_name():
    letters = string.ascii_letters
    return 'API_AUTO_'+''.join(random.choice(string.ascii_lowercase) for _ in range(4))


def get_valid_post_schedule_payload():
    return readwrite_json_from_file("post_schedule_workflow_payload.json")


def get_invalid_post_schedule_payload():
    return read_json_from_file("invalid_post_schedule_workflow_payload.json")


def get_valid_update_workflow_payload():
    return readwrite_json_from_file("update_sf_workflow_payload.json")


def get_invalid_update_workflow_payload():
    return readwrite_json_from_file("invalid_update_sf_workflow_payload.json")


def get_valid_post_pause_workflow_payload():
    return read_json_from_file("post_sf_pause_workflow_payload.json")


def get_invalid_post_pause_workflow_payload():
    return read_json_from_file("invalid_post_sf_pause_workflow_payload.json")


def get_valid_post_unpause_workflow_payload():
    return read_json_from_file("post_sf_unpause_workflow_payload.json")


def get_invalid_post_unpause_workflow_payload():
    return read_json_from_file("invalid_post_sf_unpause_workflow_payload.json")

