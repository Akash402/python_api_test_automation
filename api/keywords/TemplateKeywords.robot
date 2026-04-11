*** Settings ***
Variables    ../../lib/config.py
Library      ../../lib/methods.py
Library      json
Resource     ../../keywords/CommonKeywords.robot

# Copy this file and rename it to match your resource (e.g. UserKeywords.robot).
# Each keyword here maps to one API operation.
# Add as many keywords as you have endpoints to test.

*** Variables ***
# Path to your request payload JSON file (relative to repo root).
# Add a JSON file under api/data/ for each request body you need.
${payload_path}    ${EXECDIR}${/}api${/}data${/}your_payload.json

*** Keywords ***
# --- GET ---
# Replace 'Get Resource' with a descriptive name (e.g. 'Get User By ID').
# Replace ENDPOINTS['your_endpoint'] with the key from lib/config.py.
Get Resource
    [Arguments]    ${id}
    ${response}    Get Method    ${BASE_URL}    ${ENDPOINTS['your_endpoint']}${id}
    Status Code Should Be    ${response}    200
    Response Should Contain Field    ${response}    id    # Replace 'id' with a field you expect
    [Return]    ${response}

# --- POST ---
# Replace 'Create Resource' with a descriptive name (e.g. 'Create User').
Create Resource
    ${payload}    Read Json File    ${payload_path}
    ${body}       json.Dumps    ${payload}
    ${response}   Post Method    ${BASE_URL}    ${ENDPOINTS['your_endpoint']}    ${body}
    Status Code Should Be    ${response}    201    # Adjust expected status code
    ${created_id}    Set Variable    ${response.json()['id']}    # Replace 'id' with the ID field in your response
    Set Suite Variable    ${RESOURCE_ID}    ${created_id}
    [Return]    ${response}

# --- PUT ---
# Replace 'Update Resource' with a descriptive name (e.g. 'Update User').
Update Resource
    [Arguments]    ${id}
    ${payload}    Read Json File    ${payload_path}
    ${body}       json.Dumps    ${payload}
    ${response}   Put Method    ${BASE_URL}    ${ENDPOINTS['your_endpoint']}${id}    ${body}
    Status Code Should Be    ${response}    200
    [Return]    ${response}

# --- PATCH ---
# Replace 'Partial Update Resource' with a descriptive name.
Partial Update Resource
    [Arguments]    ${id}    ${patch_data}
    ${body}       json.Dumps    ${patch_data}
    ${response}   Patch Method    ${BASE_URL}    ${ENDPOINTS['your_endpoint']}${id}    ${body}
    Status Code Should Be    ${response}    200
    [Return]    ${response}

# --- DELETE ---
# Replace 'Delete Resource' with a descriptive name (e.g. 'Delete User').
Delete Resource
    [Arguments]    ${id}
    ${response}    Delete Method    ${BASE_URL}    ${ENDPOINTS['your_endpoint']}${id}
    Status Code Should Be    ${response}    204    # Adjust expected status code
    [Return]    ${response}
