# Gerador de Senhas Fortes

Este repositório contém um script em Python para gerar senhas fortes. O script garante que a senha gerada contenha uma combinação de letras maiúsculas, minúsculas, dígitos e caracteres especiais, garantindo maior segurança.

## Descrição

O script `generate_password.py` foi criado para ajudar os usuários a gerar senhas fortes e seguras de maneira rápida e fácil. O código inclui verificações para assegurar que a senha tenha um comprimento mínimo e máximo recomendável para manter um bom equilíbrio entre segurança e praticidade.

## Funcionalidades

- Geração de senhas seguras com comprimento entre 8 e 20 caracteres.
- Assegura a inclusão de pelo menos um caractere de cada tipo (maiúsculo, minúsculo, dígito e caractere especial).
- Embaralhamento da senha para garantir imprevisibilidade.
- Mensagens de aviso coloridas para melhor orientação do usuário.

## Instalação

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Clone este repositório:
    ```bash
    git clone https://github.com/guimileib/gerador-de-senha.git
    ```
3. Navegue até o diretório do projeto:
    ```bash
    cd gerador-de-senhas
    ```

## Como Usar

1. Execute o script `generate_password.py`:
    ```bash
    python generate_password.py
    ```
2. Siga as instruções no terminal para inserir o comprimento desejado para a senha.

## Exemplo

Ao executar o script, você verá uma mensagem como a seguinte:

```
[AVISO]: É mais seguro utilizar senhas de 12 caracteres.
[AVISO]: As senhas geradas utilizam os padrões de senha forte

Digite o comprimento desejado para a senha: 12
Sua senha gerada é: aB3$7Xy@1!

```

## Avisos

- É mais seguro utilizar senhas de pelo menos 12 caracteres.
- O comprimento mínimo da senha é de 8 caracteres.
- O comprimento máximo recomendado é de 20 caracteres para facilitar a memorização.

## Autor

Criado por [guimileib](https://github.com/guimileib)

---

Este script é distribuído sob a licença MIT. Sinta-se à vontade para contribuir e melhorar este projeto!
