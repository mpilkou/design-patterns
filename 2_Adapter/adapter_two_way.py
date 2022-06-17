

class SystemInt():
    def request_add_int(self, number_1):
        return number_1 + 1


class SystemString():
    def request_add_string(self, string_1):
        return string_1 + '1'


class Adapter(SystemInt, SystemString):

    def request_add_int(self, number_1):
        return int(
            super().request_add_int(int(number_1)))

    def request_add_string(self, string_1):
        return str(
            super().request_add_string(str(string_1)))
