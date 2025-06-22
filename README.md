# QA Testing AI

Projeto para automação, rastreamento e análise de fluxos de testes de IA utilizando PromptFlow e.

## Visão Geral
Este repositório foi criado para facilitar o desenvolvimento, execução e rastreamento de experimentos de IA, com foco em fluxos de geração de piadas e integração robusta com MLflow para logging de parâmetros, métricas e artefatos.

## Estrutura do Projeto
```
QA_testing_AI/
├── check_env.py                # Script de verificação do ambiente
├── mlruns/                     # Diretório de experimentos do MLflow (ignorado pelo git)
├── simple_joke/
│   ├── hello.py                # Exemplo de fluxo PromptFlow
│   ├── mlflow_test_run.py      # Script de logging e integração com MLflow
│   ├── requirements.txt        # Dependências do projeto
│   └── ...
└── ...
```

## Como usar

### 1. Instale as dependências
```bash
conda run -p /home/edu/miniconda3 pip install -r simple_joke/requirements.txt
```

### 2. Execute o MLflow UI
```bash
mlflow ui --host 0.0.0.0 --port 5000
```

### 3. Execute o fluxo de teste e logging
```bash
conda run -p /home/edu/miniconda3 python simple_joke/mlflow_test_run.py
```

Acesse a interface do MLflow em: [http://localhost:5000](http://localhost:5000)

## Boas práticas
- Nunca suba arquivos sensíveis como `.env` ou bancos de dados locais para o git.
- Use o `.gitignore` fornecido para evitar versionar arquivos temporários, ambientes virtuais e dados de execução.
- Documente seus experimentos e mantenha o código limpo e modular.

## Sobre
Desenvolvido para facilitar a rastreabilidade e automação de testes de IA, integrando PromptFlow e MLflow de forma profissional.

---

> Para dúvidas ou sugestões, abra uma issue ou envie um pull request.
