import requests
import pytest
import json
import string
import random
import os
from sf_workflows_utils import *

workflow_id = 0


# API Test for List Workflows
@pytest.mark.sanity
def test_sf_get_workflows():

    url = base_url+"/workflows"
    
    response = requests.get(url, headers=headers)

    print("Print URL "+url)

    response_body = response.json()
    json_str = json.dumps(response_body, indent=4)
    print("json POST response body: ", json_str)

    # check for response status code
    assert response.status_code == 200


    # Key-level assertions
    assert "http_code" in response_body
    assert "metadata" in response_body
    assert "method" in response_body
    assert "request_id" in response_body
    assert "data" in response_body

    # Assertion for http_code
    assert response_body["http_code"] == 200, "HTTP code should be 200"

    # Assertion for method
    assert response_body["method"] == "GET", "Method should be GET"

    # Assertion for workflow_id
    assert response_body["data"][0]["workflow_id"] is not None

    # Assertion for name
    assert response_body["data"][0]["name"] is not None


# API Test for single Workflow

def test_sf_get_workflow():

    url = base_url+"/workflows/23a8b942-d36f-4723-8800-7515a0201f94"

    response = requests.get(url, headers=headers)

    print("Print URL "+url)

    response_json = response.json()
    json_str = json.dumps(response_json, indent=4)
    print("json POST response body: ", json_str)

    # check for response status code
    assert response.status_code == 200

    # Assertions to validate specific values within the JSON structure
    assert response_json["http_code"] == 200, "Unexpected http_code"
    assert response_json["method"] == "GET", "Unexpected method"
    assert response_json["data"]["workflow_id"]  is not None, "Unexpected workflow_id"


# API Test for create schedule workflow of HubSpot
def test_sf_create_workflow():
    global workflow_id
    url = base_url+"/workflows"
    print("print URL" + url)
    valid_post_payload =get_valid_post_schedule_payload()
    response = requests.post(url, json=valid_post_payload, headers=headers)

    # check for response status code

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    workflow_id = json_data["data"]["workflow_id"]
    print("workflow_id ===>", workflow_id)
    assert response.status_code == 201
    # Asserting the presence of keys and their values
    assert json_data["http_code"] == 201
    assert json_data["method"] == "POST"
    assert json_data["data"]["name"] is not None
    assert json_data["data"]["sor"] == "SFDC"
    assert json_data["data"]["sor_object_name"] == "Opportunity"
    assert json_data["data"]["state"] == "ACTIVE"
    assert json_data["data"]["evaluation"]["type"] == "SCHEDULE"
    assert json_data["data"]["actions"][0]["type"] == "slack-message"
    return workflow_id


# API Test for update WorkFlow
@pytest.mark.sanity
def test_sf_update_workflow():
    global workflow_id
    url = base_url + f"/workflows/{workflow_id}"
    valid_put_payload =get_valid_update_workflow_payload()

    print("print URL" + url)

    response = requests.put(url, json=valid_put_payload, headers=headers)

    print("print URL" + url)

    # check for response status code
    assert response.status_code == 202

    response_body = response.json()
    json_str = json.dumps(response_body, indent=4)
    print("json POST response body: ", json_str)
    # Asserting the presence of keys and their values
    assert response_body["http_code"] == 202
    assert response_body["method"] == "PUT"
    assert response_body["data"]["name"] is not None
    assert response_body["data"]["sor"] == "SFDC"
    assert response_body["data"]["sor_object_name"] == "Opportunity"
    assert response_body["data"]["state"] == "ACTIVE"
    assert response_body["data"]["evaluation"]["type"] == "SCHEDULE"
    assert response_body["data"]["actions"][0]["type"] == "slack-message"



# API Test for pause WorkFlow
@pytest.mark.sanity
def test_pause_workflow():
    global workflow_id
    url = base_url + f"/workflows/{workflow_id}/pause"
    valid_post_pause_payload =get_valid_post_pause_workflow_payload()
    response = requests.post(url, json=valid_post_pause_payload, headers=headers)

    print("print URL" + url)

    # check for response status code
    assert response.status_code == 200

    response_body = response.json()
    json_str = json.dumps(response_body, indent=4)
    print("json response body: ", json_str)

   # Asserting the presence of keys and their values
    assert response_body["http_code"] == 200
    assert response_body["method"] == "POST"
    assert response_body["http_code"] == 200
    assert response_body["method"] == "POST"
    assert response_body["data"]["workflow_id"] is not None
    assert response_body["data"]["evaluation"]["type"] == "SCHEDULE"
    assert response_body["data"]["actions"][0]["type"] == "slack-message"
 


# API Test for unpause WorkFlow
@pytest.mark.sanity
def test_unpause_workflow():
    global workflow_id
    url = base_url + f"/workflows/{workflow_id}/unpause"
    valid_post_unpause_payload =get_valid_post_unpause_workflow_payload()
    response = requests.post(url, json=valid_post_unpause_payload, headers=headers)

    print("print URL" + url)

    # check for response status code
    assert response.status_code == 200

    response_body = response.json()
    json_str = json.dumps(response_body, indent=4)
    print("json response body: ", json_str)

   # Asserting the presence of keys and their values
    assert response_body["http_code"] == 200
    assert response_body["method"] == "POST"
    assert response_body["data"]["workflow_id"] is not None
    assert response_body["data"]["evaluation"]["type"] == "SCHEDULE"
    assert response_body["data"]["actions"][0]["type"] == "slack-message"

# API Test for delete Note
@pytest.mark.sanity
def test_delete_workflow():
    global workflow_id
    url = base_url + f"/workflows/{workflow_id}"
    response = requests.delete(url, headers=headers)

    print("print URL" + url)

    # print response body
    data = response.json()
    json_str = json.dumps(data, indent=4)

    print("json delete response body: ", json_str)

    assert response.status_code == 200
    # Assertion for each key and value 
    assert data["http_code"] == 200
    assert data["metadata"] is None
    assert data["method"] == "DELETE"
    assert data["request_id"] is not None
    assert data["error_data"] is None


