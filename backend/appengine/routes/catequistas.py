# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property

#
# class Catequista(Node):
#     nome = ndb.StringProperty(required=True)
#
#
# def salvar(nome, **outras_propriedades):
#     catequista = Catequista(nome=nome)
#     catequista.put()


@login_not_required
@no_csrf
def index():
    context = {}
    return TemplateResponse(context, template_path='/catequistas.html')