

class File:

    def __init__(self, name):
        self._name = name
        self._text = ""
        with open(self._name + ".txt", "w") as my_file:
            my_file.write(self._name + " text")

    def file_load(self):
        print("loading file: " + self._name)
        return 1

    def file_show(self):
        text = None
        with open(self._name + ".txt", "r") as my_file:
            text = my_file.read()
        print(text)
        return 2

    def __del__(self):
        import os
        try:
            os.remove(self._name + ".txt")
        except OSError:
            print("Error in remove")


class Proxy:
    def __init__(self, file):
        self._file = file
        self._stage = None


class ProxyFileLoader(Proxy):

    def file_show(self):
        if self._stage is None:
            self._stage = self._file.file_load()
            self._stage = self._file.file_show()
            self._stage is None
        return self._stage

    def __del__(self):
        del self._file
