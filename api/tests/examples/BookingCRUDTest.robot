*** Settings ***
Resource    ../../keywords/BookingKeywords.robot

# This suite demonstrates a full CRUD flow against the Restful Booker API.
# Tests run in order — the booking ID created in the first test is shared
# across the suite via a suite-level variable.
# Replace these keywords with your own when building your test suite.

*** Test Cases ***
Create Booking
    [Tags]    smoke    regression
    Create New Booking

Get Booking
    [Tags]    smoke    regression
    Get Booking

Update Booking
    [Tags]    regression
    Update Booking

Partial Update Booking
    [Tags]    regression
    Partial Update Booking

Delete Booking
    [Tags]    regression
    Delete Booking
