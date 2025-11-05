# Guia de Migração - Dolfidoc

## Migração da Arquitetura Antiga para REST API

Este documento descreve o processo de migração do projeto Dolfidoc da arquitetura tradicional Django com templates para a nova arquitetura REST API.

## Mudanças Principais

### 1. Estrutura de Arquivos

**Antes:**
```
dolfidoc/
├── dolfidoc/
│   ├── settings.py (monolítico)
│   ├── urls.py
│   └── wsgi.py
└── dolfidocapp/
    ├── models.py
    ├── views.py (views baseadas em templates)
    ├── urls.py
    └── templates/
```

**Depois:**
```
backend/
├── dolfidoc/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── api/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py (ViewSets REST)
│   │   └── urls.py
│   └── users/
│       ├── models.py (User customizado)
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
```

### 2. Modelos

#### Modelos Migrados

Todos os modelos foram migrados de `dolfidocapp/models.py` para `dolfidoc/api/models.py`:

- **Cardiologista**: Mantido com todos os campos originais
- **Medicos**: Mantido com todos os campos originais
- **Config**: Mantido com todos os campos originais

#### Mudanças nos Modelos

- **Removido `managed = False`**: Agora o Django gerencia as tabelas
- **Adicionados `Meta.verbose_name` e `Meta.ordering`**: Melhor organização no admin
- **Adicionados métodos `__str__`**: Melhor representação dos objetos

#### Novo Modelo

- **Cliente**: Novo modelo para CRUD conforme especificação do documento

### 3. Views

#### Views Antigas (Template-based)

```python
# views.py antigo
def medInfo(request):
    # Lógica de filtros e paginação
    return JsonResponse(response_data)

def index(request):
    return render(request, 'pagina_inicial.html')
```

#### Views Novas (REST API)

```python
# views.py novo
class CardiologistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cardiologista.objects.all()
    serializer_class = CardiologistaSerializer
    
    def list(self, request, *args, **kwargs):
        # Lógica de filtros e paginação mantida
        ...
```

#### Mapeamento de Views

| View Antiga | ViewSet Novo | Endpoint |
|-------------|--------------|----------|
| `medInfo` | `CardiologistaViewSet.list()` | `GET /api/v1/cardiologistas/` |
| `obter_imagem_foto` | `CardiologistaViewSet.foto()` | `GET /api/v1/cardiologistas/<id>/foto/` |
| `index`, `contato`, `sobre` | Removidos | Frontend Vue.js assume |

### 4. URLs

#### URLs Antigas

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('medinfo/', views.medInfo, name='medinfo'),
    path('medico/imagem/<int:medico_id>/', views.obter_imagem_foto),
    path('contato/', views.contato),
    path('sobre/', views.sobre),
]
```

#### URLs Novas

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/', include('dolfidoc.api.urls')),
    path('api/v1/users/', include('dolfidoc.users.urls')),
]
```

### 5. Autenticação

**Antes:** Autenticação baseada em sessões Django

**Depois:** Autenticação JWT (JSON Web Token)

```bash
# Obter token
POST /api/token/
{
  "username": "admin",
  "password": "senha123"
}

# Usar token
GET /api/v1/users/profile/
Authorization: Bearer <token>
```

### 6. CORS

Adicionado suporte a CORS para integração com frontend Vue.js:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8080",
]
```

## Lógica de Negócio Preservada

### Filtros de Cardiologistas

A lógica original de filtragem foi **totalmente preservada**:

- Filtro por `nome_completo`, `especialidade`, `cidade`
- Paginação de 50 itens
- Modo agrupado por CRM quando `nome_completo` é fornecido
- Modo lista simples ordenado por valor quando `nome_completo` está vazio
- Busca geral sem paginação quando todos os campos estão vazios

### Exemplo de Requisição

**Antes:**
```
GET /medinfo/?nome_completo=João&especialidade=Cardiologia&cidade=São Paulo
```

**Depois:**
```
GET /api/v1/cardiologistas/?nome_completo=João&especialidade=Cardiologia&cidade=São Paulo
```

**Resposta mantém o mesmo formato:**
```json
{
  "especialidade": "Cardiologia",
  "cidade": "São Paulo",
  "agrupado": true,
  "medicos": { ... },
  "total_results": 10
}
```

## Banco de Dados

### Tabelas Existentes

As tabelas existentes (`cardiologista`, `medicos`, `config`) são **mantidas** através da configuração `db_table` nos modelos.

### Novas Tabelas

Serão criadas novas tabelas para:

- `users_user`: Modelo User customizado
- `api_cliente`: Modelo Cliente

### Comandos de Migração

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate
```

## Passos para Migração

### 1. Backup do Banco de Dados

```bash
pg_dump dolfidoc_db > backup_dolfidoc_$(date +%Y%m%d).sql
```

### 2. Instalar Novo Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar Banco de Dados

Edite `dolfidoc/settings/dev.py` ou use variáveis de ambiente para configurar a conexão com o banco existente.

### 4. Executar Migrações

```bash
python manage.py migrate
```

Isso criará apenas as **novas tabelas** (User, Cliente) sem afetar as tabelas existentes.

### 5. Criar Superusuário

```bash
python manage.py createsuperuser
```

### 6. Testar Endpoints

```bash
# Iniciar servidor
python manage.py runserver

# Testar healthcheck
curl http://localhost:8000/api/v1/healthcheck/

# Obter token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "senha"}'

# Testar endpoint de cardiologistas
curl http://localhost:8000/api/v1/cardiologistas/
```

### 7. Integrar Frontend Vue.js

Configure o Axios no frontend para usar a nova API:

```javascript
const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
});
```

## Compatibilidade

### Dados Preservados

- ✅ Todos os dados de `cardiologista` são preservados
- ✅ Todos os dados de `medicos` são preservados
- ✅ Todos os dados de `config` são preservados

### Funcionalidades Preservadas

- ✅ Busca de médicos por nome, especialidade e cidade
- ✅ Filtros dinâmicos
- ✅ Paginação
- ✅ Modo agrupado por CRM
- ✅ Exibição de fotos (BinaryField)

### Novas Funcionalidades

- ✅ Autenticação JWT
- ✅ CRUD de clientes
- ✅ CRUD de usuários
- ✅ Permissões granulares
- ✅ Healthcheck
- ✅ Versionamento de API (`/api/v1/`)
- ✅ CORS configurado
- ✅ Settings modular (dev/prod)

## Rollback

Caso seja necessário reverter para a versão antiga:

1. Restaurar backup do banco de dados
2. Voltar para o código anterior
3. As tabelas novas (`users_user`, `api_cliente`) podem ser mantidas ou removidas

```bash
# Restaurar backup
psql dolfidoc_db < backup_dolfidoc_YYYYMMDD.sql
```

## Checklist de Migração

- [ ] Backup do banco de dados realizado
- [ ] Ambiente virtual criado e dependências instaladas
- [ ] Configurações de banco de dados ajustadas
- [ ] Migrações executadas com sucesso
- [ ] Superusuário criado
- [ ] Endpoints testados e funcionando
- [ ] Frontend Vue.js integrado e testado
- [ ] Autenticação JWT funcionando
- [ ] CORS configurado corretamente
- [ ] Testes automatizados executados
- [ ] Documentação atualizada

## Suporte

Para dúvidas ou problemas durante a migração, consulte:

- README.md - Documentação completa do backend
- Código original em `/home/ubuntu/dolfidoc/`
- Planejamento em `/home/ubuntu/planejamento_nova_arquitetura.md`
