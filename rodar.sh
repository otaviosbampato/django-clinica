if [ ! -f ".venv/bin/activate" ]; then
    echo "Criando ambiente virtual..."
    rm -rf .venv
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Erro ao criar o ambiente virtual."
        echo "Você precisa instalar o pacote venv. Execute manualmente o comando abaixo e depois rode ./rodar.sh novamente:"
        echo "sudo apt install python3-venv"
        rm -rf .venv
        exit 1
    fi
fi

echo "Ativando ambiente virtual..."
source .venv/bin/activate

echo "Instalando dependências (Django, Psycopg2, Crispy Forms, Dotenv)..."
pip install --upgrade pip
pip install django psycopg2-binary django-crispy-forms crispy-bootstrap5 python-dotenv dj-database-url

cd clinica

echo "Conectando ao banco de dados externo no Render..."
sleep 2

echo "Executando as migrações do banco de dados..."
python manage.py makemigrations
python manage.py migrate || { echo "Falha na migração! Verifique se seu banco PostgreSQL está de pé e configurado."; exit 1; }

echo "Iniciando o servidor..."
python manage.py runserver
