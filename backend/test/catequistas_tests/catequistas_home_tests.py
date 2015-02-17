# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from catequistas_app.catequistas_model import Catequistas
from routes.catequistass.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Catequistas)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        catequistas = mommy.save_one(Catequistas)
        redirect_response = delete(catequistas.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(catequistas.key.get())

    def test_non_catequistas_deletion(self):
        non_catequistas = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_catequistas.key.id())
        self.assertIsNotNone(non_catequistas.key.get())

