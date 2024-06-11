import mysql.connector

# Função para iniciar conexão com o mysql
def criarConexaoInicial(endereco, usuario, senha):
    return mysql.connector.connect(
        host=endereco,
        user=usuario,
        password=senha
    )

# Função para finalizar conexão com o mysql
def encerrarBancoDados(connection):
    connection.close()


# Funçaõ para criar o banco de dados
def criarBancoDados(connection, nome_bd):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % (nome_bd))
    cursor.close()

# função para criar a tabela
def criarTabela(connection, nome_tabela, campos, nome_banco_dados):
    cursor = connection.cursor()
    cursor.execute("USE %s" % (nome_banco_dados))
    sql = "CREATE TABLE IF NOT EXISTS %s (%s)" % (nome_tabela, ', '.join(campos))
    cursor.execute(sql)
    cursor.close()
    print("Tabela '%s' criada ou já existente." % (nome_tabela))

# Função para listar as tabelas
def listarTabelas(connection):
    cursor = connection.cursor()    
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    cursor.close()
    return tabelas

# Função para inserir dados na tabela
def insertNoBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

# Função para listar dados da tabela
def listarBancoDados(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results

# Função para atualizar dados na tabela
def atualizarBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas

# Função para excluir dados da tabela
def excluirBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados) 
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas
