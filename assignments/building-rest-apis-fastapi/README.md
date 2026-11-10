# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar itens de um inventário usando FastAPI. Você praticará métodos HTTP, modelos de dados com validação e respostas para recursos inexistentes.

## 📝 Tarefas

### 🛠️ Listagem de Itens do Inventário

#### Descrição
Instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`. Complete o endpoint de listagem no código inicial e execute a aplicação com `uvicorn starter-code:app --reload`; explore a documentação interativa em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Responder a `GET /items` com todos os itens armazenados em memória
- Retornar uma lista vazia quando ainda não houver itens
- Manter o endpoint `GET /` disponível como mensagem de boas-vindas


### 🛠️ Criação e Consulta de Itens

#### Descrição
Adicione endpoints para criar um item e consultar um item específico pelo ID. Use o modelo Pydantic fornecido para validar os dados enviados à API.

#### Requisitos
O programa concluído deve:

- Aceitar `POST /items` com um item contendo `id`, `name` e `quantity`
- Retornar o item criado e disponibilizá-lo nas consultas seguintes
- Responder a `GET /items/{item_id}` com o item correspondente ou status HTTP 404 quando ele não existir
- Rejeitar quantidades negativas por meio da validação do modelo


### 🛠️ Atualização e Remoção de Itens

#### Descrição
Complete a API com operações para substituir os dados de um item existente e removê-lo do inventário.

#### Requisitos
O programa concluído deve:

- Atualizar um item existente com `PUT /items/{item_id}`
- Remover um item existente com `DELETE /items/{item_id}`
- Responder com status HTTP 404 ao tentar atualizar ou remover um ID inexistente
- Confirmar que as alterações e remoções aparecem nas chamadas posteriores a `GET /items` e `GET /items/{item_id}`