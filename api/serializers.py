from datetime import date
from marshmallow import Schema, fields

# Serializador de Notas
class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)
