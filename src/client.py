class Client:
    client_id = int
    phone_nuber = str
    wallet_balance = int
    first_name = str
    last_name = str
    birth_date = int
    sex = str
    email = str
    request_time = int
    pickup = []
    dropoff = []

    def set_id(self, client_id):
        self.client_id = client_id

    def set_phone_number(self, phone_number):
        self.phone_nuber = phone_number

    def set_wallet_balance(self, wallet_balance):
        self.phone_nuber = wallet_balance

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birth_date(self, birth_date):
        self.phone_nuber = birth_date

    def set_sex(self, sex):
        self.phone_nuber = sex

    def set_email(self, email):
        self.phone_nuber = email

    def set_request_time(self, request_time):
        self.request_time = request_time

    def set_pickup(self, value):
        self.pickup.append(value)

    def set_dropoff(self, value):
        self.dropoff.append(value)

    def get_client_id(self):
        return self.client_id

    def get_phone_nuber(self):
        return self.phone_nuber

    def get_wallet_balance(self):
        return self.wallet_balance

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_date(self):
        return self.birth_date

    def get_sex(self):
        return self.sex

    def get_email(self):
        return self.email

    def get_request_time(self):
        return self.request_time

    def get_pickup(self):
        return self.pickup

    def get_dropoff(self):
        return self.dropoff
