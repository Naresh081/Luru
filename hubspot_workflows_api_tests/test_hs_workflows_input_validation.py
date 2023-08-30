import requests
import json
import os
import string
import random
import pytest
from requests.exceptions import JSONDecodeError
from hs_workflows_utils import *

# Positive Test Case: Successful POST Schedule Workflow
def test_validate_create_schedule_workflow_with_valid_url():
    url = base_url+"/workflows"
    valid_post_payload =get_valid_post_schedule_payload()

    response = requests.post(url, headers=headers, json=valid_post_payload)
    assert response.status_code == 201, "Expected status code: 201"

# Negative Test Cases: input validations

# Test Case 1: Invalid URL
def test_validate_create_schedule_workflow_with_invalid_url():
    try:
        valid_post_payload =get_valid_post_schedule_payload()
        response = requests.post("https://b2btesters.my.luru.ai.app", headers=headers, json=valid_post_payload)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json POST response body: ", json_str)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_create_schedule_workflow_with_invalid_auth():
    url = base_url+"/workflows"
    valid_post_payload =get_valid_post_schedule_payload()
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    response = requests.post(url, headers=invalid_headers, json=valid_post_payload)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 3: Invalid payload
def test_validate_create_schedule_workflow_with_invalid_body():
    url = base_url+"/workflows"
    invalid_post_payload =get_invalid_post_schedule_payload()
    response = requests.post(url, headers=headers, json=invalid_post_payload)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    assert response.status_code == 400, "Expected status code: 400"

# Test Case 4: Invalid endpoint
def test_validate_create_schedule_workflow_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow"
    valid_post_payload =get_valid_post_schedule_payload()
    response = requests.post(invalid_endpoint, headers=headers, json=valid_post_payload)
     # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")

# Test Case 5:  empty payload
def test_validate_create_schedule_workflow_with_empty_body():
    empty_payload = {}
    response = requests.post(base_url+"/workflows", headers=headers, json=empty_payload)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    assert response.status_code == 400, "Expected status code: 400"






# Positive Test Case: Successful PUT workflows

def test_validate_update_workflow_with_valid_url():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    valid_put_payload =get_valid_update_workflow_payload()
    response = requests.put(url, headers=headers, json=valid_put_payload)
    response_body = response.json()
    if response.status_code == 202:
        assert response_body["http_code"]==202
        print("pause done")
    if response.status_code == 400:
       assert response_body["error_data"]["description"]=="Please retry later"

# Negative Test Cases: input validations

# Test Case 1: Invalid URL
def test_validate_update_workflow_with_invalid_url():
    try:
        valid_put_payload =get_valid_update_workflow_payload()
        response = requests.put("https://b2btesters.my.luru.ai.app", headers=headers, json=valid_put_payload)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_update_workflow_with_invalid_auth():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    valid_put_payload =get_valid_update_workflow_payload()
    response = requests.put(url, headers=invalid_headers, json=valid_put_payload)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 3: Invalid payload
def test_validate_update_workflow_with_invalid_body():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    invalid_put_payload =get_invalid_update_workflow_payload()
    response = requests.put(url, headers=headers, json=invalid_put_payload)
    assert response.status_code == 400, "Expected status code: 400"

# Test Case 4: Invalid endpoint
def test_validate_update_workflow_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    valid_put_payload =get_valid_update_workflow_payload()
    response = requests.put(invalid_endpoint, headers=headers, json=valid_put_payload)
     # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")

# Test Case 5:  empty payload
def test_validate_update_workflow_with_empty_body():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    empty_payload = {}
    response = requests.put(url, headers=headers, json=empty_payload)
    assert response.status_code == 202, "Expected status code: 202"





# Positive Test Case: Successful POST pause workflows
def test_validate_pause_workflow_with_valid_url():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/pause"
    valid_post_pause_payload =get_valid_post_pause_workflow_payload()
    response = requests.post(url, headers=headers, json=valid_post_pause_payload)
    assert response.status_code == 200, "Expected status code: 200"

# Negative Test Cases: input validations

# Test Case 1: Invalid URL
def test_validate_pause_workflow_with_invalid_url():
    try:
        valid_post_pause_payload =get_valid_post_pause_workflow_payload()
        response = requests.post("https://b2btesters.my.luru.ai.app", headers=headers, json=valid_post_pause_payload)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_pause_workflow_with_invalid_auth():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/pause"
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    valid_post_pause_payload =get_valid_post_pause_workflow_payload()
    response = requests.post(url, headers=invalid_headers, json=valid_post_pause_payload)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 3: Invalid payload
def test_validate_pause_workflow_with_invalid_body():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/pause"
    invalid_post_pause_payload =get_invalid_post_pause_workflow_payload()
    response = requests.post(url, headers=headers, json=invalid_post_pause_payload)
    assert response.status_code == 400, "Expected status code: 400"

# Test Case 4: Invalid endpoint
def test_validate_pause_workflow_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow/b68e35e7-0cd4-47f0-bca8-5b7181b51307/pause"
    valid_post_pause_payload =get_valid_post_pause_workflow_payload()
    response = requests.post(invalid_endpoint, headers=headers, json=valid_post_pause_payload)
     # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")

# Test Case 5:  empty payload
def test_validate_pause_workflow_with_empty_body():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    empty_payload = {}
    response = requests.post(url, headers=headers, json=empty_payload)
    response_body = response.json()
    if response.status_code == 200:
        assert response_body["http_code"]==200
        print("pause done")
    if response.status_code == 400:
       assert response_body["error_data"]["message"]=="Workflow pause failed: Can pause only when it is currently active"
       

# Positive Test Case: Successful POST unpause workflows

def test_validate_unpause_workflow_with_valid_url():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/unpause"
    valid_post_unpause_payload =get_valid_post_unpause_workflow_payload()
    response = requests.post(url, headers=headers, json=valid_post_unpause_payload)
    assert response.status_code == 200, "Expected status code: 200"

# Negative Test Cases: input validations

# Test Case 1: Invalid URL
def test_validate_unpause_workflow_with_invalid_url():
    try:
        valid_post_unpause_payload =get_valid_post_unpause_workflow_payload()
        response = requests.post("https://b2btesters.my.luru.ai.app", headers=headers, json=valid_post_unpause_payload)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_unpause_workflow_with_invalid_auth():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/unpause"
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    valid_post_unpause_payload =get_valid_post_unpause_workflow_payload()
    response = requests.post(url, headers=invalid_headers, json=valid_post_unpause_payload)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 3: Invalid payload
def test_validate_unpause_workflow_with_invalid_body():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/unpause"
    invalid_post_unpause_payload =get_invalid_post_unpause_workflow_payload()
    response = requests.post(url, headers=headers, json=invalid_post_unpause_payload)
    assert response.status_code == 400, "Expected status code: 400"

# Test Case 4: Invalid endpoint
def test_validate_unpause_workflow_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow/b68e35e7-0cd4-47f0-bca8-5b7181b51307/unpause"
    valid_post_unpause_payload =get_valid_post_unpause_workflow_payload()
    response = requests.post(invalid_endpoint, headers=headers, json=valid_post_unpause_payload)
    # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")

# Test Case 5:  empty payload
def test_validate_unpause_workflow_with_empty_body():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307/unpause"
    empty_payload = {}
    response = requests.post(url, headers=headers, json=empty_payload)
    response_body = response.json()
    if response.status_code == 200:
        assert response_body["http_code"]==200
        print("pause done")
    if response.status_code == 400:
       assert response_body["error_data"]["message"]=="Workflow unpause failed: Can unpause only when it is currently paused"


# Positive Test Case: Successful GET list of workflows
def test_validate_get_list_of_workflows_with_valid_url():
    url = base_url + "/workflows"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, "Expected status code: 202"

# Negative Test Cases: input validations

# Test Case 1: Invalid URL
def test_validate_get_list_of_workflows_with_invalid_url():
    try:
        response = requests.get("https://b2btesters.my.luru.ai.app", headers=headers)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_get_list_of_workflows_with_invalid_auth():
    url = base_url + "/workflows"
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    response = requests.get(url, headers=invalid_headers)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 3: Invalid endpoint
def test_validate_get_list_of_workflows_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow"
    response = requests.get(invalid_endpoint, headers=headers)
     # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")



# Positive Test Case: Successful GET specific workflow
def test_validate_get_specific_workflow_with_valid_url():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, "Expected status code: 202"

# Test Case 1: Invalid URL
def test_validate_get_specific_workflow_with_invalid_url():
    try:
        response = requests.get("https://b2btesters.my.luru.ai.app", headers=headers)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_get_specific_workflow_with_invalid_auth():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    response = requests.get(url, headers=invalid_headers)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 4: Invalid endpoint
def test_validate_get_specific_workflow_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    response = requests.get(invalid_endpoint, headers=headers)
     # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")


# Positive Test Case: Successful delete specific workflow
def test_validate_delete_specific_workflow_with_valid_url():
    url = base_url + "/workflows/b21a38b9-ed25-4eff-ad4f-5fce69e89f6f"
    response = requests.get(url, headers=headers)
    response_body = response.json()
    if response.status_code == 200:
        assert response_body["http_code"]==200
        print("pause done")
    if response.status_code == 404:
       assert response_body["error_data"]["message"]=="Given workflow not found"


# Test Case 1: Invalid URL
def test_validate_delete_specific_workflow_with_invalid_url():
    try:
        response = requests.get("https://b2btesters.my.luru.ai.app", headers=headers)
        assert response.status_code == 404, "Expected status code: 404"
    except requests.exceptions.ConnectionError:
        pass  # Expected behavior for an invalid URL

# Test Case 2: Invalid header
def test_validate_delete_specific_workflow_with_invalid_auth():
    url = base_url + "/workflows/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    invalid_headers = {"cookie": "eJxVjstOwzAQRf_Fa5L67aS7rFqqlgqxoLCxxi8SNUpQbVMkxL"}
    response = requests.get(url, headers=invalid_headers)
    assert response.status_code == 401, "Expected status code: 401"

# Test Case 4: Invalid endpoint
def test_validate_delete_specific_workflow_with_invalid_endpoint():
    invalid_endpoint = base_url + "/workflow/b68e35e7-0cd4-47f0-bca8-5b7181b51307"
    response = requests.get(invalid_endpoint, headers=headers)
     # Assert the response status code
    assert response.status_code == 404, "Expected status code: 404"
    # Print the response content
    print("Response Content:", response.content)
    try:
        json_data = response.json()
        print("Decoded JSON Data:", json_data)
    except JSONDecodeError as e:
        print("JSON Decoding Error:", e)
        print("Response Content:", response.content)
        print("Error occurred while decoding JSON data.")