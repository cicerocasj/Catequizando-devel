# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from catequistas_app import catequistas_facade
from routes.catequistass import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = catequistas_facade.list_catequistass_cmd()
    catequistass = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    catequistas_form = catequistas_facade.catequistas_form()

    def localize_catequistas(catequistas):
        catequistas_dct = catequistas_form.fill_with_model(catequistas)
        catequistas_dct['edit_path'] = router.to_path(edit_path, catequistas_dct['id'])
        catequistas_dct['delete_path'] = router.to_path(delete_path, catequistas_dct['id'])
        return catequistas_dct

    localized_catequistass = [localize_catequistas(catequistas) for catequistas in catequistass]
    context = {'catequistass': localized_catequistass,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'catequistass/catequistas_home.html')


def delete(catequistas_id):
    catequistas_facade.delete_catequistas_cmd(catequistas_id)()
    return RedirectResponse(router.to_path(index))

