import pathlib

# Define o caminho do arquivo
path = pathlib.Path("/etc/os-release")

# Dicionário para armazenar as informações
os_release = {}

# Lê o arquivo linha por linha
with open(path) as stream:
    for line in stream:
        # Remove espaços e quebras de linha
        line = line.strip()
        # Ignora linhas que não têm '='
        if "=" in line:
            key, value = line.split("=", 1)
            # Remove aspas, se houver
            os_release[key] = value.strip('"')

# Imprime todas as informações
from pprint import pprint
pprint(os_release)

# Imprime apenas o ID da distribuição Linux
print("ID da distribuição Linux:", os_release.get("ID"))