# Importa a ferramenta necessária do promptflow
from promptflow import tool

# O decorador @tool diz ao PromptFlow que esta função é uma "estação de trabalho"
# na nossa linha de montagem.
@tool
def prepare_prompt(question: str) -> str:
    """
    Prepara o prompt para ser enviado ao LLM, encapsulando a pergunta do usuário
    em um template.
    """
    # Linha a linha:
    # 1. Print para podermos ver no log o que chegou neste nó. Ótimo para debug.
    print(f"Preparando prompt para a pergunta: {question}")

    # 2. Cria um template de prompt. Em um caso real, isso seria muito mais complexo,
    #    possivelmente incluindo exemplos e instruções detalhadas (few-shot learning).
    prompt_template = f"""
    Você é um assistente de atendimento ao cliente.
    Responda a seguinte pergunta do usuário de forma clara e direta.

    Pergunta do Usuário: "{question}"
    """

    # 3. Retorna o prompt formatado. Esta será a saída do nó.
    return prompt_template