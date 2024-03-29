# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    context = {}
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas.html')