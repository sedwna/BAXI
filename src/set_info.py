import datetime
from shapely.geometry import Point


class InsertInfo:
    insert_client_dict = {'client_id': None,
                          'phone_number': None,
                          'wallet_balance': 0,
                          'signup_time': datetime,
                          'first_name': None,
                          'last_name': None,
                          'birth_date': datetime,
                          'sex': None,
                          'email': None}

    insert_driver_dict = {'id': None,
                          'referral_code': None,
                          'phone_number': None,
                          'shaba_number': None,
                          'wallet_balance': 0,
                          'signup_time': datetime,
                          'disability': None,
                          'first_name': None,
                          'last_name': None,
                          'birth_date': datetime,
                          'national_code': None,
                          'license_photo_path': None,
                          'national_card_photo_path': None,
                          'sex': 'M',
                          'license_verification_date': None,
                          'judicial_letter_path': None,
                          'judicial_letter_verification_date': None,
                          'final_verification_date': None,
                          'latitude': None,
                          'longitude': None,
                          'profile_picture_path': None,
                          'verifier_personnel_code': None}

    insert_baxi_dict = {'vehicle_license_plate': 'none',
                        'vehicle_capacity': 4,
                        'vehicle_color': 'none',
                        'vehicle_name': 'none',
                        'vehicle_production_date': None,
                        'vehicle_card_photo': '../C:desktop/vehicle card',
                        'vehicle_fuel_type': 'none',
                        'driver_id': 0}

    def set_vehicle_license_plate_insert_baxi_dict(self, vehicle_license_plate):
        self.insert_baxi_dict['vehicle_license_plate'] = vehicle_license_plate

    def set_vehicle_capacity_insert_baxi_dict(self, vehicle_capacity):
        self.insert_baxi_dict['vehicle_capacity'] = vehicle_capacity

    def set_vehicle_color_insert_baxi_dict(self, vehicle_color):
        self.insert_baxi_dict['vehicle_color'] = vehicle_color

    def set_vehicle_name_insert_baxi_dict(self, vehicle_name):
        self.insert_baxi_dict['vehicle_name'] = vehicle_name

    def set_vehicle_production_date_insert_baxi_dict(self, vehicle_production_date):
        self.insert_baxi_dict['vehicle_production_date'] = vehicle_production_date

    def set_vehicle_card_photo_insert_baxi_dict(self, vehicle_card_photo):
        self.insert_baxi_dict['vehicle_card_photo'] = vehicle_card_photo

    def set_vehicle_fuel_type_insert_baxi_dict(self, vehicle_fuel_type):
        self.insert_baxi_dict['vehicle_fuel_type'] = vehicle_fuel_type

    def set_driver_id_insert_baxi_dict(self, driver_id):
        self.insert_baxi_dict['driver_id'] = driver_id

    insert_baar_dict = {'vehicle_license_plate': 'none',
                        'vehicle_capacity': 4,
                        'vehicle_color': 'none',
                        'vehicle_name': 'none',
                        'vehicle_production_date': None,
                        'vehicle_card_photo': '../C:desktop/vehicle card',
                        'vehicle_fuel_type': 'none',
                        'driver_id': 0}

    def set_vehicle_license_plate_insert_baar_dict(self, vehicle_license_plate):
        self.insert_baar_dict['vehicle_license_plate'] = vehicle_license_plate

    def set_vehicle_capacity_insert_baar_dict(self, vehicle_capacity):
        self.insert_baar_dict['vehicle_capacity'] = vehicle_capacity

    def set_vehicle_color_insert_baar_dict(self, vehicle_color):
        self.insert_baar_dict['vehicle_color'] = vehicle_color

    def set_vehicle_name_insert_baar_dict(self, vehicle_name):
        self.insert_baar_dict['vehicle_name'] = vehicle_name

    def set_vehicle_production_date_insert_baar_dict(self, vehicle_production_date):
        self.insert_baar_dict['vehicle_production_date'] = vehicle_production_date

    def set_vehicle_card_photo_insert_baar_dict(self, vehicle_card_photo):
        self.insert_baar_dict['vehicle_card_photo'] = vehicle_card_photo

    def set_vehicle_fuel_type_insert_baar_dict(self, vehicle_fuel_type):
        self.insert_baar_dict['vehicle_fuel_type'] = vehicle_fuel_type

    def set_driver_id_insert_insert_baar_dict(self, driver_id):
        self.insert_baar_dict['driver_id'] = driver_id

    insert_box_dict = {'vehicle_license_plate': 'none',
                       'vehicle_capacity': 4,
                       'vehicle_color': 'none',
                       'vehicle_name': 'none',
                       'vehicle_production_date': None,
                       'vehicle_card_photo': '../C:desktop/vehicle card',
                       'driver_id': 0}

    def set_vehicle_license_plate_insert_box_dict(self, vehicle_license_plate):
        self.insert_box_dict['vehicle_license_plate'] = vehicle_license_plate

    def set_vehicle_capacity_insert_box_dict(self, vehicle_capacity):
        self.insert_box_dict['vehicle_capacity'] = vehicle_capacity

    def set_vehicle_color_insert_box_dict(self, vehicle_color):
        self.insert_box_dict['vehicle_color'] = vehicle_color

    def set_vehicle_name_insert_box_dict(self, vehicle_name):
        self.insert_box_dict['vehicle_name'] = vehicle_name

    def set_vehicle_production_date_insert_box_dict(self, vehicle_production_date):
        self.insert_box_dict['vehicle_production_date'] = vehicle_production_date

    def set_vehicle_card_photo_insert_box_dict(self, vehicle_card_photo):
        self.insert_box_dict['vehicle_card_photo'] = vehicle_card_photo

    def set_driver_id_insert_insert_box_dict(self, driver_id):
        self.insert_box_dict['driver_id'] = driver_id

    insert_employee_dict = {'personnel_code': None,
                            'shaba_number': None,
                            'signup_time': None,
                            'password': None,
                            'first_name': None,
                            'last_name': None,
                            'birth_date': None,
                            'salary': 0,
                            'department': None,
                            'proficiency': None,
                            'education': 'none',
                            'position': None,
                            'profile_picture_path': None}

    def set_personnel_code_insert_employee_dict(self, personnel_code):
        self.insert_employee_dict['personnel_code'] = personnel_code

    def set_shaba_number_insert_employee_dict(self, shaba_number):
        self.insert_employee_dict['shaba_number'] = shaba_number

    def set_signup_time_insert_employee_dict(self):
        self.insert_employee_dict['signup_time'] = datetime.datetime.now()

    def set_password_insert_employee_dict(self, password):
        self.insert_employee_dict['password'] = password

    def set_first_name_insert_employee_dict(self, first_name):
        self.insert_employee_dict['first_name'] = first_name

    def set_last_name_insert_employee_dict(self, last_name):
        self.insert_employee_dict['last_name'] = last_name

    def set_birth_date_insert_employee_dict(self, birth_date):
        self.insert_employee_dict['birth_date'] = birth_date

    def set_salary_insert_employee_dict(self, salary):
        self.insert_employee_dict['salary'] = salary

    def set_department_insert_employee_dict(self, department):
        self.insert_employee_dict['department'] = department

    def set_proficiency_insert_employee_dict(self, proficiency):
        self.insert_employee_dict['proficiency'] = proficiency

    def set_education_insert_employee_dict(self, education):
        self.insert_employee_dict['education'] = education

    def set_position_code_insert_employee_dict(self, position):
        self.insert_employee_dict['position'] = position

    def set_profile_picture_path_insert_employee_dict(self, profile_picture_path):
        self.insert_employee_dict['profile_picture_path'] = profile_picture_path

    def set_phone_number_insert_driver_dict(self, phone_number):
        self.insert_driver_dict['phone_number'] = phone_number

    def set_shaba_number_insert_driver_dict(self, shaba_number):
        self.insert_driver_dict['shaba_number'] = shaba_number

    def set_referral_code_insert_driver_dict(self, referral_code):
        self.insert_driver_dict['referral_code'] = referral_code

    def set_wallet_balance_insert_driver_dict(self, wallet_balance):
        self.insert_driver_dict['wallet_balance'] = wallet_balance

    def set_signup_time_insert_driver_dict(self):
        self.insert_driver_dict['signup_time'] = datetime.datetime.now()

    def set_disability_insert_driver_dict(self, disability):
        self.insert_driver_dict['disability'] = disability

    def set_first_name_insert_driver_dict(self, first_name):
        self.insert_driver_dict['first_name'] = first_name

    def set_last_name_insert_driver_dict(self, last_name):
        self.insert_driver_dict['last_name'] = last_name

    def set_birth_date_insert_driver_dict(self, year, month, day):
        self.insert_driver_dict['birth_date'] = datetime.datetime(year, month, day)

    def set_national_code_insert_driver_dict(self, national_code):
        self.insert_driver_dict['national_code'] = national_code

    def set_license_photo_path_insert_driver_dict(self, license_photo_path):
        self.insert_driver_dict['license_photo_path'] = license_photo_path

    def set_national_card_photo_path_insert_driver_dict(self, national_card_photo_path):
        self.insert_driver_dict['national_card_photo_path'] = national_card_photo_path

    def set_sex_insert_driver_dict(self, sex):
        self.insert_driver_dict['sex'] = sex

    def set_license_verification_date_insert_driver_dict(self, license_verification_date):
        self.insert_driver_dict['license_verification_date'] = license_verification_date

    def set_judicial_letter_path_insert_driver_dict(self, judicial_letter_path):
        self.insert_driver_dict['judicial_letter_path'] = judicial_letter_path

    def set_judicial_letter_verification_date_insert_driver_dict(self, judicial_letter_verification_date):
        self.insert_driver_dict['judicial_letter_verification_date'] = judicial_letter_verification_date

    def set_final_verification_date_insert_driver_dict(self, final_verification_date):
        self.insert_driver_dict['final_verification_date'] = final_verification_date

    def set_latitude_insert_driver_dict(self, latitude):
        self.insert_driver_dict['latitude'] = latitude

    def set_longitude_insert_driver_dict(self, longitude):
        self.insert_driver_dict['longitude'] = longitude

    def set_profile_picture_path_insert_driver_dict(self, profile_picture_path):
        self.insert_driver_dict['profile_picture_path'] = profile_picture_path

    def set_verifier_personnel_code_insert_driver_dict(self, verifier_personnel_code):
        self.insert_driver_dict['verifier_personnel_code'] = verifier_personnel_code

    def set_client_id_insert_client_dict(self, client_id):
        self.insert_client_dict['client_id'] = client_id

    def set_phone_number_insert_client_dict(self, phone_number):
        self.insert_client_dict['phone_number'] = phone_number

    def set_wallet_balance_insert_client_dict(self, wallet_balance):
        self.insert_client_dict['wallet_balance'] = wallet_balance

    def set_sign_up_time_insert_client_dict(self):
        self.insert_client_dict['signup_time'] = datetime.datetime.now()

    def set_first_name_insert_client_dict(self, first_name):
        self.insert_client_dict['first_name'] = first_name

    def set_last_name_insert_client_dict(self, last_name):
        self.insert_client_dict['last_name'] = last_name

    def set_birth_date_insert_client_dict(self, birth_date):
        self.insert_client_dict['birth_date'] = birth_date

    def set_sex_insert_client_dict(self, sex):
        self.insert_client_dict['sex'] = sex

    def set_email_insert_client_dict(self, email):
        self.insert_client_dict['email'] = email

    insert_request_dict = {'pickup_latitude': float,
                           'pickup_longitude': float,
                           'pickup_province': str,
                           'pickup_city': str,
                           'client_id': int,
                           'request_time': datetime}

    def set_pickup_latitude_insert_request_dict(self, pickup_latitude):
        self.insert_request_dict['pickup_latitude'] = pickup_latitude

    def set_pickup_longitude_insert_request_dict(self, pickup_longitude):
        self.insert_request_dict['pickup_longitude'] = pickup_longitude

    def set_pickup_province_insert_request_dict(self, pickup_province):
        self.insert_request_dict['pickup_province'] = pickup_province

    def set_pickup_city_insert_request_dict(self, pickup_city):
        self.insert_request_dict['pickup_city'] = pickup_city

    def set_client_id_insert_request_dict(self, client_id):
        self.insert_request_dict['client_id'] = client_id

    def set_request_time_insert_request_dict(self, request_time):
        self.insert_request_dict['request_time'] = request_time

    insert_destination_dict = {'city': str,
                               'client_id': int,
                               'request_time': datetime,
                               'latitude': float,
                               'longitude': float}

    def set_latitude_insert_destination_dict(self, latitude):
        self.insert_destination_dict['latitude'] = latitude

    def set_longitude_insert_destination_dict(self, longitude):
        self.insert_destination_dict['longitude'] = longitude

    def set_city_insert_destination_dict(self, city):
        self.insert_destination_dict['city'] = city

    def set_client_id_insert_destination_dict(self, client_id):
        self.insert_destination_dict['client_id'] = client_id

    def set_request_time_insert_destination_dict(self, request_time):
        self.insert_destination_dict['request_time'] = request_time

    insert_trip_dict = {'cost': int,
                        'round_trip': None,
                        'client_id': int,
                        'request_time': datetime}

    def set_cost_insert_trip_dict(self, cost):
        self.insert_trip_dict['cost'] = cost

    def set_round_trip_insert_trip_dict(self, round_trip):
        self.insert_trip_dict['round_trip'] = round_trip

    def set_client_id_insert_trip_dict(self, client_id):
        self.insert_trip_dict['client_id'] = client_id

    def set_request_time_insert_trip_dict(self, request_time):
        self.insert_trip_dict['request_time'] = request_time

    insert_heavy_dict = {'cost': int,
                         'cargo_weight': int,
                         'cargo_value': int,
                         'dropoff_latitude': float,
                         'dropoff_longitude': float,
                         'dropoff_city': str,
                         'cargo_type': str,
                         'client_helped': str,
                         'client_id': int,
                         'request_time': datetime}

    def set_cost_insert_heavy_dict(self, cost):
        self.insert_heavy_dict['cost'] = cost

    def set_cargo_weight_insert_heavy_dict(self, cargo_weight):
        self.insert_heavy_dict['cargo_weight'] = cargo_weight

    def set_cargo_value_insert_heavy_dict(self, cargo_value):
        self.insert_heavy_dict['cargo_value'] = cargo_value

    def set_dropoff_latitude_insert_heavy_dict(self, dropoff_latitude):
        self.insert_heavy_dict['dropoff_latitude'] = dropoff_latitude

    def set_dropoff_longitude_insert_heavy_dict(self, dropoff_longitude):
        self.insert_heavy_dict['dropoff_longitude'] = dropoff_longitude

    def set_dropoff_city_insert_heavy_dict(self, dropoff_city):
        self.insert_heavy_dict['dropoff_city'] = dropoff_city

    def set_client_helped_insert_heavy_dict(self, client_helped):
        self.insert_heavy_dict['client_helped'] = client_helped

    def set_cargo_type_insert_heavy_dict(self, cargo_type):
        self.insert_heavy_dict['cargo_type'] = cargo_type

    def set_request_time_insert_heavy_dict(self, request_time):
        self.insert_heavy_dict['request_time'] = request_time

    def set_client_id_insert_heavy_dict(self, client_id):
        self.insert_heavy_dict['client_id'] = client_id
