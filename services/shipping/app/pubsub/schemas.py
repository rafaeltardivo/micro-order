from marshmallow import Schema, fields


OrderConsumerSchema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'customer': fields.Integer()
    }
)

ShippingProducerSchema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'customer': fields.Integer()
    }
)
