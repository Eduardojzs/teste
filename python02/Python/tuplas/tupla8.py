"""
Exercício: Diferenças entre Listas e Tuplas

Contexto:
Você é o arquiteto de software de uma startup de turismo. Seu software 
precisa lidar com informações sobre destinos turísticos e os feedbacks 
dos usuários sobre esses destinos.

Tarefas:

    1. Destinos Turísticos:
    Cada destino turístico tem informações fixas como nome, país, e um 
    código identificador único. Essas informações não mudam uma vez que o destino é adicionado ao sistema.
    
        Crie uma representação adequada para um destino turístico no sistema.

    2. Feedbacks dos Usuários:
    Os usuários do sistema podem adicionar feedbacks sobre os destinos 
    visitados. Estes feedbacks são dinâmicos, já que os usuários 
    podem adicionar, editar ou deletar seus comentários.
        
        Crie uma representação adequada para armazenar feedbacks de um destino turístico.

    3. Análise:
        Explique por que você escolheu a estrutura de dados 
        específica (lista ou tupla) para cada um dos casos acima.
        
        Dê um exemplo de uma situação em que seria desvantajoso usar a estrutura 
        de dados oposta em cada um dos casos.

Objetivo:
O principal objetivo deste exercício é fazer com que você pense sobre a natureza 
mutável das listas e a natureza imutável das tuplas, e como essa característica influencia 
a decisão de qual estrutura de dados usar em diferentes cenários práticos.
"""


#Solução: Diferenças entre Listas e Tuplas

#1. Destinos Turísticos:

#Como o nome, país e código identificador de um destino turístico 
#são fixos e não mudam uma vez que o destino é adicionado ao 
#sistema, é apropriado usar uma tupla.
destino_turistico = ("Torre Eiffel", "França", "FR-001")

print(destino_turistico)

print()


#2. Feedbacks dos Usuários

#Os feedbacks dos usuários são dinâmicos, e é necessário ter 
#a capacidade de adicionar, editar ou remover comentários. Portanto, uma 
#lista é a estrutura de dados adequada.
feedbacks_torre_eiffel = [
    "Maravilhoso!",
    "A vista é espetacular.",
    "Muito lotado durante a temporada alta."
]

print(feedbacks_torre_eiffel)

print()

#Para adicionar um novo feedback:
feedbacks_torre_eiffel.append("Recomendo visitar à noite.")


print(feedbacks_torre_eiffel)


#3. Análise:
