# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from catequistas_app.catequistas_model import Catequistas
from routes.catequistass.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        catequistas = mommy.save_one(Catequistas)
        template_response = index(catequistas.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        catequistas = mommy.save_one(Catequistas)
        old_properties = catequistas.to_dict()
        redirect_response = save(catequistas.key.id(), complemento='complemento_string', nome='nome_string', bairro='bairro_string', cidade='cidade_string', rua='rua_string', numero='numero_string', nascimento='1/7/2014', cpf='8', responsavel='responsavel_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_catequistas = catequistas.key.get()
        self.assertEquals('complemento_string', edited_catequistas.complemento)
        self.assertEquals('nome_string', edited_catequistas.nome)
        self.assertEquals('bairro_string', edited_catequistas.bairro)
        self.assertEquals('cidade_string', edited_catequistas.cidade)
        self.assertEquals('rua_string', edited_catequistas.rua)
        self.assertEquals('numero_string', edited_catequistas.numero)
        self.assertEquals(date(2014, 1, 7), edited_catequistas.nascimento)
        self.assertEquals(8, edited_catequistas.cpf)
        self.assertEquals('responsavel_string', edited_catequistas.responsavel)
        self.assertNotEqual(old_properties, edited_catequistas.to_dict())

    def test_error(self):
        catequistas = mommy.save_one(Catequistas)
        old_properties = catequistas.to_dict()
        template_response = save(catequistas.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['complemento', 'nome', 'bairro', 'cidade', 'rua', 'numero', 'nascimento', 'cpf', 'responsavel']), set(errors.keys()))
        self.assertEqual(old_properties, catequistas.key.get().to_dict())
        self.assert_can_render(template_response)
