from pyArango.collection import  *
from pyArango.graph import *
import pyArango.validation as VAL
import types

class Blocks(Collection):
    _validation = {
        'on_save': False,
        'on_set': False,
        'allow_foreign_fields': True # allow fields that are not part of the schema
    }

    _fields = {
        'hash': Field(validators=[VAL.NotNull()])
    }


class Addresses(Collection):
    _validation = {
        'on_save': False,
        'on_set': False,
        'allow_foreign_fields': True # allow fields that are not part of the schema
    }

    _fields = {
        'hash': Field(validators=[VAL.NotNull()])
    }


class Transaction(Edges):
    _validation = {
        'on_save': False,
        'on_set': False,
        'allow_foreign_fields': True # allow fields that are not part of the schema
    }

    _fields = {
        'hash': Field(validators=[VAL.NotNull()]),
        'amount': Field(validators=[VAL.NotNull()])
    }


class Blockchain(Graph):
    _edgeDefinitions = (EdgeDefinition("Transaction", fromCollections=["Addresses"], toCollections=["Addresses"]),)
    _orphanedCollections = []