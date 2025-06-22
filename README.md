# QA Testing LLM com PromptFlow

Projeto para automação, rastreamento e análise de fluxos de testes de LLM (Large Language Models) como um engenheiro de QA, utilizando PromptFlow para orquestrar e visualizar cada etapa do processo.

## Visão Geral
Este repositório foi criado para facilitar o desenvolvimento, execução e rastreamento de experimentos de QA em LLMs, permitindo quebrar o processo em estações de trabalho (nós), de forma clara e modular:

- **Nó 1:** Prepara a matéria-prima (ex: formata a pergunta do usuário).
- **Nó 2:** Envia para a máquina principal (ex: chama o LLM).
- **Nó 3:** Inspeciona a qualidade do produto (ex: avalia se a resposta é tóxica).
- **Nó 4:** Registra o resultado.

A grande vantagem do PromptFlow é a clareza visual, a reutilização de cada "estação" e a capacidade de processar lotes gigantescos de testes de uma só vez, algo essencial para QA de LLMs.

## Estrutura do Projeto

```
pipeline_test_llm/
├── README.md
├── check_env.py                # Script de verificação do ambiente
└── basic_flow/                 # Fluxo principal de testes com PromptFlow
    ├── requirements.txt        # Dependências do fluxo
    ├── flow.dag.yaml           # Definição do pipeline (DAG) do PromptFlow
    ├── data.jsonl              # Dados de entrada para testes em lote
    ├── hello.py                # Exemplo de nó Python
    ├── prepare_prompt.py       # Nó: prepara a pergunta do usuário
    ├── prepare_prompt2.py      # Nó: prepara uma segunda pergunta
    ├── echo_response.py        # Nó: simula resposta do LLM
    ├── hello.jinja2            # Template de prompt
    ├── openai_test.jinja2      # Template para chamada do LLM
    ├── prompt_01.jinja2        # Outro template de prompt
    └── __pycache__/            # Cache de execução Python
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
