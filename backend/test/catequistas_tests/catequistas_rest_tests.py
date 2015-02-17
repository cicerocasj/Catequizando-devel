# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from catequistas_app.catequistas_model import Catequistas
from routes.catequistass import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Catequistas)
        mommy.save_one(Catequistas)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        catequistas_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'complemento', 'nome', 'bairro', 'cidade', 'rua', 'numero', 'nascimento', 'cpf', 'responsavel']), set(catequistas_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Catequistas.query().get())
        json_response = rest.new(None, complemento='complemento_string', nome='nome_string', bairro='bairro_string', cidade='cidade_string', rua='rua_string', numero='numero_string', nascimento='1/7/2014', cpf='8', responsavel='responsavel_string')
        db_catequistas = Catequistas.query().get()
        self.assertIsNotNone(db_catequistas)
        self.assertEquals('complemento_string', db_catequistas.complemento)
        self.assertEquals('nome_string', db_catequistas.nome)
        self.assertEquals('bairro_string', db_catequistas.bairro)
        self.assertEquals('cidade_string', db_catequistas.cidade)
        self.assertEquals('rua_string', db_catequistas.rua)
        self.assertEquals('numero_string', db_catequistas.numero)
        self.assertEquals(date(2014, 1, 7), db_catequistas.nascimento)
        self.assertEquals(8, db_catequistas.cpf)
        self.assertEquals('responsavel_string', db_catequistas.responsavel)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['complemento', 'nome', 'bairro', 'cidade', 'rua', 'numero', 'nascimento', 'cpf', 'responsavel']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        catequistas = mommy.save_one(Catequistas)
        old_properties = catequistas.to_dict()
        json_response = rest.edit(None, catequistas.key.id(), complemento='complemento_string', nome='nome_string', bairro='bairro_string', cidade='cidade_string', rua='rua_string', numero='numero_string', nascimento='1/7/2014', cpf='8', responsavel='responsavel_string')
        db_catequistas = catequistas.key.get()
        self.assertEquals('complemento_string', db_catequistas.complemento)
        self.assertEquals('nome_string', db_catequistas.nome)
        self.assertEquals('bairro_string', db_catequistas.bairro)
        self.assertEquals('cidade_string', db_catequistas.cidade)
        self.assertEquals('rua_string', db_catequistas.rua)
        self.assertEquals('numero_string', db_catequistas.numero)
        self.assertEquals(date(2014, 1, 7), db_catequistas.nascimento)
        self.assertEquals(8, db_catequistas.cpf)
        self.assertEquals('responsavel_string', db_catequistas.responsavel)
        self.assertNotEqual(old_properties, db_catequistas.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        catequistas = mommy.save_one(Catequistas)
        old_properties = catequistas.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, catequistas.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['complemento', 'nome', 'bairro', 'cidade', 'rua', 'numero', 'nascimento', 'cpf', 'responsavel']), set(errors.keys()))
        self.assertEqual(old_properties, catequistas.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        catequistas = mommy.save_one(Catequistas)
        rest.delete(None, catequistas.key.id())
        self.assertIsNone(catequistas.key.get())

    def test_non_catequistas_deletion(self):
        non_catequistas = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_catequistas.key.id())
        self.assertIsNotNone(non_catequistas.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

