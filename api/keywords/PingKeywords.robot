*** Settings ***
Variables    ../../config.py
Library    ../../methods.py

*** Keywords ***
Test Successful Ping to Restful booker
    ${response}    Get Method    ${BASE_URL}    ${ENDPOINTS['ping']}
    Should Be Equal As Integers    201    ${response.status_code}
    Should Be Equal As Strings    Created    ${response.content}