# Projeto Ecommerce

O objetivo deste projeto é construir um pequeno **ecommerce** utilizando **Python** e **Django**, com funcionalidades básicas de gerenciamento de produtos, autenticação de usuários e simulação de compra. Este é um projeto em desenvolvimento, focado em aprender e aplicar conceitos de programação web, integração de banco de dados e boas práticas de desenvolvimento.

## Status

Este projeto está em **desenvolvimento**. Atualmente, há funcionalidades a serem implementadas.

### Funcionalidades Planejadas

- **Simulação de Compra**: Implementação de um fluxo simples de compra, com carrinho de compras e finalização de pedido.

### Funcionalidades Implementadas

- **Autenticação de Usuários**: Cadastro, login e logout de usuários.
- **Gestão de Produtos**: Cadastro, listagem, atualização e exclusão de produtos.
- **Administração**: Interface administrativa para gerenciar produtos.

## Como executar

### 1. Clone o repositório em sua máquina

```bash
git clone https://github.com/AfonsoDolmen/projeto-ecommerce.git
```

### 2. Crie um ambiente virtual Python dentro da pasta do projeto

```bash
python -m venv .venv
```

### 3. ative seu ambiente Python virtual


#### No Windows:
```bash
.venv\Scripts\activate
```

#### No Linux/Mac:
```bash
source .venv/bin/activate
```


### 4. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

### 5. Aplique as migrações do banco de dados

```bash
python manage.py migrate
```

### 6. Inicie o servidor local

```bash
python manage.py runserver
```

O servidor estará acessivel no navegador em http://127.0.0.1:8000
