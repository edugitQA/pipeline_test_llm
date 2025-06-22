from promptflow import tool

# Este nó recebe a saída do nó anterior como sua entrada.
@tool
def echo_response(prepared_prompt: str) -> str:
    """
    Simula a resposta de um LLM. Por enquanto, apenas retorna o prompt que recebeu.
    """
    # Linha a linha:
    # 1. Print para debug, para vermos o que este nó recebeu.
    print(f"Nó 'echo' recebeu o prompt: {prepared_prompt}")

    # 2. Em um fluxo real, aqui estaria o código para chamar a API do OpenAI,
    #    Azure, Gemini, etc., passando o 'prepared_prompt'.
    #    Ex: response = client.chat.completions.create(...)

    # 3. Para nosso teste inicial, simplesmente criamos uma resposta "falsa"
    #    que inclui o prompt original, para podermos validar o fluxo de dados.
    simulated_answer = f"SIMULAÇÃO DE RESPOSTA DO LLM PARA O PROMPT:\n--- \n{prepared_prompt}"

    # 4. Retorna a resposta simulada.
    return simulated_answer