# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from catequistas_app.catequistas_model import Catequistas
from routes.catequistass.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Catequistas.query().get())
        redirect_response = save(complemento='complemento_string', nome='nome_string', bairro='bairro_string', cidade='cidade_string', rua='rua_string', numero='numero_string', nascimento='1/7/2014', cpf='8', responsavel='responsavel_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_catequistas = Catequistas.query().get()
        self.assertIsNotNone(saved_catequistas)
        self.assertEquals('complemento_string', saved_catequistas.complemento)
        self.assertEquals('nome_string', saved_catequistas.nome)
        self.assertEquals('bairro_string', saved_catequistas.bairro)
        self.assertEquals('cidade_string', saved_catequistas.cidade)
        self.assertEquals('rua_string', saved_catequistas.rua)
        self.assertEquals('numero_string', saved_catequistas.numero)
        self.assertEquals(date(2014, 1, 7), saved_catequistas.nascimento)
        self.assertEquals(8, saved_catequistas.cpf)
        self.assertEquals('responsavel_string', saved_catequistas.responsavel)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['complemento', 'nome', 'bairro', 'cidade', 'rua', 'numero', 'nascimento', 'cpf', 'responsavel']), set(errors.keys()))
        self.assert_can_render(template_response)
