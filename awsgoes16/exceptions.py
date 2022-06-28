class Error(Exception):
    pass


class ValueNotProvidedError(Error):
    def __init__(self, message):
        print(f'Error: {message}')


class NotFoundError(Error):
    def __init__(self, message):
        print(f'Error: {message}')
