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

if __name__ == '__main__':
    conexao = criarConexaoInicial('localhost', 'root', 'admin')

    criarBancoDados(conexao, 'escola')

    cursor = conexao.cursor()

    cursor.execute("""
    SHOW DATABASES;
    """)

    for database in cursor:
        print(database)

    cursor.close()

    campos_alunos = [
            "id INT AUTO_INCREMENT PRIMARY KEY",
            "nome VARCHAR(100)",
            "idade INT",
            "curso VARCHAR(50)"
        ]

        # Criar tabela 'alunos'
    criarTabela(conexao, 'alunos', campos_alunos, "escola")

    print(listarTabelas(conexao))

    campos_professores = [
            "id INT AUTO_INCREMENT PRIMARY KEY",
            "nome VARCHAR(100)",
            "disciplina VARCHAR(50)"
        ]

    # Criar tabela 'professores' no banco de dados 'seu_banco_de_dados'
    criarTabela(conexao, 'professores', campos_professores, 'escola')

    print(listarTabelas(conexao))

    sql_insert = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"
    dados_aluno = ("João", 20, "Matemática")
    insertNoBancoDados(conexao, sql_insert, dados_aluno)

    sql_select = "SELECT * FROM alunos"
    alunos = listarBancoDados(conexao, sql_select)
    for aluno in alunos:
        print(aluno)

    sql_update = "UPDATE alunos SET idade = %s WHERE nome = %s"
    dados_update = (21, "João")
    linhas_afetadas = atualizarBancoDados(conexao, sql_update, dados_update)
    print(f"{linhas_afetadas} linhas foram atualizadas.")

    sql_delete = "DELETE FROM alunos WHERE nome = %s"
    dados_delete = ("João",)
    linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
    print(f"{linhas_afetadas} linhas foram excluídas.")