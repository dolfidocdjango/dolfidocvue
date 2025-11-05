# Dolfidoc Backend - API REST

Backend Django moderno com Django REST Framework, autenticação JWT e PostgreSQL.

## Descrição

API REST completa para o sistema Dolfidoc, desenvolvida com Django 5.x e Django REST Framework. Fornece endpoints para gerenciamento de médicos, cardiologistas, clientes e usuários, com autenticação via JWT.

## Tecnologias

- **Django 5.x** - Framework web Python
- **Django REST Framework** - Toolkit para construção de APIs REST
- **Django CORS Headers** - Gerenciamento de CORS
- **djangorestframework-simplejwt** - Autenticação JWT
- **PostgreSQL** - Banco de dados relacional
- **Gunicorn** - Servidor WSGI para produção

## Estrutura do Projeto

```
backend/
├── manage.py
├── requirements.txt
├── README.md
├── dolfidoc/
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py      # Configurações comuns
│   │   ├── dev.py       # Configurações de desenvolvimento
│   │   └── prod.py      # Configurações de produção
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py         # Modelos: Cardiologista, Medicos, Config, Cliente
│   │   ├── serializers.py    # Serializers REST
│   │   ├── views.py          # ViewSets e views
│   │   ├── urls.py           # Rotas da API
│   │   ├── permissions.py    # Permissões customizadas
│   │   ├── tests.py          # Testes
│   │   ├── apps.py
│   │   └── migrations/
│   └── users/
│       ├── __init__.py
│       ├── models.py         # Modelo User customizado
│       ├── serializers.py    # Serializers de usuário
│       ├── views.py          # ViewSets de usuário
│       ├── urls.py           # Rotas de usuário
│       ├── permissions.py    # Permissões de usuário
│       ├── apps.py
│       ├── admin.py          # Admin customizado
│       └── migrations/
```

## Instalação

### Pré-requisitos

- Python 3.11+
- PostgreSQL 12+
- pip

### Passos para Instalação

1. **Clone o repositório** (se ainda não clonou):

```bash
git clone https://github.com/dolfidocdjango/dolfidoc.git
cd dolfidoc/backend
```

2. **Crie e ative um ambiente virtual**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Configure o banco de dados PostgreSQL**:

Crie um banco de dados chamado `dolfidoc_db`:

```sql
CREATE DATABASE dolfidoc_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE dolfidoc_db TO postgres;
```

5. **Execute as migrações**:

```bash
python manage.py migrate
```

6. **Crie um superusuário**:

```bash
python manage.py createsuperuser
```

7. **Execute o servidor de desenvolvimento**:

```bash
python manage.py runserver
```

8. **Acesse a API**:

- API: `http://localhost:8000/api/v1/`
- Admin: `http://localhost:8000/admin/`
- Healthcheck: `http://localhost:8000/api/v1/healthcheck/`

## Endpoints da API

### Autenticação JWT

- `POST /api/token/` - Obter token de acesso e refresh
- `POST /api/token/refresh/` - Renovar token de acesso

**Exemplo de requisição para obter token**:

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "senha123"}'
```

**Resposta**:

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### API v1

#### Cardiologistas

- `GET /api/v1/cardiologistas/` - Lista todos os cardiologistas
- `GET /api/v1/cardiologistas/?nome_completo=X&especialidade=Y&cidade=Z` - Busca filtrada
- `GET /api/v1/cardiologistas/<id>/` - Detalhes de um cardiologista
- `GET /api/v1/cardiologistas/<id>/foto/` - Foto do cardiologista

#### Médicos

- `GET /api/v1/medicos/` - Lista todos os médicos
- `GET /api/v1/medicos/?nome=X&especialidade=Y&cidade=Z` - Busca filtrada
- `GET /api/v1/medicos/<id>/` - Detalhes de um médico

#### Clientes

- `GET /api/v1/clientes/` - Lista todos os clientes
- `POST /api/v1/clientes/` - Cria um novo cliente
- `GET /api/v1/clientes/<id>/` - Detalhes de um cliente
- `PUT /api/v1/clientes/<id>/` - Atualiza um cliente
- `PATCH /api/v1/clientes/<id>/` - Atualiza parcialmente um cliente
- `DELETE /api/v1/clientes/<id>/` - Remove um cliente

#### Usuários

- `GET /api/v1/users/` - Lista todos os usuários (somente admin)
- `POST /api/v1/users/` - Cria um novo usuário
- `GET /api/v1/users/<id>/` - Detalhes de um usuário
- `PUT /api/v1/users/<id>/` - Atualiza um usuário
- `PATCH /api/v1/users/<id>/` - Atualiza parcialmente um usuário
- `DELETE /api/v1/users/<id>/` - Remove um usuário (somente admin)
- `GET /api/v1/users/profile/` - Perfil do usuário autenticado

#### Configurações

- `GET /api/v1/config/` - Lista todas as configurações
- `GET /api/v1/config/<id>/` - Detalhes de uma configuração

#### Healthcheck

- `GET /api/v1/healthcheck/` - Status do sistema

## Autenticação

A API usa autenticação JWT (JSON Web Token). Para acessar endpoints protegidos:

1. Obtenha um token em `/api/token/`
2. Inclua o token no header das requisições:

```
Authorization: Bearer <seu_token_aqui>
```

**Exemplo com curl**:

```bash
curl -X GET http://localhost:8000/api/v1/users/profile/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

## Configurações de Ambiente

### Desenvolvimento

Use `dolfidoc.settings.dev`:

```bash
export DJANGO_SETTINGS_MODULE=dolfidoc.settings.dev
python manage.py runserver
```

### Produção

Use `dolfidoc.settings.prod`:

```bash
export DJANGO_SETTINGS_MODULE=dolfidoc.settings.prod
gunicorn dolfidoc.wsgi:application
```

## CORS

O backend está configurado para aceitar requisições dos seguintes origins:

- `http://localhost:5173` (Vite/Vue.js)
- `http://localhost:8080` (Vue CLI)
- `http://localhost:3000` (React/Next.js)

Para adicionar mais origins, edite `CORS_ALLOWED_ORIGINS` em `settings/base.py`.

## Testes

Execute os testes com:

```bash
python manage.py test
```

## Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Verificar configurações
python manage.py check

# Shell interativo
python manage.py shell
```

## Integração com Frontend Vue.js

O backend está pronto para integração com Vue.js via Axios. Exemplo de configuração do Axios:

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para adicionar token JWT
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
```

## Modelos de Dados

### Cardiologista

- nome, crm, uf, cidade, nome_fantasia, cnpj, especialidade
- numero, valor, fid, logradouro, complemento, foto

### Medicos

- nome, crm, situacao, uf, cidade, nome_fantasia, cnpj
- especialidade, numero, logradouro, complemento, valor

### Cliente

- nome, email, telefone, data_criacao, ativo

### User (Customizado)

- username, email, first_name, last_name, telefone, data_nascimento
- is_active, is_staff, date_joined, last_login

## Permissões

- **IsAuthenticatedOrReadOnly**: Leitura para todos, escrita apenas autenticados
- **IsAdminOrReadOnly**: Leitura para autenticados, escrita apenas para admins
- **IsAdminOrOwner**: Admin ou proprietário do recurso
- **IsAdminUser**: Apenas administradores

## Licença

Este projeto está sob a licença MIT.

## Contato

Para mais informações, visite o repositório no GitHub.

**Desenvolvido com ❤️ pela equipe Dolfidoc**
