from db.database import *
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
                 'shaba_number': '100000372365825',
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
# importing modules
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
