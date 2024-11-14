# Version 1.0.0

import pathlib
import subprocess

erros = 0

TGREEN =  '\033[32m' # Green Text
print (TGREEN + "This is some green text!")

# List of packages to install
packages = [
    "git",
    "nano",
    "cockpit",
    "nginx",
    "mariadb-server",
    "epel-release",
    "certbot",
    "python3-certbot-nginx",
]

docker_packages = [
    "docker-ce", 
    "docker-ce-cli", 
    "containerd.io", 
    "docker-compose-plugin",
]

docker_dnf_repo = "https://download.docker.com/linux/rhel/docker-ce.repo"

def detect_os_release(id):
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

    # Imprime apenas o ID da distribuição Linux
    if id == "ID":
        return os_release.get("ID")
    if id == "PRETTY_NAME":
        return os_release.get("PRETTY_NAME")

# Detect the package manager based on the Linux distribution
def detect_package_manager():
    system_os = detect_os_release("ID")
    system_name = detect_os_release("PRETTY_NAME")
    if system_os == "rocky":
        print(TGREEN + f"[S.I.S - Server Installer Script] Distribuição Linux: {system_name}")
        return "dnf"
    else:
        raise Exception(TGREEN + f"[S.I.S - Server Installer Script] A sua distribuição Linux não é suportada.")

# Função para instalar pacotes
def install_packages(packages):
    package_manager = detect_package_manager()
    print(TGREEN + f"[S.I.S - Server Installer Script] Gerenciador de pacotes: {package_manager.upper()}")
    global docker_choice
    docker_choice = input("[S.I.S - Server Installer Script] Deseja instalar o Docker além dos pacotes principais? (s/n): ")
    print(TGREEN + f"[S.I.S - Server Installer Script] Atualizando o sistema e iniciando a instalação dos pacotes principais...")
# Instala os pacotes normais
    for package in packages:
        try:
            print(TGREEN + f"[S.I.S - Server Installer Script] Instalando o pacote {package}...")
            if package_manager == "dnf":
                subprocess.run(["sudo", "dnf", "update", "-y"], check=True)
                subprocess.run(["sudo", "dnf", "install", "-y", package], check=True)
            elif package_manager == "apt":
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
            elif package_manager == "yum":
                subprocess.run(["sudo", "yum", "install", "-y", package], check=True)
            print(TGREEN + f"[S.I.S - Server Installer Script] O pacote {package} foi instalado com sucesso!")
        except subprocess.CalledProcessError:
            print(TGREEN + f"[S.I.S - Server Installer Script] O pacote {package} não foi instalado. Tente instalar manualmente.")
            erros += 1
# Parte do Docker
    if docker_choice == "s" or docker_choice == "S":
        # Adiciona o repositório do Docker
        print(TGREEN + F"[S.I.S - Server Installer Script] Adicionando o repositório do Docker...")
        if package_manager == "dnf":
            subprocess.run(["sudo", "dnf", "config-manager", "--add-repo", docker_dnf_repo], check=True)
            subprocess.run(["sudo", "dnf", "update", "-y"], check=True)
        elif package_manager == "apt":
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
        elif package_manager == "yum":
            subprocess.run(["sudo", "yum", "install", "-y", package], check=True)
        # Instala os pacotes do Docker
        print(TGREEN + f"[S.I.S - Server Installer Script] Instalando o Docker...")
        for package in docker_packages:
            try:
                if package_manager == "dnf":
                    subprocess.run(["sudo", "dnf", "update", "-y"], check=True)
                    subprocess.run(["sudo", "dnf", "install", "-y", package], check=True)
                elif package_manager == "apt":
                    subprocess.run(["sudo", "apt", "update"], check=True)
                    subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                elif package_manager == "yum":
                    subprocess.run(["sudo", "yum", "install", "-y", package], check=True)
                print(TGREEN + f"[S.I.S - Server Installer Script] O pacotes do Docker ({package}) foi instalado com sucesso!")
            except subprocess.CalledProcessError:
                print(TGREEN + f"[S.I.S - Server Installer Script] O pacote do Docker ({package}) não foi instalado. Tente instalar manualmente.")
                erros += 1

def enable_services():
    print(TGREEN + f"[S.I.S - Server Installer Script] Ativando os serviços...")
    subprocess.run(["sudo", "systemctl", "enable", "--now", "cockpit.socket"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "--now", "nginx"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "--now", "mariadb"], check=True)
    if docker_choice == "s" or docker_choice == "S":
        subprocess.run(["sudo", "systemctl", "enable", "--now", "docker"], check=True)
    print(TGREEN + f"[S.I.S - Server Installer Script] Serviços ativados com sucesso!")

# Run the installation function
if __name__ == "__main__":
    print(TGREEN + f"[S.I.S - Server Installer Script] Iniciando a instalação...")
    install_packages(packages)
    enable_services()
    if erros > 0:
        print(TGREEN + f"[S.I.S - Server Installer Script] Instalação concluida com {erros} erros. Verifique manualmente os pacotes que não foram instalados.")
    else:
        print(TGREEN + f"[S.I.S - Server Installer Script] Instalação concluida com sucesso!")