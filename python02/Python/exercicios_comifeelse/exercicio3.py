""""
O programa irá informar a classificação
 da nota de acordo com 
os seguintes critérios:
        Excelente: 90-100
        Bom: 70-89
        Satisfatório: 50-69
        Insuficiente: 0-49
        """

nota = int(input('Insira a nota do estudante quando solicitado (entre 0 e 100): '))

if nota >= 90 and nota <= 100:
    
    print("Excelente!")
    
elif nota >= 70 and nota <= 89:
    
    print("Bom!")
    
elif nota >= 50 and nota <= 69:
    
    print("Satisfatório!")
    
else:
    
    print("Insuficiente!")