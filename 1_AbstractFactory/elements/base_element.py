class HTMLElement():

    def __init__(self, parameters: str = ""):
        self.parameters = parameters

    def __str__(self) -> str:
        return f"<{self.tag}{self.parameters}>  </{self.tag}>"