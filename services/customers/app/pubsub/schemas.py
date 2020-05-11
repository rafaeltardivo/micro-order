from marshmallow import Schema, fields

customer_detail_schema = Schema.from_dict(
    {
        'email': fields.Email(),
        'address': fields.Str()
    }
)

customer_shipping_schema = Schema.from_dict(
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
