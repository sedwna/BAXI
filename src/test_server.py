from database import *
import datetime

birth_date = datetime.datetime(1381, 8, 22)
date_now = datetime.datetime.now()
# insert_driver({'id': None,
#                'phone_number': "904785",
#                'shaba_number': "7486",
#                'referral_code': "12",
#                'wallet_balance': 0,
#                'signup_time': birth_date,
#                'disability': 'epilepsy',
#                'first_name': "sajad",
#                'last_name': "david",
#                'birth_date': birth_date,
#                'national_code': "06354636",
#                'license_photo_path': 'dsggagareg',
#                'national_card_photo_path': 'arsgarbgafb',
#                'sex': 'M',
#                'license_verification_date': birth_date,
#                'judicial_letter_path': None,
#                'judicial_letter_verification_date': None,
#                'final_verification_date': None,
#                'location': None,
#                'profile_picture_path': None,
#                'verifier_personnel_code': None})


insert_employee({'personnel_code': 372365825,
                 'shaba_number': '100000365825',
                 'signup_time': date_now,
                 'password': 'sedwna',
                 'first_name': 'Sajad',
                 'last_name': 'Dehqan',
                 'birth_date': birth_date,
                 'salary': 3000,
                 'department': 'HR',
                 'proficiency': 'basic',
                 'education': 'high school diploma',
                 'position': 'department manager',
                 'profile_picture_path': None})
# # importing modules
# from geopy.geocoders import Nominatim
#
# # calling the nominatim tool
# geoLoc = Nominatim(user_agent="GetLoc")
#
# # passing the coordinates
# locname = geoLoc.reverse("34.792763, 48.500777")
#
# # printing the address/location name
# print(locname.address)
# print(locname)
# try:
#     print("1")
#     insert_request({'pickup_latitude': 34.793, 'pickup_longitude': 48.491, 'pickup_province': 'srhs',
#                     'pickup_city': 'adfrh', 'client_id': 1,
#                     'request_time': datetime.datetime(2024, 3, 8, 23, 8, 1, 144561)})
#     print("2")
# except Exception as err:
#     print(err)
# try:
#     insert_acceptance({'estimated_end_time': datetime.datetime(2024, 3, 11, 12, 41, 59, 931439), 'end_time': datetime.datetime(2024, 3, 11, 12, 41, 59, 931439), 'driver_id': 1, 'method_of_payment': 'wallet-to-wallet', 'wait_time': '0-to-5 minutes', 'driver_rating': '0-star', 'client_rating': None, 'client_id': 1, 'request_time': datetime.datetime(2024, 3, 10, 17, 38, 11), 'tracking_code': None})
# except Exception as err:
#     print(err)