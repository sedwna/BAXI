import secrets
import string


class GenerateRandom:
    password_code = 0
    referral_code = 0
    tracking_code = 0

    def gen_password_code_rand(self):
        # letters = string.ascii_letters

        digits = string.digits

        # special_chars = string.punctuation

        selection_list = digits

        password_len = 4

        password = ''
        for i in range(password_len):
            password += ''.join(secrets.choice(selection_list))

        self.password_code = password
        print('password: ', password)

    def gen_referral_code_rand(self):
        # letters = string.ascii_letters

        digits = string.digits

        # special_chars = string.punctuation

        selection_list = digits

        referral_code_len = 8

        referral_code = ''
        for i in range(referral_code_len):
            referral_code += ''.join(secrets.choice(selection_list))

        self.referral_code = referral_code
        print("rc", type(referral_code))
        print('referral_code: ', referral_code)
        print(type(referral_code))

    def gen_tracking_code_rand(self):

        # letters = string.ascii_letters

        digits = string.digits

        # special_chars = string.punctuation

        selection_list = digits

        tracking_code_len = 15

        tracking_code = ''
        for i in range(tracking_code_len):
            tracking_code += ''.join(secrets.choice(selection_list))

        self.tracking_code = tracking_code
        print('tracking_code: ', tracking_code)
