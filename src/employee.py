class Employee:
    first_name = str
    last_name = str

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
