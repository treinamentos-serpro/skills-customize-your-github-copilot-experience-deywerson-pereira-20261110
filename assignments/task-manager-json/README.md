# 📘 Atividade: Gerenciador de Tarefas com JSON

## 🎯 Objetivo

Construa um gerenciador de tarefas em Python que permita organizar tarefas e preservar seus dados entre execuções. Pratique classes, coleções e leitura e escrita de arquivos JSON.

## 📝 Tarefas

### 🛠️ Modelar e gerenciar tarefas

#### Descrição
Crie uma classe `Task` para representar uma tarefa e um programa de linha de comando que permita adicionar tarefas, listar as tarefas existentes e marcar uma tarefa como concluída. Nesta primeira etapa, mantenha as tarefas em uma lista na memória.

#### Requisitos
O programa concluído deve:

- Definir uma classe `Task` com título e estado de conclusão
- Permitir adicionar e listar tarefas, exibindo claramente quais foram concluídas
- Permitir marcar uma tarefa existente como concluída sem alterar as demais
- Mostrar uma mensagem adequada quando o usuário tentar concluir uma tarefa inexistente

### 🛠️ Salvar e carregar tarefas em JSON

#### Descrição
Adicione persistência ao gerenciador usando o módulo `json` da biblioteca padrão. Ao iniciar o programa, carregue as tarefas do arquivo `tasks.json`; ao encerrar ou após uma alteração, salve o estado atual para que ele possa ser recuperado na próxima execução.

#### Requisitos
O programa concluído deve:

- Converter as tarefas para um formato serializável e gravá-las em `tasks.json`
- Reconstruir objetos `Task` a partir dos dados carregados
- Começar com uma lista vazia quando `tasks.json` ainda não existir
- Preservar títulos e estados de conclusão após salvar e carregar as tarefas
- Demonstrar que uma tarefa adicionada ou concluída continua no estado correto após reiniciar o programa
