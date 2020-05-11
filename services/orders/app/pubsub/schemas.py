from marshmallow import Schema, fields

shipping_update_schema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'order': fields.Integer(),
        'status': fields.Integer()
    }
)

order_create_schema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'customer': fields.Integer()
    }
)
