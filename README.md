# 🏥 Sistema de Reservas — Clínica+

Aplicação web desenvolvida com **Django** para gerenciamento de consultas médicas. Permite que pacientes agendem consultas e que administradores gerenciem médicos, especialidades e agendamentos.

---

## 📋 Funcionalidades

- **Área do Paciente** (login/senha): cadastro, login, agendamento e cancelamento de consultas, visualização do histórico e perfil.
- **Painel Administrativo** (Jazzmin): gestão completa de médicos, pacientes, especialidades e consultas com filtros, buscas e inlines.
- **Interface responsiva** com Bootstrap 5.
- **Banco de dados** PostgreSQL.
- **Containerização** com Docker.

---

## 🗂️ Estrutura do Projeto

```
django-clinica/
├── clinica/                  # Projeto Django
│   ├── core/                 # Configurações (settings, urls, wsgi)
│   ├── medical/              # App principal
│   │   ├── models.py         # Modelos: Especialidade, Medico, Paciente, Consulta
│   │   ├── admin.py          # Admin customizado com Jazzmin + inlines
│   │   ├── views.py          # Views da área do paciente
│   │   ├── urls.py           # Rotas do app
│   │   └── forms.py          # Formulários de registro e agendamento
│   └── templates/medical/    # Templates HTML
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🗃️ Diagrama do Banco de Dados

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ Especialidade│       │    Medico    │       │   Paciente   │
│──────────────│       │──────────────│       │──────────────│
│ id (PK)      │◄──┐   │ id (PK)      │       │ id (PK)      │
│ nome         │   └───│ especialidade│       │ user (FK)    │
│ descricao    │       │ user (FK)    │       │ nome         │
└──────────────┘       │ crm          │       │ cpf          │
                       │ telefone     │       │ data_nasc.   │
                       │ bio          │       │ telefone     │
                       └──────┬───────┘       │ email        │
                              │               └──────┬───────┘
                              │    ┌──────────────┐  │
                              └───►│   Consulta   │◄─┘
                                   │──────────────│
                                   │ id (PK)      │
                                   │ medico (FK)  │
                                   │ paciente (FK)│
                                   │ data_hora    │
                                   │ status       │
                                   │ observacoes  │
                                   │ criado_em    │
                                   └──────────────┘
```

---

## 🚀 Como Rodar

### Com Docker (recomendado)

```bash
# 1. Clone o repositório
git clone <url-do-repo>
cd django-clinica

# 2. Suba os contêineres
docker compose up --build

# 3. Crie o superusuário (em outro terminal)
docker compose exec web python manage.py createsuperuser

# 4. Acesse
# Área do paciente:  http://localhost:8000/
# Admin:             http://localhost:8000/admin/
```

### Sem Docker (ambiente local)

```bash
# 1. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure o .env
cd clinica
# Edite o arquivo .env com sua DATABASE_URL

# 4. Execute as migrações
python manage.py migrate

# 5. Crie o superusuário
python manage.py createsuperuser

# 6. Rode o servidor
python manage.py runserver

# 7. Acesse http://localhost:8000/
```

---

## ⚙️ Variáveis de Ambiente (`.env`)

| Variável | Descrição | Exemplo |
|---|---|---|
| `DATABASE_URL` | URL de conexão PostgreSQL | `postgresql://user:pass@host/db` |
| `SECRET_KEY` | Chave secreta Django | string aleatória longa |
| `DEBUG` | Modo debug | `True` / `False` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Django 5.x | Framework web principal |
| PostgreSQL | Banco de dados relacional |
| Jazzmin | Tema do admin |
| Bootstrap 5 | Interface responsiva |
| Docker | Containerização |
| django-crispy-forms | Formulários estilizados |

---

## 👥 Autores

- [Gabriel Coelho Costa](https://github.com/gabrielzinCoelho)
- [Frederico Maia Estrella](https://github.com/FredMaia)
- [Otávio Sbampato](https://github.com/otaviosbampato)
