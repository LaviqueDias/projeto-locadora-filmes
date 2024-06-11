import mysql.connector
from operacoesbd import *

conexao = criarConexaoInicial('localhost', 'root', 'admin')

criarBancoDados(conexao, 'locadora')

cursor = conexao.cursor()

cursor.close()

campos_filmes = [
        "codigo int auto_increment primary key",
        "nome varchar(100)",
        "autor varchar(100)",
        "diretor varchar(100)",
        "categoria varchar(100)"
    ]

# Criar tabela 'alunos'
criarTabela(conexao, 'filmes', campos_filmes, "locadora")

opcao = 1

while opcao != 6:
    print('\n=====LOCADORA=====')
    print("1. Listar filmes")
    print("2. Listar por tipo")
    print("3. Pesquisar")
    print("4. Inserir")
    print('5. Deletar filme pelo código')
    print("6. Sair")

    opcao = int(input('\nDigite uma opção: '))

    if opcao == 1: # Listar filmes
        sql_select = 'select * from filmes'

        filmes = listarBancoDados(conexao, sql_select)

        print('\nLista de Filmes: ')
        for filme in filmes:
            print('\nCódigo: %d\nNome: %s\nAutor: %s\nDiretor: %s\nCategoria: %s\n' % (filme[0], filme[1], filme[2], filme[3], filme[4]))

    elif opcao == 2:
        categoria = input('Digite a categoria que deseja listar: ')

        sql_select = 'select * from filmes where categoria = \'%s\'' % (categoria.lower())

        filmes = listarBancoDados(conexao, sql_select)

        print('\nLista de filmes da categoria %s' % (categoria))
        for filme in filmes:
            print('\nCódigo: %d\nNome: %s\nAutor: %s\nDiretor: %s\nCategoria: %s\n' % (filme[0], filme[1], filme[2], filme[3], filme[4]))
            

    elif opcao == 3:
        codigo = int(input('\nDigite o código do filme: '))

        sql_select = 'select * from filmes where codigo = %d' % (codigo)

        filmes = listarBancoDados(conexao, sql_select)

        if len(filmes) != 0:
            print('\nFilme do código %d encontrado!' % (codigo))
            for filme in filmes:
                print('\nCódigo: %d\nNome: %s\nAutor: %s\nDiretor: %s\nCategoria: %s\n' % (filme[0], filme[1], filme[2], filme[3], filme[4]))
        else:
            print('\nFilme não encontrado!')
    
    elif opcao == 4: # Inserir
        nome = input('Digite o nome do filme: ')
        autor = input('Digite o autor do filme: ')
        diretor = input('Digite o diretor do filme: ')
        categoria = input('Digite a categoria do filme: ')
        dados_filme = (nome, autor, diretor, categoria.lower())

        sql_insert = 'insert into filmes (nome, autor, diretor, categoria) values (%s, %s, %s, %s)'
        insertNoBancoDados(conexao, sql_insert, dados_filme)

    elif opcao == 5: 
        codigo = int(input('Digite o código do filme a ser deletado: '))

        sql_delete = 'delete from filmes where codigo = %s'
        dados_delete = (codigo,)
        linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
        print("%s linhas foram excluídas." % (linhas_afetadas))



    elif opcao != 6:
        print('\nOpção Inválida')



print('\nObrigado por usar a locadora!')
encerrarBancoDados(conexao)

