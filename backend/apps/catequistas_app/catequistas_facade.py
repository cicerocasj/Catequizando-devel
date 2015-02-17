# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from catequistas_app.catequistas_commands import ListCatequistasCommand, SaveCatequistasCommand, UpdateCatequistasCommand, CatequistasForm,\
    GetCatequistasCommand, DeleteCatequistasCommand


def save_catequistas_cmd(**catequistas_properties):
    """
    Command to save Catequistas entity
    :param catequistas_properties: a dict of properties to save on model
    :return: a Command that save Catequistas, validating and localizing properties received as strings
    """
    return SaveCatequistasCommand(**catequistas_properties)


def update_catequistas_cmd(catequistas_id, **catequistas_properties):
    """
    Command to update Catequistas entity with id equals 'catequistas_id'
    :param catequistas_properties: a dict of properties to update model
    :return: a Command that update Catequistas, validating and localizing properties received as strings
    """
    return UpdateCatequistasCommand(catequistas_id, **catequistas_properties)


def list_catequistass_cmd():
    """
    Command to list Catequistas entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCatequistasCommand()


def catequistas_form(**kwargs):
    """
    Function to get Catequistas's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CatequistasForm(**kwargs)


def get_catequistas_cmd(catequistas_id):
    """
    Find catequistas by her id
    :param catequistas_id: the catequistas id
    :return: Command
    """
    return GetCatequistasCommand(catequistas_id)



def delete_catequistas_cmd(catequistas_id):
    """
    Construct a command to delete a Catequistas
    :param catequistas_id: catequistas's id
    :return: Command
    """
    return DeleteCatequistasCommand(catequistas_id)

