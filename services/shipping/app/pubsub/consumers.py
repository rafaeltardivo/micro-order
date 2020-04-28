from marshmallow import Schema, fields


class Consumer:
    __instance = None

    @staticmethod
    def get_instance(connection):
        """Static access to Producer singleton.
        Args:
            connection (pika.BlockingConnection): BlockingConnection object.
        Returns:
            Consumer singleton.
        """

        if Consumer.__instance is None:
            Consumer(connection)
            return Consumer.__instance

    def __init__(self, connection):
        """Virtually private constructor for Producer singleton.
        Args:
            connection (pika.BlockingConnection): BlockingConnection object.
        """

        if Consumer.__instance is not None:
            raise TypeError("This class is a Singleton!")
        else:
            Consumer.__instance = self
            Consumer.__instance.connection = connection
            Consumer.__instance.order_create_schema = Schema.from_dict(
                {
                    'id': fields.Integer(),
                    'customer': fields.Integer()
                }
            )
            Consumer.__instance.customer_detail_schema = Schema.from_dict(
                {
                    'id': fields.Integer(),
                    'customer': fields.Nested(
                        Schema.from_dict(
                            {
                                'email': fields.Email(),
                                'address': fields.Str()
                            }
                        )
                    )
                }
            )
