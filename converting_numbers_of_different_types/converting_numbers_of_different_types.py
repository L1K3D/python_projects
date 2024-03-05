#CEFSA - Centro Educacional da Fundação Salvador Arena
#FESA - Faculdade Engenheiro Salvador Arena
#Heitor Santos Ferreira - RA: 081230042
#Engenharia de Computação - Quarto Semestre - EC4
#Professor: Marco Aurélio
#Disciplina: Eletrônica analógica

#Lista de exercicios 01 - Exercicio 8#

# 1. Criando função especifica para conversão dos valores do tipo string para valor inteiro
# 1.1. Nomeando a função juntamente com seus parametros a serem definidos
def conversorTextoParaInteiro(texto, verifica_numeros=True): # OBS 1.1. -> Os parametros a serem definidos nessa função competem ao texto que será fornecido, compreendido na variavel de nome 'texto', e outra variavel do tipo boleana que compete a verificação dos itens contidos na cadeia de texto que será digitada a fim de compreender se a mesma é ou não um digito númerico

    # 1.2. Criando condição de verificação para onde o texto digitado deve ser de fato do tipo 'string'
    if not isinstance(texto, str):
        raise ValueError("O texto digitado deve ser uma 'string' ")
    
    # 1.3. Criando condição de verificação para onde o texto digitado deve conter de fato apenas números
    if verifica_numeros and not texto.isdigit():
        raise ValueError(" O texto digitado deve conter apenas números! ")

    # 1.4. Criando condição de verificação para onde o texto digitado deve conter no máximo três caracteres
    if len(texto) > 3:
        raise ValueError("O texto digitado deve ser no máximo de digitos ")

    # 1.5. Criando lista de digitos que estão contidos dentro do texto digitado
    digitos = [int(char) for char in texto]

    # 1.6. Definindo o valor inteiro obtido como 0 a fim de forçar o input do valor que será obtido a ser um número inteiro que será armazenado nessa variavel
    valor_inteiro_obtido = 0

    # 1.7. Realizando laço de repetição onde para cada elemento e digito contido na lista de 'digitos' o valor é baseado na base númerica de 10, ou seja, é realizada uma conversão decimal forçada a partir dos elementos e variações computacionais
    for elemento, digito in enumerate(digitos):
        valor_inteiro_obtido += digito * 10**(len(digitos) - elemento - 1)

    # 1.8. Retorna o valor inteiro obtido
    return valor_inteiro_obtido

# 2. Realizando captura e exibição de valores
# 2.1. Realizando captura de valores a serem informados pelo usuario do script
# 2.1.1. Obtendo os números/valores que serão convertidos posteriormente a partir de um 'input' do usuario
texto_digitado = input("Digite um texto que será convertido em inteiro: ")

# 2.1.2. Exibe para o usuário a tipagem descritiva sistemica do texto digitado por ele
print(f"Tipagem descritiva sistemica do texto digitado: {type(texto_digitado)}")

# 2.2. Criando modelo de tentativa e exceção ("'try' and 'excepct'") para garantir execução do processo de conversão ou de evidência de erro ao usuário
# 2.2.1. Criando modelo de tentativa ('try')
try:
    
    # 2.1.1.1. Definindo variavel 'numero_convertido' como variavel que irá receber o número que foi convertido a partir da execução da função
    numero_convertido = conversorTextoParaInteiro(texto_digitado)

    # 2.1.1.2. Exibindo para o usuário os parametros de conversão, revelando que o valor em strin foi convertido para inteiro
    print(f"O valor foi convertido de '{texto_digitado}' para: {numero_convertido} inteiro")

    # 2.1.1.3. Exibe para o usuário a tipagem descritiva sistemica do texto convertido para inteiro
    print(f"Tipagem descritiva sistemica do valor convertido para inteiro: {type(numero_convertido)}")

# 2.2.2. Criando modelo de exceção ('except')
except ValueError as erro: # OBS 2.2.2. -> Essa linha de código condiciona o modelo de exceção com uma variavel de erro que pode ser exibida ao longo das tratativas de exceção do código

    # 2.2.2.1. Exibe para o usuario uma mensagem de erro de durante a execução de exceção de processamento "não bem sucedido" do código
    print(f'Não foi possível executar a conversão... Erro: {erro}')