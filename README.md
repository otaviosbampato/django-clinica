# Sistema de Reservas — Clínica+

Aplicação web desenvolvida com **Django** para gerenciamento de consultas médicas. Permite que pacientes agendem consultas e que administradores gerenciem médicos, especialidades e agendamentos.

---

## Funcionalidades

- **Área do Paciente** (login/senha): cadastro, login, agendamento e cancelamento de consultas, visualização do histórico e perfil.
- **Painel Administrativo** (Jazzmin): gestão completa de médicos, pacientes, especialidades e consultas com filtros, buscas e inlines.
- **Interface responsiva** com Bootstrap 5.
- **Banco de dados** PostgreSQL.
- **Containerização** com Docker.

---

## Estrutura do Projeto

```
django-clinica/
├── clinica/                  
│   ├── core/                 
│   ├── medical/              
│   │   ├── models.py          
│   │   ├── admin.py            
│   │   ├── views.py           
│   │   ├── urls.py           
│   │   └── forms.py          
│   └── templates/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Diagrama do Banco de Dados

```
                       ┌──────────────┐       ┌──────────────┐
                       │    Medico    │       │   Paciente   │
                       │──────────────│       │──────────────│
                       │ id (PK)      │       │ id (PK)      │
                       │ especialidade│       │ user (FK)    │
                       │ user (FK)    │       │ nome         │
                       │ crm          │       │ cpf          │
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

## Como Rodar

### Com Docker (recomendado)

```bash
git clone <url-do-repo>
cd django-clinica
docker compose up --build
docker compose exec web python manage.py createsuperuser
```

### Sem Docker (ambiente local)

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt

cd clinica

# Edite o arquivo .env com sua DATABASE_URL

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# 7. Acesse http://localhost:8000/
```

---

## Variável de Ambiente (`.env`)

| Variável | Descrição | Exemplo |
|---|---|---|
| `DATABASE_URL` | URL de conexão PostgreSQL | `postgresql://user:pass@host/db` |

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Django 5.x | Framework web principal |
| PostgreSQL | Banco de dados relacional |
| Jazzmin | Tema do admin |
| Bootstrap 5 | Interface responsiva |
| Docker | Containerização |
| django-crispy-forms | Formulários estilizados |

---

## Autores

- [Gabriel Coelho Costa](https://github.com/gabrielzinCoelho)
- [Frederico Maia Estrella](https://github.com/FredMaia)
- [Otávio Sbampato](https://github.com/otaviosbampato)
