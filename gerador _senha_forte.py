# Obs: \033[style; text; back m
# Create by guimileib
import random
import string

def gera_senha(tamanho):
    if tamanho < 8:
        raise ValueError("\033[91m[AVISO]: O comprimento da senha deve ser pelo menos 4 para garantir a segurança.")
    if tamanho > 20:
        raise ValueError("\033[91m[AVISO]: É recomendável que o comprimento de sua senha tenha no máximo 20 caracteres para que você não esqueça.")

    # Garante que a senha tenha pelo menos um de cada tipo de caractere
    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Preenche o resto da senha com caracteres aleatórios
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha += [random.choice(caracteres) for _ in range(tamanho - 4)]
    
    # Embaralha a senha para que os primeiros caracteres não sejam previsíveis
    random.shuffle(senha)

    return ''.join(senha)

def main():
    print("\033[91m[AVISO]: É mais seguro utilizar senhas de 12 caracteres.")
    print("\033[91m[AVISO]: As senhas geradas utilizam os padrões de senha forte\n")
    tamanho = int(input("\033[0mDigite o comprimento desejado para a senha: "))
    try:
        senha = gera_senha(tamanho)
        print(f"Sua senha gerada é: {senha}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
