import datetime


class InsertInfo:
    insert_driver_dict = {'id': None,
                          'referral_code': None,
                          'phone_number': None,
                          'shaba_number': None,
                          'wallet_balance': 0,
                          'signup_time': None,
                          'disability': None,
                          'first_name': None,
                          'last_name': None,
                          'birth_date': None,
                          'national_code': None,
                          'license_photo_path': None,
                          'national_card_photo_path': None,
                          'sex': 'M',
                          'license_verification_date': None,
                          'judicial_letter_path': None,
                          'judicial_letter_verification_date': None,
                          'final_verification_date': None,
                          'location': None,
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
    insert_baar_dict = {'vehicle_license_plate': 'none',
                        'vehicle_capacity': 4,
                        'vehicle_color': 'none',
                        'vehicle_name': 'none',
                        'vehicle_production_date': 'none',
                        'vehicle_card_photo': '../C:desktop/vehicle card',
                        'vehicle_fuel_type': 'none',
                        'driver_id': 0}
    insert_box_dict = {'vehicle_license_plate': 'none',
                       'vehicle_capacity': 4,
                       'vehicle_color': 'none',
                       'vehicle_name': 'none',
                       'vehicle_production_date': None,
                       'vehicle_card_photo': '../C:desktop/vehicle card',
                       'driver_id': 0}

    insert_employee_dict = {'personnel_code': 11111111,
                            'shaba_number': None,
                            'signup_time': None,
                            'password': None,
                            'first_name': None,
                            'last_name': None,
                            'birth_date': None,
                            'salary': 0,
                            'department': None,
                            'proficiency': None,
                            'education': None,
                            'position': None,
                            'profile_picture_path': None}

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

    def set_location_insert_driver_dict(self, location):
        self.insert_driver_dict['location'] = location

    def set_profile_picture_path_insert_driver_dict(self, profile_picture_path):
        self.insert_driver_dict['profile_picture_path'] = profile_picture_path

    def set_verifier_personnel_code_insert_driver_dict(self, verifier_personnel_code):
        self.insert_driver_dict['verifier_personnel_code'] = verifier_personnel_code
