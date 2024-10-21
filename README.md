# POBRE

Plataforma financeira para controle de gastos pessoais.

## Requisitos

- Python 3.12.7
- Django 5.1.2

## Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/mateusroerig/pobre.git
    cd pobre
    ```

2. **Crie um ambiente virtual**:

    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```

3. **Instale as dependências**:

    ```bash
    pip install django mysqlclient python-dotenv
    ```

## Configuração

1. **Crie um arquivo `.env` utilizando o `.env.example` como base**:

    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

    ```properties
    DATABASE_USER=usuario_do_banco
    DATABASE_PASSWORD=senha_do_banco
    ```

2. **Crie as migrações e banco de dados**:

    Execute o comando para criar o banco de dados e aplicar as migrações iniciais:

    ```bash
    python manage.py migrate
    ```

3. **Crie um superusuário** (para poder acessar a área administrativa e testar o login):

    ```bash
    python manage.py createsuperuser
    ```

    Siga as instruções para criar o usuário administrador.

## Executando o Servidor

Para iniciar o servidor de desenvolvimento, execute:

```bash
python manage.py runserver
```
