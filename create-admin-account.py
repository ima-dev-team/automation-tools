import sys
import pexpect

# Configurações do servidor Axigen
host = "172.18.120.25"  # Substitua pelo IP do seu servidor Axigen
port = 7000

# Verifica se o nome do novo usuário administrador e a senha foram fornecidos como argumentos
if len(sys.argv) < 3:
    print("É necessário fornecer o nome do novo usuário administrador e a senha como argumentos.")
    sys.exit(1)

# Informações de autenticação
login = "admin"
password = "IM@54321#"

# Nome do novo usuário administrador e senha fornecidos como argumentos
new_admin_user = sys.argv[1]
new_admin_user_password = sys.argv[2]

# Comandos para criar o usuário administrador
commands = [
    f"user {login}",
    f"{password}",
    "enter aacl",
    f"add admin-user name {new_admin_user} password {new_admin_user_password}",
    "quit",
    "commit",
    "quit"
]

# Conexão com o servidor Axigen
tn = pexpect.spawn(f"telnet {host} {port}")
tn.expect([b"Escape character is", pexpect.TIMEOUT], timeout=10)
tn.sendline()

# Envia os comandos
for command in commands:
    tn.expect([b"<login>", b"<password>", b"<#>", pexpect.TIMEOUT], timeout=10)
    tn.sendline(command)

# Fecha a conexão
tn.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=10)
tn.close()
