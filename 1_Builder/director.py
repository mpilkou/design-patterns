from builder import Builder


class Director:
    _builder = None

    def __init__(self, builder: Builder):
        self._builder = builder

    def construct(self):
        self._builder.build_engine()
        self._builder.build_frame()
        self._builder.build_wheels()
        self._builder.build_doors()

        return self._builder.get_result()
