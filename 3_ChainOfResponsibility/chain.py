import abc


class HandleLevel:
    HTML = 1
    CONSOLE = 2
    ERROR = 3


class Message:
    def __init__(self, message_type: str):
        self.title = 'Message title'
        self.text = ['1. topic', '2. topic', '3. topic']
        self.message_type = message_type


class Handler(abc.ABC):

    def __init__(self):
        self.next_handler = None

    def handle(self, request: type(Message)):
        if self.message_type == request.message_type:
            self.output(request)
        else:
            self.next_handler.handle(request)

    @abc.abstractmethod
    def output(self, request: type(Message)):
        pass


class HTMLHandler(Handler):

    def __init__(self):
        self.message_type = HandleLevel.HTML

    def output(self, request: type(Message)):
        print('<html>')
        print('\t<head>')
        print('\t\t<title>{}</title>'.format(request.title))
        print('\t</head>')
        print('\t<body>')
        for item in request.text:
            print('\t\t<p>{}</p>'.format(item))
        print('\t</body>')
        print('</html>')


class ConsoleHandler(Handler):
    def __init__(self):
        self.message_type = HandleLevel.CONSOLE

    def output(self, request: type(Message)):
        print('{0} {1} {0}'.format('-'*3, request.title))
        for item in request.text:
            print(item)


class ErrorHandler(Handler):
    def __init__(self):
        self.message_type = HandleLevel.ERROR

    def output(self, request: type(Message)):
        print("Invalid request")


if __name__ == '__main__':
    report = Message(HandleLevel.CONSOLE)
    html_handler = HTMLHandler()
    console_handler = ConsoleHandler()

    html_handler.next_handler = console_handler
    console_handler.next_handler = ErrorHandler()
    html_handler.handle(report)
