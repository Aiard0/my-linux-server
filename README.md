<h1 align="center"> My Linux Server </h1> <br>
<p align="center">
<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXBzZmlhYmdseHM3bXN6M3dzaDF6ajBncXB5MHA3bGpkOGN4eW9hbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0ICG4WxdKSRzE3K/giphy.webp">
 <p align="center">Elevando os níveis para não combater a preguiça...</p>
</p>

## Introdução
A intenção de criar esse repositório foi economizar tempo nas diversas reinstalações de sistema nos meus servidores. 

## Features:

- __Script Python automático chamado S.I.S (Server Installer Script)__
- __Instalação automática de pacotes predefinidos__
- __Instalão do repositório Docker e seus pacotes__
- __Configurações do NGINX predenifidas__
- __Arquivos__ ```docker-compose.yml``` __configurados para alguns projetos__

## Instalação:

> Apenas esses sistemas são suportados atualmente:
> - Rocky Linux 9

### 1. Instale o Python 3 na sua distribuição Linux

#### Rocky Linux
1. Atualize o repositório:
```bash
sudo dnf update -y
```
2. Instale o pacote python3:
```bash
sudo dnf install python3 -y
```

#### Debian e Ubuntu
Em breve...


#### Arch Linux
Em breve...

### 2. Utilize o repositório atual
1. Clone o repositório:
```
git clone https://github.com/Aiard0/my-linux-server.git
```
2. Entre na pasta do repositório:
```bash
cd my-linux-server/
```

### 3. Execute o S.I.S usando o Python

> Atenção: não utilize __sudo__ no comando abaixo, durante a instalação dos pacotes, será pedido a senha do usuário.

Execute o script com o comando:
```bash
python3 script.py
```

## Objetivos futuros:

### S.I.S Toolbox:
- Instalador das configurações do NGINX do repositório
- Criação de novas configurações para o NGINX
- Subir configurações do ```docker-compose.yml``` automaticamente

## Contato
> 📫 Se você está interessado em colaborar em projetos ou apenas quer bater um papo sobre programação, sinta-se à vontade para entrar em contato comigo!

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/abdonwerner/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdon-werner-454aa6299) [![Github](https://img.shields.io/badge/Github-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Aiard0) [![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/378889299250249728)
