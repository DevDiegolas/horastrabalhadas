#Guardando quantas aulas de cada dia
sabado = int(input("Coloque quantos sábados deu aula: "))
segunda = int(input("Coloque quantas segundas deu aula: "))
quarta = int(input("Coloque quantas quartas deu aula: "))
sexta = int(input("Coloque quantas sextas deu aula: "))
print()

#Conta utilizando como base o site 
sabadoaula = sabado * 1.50
segundaaula = segunda * 1.50
quartaaula = quarta * 1.50
sextaaula = sexta * 1.50

#Contas utilizando o site como base
totalaulas = segunda + quarta + sexta + sabado
totalhoras = sabadoaula + segundaaula + quartaaula + sextaaula
total = totalaulas * 37.50

#Transformando em inteiro
total = int(total)
totalhoras = int(totalhoras)

#Printando tudo
print("O total de horas trabalhadas é:", totalhoras)
print("O total de aulas é:", totalaulas)
print("O total de dinheiro recebido é:", total)
