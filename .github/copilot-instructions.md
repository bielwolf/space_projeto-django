# Instruções rápidas para agentes (space-django)

Objetivo: permitir que agentes de código (Copilot/assistentes) fiquem produtivos rapidamente ao entender, executar e alterar este repositório Django.

1) Primeiros passos — descoberta
- Verifique se o repositório contém um projeto Django/projeto Python padrão: procure por `manage.py`, `requirements.txt`, `Pipfile`, `pyproject.toml`, `Dockerfile`, `docker-compose.yml` e pastas de apps (`*/apps` ou `*/models.py`).
- Busque configurações divididas em `settings/` ou arquivos `settings.py` (base/dev/prod).
- Localize testes em `tests/` ou `*/tests.py` e pipelines em `.github/workflows/`.

2) Arquitetura esperada (como ler o código)
- Este repositório segue o padrão Django com apps autocontidos: cada app geralmente tem `models.py`, `views.py`, `urls.py`, `admin.py` e `migrations/`.
- APIs REST, quando presentes, usam `serializers.py` e `views.py` (ou `viewsets` em `views.py`).
- Tarefas assíncronas aparecem em `celery.py` ou `tasks.py` dentro das apps.

3) Comandos de desenvolvimento e verificação
- Criar ambiente e instalar dependências:
  - `python -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`
- Banco e migrações:
  - `python manage.py migrate`
  - `python manage.py makemigrations <app>` (se criar/alterar modelos)
- Rodar servidor de dev: `python manage.py runserver`
- Testes: `python manage.py test` ou `pytest` (verifique `pytest.ini`)
- Linters/formatadores: execute `black`, `flake8` ou `isort` se os arquivos de configuração estiverem presentes.

4) Convenções de projeto úteis para mudanças
- Mantenha apps autocontidos — não mover lógica entre apps sem motivo claro.
- Testes unitários geralmente ficam próximos ao código testado: `app/tests.py` ou `app/tests/`.
- Ao modificar modelos, gere migrações e inclua-as no commit.
- Use variáveis de ambiente para credenciais e URLs externos; verifique `settings.py` por leitores de `os.environ`.

5) Integrações e pontos externos a checar
- Banco de dados: procure `DATABASES` em `settings.py` (Postgres é comum em produções).
- Cache/Broker: Redis/Celery — procure por `CELERY_BROKER_URL` ou importações `celery`.
- Arquivos Docker: `Dockerfile`, `docker-compose.yml` descrevem como o app é empacotado e dependências (Postgres, Redis).
- Pipelines CI: verifique `.github/workflows/` para comandos testados automaticamente.

6) Como propor mudanças (PRs)
- Reproduza localmente os problemas antes de corrigir.
- Rode `python manage.py test` e linters localmente; inclua correções de estilo separadas quando possível.
- Se adicionar/alterar modelos, inclua migrações geradas e documente por que a mudança é necessária.

7) Quando não houver arquivos detectáveis
- Se o repositório estiver vazio ou faltarem arquivos padrão, confirme com:
  - `ls -la` na raiz do projeto
  - `git status` para branches/arquivos não comitados
- Em repositórios vazios, peça ao mantenedor os artefatos ausentes (manage.py, requirements, etc.) antes de mudanças significativas.

8) Observações finais
- Seja conservador: pequenas mudanças, rodar testes, gerar migrações quando necessário.
- Sempre referencie e linke os arquivos alterados nas descrições de PR.

Se algum trecho ficou vago ou você quiser que eu incorpore exemplos diretos de arquivos encontrados aqui, diga quais arquivos devo analisar primeiro.
