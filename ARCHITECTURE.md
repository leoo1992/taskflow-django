# Arquitetura

TaskFlow é uma aplicação Django organizada em camadas simples:

- **Web/UI**: templates e arquivos estáticos em `templates/` e `static/`.
- **Aplicação**: projeto Django em `taskflow/` e domínio de tarefas em `tasks/`.
- **Persistência**: ORM do Django, configurado por variáveis de ambiente.
- **Entrega**: GitHub Actions valida a aplicação e um pipeline separado valida os controles de qualidade do repositório.
