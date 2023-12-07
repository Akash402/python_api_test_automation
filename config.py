BASE_URL = "https://restful-booker.herokuapp.com/"
USERNAME = "admin"
PASSWORD = "password123"
CREATE_BOOKING = {
    "firstname" : "fname1",
    "lastname" : "lname1",
    "totalprice" : 100,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin": "2023-12-24",
        "checkout": "2023-12-31"
    },
    "additionalneeds" : "Balcony room"
}
ENDPOINTS = {
    "ping": "ping",
    "all_bookings": "booking",
    "authentication": "auth"
}
