import requests
import json
import os
import string
import random
import pytest
from requests.exceptions import JSONDecodeError

base_url = "https://b2btesterscom.s1.my.looru.ai/api"
headers_value= "sessionid=.eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL-TqFnQ1czV6Nw5P2jw3wmt0WqeK_SA2mzi55h0TJD8dDjk50Z-HY5Pm1MLzfD6_ra9stMVdhsp9i_8cUI05NTqHP1Fd25CKucFCMwLI4IqOFahAOF9AcArhYFYyfE9ZsCe_TCzcyyXGMtFptznS97e9mMzUfQebyG2819CKQuqwpJVwuPaeEWscwDBMeJqTI2A2tUgiMHW8kApYGUkFooRHiyfSuNoO-hv1T3EpPvxoxv--S1G6PcPkK9mYQ:1qWbWj:P1SZGdU_Tubf9t1HBaOEM6XEw4vB-f9263b18lteEJQ;base_url=https://b2btesterscom.s1.my.looru.ai"
headers = {"cookie": headers_value}


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "testdata_hs_notes")


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


def get_valid_post_luru_note_payload():
    return readwrite_json_from_file("create_note_payload.json")


def get_invalid_post_luru_note_payload():
    return read_json_from_file("invalid_create_note_payload.json")


def get_valid_update_note_payload():
    return readwrite_json_from_file("update_note_payload.json")


def get_invalid_update_note_payload():
    return readwrite_json_from_file("invalid_update_note_payload.json")


def get_valid_post_add_note_connection_payload():
    return read_json_from_file("create_add_note_connection_payload.json")


def get_invalid_post_add_note_connection_payload():
    return read_json_from_file("invalid_create_add_note_connection_payload.json")





























# def generate_random_name():
#  letters = string.ascii_letters
#  return 'API_AUTO_'+''.join(random.choice(string.ascii_lowercase) for _ in range(4))


# #valid post create new Notes Payload
# relative_path = os.path.join(
#         "testdata_notes", "create_note_payload.json")
# script_directory = os.path.dirname(__file__)
# absolute_path = os.path.join(script_directory, relative_path)
# with open(absolute_path, "r") as json_file:
#     valid_post_payload = json.load(json_file)



# # invalid post create new Notes Payload
# relative_path = os.path.join(
#         "testdata_notes", "invalid_create_note_payload.json")
# script_directory = os.path.dirname(__file__)
# absolute_path = os.path.join(script_directory, relative_path)
# with open(absolute_path, "r") as json_file:
#     invalid_post_note_payload = json.load(json_file)
# print(invalid_post_note_payload)


# #valid update Notes paylod
# relative_path = os.path.join("testdata_notes", "update_note_payload.json")
#     # Get the absolute path of the script's directory and join it with the relative path
# script_directory = os.path.dirname(__file__)
# absolute_path = os.path.join(script_directory, relative_path)
#     # Load JSON data from the specified file
# with open(absolute_path, "r") as json_file:
#         valid_put_payload = json.load(json_file)



# #invalid update Notes paylod
# relative_path = os.path.join("testdata_notes", "invalid_update_note_payload.json")
#     # Get the absolute path of the script's directory and join it with the relative path
# script_directory = os.path.dirname(__file__)
# absolute_path = os.path.join(script_directory, relative_path)
#     # Load JSON data from the specified file
# with open(absolute_path, "r") as json_file:
#         invalid_note_put_payload = json.load(json_file)
# print(invalid_note_put_payload)



# #valid create add noteconnection paylod
# relative_path = os.path.join("testdata_notes", "create_add_note_connection_payload.json")
#     # Get the absolute path of the script's directory and join it with the relative path
# script_directory = os.path.dirname(__file__)
# absolute_path = os.path.join(script_directory, relative_path)
#     # Load JSON data from the specified file
# with open(absolute_path, "r") as json_file:
#         valid_post_add_note_connection_payload = json.load(json_file)
# print(valid_post_add_note_connection_payload)



# #invalid add noteconnection paylod
# relative_path = os.path.join("testdata_notes", "invalid_create_add_note_connection_payload.json")
#     # Get the absolute path of the script's directory and join it with the relative path
# script_directory = os.path.dirname(__file__)
# absolute_path = os.path.join(script_directory, relative_path)
#     # Load JSON data from the specified file
# with open(absolute_path, "r") as json_file:
#         invalid_post_add_note_connection_payload = json.load(json_file)
# print(invalid_post_add_note_connection_payload)


