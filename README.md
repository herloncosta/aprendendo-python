# Todo List - Estudos em Python

Este é um projeto simples de uma Lista de Tarefas (Todo List) desenvolvido em Python, criado com o objetivo de estudar e praticar os conceitos da linguagem. O projeto utiliza o banco de dados SQLite para persistir as tarefas localmente.

## Funcionalidades

O sistema possui a base lógica (operações de banco de dados) implementada para realizar as seguintes operações (CRUD):

- **Adicionar** novas tarefas.
- **Editar** o título de tarefas existentes.
- **Remover** tarefas.
- **Listar** tarefas (exibir uma tarefa específica, todas as tarefas, apenas concluídas ou apenas pendentes).
- **Marcar** tarefas como concluídas ou não concluídas.


## Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** (Biblioteca padrão do Python para banco de dados relacional leve)

## Como clonar e reproduzir o projeto

Siga as instruções abaixo de acordo com o seu sistema operacional para rodar o projeto na sua máquina.

### Linux ou macOS

1. **Clone o repositório:**
   Abra o seu terminal e execute:

   ```bash
   git clone https://github.com/herloncosta/aprendendo-python.git
   ```

2. **Acesse a pasta do projeto:**

   ```bash
   cd aprendendo-python/todo-list
   ```

   _(Nota: Considerando que a pasta do projeto se chama `todo-list` dentro do repositório)_

3. **Crie um ambiente virtual (recomendado):**

   ```bash
   python3 -m venv venv
   ```

4. **Ative o ambiente virtual:**

   ```bash
   source venv/bin/activate
   ```

5. **Execute o projeto:**
   ```bash
   python3 main.py
   ```

### Windows

1. **Clone o repositório:**
   Abra o Prompt de Comando (CMD) ou PowerShell e execute:

   ```cmd
   git clone https://github.com/herloncosta/aprendendo-python.git
   ```

2. **Acesse a pasta do projeto:**

   ```cmd
   cd aprendendo-python\todo-list
   ```

   _(Nota: Considerando que a pasta do projeto se chama `todo-list` dentro do repositório)_

3. **Crie um ambiente virtual (recomendado):**

   ```cmd
   python -m venv venv
   ```

4. **Ative o ambiente virtual:**

   ```cmd
   venv\Scripts\activate
   ```

5. **Execute o projeto:**
   ```cmd
   python main.py
   ```

---

## Estrutura do Projeto

- `main.py`: Arquivo principal, ponto de entrada do projeto e responsável por inicializar o banco de dados.
- `operations.py`: Contém as funções lógicas e queries SQL responsáveis pelas interações com os dados (adicionar, remover, listar, concluir tarefas).
- `database.py`: Gerencia a conexão com o banco de dados SQLite (`tarefas.db`) e realiza a criação da estrutura inicial (tabela `tasks`).
- `tarefas.db`: Arquivo físico do banco de dados gerado automaticamente na primeira execução.
