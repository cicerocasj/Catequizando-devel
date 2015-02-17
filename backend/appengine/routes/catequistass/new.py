# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from catequistas_app import catequistas_facade
from routes import catequistass
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'catequistass/catequistas_form.html')


def save(**catequistas_properties):
    cmd = catequistas_facade.save_catequistas_cmd(**catequistas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catequistas': catequistas_properties}

        return TemplateResponse(context, 'catequistass/catequistas_form.html')
    return RedirectResponse(router.to_path(catequistass))

