import secrets
import string


class GenerateRandom4Digit:
    rand_number = 0000

    def gen_rand(self):
        # letters = string.ascii_letters

        digits = string.digits

        # special_chars = string.punctuation

        selection_list = digits

        password_len = 4

        password = ''
        for i in range(password_len):
            password += ''.join(secrets.choice(selection_list))

        self.rand_number = password
        print(password)
