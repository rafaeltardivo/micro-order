import pika


class Consumer:
    __instance = None

    @staticmethod 
    def get_instance(connection):
        """Static access method."""

        if Consumer.__instance == None:
            Consumer(connection)
            return Consumer.__instance

    def __init__(self, connection):
        """Virtually private constructor."""

        if Consumer.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            Consumer.__instance = self
            Consumer.__instance.connection = connection
