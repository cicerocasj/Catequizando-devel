# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from catequistas_app import catequistas_facade


def index():
    cmd = catequistas_facade.list_catequistass_cmd()
    catequistas_list = cmd()
    catequistas_form = catequistas_facade.catequistas_form()
    catequistas_dcts = [catequistas_form.fill_with_model(m) for m in catequistas_list]
    return JsonResponse(catequistas_dcts)


def new(_resp, **catequistas_properties):
    cmd = catequistas_facade.save_catequistas_cmd(**catequistas_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **catequistas_properties):
    cmd = catequistas_facade.update_catequistas_cmd(id, **catequistas_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = catequistas_facade.delete_catequistas_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        catequistas = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    catequistas_form = catequistas_facade.catequistas_form()
    return JsonResponse(catequistas_form.fill_with_model(catequistas))

