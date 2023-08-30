import requests

from hs_notes_utils import *

# Negative Test Case: POST Workflows
def test_post_luru_note_with_error_handling():
    invalid_post_note_payload=get_invalid_post_luru_note_payload()
    response = requests.post(base_url+"/notes", headers=headers, json=invalid_post_note_payload)
    assert response.status_code == 400, "Expected status code: 400"

# Negative Test Case: PUT Workflows
def test_put_note_with_error_handling():
    url = base_url+"/workflows/87f05ba7-f2e0-42f5-8bc3-fc0934ebc3c0"
    try:
        invalid_note_put_payload=get_invalid_update_note_payload()
        response =requests.put(url, headers=headers, json=invalid_note_put_payload)
        response.raise_for_status() 
        print("Response:", response.status_code, response.json())
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", str(e))
    except requests.exceptions.RequestException as e:
        print("Request error:", str(e))


# Negative Test Case:POST pause workflow
def test_post_add_note_connections_with_error_handling():
    url = base_url + "/workflows/0a3f65a3-b3ee-4dfe-9f9f-2c7b3fed546f/pause"
    try:
        invalid_note_put_payload=get_invalid_update_note_payload()
        response = requests.post(url, headers=headers, json=invalid_note_put_payload)
        response.raise_for_status()  # Raise an exception if the response status is not 2xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None



# Negative Test Case: delete workflows
def test_delete_workflow_with_error_hadling():
    url = base_url + "/notes/0a3f65a3-b3ee-4dfe-9f9f-2c7b3fed546"
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()  # Raise an error if the status code is not 2xx
        print("Request successful!")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)




























