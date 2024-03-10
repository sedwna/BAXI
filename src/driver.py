class Driver:
    driver_id = int
    phone_number = str
    wallet_balance = int
    first_name = str
    last_name = str
    birth_date = int
    sex = str
    request_time = int
    pickup = []
    shaba = str


    def set_id(self, driver_id):
        self.driver_id = driver_id

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_wallet_balance(self, wallet_balance):
        self.wallet_balance = wallet_balance

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_sex(self, sex):
        self.sex = sex

    def set_request_time(self, request_time):
        self.request_time = request_time

    def set_pickup(self, value):
        self.pickup.append(value)

    def set_shaba(self, shaba):
        self.shaba = shaba

    def get_driver_id(self):
        return self.driver_id

    def get_phone_number(self):
        return self.phone_number

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

    def get_request_time(self):
        return self.request_time

    def get_pickup(self):
        return self.pickup

    def get_shaba(self):
        return self.shaba
