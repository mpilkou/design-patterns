class System_Int():
    def request_add_int(self, number_1):
        return number_1 + 1

class System_String():
    def request_add_string(self, string_1):
        return string_1 + '1'

class Adapter(System_Int, System_String):

    def request_add_int(self, number_1):
        return int(
            super().request_add_int(int(number_1)))

    def request_add_string(self, string_1):
        return str(
            super().request_add_string(str(string_1)))

