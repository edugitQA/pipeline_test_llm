import sys
import os
import subprocess
import shutil

# --- Funções de verificação e impressão ---
def print_status(check_name, success, message=""):
    """Imprime o status de uma verificação com cores."""
    OK_GREEN = '\033[92m'
    FAIL_RED = '\033[91m'
    ENDC = '\033[0m'
    symbol = f"{OK_GREEN}✅ OK{ENDC}" if success else f"{FAIL_RED}❌ FALHA{ENDC}"
    print(f"[{symbol}] {check_name:30} {message}")
    return success

def check_python_version():
    """Verifica se a versão do Python é 3.10 ou superior."""
    is_ok = sys.version_info >= (3, 10)
    message = f"Versão encontrada: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    return print_status("Versão do Python (>= 3.10)", is_ok, message)

def check_virtual_env():
    """Verifica se estamos dentro de um ambiente virtual."""
    is_ok = (sys.prefix != sys.base_prefix)
    message = f"Ambiente virtual ativado em: {sys.prefix}" if is_ok else "Script não está rodando em um venv!"
    return print_status("Ambiente Virtual (venv)", is_ok, message)

def check_command_exists(command):
    """Verifica se um comando existe no PATH do sistema."""
    is_ok = shutil.which(command) is not None
    message = f"Comando '{command}' encontrado." if is_ok else f"Comando '{command}' NÃO encontrado no PATH."
    return print_status(f"Comando '{command}'", is_ok, message)

def check_azure_login():
    """Verifica se a Azure CLI está instalada e logada."""
    if not shutil.which("az"):
        return False # Pula se 'az' não existe

    try:
        # Roda 'az account show' e suprime a saída para não poluir o terminal
        subprocess.check_output("az account show", stderr=subprocess.STDOUT, shell=True)
        is_ok = True
        message = "Login na Azure CLI ativo."
    except subprocess.CalledProcessError:
        is_ok = False
        message = "Azure CLI instalada, mas não logada. Rode 'az login'."

    return print_status("Login na Azure CLI", is_ok, message)


# --- Execução Principal ---
print("\n--- Mentor AI QA: Verificação do Ambiente de Desenvolvimento ---\n")

results = []
results.append(check_python_version())
results.append(check_virtual_env())
results.append(check_command_exists("code")) # Checa se o comando 'code' do VS Code está no PATH
results.append(check_azure_login())

print("\n-------------------------------------------------------------\n")

if all(results):
    OK_GREEN = '\033[92m'
    ENDC = '\033[0m'
    print(f"{OK_GREEN}🎉 Parabéns! Seu ambiente está configurado corretamente.{ENDC}")
    print("   Você tem sinal verde para começar o Módulo 1.\n")
else:
    FAIL_RED = '\033[91m'
    ENDC = '\033[0m'
    print(f"{FAIL_RED}⚠️ Atenção! Encontramos problemas no seu ambiente.{ENDC}")
    print("   Corrija os itens marcados com [❌ FALHA] antes de prosseguir.\n")