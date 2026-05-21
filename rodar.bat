@echo off
echo 🚀 Iniciando configuracao do projeto Clinica Django...

if not exist ".venv\Scripts\activate" (
    echo Criando ambiente virtual...
    if exist ".venv" (
        rmdir /s /q .venv
    )
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo Erro ao criar o ambiente virtual.
        echo Verifique se o Python e o venv estao instalados e no PATH.
        exit /b 1
    )
)

echo Ativando ambiente virtual...
call .venv\Scripts\activate

echo Instalando dependencias (Django, Psycopg2, Crispy Forms, Dotenv)...
pip install --upgrade pip
pip install -r requirements.txt

cd clinica

echo Conectando ao banco de dados externo no Render...
timeout /t 2 /nobreak > nul

echo Executando as migracoes do banco de dados...
python manage.py makemigrations
python manage.py migrate
if %errorlevel% neq 0 (
    echo Falha na migracao! Verifique se seu banco PostgreSQL esta de pe e configurado.
    exit /b 1
)

echo Iniciando o servidor...
python manage.py runserver
