# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

# ADD

# http://localhost:8000/Sigedo/default/aluno

def aluno():
    form = SQLFORM(Aluno)
    if form.process().accepted:
        session.flash = 'Novo Aluno cadastrado: %s' % form.vars.nome
        redirect(URL('aluno'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)
    
# http://localhost:8000/Sigedo/default/empresa

def empresa():
    form = SQLFORM(Empresa)
    if form.process().accepted:
        session.flash = 'Nova empresa cadastrada: %s' % form.vars.nome
        redirect(URL('empresa'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# http://localhost:8000/Sigedo/default/estagio

# @auth.requires_login()
# @auth.requires_membership('funcionario')
def estagio():
    form = SQLFORM(Estagio)
    if form.process().accepted:
        response.flash = 'Novo estagio cadastrado: %s' % form.vars.titulo
        redirect(URL('estagio'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = ''
    return dict(form=form)

# READ
    
# http://localhost:8000/Sigedo/default/ver_aluno
    
'''def ver_aluno():
    aluno = db(Aluno).select()
    return dict(aluno=aluno)
----------------------------------------------
ver_aluno?aluno=Edilson

def ver_aluno():
    if request.vars.aluno:
         aluno = db(Aluno.titulo.like('%'+request.vars.aluno+'%')).select()
    else:
        aluno = db(Aluno).select()
    return dict(aluno=aluno)'''

# http://localhost:8000/Sigedo/default/ver_aluno?keywords=

#@auth.requires_membership('funcionario')
def ver_aluno():
    grid = SQLFORM.grid(Aluno)
    return dict(grid=grid)


# http://localhost:8000/Sigedo/default/editar_aluno/1
# Passagem de argumentos

#@auth.requires_membership('funcionario')
def editar_aluno():
    form = SQLFORM(Aluno, request.args(0, cast=int), showid = False) 
    if form.process().accepted:
        session.flash = 'Aluno atualizado: %s' % form.vars.nome
        redirect(URL('ver_aluno'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        response.flash = 'Preencha o formulário!'
    return dict(form=form)

#@auth.requires_membership('funcionario')
def deletar_aluno():
    db(Aluno.id==request.args(0, cast=int)).delete()
    session.flash = 'Aluno excluido'
    redirect(URL('ver_aluno'))

