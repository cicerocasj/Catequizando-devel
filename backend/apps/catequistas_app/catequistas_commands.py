# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from catequistas_app.catequistas_model import Catequistas



class CatequistasSaveForm(ModelForm):
    """
    Form used to save and update Catequistas
    """
    _model_class = Catequistas
    _include = [Catequistas.complemento, 
                Catequistas.nome, 
                Catequistas.bairro, 
                Catequistas.cidade, 
                Catequistas.rua, 
                Catequistas.numero, 
                Catequistas.nascimento, 
                Catequistas.cpf, 
                Catequistas.responsavel]


class CatequistasForm(ModelForm):
    """
    Form used to expose Catequistas's properties for list or json
    """
    _model_class = Catequistas


class GetCatequistasCommand(NodeSearch):
    _model_class = Catequistas


class DeleteCatequistasCommand(DeleteNode):
    _model_class = Catequistas


class SaveCatequistasCommand(SaveCommand):
    _model_form_class = CatequistasSaveForm


class UpdateCatequistasCommand(UpdateNode):
    _model_form_class = CatequistasSaveForm


class ListCatequistasCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCatequistasCommand, self).__init__(Catequistas.query_by_creation())

