from generate_random_number import gen_2digit_rand


class Trip:
    client_fname = str
    client_lname = str
    client_id = int
    request_time = int
    pickup_latitude = str
    pickup_longitude = int
    latitude = str
    longitude = int
    cost = str
    round_trip = str
    address_origin = dict
    address_destination = dict
    km = int
    time = int
    estimated_end_time = int

    def estimated_time(self):
        print('3')
        if int(gen_2digit_rand()) % 2 == 0:
            self.estimated_end_time = int(self.time) + 2
        else:
            self.estimated_end_time = int(self.time) - 2
