*** Settings ***
Library    Collections

# Reusable assertion keywords for any API test suite.
# Import this file in your keyword files:
#   Resource    ../../keywords/CommonKeywords.robot

*** Keywords ***
Status Code Should Be
    [Arguments]    ${response}    ${expected_status}
    Should Be Equal As Integers    ${response.status_code}    ${expected_status}
    ...    msg=Expected status ${expected_status}, got ${response.status_code}

Response Should Be Successful
    [Arguments]    ${response}
    Should Be True    ${response.status_code} >= 200 and ${response.status_code} < 300
    ...    msg=Expected a 2xx response, got ${response.status_code}

Response Should Contain Field
    [Arguments]    ${response}    ${field}
    Dictionary Should Contain Key    ${response.json()}    ${field}
    ...    msg=Response body does not contain field '${field}'

Response Field Should Equal
    [Arguments]    ${response}    ${field}    ${expected_value}
    Should Be Equal As Strings    ${response.json()['${field}']}    ${expected_value}
    ...    msg=Expected '${field}' to be '${expected_value}', got '${response.json()['${field}']}'

Response Should Not Be Empty
    [Arguments]    ${response}
    Should Not Be Empty    ${response.content}
    ...    msg=Response body is empty
