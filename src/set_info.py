import datetime


class DriverInfo:
    insert_driver = {'id': None,
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
                     'verifier_personnel_code': 1001}

    def set_phone_number(self, phone_number):
        self.insert_driver['phone_number'] = phone_number

    def set_shaba_number(self, shaba_number):
        self.insert_driver['shaba_number'] = shaba_number

    def set_referral_code(self, referral_code):
        self.insert_driver['referral_code'] = referral_code

    def set_wallet_balance(self, wallet_balance):
        self.insert_driver['wallet_balance'] = wallet_balance

    def set_signup_time(self):
        self.insert_driver['signup_time'] = datetime.datetime.now()

    def set_disability(self, disability):
        self.insert_driver['disability'] = disability

    def set_first_name(self, first_name):
        self.insert_driver['first_name'] = first_name

    def set_last_name(self, last_name):
        self.insert_driver['last_name'] = last_name

    def set_birth_date(self, birth_date):
        self.insert_driver['birth_date'] = birth_date

    def set_national_code(self, national_code):
        self.insert_driver['national_code'] = national_code

    def set_license_photo_path(self, license_photo_path):
        self.insert_driver['license_photo_path'] = license_photo_path

    def set_national_card_photo_path(self, national_card_photo_path):
        self.insert_driver['national_card_photo_path'] = national_card_photo_path

    def set_sex(self, sex):
        self.insert_driver['sex'] = sex

    def set_license_verification_date(self, license_verification_date):
        self.insert_driver['license_verification_date'] = license_verification_date

    def set_judicial_letter_path(self, judicial_letter_path):
        self.insert_driver['judicial_letter_path'] = judicial_letter_path

    def set_judicial_letter_verification_date(self, judicial_letter_verification_date):
        self.insert_driver['judicial_letter_verification_date'] = judicial_letter_verification_date

    def set_final_verification_date(self, final_verification_date):
        self.insert_driver['final_verification_date'] = final_verification_date

    def set_location(self, location):
        self.insert_driver['location'] = location

    def set_profile_picture_path(self, profile_picture_path):
        self.insert_driver['profile_picture_path'] = profile_picture_path

    def set_verifier_personnel_code(self, verifier_personnel_code):
        self.insert_driver['verifier_personnel_code'] = verifier_personnel_code
