# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Catequistas(Node):
    nome = ndb.StringProperty(required=True)
    cpf = ndb.IntegerProperty(required=True)
    nascimento = ndb.DateProperty(required=True)
    responsavel = ndb.StringProperty(required=True)
    rua = ndb.StringProperty(required=True)
    numero = ndb.StringProperty(required=True)
    complemento = ndb.StringProperty(required=True)
    bairro = ndb.StringProperty(required=True)
    cidade = ndb.StringProperty(required=True)