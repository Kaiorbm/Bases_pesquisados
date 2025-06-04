# API Verifica ID Base Pesquisados

- Este projeto verifica se um ID específico existe na Base Pesquisados. A verifi
cação é feita mediante requisição API REST.

## Estrutura Projeto
app/
├── main.py
├── models.py # Verifica se o conteúdo da requisição é uma String
├── routes.py # Rotas API
├── utils.py # Função que verifica se o ID existe na Base Pesquisados
└── data/ # Pasta onde fica o csv
└── base_pesquisados.csv # CSV Base Pesquisados

## Pacotes

Criação Ambiente Virtual

- python -m venv venv # Cria Ambiente Virtual

Ativação Ambiente Virtual
- source venv/bin/activate # Ativa Ambiente Virtual (Linux)
- venv/Scripts/activate # Ativa Ambiente Virtual (Windows)

Instalação Pacotes

- pip install -r requirements.txt

## Rodando Aplicação

- Abrir terminal na pasta app
- Ativar Ambiente Virtual
- Executar uvicorn app.main:app --reload
- Testar Postman