*** Settings ***
Variables    ../../lib/config.py
Library    ../../lib/methods.py
Library    json

*** Variables ***
${create_booking_path}    ${EXECDIR}${/}api${/}data${/}create_booking.json
${update_booking_path}    ${EXECDIR}${/}api${/}data${/}update_booking.json

*** Keywords ***
Create New Booking
    ${payload}    Read Json File    ${create_booking_path}
    ${booking_payload}    json.Dumps    ${payload}
    ${response}    Post Method    ${BASE_URL}    ${ENDPOINTS['all_bookings']}    ${booking_payload}
    Should Be Equal As Integers    200    ${response.status_code}
    Should Be Equal    ${response.json()['booking']['firstname']}    ${payload['firstname']}
    ${booking_id}    Set Variable    ${response.json()['bookingid']}
    Set Suite Variable    ${BOOKING_ID}    ${booking_id}

Get Booking
    ${response}    Get Method    ${BASE_URL}    ${ENDPOINTS['get_booking']}${BOOKING_ID}
    Should Be Equal As Integers    200    ${response.status_code}
    Should Not Be Empty    ${response.json()['firstname']}

Update Booking
    ${payload}    Read Json File    ${update_booking_path}
    ${booking_payload}    json.Dumps    ${payload}
    ${response}    Put Method    ${BASE_URL}    ${ENDPOINTS['get_booking']}${BOOKING_ID}    ${booking_payload}
    Should Be Equal As Integers    200    ${response.status_code}
    Should Be Equal    ${response.json()['firstname']}    ${payload['firstname']}

Partial Update Booking
    ${patch_payload}    json.Dumps    ${{{"firstname": "UpdatedName"}}}
    ${response}    Patch Method    ${BASE_URL}    ${ENDPOINTS['get_booking']}${BOOKING_ID}    ${patch_payload}
    Should Be Equal As Integers    200    ${response.status_code}
    Should Be Equal    ${response.json()['firstname']}    UpdatedName

Delete Booking
    ${response}    Delete Method    ${BASE_URL}    ${ENDPOINTS['get_booking']}${BOOKING_ID}
    Should Be Equal As Integers    201    ${response.status_code}
