from marshmallow import Schema, fields

order_create_schema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'customer': fields.Integer()
    }
)
customer_detail_schema = Schema.from_dict(
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

customer_request_schema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'customer': fields.Integer()
    }
)

shipping_update_schema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'order': fields.Integer(),
        'status': fields.Integer()
    }
)
