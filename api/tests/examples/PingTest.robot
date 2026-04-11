*** Settings ***
Resource    ../../keywords/PingKeywords.robot
Test Tags   smoke

*** Test Cases ***
Testing Ping
    Test Successful Ping to Restful booker
