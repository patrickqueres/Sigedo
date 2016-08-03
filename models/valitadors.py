# -*- coding: utf-8 -*-
# Author: Alzemand 


## Validadores de Aluno
Aluno.nome.requires = [IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'aluno.nome')]
Aluno.matricula.requires = [IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'aluno.matricula')]
Aluno.curso.requires = requires=IS_IN_SET(['Administração', 'Engenharia de Produção', 'Sistemas de Informação', 'Matemática'])
Aluno.periodo.requires = IS_NOT_EMPTY()
#= IS_EMPTY_OR(IS_IMAGE())

## Validadores de Empresa
Empresa.nome.requires = IS_NOT_EMPTY()
Empresa.razao.requires = [IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'empresa.razao')]
Empresa.cnpj.requires = [IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'empresa.cnpj')]
Empresa.telefone.requires = IS_NOT_EMPTY()

# Validadores de Estagio
#Estagio.empresa.requires = IS_IN_DB(db, 'empresa.cnpj', '%(nome)s', _and=IS_NOT_IN_DB(db,'estagio.empresa'))
Estagio.empresa.requires = IS_IN_DB(db, 'empresa.cnpj', '%(nome)s')
Estagio.aluno.requires = IS_IN_DB(db, 'aluno.matricula', '%(nome)s')



### Validadores de Estoque
#ItemsEstoque.filme.requires = IS_IN_DB(db, 'filmes.id', '%(titulo)s', _and=IS_NOT_IN_DB(db, 'items_estoque.filme'))

### Validadores de Locação
#Locacao.filmes.requires = IS_IN_DB(db, 'filmes.id', '%(titulo)s')
#Locacao.cliente.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s')
#Locacao.data_locacao.requires = IS_DATETIME(format='%d/%m/%Y')
#Locacao.data_devolucao.requires = IS_DATETIME(format='%d/%m/%Y')
