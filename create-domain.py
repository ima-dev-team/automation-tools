import sys
import pexpect

# Verifica se o domínio foi fornecido como argumento
if len(sys.argv) < 2:
    print("É necessário fornecer o nome do subdomínio como argumento.")
    sys.exit(1)

# Configurações do servidor Axigen
host = "172.18.120.25"
port = 7000

# Informações de autenticação
login = "admin"
password = "IM@54321#"

# Nome do subdomínio fornecido como argumento
subdomain_name = sys.argv[1]

# Nome completo do domínio
domain_name = f"{subdomain_name}"

# Comandos para criar o domínio
commands = [
    f"user {login}",
    f"{password}",
    f"create domain name {domain_name} domainlocation /var/opt/axigen/domains/{domain_name} postmasterpassword secret_password",
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
