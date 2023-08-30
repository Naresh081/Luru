import requests
import pytest
import json
import string
import random
import os
from hs_objects_utils import *

hs_object_id = 0


# API Test for create schedule Workflow
def test_create_record_deal():
    global hs_object_id
    url = base_url+"/sor/hubspot/objects/deals"
    print("print URL" + url)
    valid_post_payload =get_valid_post_record_payload()
    response = requests.post(url, json=valid_post_payload, headers=headers)

    json_data = response.json()

    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)

    hs_object_id = json_data["data"]["properties"]["hs_object_id"]

    print("hs_object_id ===>", hs_object_id)
    assert response.status_code == 201

    # Asserting the presence of keys and their values
    assert json_data["http_code"] == 201
    assert json_data["metadata"] is None
    assert json_data["method"] == "POST"
    assert json_data["request_id"].startswith("Root=")
    assert "data" in json_data
    data = json_data["data"]

    assert "id" in data
    assert "properties" in data
    properties = data["properties"]

    assert properties["amount"] == "100"
    assert properties["amount_in_home_currency"] == "100"
    assert properties["closedate"] == "2023-08-31T04:56:00Z"

    assert "created_at" in data
    assert "updated_at" in data
    assert data["archived"] is False
    assert data["archived_at"] is None
    assert "associations" in data

    assert json_data["error_data"] is None
    return hs_object_id

def test_update_deal():
    global hs_object_id
    
    url = base_url + f"/sor/hubspot/objects/deals/{hs_object_id}"
    valid_put_payload =get_valid_update_record_payload()

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
   # Assertions to validate specific values
    assert response_body["method"] == "PUT"
    assert response_body["data"]["id"] == hs_object_id
    assert response_body["data"]["properties"]["dealname"] is not None
    assert response_body["data"]["properties"]["dealstage"] == "appointmentscheduled"
    assert response_body["data"]["properties"]["luru_deal_status"] == "OPEN"
    assert response_body["data"]["properties"]["hs_object_id"] == hs_object_id
    assert response_body["data"]["properties"]["hubspot_owner_id"]["sor_record_name"] == "Rajkumar"
    assert response_body["data"]["properties"]["closed_lost_reason"] is None
    assert response_body["data"]["properties"]["closed_won_reason"] is None    




# API Test for Get specific Deal 
def test_get_specific_deal():
    global hs_object_id
    url = base_url+f"/sor/hubspot/objects/deals/{hs_object_id}"
    response = requests.get(url, headers=headers)
    print("Print URL "+url)
    response_body = response.json()
    json_str = json.dumps(response_body, indent=4)
    print("json POST response body: ", json_str)

    # check for response status code
    assert response.status_code == 200



# API Test for delete specific deal
@pytest.mark.sanity
def test_delete_record_of_deal():
    global hs_object_id
    url = base_url + f"/sor/hubspot/objects/deals/{hs_object_id}"
    response = requests.delete(url, headers=headers)

    print("print URL" + url)

    # print response body
    data = response.json()
    json_str = json.dumps(data, indent=4)

    print("json delete response body: ", json_str)

    assert response.status_code == 200
    # Assertion for each key and value 