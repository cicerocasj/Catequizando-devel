# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    lista = {'pessoa': [1, 13], 'eu': {'voce': 'natalia', 'sim': 'sim mesmo'}}
    return TemplateResponse(lista, template_path='/turmas.html')