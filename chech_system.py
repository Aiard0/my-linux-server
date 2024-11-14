import pathlib
import subprocess

erros = 0

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
        print(f"[INSTALADOR] Distribuição Linux: {system_name}")
        return "dnf"
    else:
        raise Exception("[INSTALADOR] A sua distribuição Linux não é suportada.")

# Função para instalar pacotes
def install_packages(packages):
    package_manager = detect_package_manager()
    print(f"[INSTALADOR] Gerenciador de pacotes: {package_manager.upper()}")
    print("[INSTALADOR] Atualizando o sistema e iniciando a instalação dos pacotes...")
    # Instala os pacotes normais
    for package in packages:
        try:
            print(f"[INSTALADOR] Instalando o pacote {package}...")
            if package_manager == "dnf":
                subprocess.run(["sudo", "dnf", "update", "-y"], check=True)
                subprocess.run(["sudo", "dnf", "install", "-y", package], check=True)
            elif package_manager == "apt":
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
            elif package_manager == "yum":
                subprocess.run(["sudo", "yum", "install", "-y", package], check=True)
            print(f"[INSTALADOR] O pacote {package} foi instalado com sucesso!")
        except subprocess.CalledProcessError:
            print(f"[INSTALADOR] O pacote {package} não foi instalado. Tente instalar manualmente.")
            erros += 1

def enable_services():
    print("[INSTALADOR] Ativando os serviços...")
    subprocess.run(["sudo", "systemctl", "enable", "--now", "cockpit.socket"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "--now", "nginx"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "--now", "mariadb-server"], check=True)
    print("[INSTALADOR] Serviços ativados com sucesso!")

# Run the installation function
if __name__ == "__main__":
    print("[INSTALADOR] Iniciando a instalação...")
    install_packages(packages)
    enable_services()
    if erros > 0:
        print(f"[INSTALADOR] Instalação concluida com {erros} erros. Verifique manualmente os pacotes que não foram instalados.")
    else:
        print("[INSTALADOR] Instalação concluida com sucesso!")