*** Settings ***
Variables    ../../config.py
Library    ../../methods.py
Library    json

*** Variables ***
${booking_json_path}    \\api\\data\\create_booking.json

*** Keywords ***
Create New Booking
    ${payload}    Read Json File    ${EXECDIR}${booking_json_path}
    ${booking_payload}    json.Dumps    ${payload}
    ${response}    Post Method    ${BASE_URL}    ${ENDPOINTS['all_bookings']}    ${booking_payload}
    Log To Console    ${response}
    Should Be Equal As Integers    200    ${response.status_code}
    Should Be Equal    ${response.json()['booking']['firstname']}    ${payload['firstname']}
    Log To Console    ${response.json()}
