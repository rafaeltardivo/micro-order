from marshmallow import Schema, fields


OrderProducerSchema = Schema.from_dict(
    {
        'id': fields.Integer(),
        'customer': fields.Integer()
    }
)






