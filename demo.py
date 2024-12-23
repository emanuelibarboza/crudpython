import pypyodbc as odbc

# Configurações de conexão
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'  # Use o driver correto
SERVER_NAME = 'DESKTOP-0K3LN2A\\SQLEXPRESS'   # Nome da instância do SQL Server
DATABASE_NAME = 'cadastros'                        # Nome do banco de dados

# String de conexão corrigida
connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
"""

# Estabelecer a conexão
try:
    conn = odbc.connect(connection_string)
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
    exit()

# Funções para operações no banco de dados

def inserir_usuario(nome, email, senha, data_nascimento):
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO Usuarios (Nome, Email, Senha, DataNascimento)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (nome, email, senha, data_nascimento))
        conn.commit()
        print("Usuário inserido com sucesso!")
    except Exception as e:
        print("Erro ao inserir usuário:", e)
    finally:
        cursor.close()

def listar_usuarios():
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Usuarios"
        cursor.execute(query)
        usuarios = cursor.fetchall()
        print("Lista de usuários:")
        for usuario in usuarios:
            print(usuario)
    except Exception as e:
        print("Erro ao listar usuários:", e)
    finally:
        cursor.close()

def atualizar_usuario(usuario_id, nome, email, senha, data_nascimento):
    try:
        cursor = conn.cursor()
        query = """
        UPDATE Usuarios
        SET Nome = ?, Email = ?, Senha = ?, DataNascimento = ?
        WHERE UsuarioID = ?
        """
        cursor.execute(query, (nome, email, senha, data_nascimento, usuario_id))
        conn.commit()
        print("Usuário atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar usuário:", e)
    finally:
        cursor.close()

def deletar_usuario(usuario_id):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM Usuarios WHERE UsuarioID = ?"
        cursor.execute(query, (usuario_id,))
        conn.commit()
        print("Usuário deletado com sucesso!")
    except Exception as e:
        print("Erro ao deletar usuário:", e)
    finally:
        cursor.close()

# Exemplo de uso
if __name__ == "__main__":
    # Inserir um novo usuário
    inserir_usuario(
        nome="Luciani",
        email="luciani@example.com",
        senha="luciani",
        data_nascimento="1974-12-10"
    )

    # Listar todos os usuários
    listar_usuarios()

    # Atualizar um usuário
    atualizar_usuario(
        usuario_id=1,
        nome="luciani barboza",
        email="lucianibarboza@novoemail.com",
        senha="luci",
        data_nascimento="1967-07-19"
    )

    # Listar novamente para confirmar a atualização
    listar_usuarios()

    # Deletar um usuário
    deletar_usuario(usuario_id=16)

    # Listar novamente para confirmar a exclusão
    listar_usuarios()

    # Encerrar a conexão
    conn.close()
    print("Conexão encerrada.")