class Vehicle:

    def __init__(self, name: str):
        self.name = name
        self.frame = None
        self.engine = None
        self.wheels = None
        self.doors = None

    def print(self):
        print("__{4}__\n frame:{0} \
                \n engine:{1} \n wheels:{2} \n doors:{3} \n".format(
                    self.frame, self.engine,
                    self.wheels, self.doors, self.name))

    def get(self):
        return {
            "name": self.name,
            "frame": self.frame,
            "engine": self.engine,
            "wheels": self.wheels,
            "doors": self.doors
        }
