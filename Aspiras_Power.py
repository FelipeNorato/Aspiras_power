#!/usr/bin/python
#-*- encoding:UTF-8 -*-

import os
from Modulos.algoritmo import Age, Number, Measure, PersonalData, Fish, Ink, \
                        Year, Letter, Average, Price, Date_time, Salary
loop = 'S'
while loop == 'S':
    print 'Para melhor visualização maximize sua tela'
    escolha = input('Programa com seleção (1) ou com repetição (2): ')
    os.system('clear')
    #################____ menu____############
    if escolha == 1:
        print '\n'
        print '                   ESCOLHA UM PROGRAMA       '
        print '\n'
        print ' 1- Programa verifica idade do usuário'
        print ' 2- Programa verifica qual é o maior número entre 3 digitados'
        print ' 3- Programa converte uma medida de metros para centímetros'
        print ' 4- Programa calcula e informa o volume da caixa'
        print ' 5- Programa calcula o seu peso ideal'
        print ' 6- Programa calcula multa para o peso excedente de peixes'
        print ' 7- Programa calcula orçamento para pintura'
        print ' 8- Programa informa se o valor é positivo ou negativo'
        print ' 9- Programa informa sexo pela letra'
        print '10- Programa determina ano Bissexto'
        print '11- Programa verifique se letra digitada é vogal ou consoante'
        print '12- Programa calcula média alcançada pelo aluno'
        print '13- Programa informa qual produto deve ser comprado'
        print '14- Programa imprime mensagem simpática'
        print '16- Programa calcula aumento do salário'
        print '17- Programa calcula folha de pagamento'
        print '18- Programa lê um número e exibe o dia correspondente da semana'
        print '19- Programa emite o preço junto de sua procedência'
        print '20- Programa emite o conceito do aluno'
        print '22- Programa define o tipo de triângulo'
        print '23- Programa imprime a quantidade de centenas, dezenas e unidades de um numero'
        print '24- Programa classifica idade da turma'

        ##################_____seleçao____##########

        opcao = input('Entre com o numero do programa que deseja executar: ')
        os.system('clear')
        print
        if opcao == 1:
            print ' 1- Programa verifica idade do usuário'
            if (Age(input('Entre com a idade: ')).adult()) == "Minor":
                print "Idade menor que 21 anos"
            else:
                print "Idade maior que 21 anos"

        if opcao == 2:
            print ' 2- Programa verifica qual é o maior numero entre 3 digitados'
            _number = Number(input('Entre com o primeiro numero: '))
            number2 = input('Entre com o segundo numero.: ')
            number3 = input('Entre com o terceiro numero: ')
            result = _number.greaterNumber(number2, number3)
            print "O maior dos três números é o %i"%(result)

        if opcao == 3:
            print ' 3- Programa converte uma medida de metros para centímetros'
            _measure_m = float(input('Entre com a medida em metros: '))
            _measure_cm = Measure(_measure_m).metersToCent()
            print "%2.f metros equivalem a %2.f centímetros"%(_measure_m, _measure_cm)

        if opcao == 4:
            print ' 4- Programa calcula e informe o volume da caixa'
            length = input('Entre com o comprimento: ')
            width =  input('Entre com a largura....: ')
            height = input('Entre com a altura.....: ')
            _volume =  Measure().cube_area(length, width, height)
            print "O volume da caixa é %2.f litros"%(_volume)

        if opcao == 5:
            print ' 5- Programa calcula o peso ideal de uma pesoa'
            sex = raw_input('Entre com seu sexo (M ou F): ')
            height = float(input('Entre com sua altura.......: '))
            weight = float(input('Entre com seu peso.........: '))
            result = PersonalData().ideal_weight(sex.upper(), height, weight)
            print "Essa pessoa está %s"%(result)

        if opcao == 6:
            print ' 6- Programa calcula a multa para o peso excedente de peixes'
            peso = input('Entre com o peso total da pesca: ')
            excesso, multa = Fish(peso).penalty()
            print "Peso pescado....: %2.1f Kg"%(peso)
            print "Execesso de peso: %2.1f Kg"%(excesso)
            print "Multa...........: %2.2f reais"%(multa)

        if opcao == 7:
            print ' 7- Programa calcula as orçamento para pintura'
            tintas = Ink(input('Entre com a área a ser pintada (em metro): '))
            liters = tintas.amount()
            print "Litros de tinta Necessários: %2.f"%(liters)
            print "- - - EM LATAS - - -"
            tuple1 = tintas.buying_cans(liters)
            print "Quantidade necessária de latas: %i"%(tuple1[0])
            print "Preço em latas................: R$ %2.2f"%(tuple1[1])
            print
            print "- - - EM GALÕES - - -"
            tuple2 = tintas.buying_gallons(liters)
            print "Quantidade necessária de galões: %i"%(tuple2[0])
            print "Preço em galões................: R$ %2.2f"%(tuple2[1])

        if opcao == 8:
            print ' 8- Programa informa se o valor é positivo ou negativo'
            value = input('Entre com um numero: ')
            result = Number(value).positive()
            print "%i is %s"%(value, result)

        if opcao == 9:
            print ' 9- Programa informa o sexo pela letra'
            letter = raw_input('Entre com seu sexo (M ou F): ')
            result = PersonalData(letter).sex_person()
            print "%s - %s"%(letter, result)

        if opcao == 10:
            print '10- Programa determina ano Bissexto'
            year = input('Entre com um ano: ')
            result = Year(year).leap_year()
            print "%i - %s"%(year, result)

        if opcao == 11:
            print '11- Programa diz se letra digitada é vogal ou consoante'
            letter = raw_input('Entre com a letra: ')
            result = Letter(letter).vowel()
            print "%s is an %s"%(letter, result)

        if opcao == 12:
            print '12- Programa calcula a média alcançada pelo aluno'
            note1 = input('Entre com a primeira nota: ')
            note2 = input('Entre com a segunda nota: ')
            result = Average(note1).concept(note2)
            print "Average: %2.1f   -   %s"%((note1 + note2) / 2, result)

        if opcao == 13:
            print '13- Programa informa qual produto você deve comprar'
            price1 = Price(float(input('Entre com o primeiro preço: ')))
            price2 = float(input('Entre com o segundo preço: '))
            price3 = float(input('Entre com o terceiro preço: '))
            result = price1.cheaper(price2, price3)
            print "Buy the product price R$ %2.2f"%(result)

        if opcao == 14:
            print '14- Programa imprime mensagem simpática'
            print "M - Turno da Manhã"
            print "V - Turno da Tarde"
            print "N - Turno da Noite"
            letter = raw_input('Entre com o período do dia(M , V ou N): ')
            print "%s   -   %s"%(letter.upper(), Date_time(letter).day_shift())


        if opcao == 16:
            print '16- Programa aumento no salário'
            salary = Salary(float(input('Entre com seu salário: ')))
            print "Starting Salary....: R$ %2.2f"%(salary)
            print "Percentage Increase: %s"%(salary.percentage())
            print "Value of Increase..: R$ %2.2f"%(salary.increase())
            print "Value of New Salary: R$ %2.2f"%(salary.new_salary())

        if opcao == 17:
            print '17- Programa calcula folha de pagamento'
            value_time = float(input('Entre com o valor da sua hora de trabalho: '))
            hour_months= input('Entre com o total de horas trabalhadas no mês: ')
            salary = Salary(value_time * hour_months)
            print "Starting Salary: R$ %2.2f"%(salary)
            print "IR Discount....: R$ %2.2f"%(salary.IR_Discount())
            print "INSS Discount..: R$ %2.2f"%(salary.INSS_Discount())
            print "FGTS Discount..: R$ %2.2f"%(salary.FGTS_Discount())
            print "Total Discounts: R$ %2.2f"%(salary.total_Discounts())
            print "Final Salary...: R$ %2.2f"%(salary.final_salary())

        if opcao == 18:
            print '18- Programa lê um número e exibe o dia correspondente da semana'
            number = input('Entre com o numero: ')
            print "%i   -   %s"%(number, Date_time(number).day_week())

        if opcao == 19:
            print '19- Programa emite o preço junto de sua procedência'
            price = Price(float(input('Entre com o preço do produto: ')))
            print price.provenance(input('Entre com o código procedência do produto: '))

        if opcao == 20:
            print '20- Programa que emite o conceito do aluno'
            note1 = input('Entre com a primeira nota: ')
            note2 = input ('Entre com a segunda nota: ')
            result = Average(note1).letter_concept(note2)
            print "Average...: %2.1f"%(result[0])
            print "Concept...: %s"%(result[1])
            print "Conclusion: %s"%(result[2])

        if opcao == 22:
            print '22- Programa que define o tipo de trângulo'
            medida = Measure()
            side1 = float(input('Entre com a medida do lado 1: '))
            side2 = float(input('Entre com a medida do lado 2: '))
            side3 = float(input('Entre com a medida do lado 3: '))
            result = medida.type_triangle(side1, side2, side3)
            if len(result) == 2:
                print "%s and your name is %s"%(result[0], result[1])
            else:
                print "%s"%(result)

        if opcao == 23:
            print '23- Programa imprime a quantidade de centenas, dezenas e unidades um numero'
            print Number(input('Entre com o numero: ')).full_name()


        if opcao == 24:
            print '24- Programa classifica idade da turma'
            age1 = input('Entre com a primeira idade: ')
            age2 = input('Entre com a segunda idade: ')
            age3 = input('Entre com a terceira idade: ')
            result =  Age(age1).mid_class(age2, age3)
            print "Average: %2.1f  -  Classification: %s"%(result[0], result[1])


    if escolha == 2:

        from Modulos.algo_rep import Number2, Temperature, Eleicao, Measure2, \
        Dados, Caixa, Resposta, Medidas

    #################____ menu____############

        print '\n'
        print '                   ESCOLHA UM PROGRAMA       '
        print '\n'
        print '25- Programa verifica se o número é primo.'
        print '26- Programa imprime a tabela de equivalência de graus Fahrenheit para Centígrados.'
        print '27- Programa calcula somatória do inversos.'
        print '28- Programa calcula o fatorial de um numero.'
        print '29- Programa imprima a série de Fibonacci.'
        print '30- Programa calcula o pagamento do Monge.'
        print '31- Programa apura uma eleição.'
        print '32- Programa calcula equivalencia de altura.'
        print '33- Programa pergunta 10 números e informar a soma, a média e o maior dos números lidos.'
        print '34- Programa identifica qual foi o maior número digitado, entre vários.'
        print '35- Programa compara vários números.'
        print '36- Programa informar a média de alturas, a mais baixa e a mais alta entre 20 pessoas.'
        print '37- Programa apura o sexo e a idade de 40 pessoas.'
        print '39- Programa de Caixa Eletrônico.'
        print '40- Programa pesquisa de opinião.'
        print '41- Programa pesquisa de opinião do Mercado.'
        print '42- Programa calcula a área de figuras geométricas.'
        print '43- Programa trabalha com prismas triangulares regulares.'

        ##################_____seleçao____##########

        opcao = input('Entre com o numero do programa que deseja executar: ')
        os.system('clear')

        if opcao == 25:
            print '25- Programa verifica se o número é primo.'
            number = input('Entre com o número: ')
            result = Number2(number).prime()
            if result == True:
                print "%i é primo"%(number)
            else:
                print "%i não é primo"%(number)

        if opcao == 26:
            print '26- Programa imprime a tabela de equivalência de graus Fahrenheit para Centígrados.'
            t = Temperature()
            start = input('Entre com a primeira temperatura em Fahrenheit: ')
            stop = input('Entre com a segunda temperatura em Fahrenheit: ')
            print t.to_Celsius(start,stop)

        if opcao == 27:
            print '27- Programa calcula somatória do inversos.'
            number = input('Entre com o número: ')
            result = Number2(number).formula()
            print "A soma de 1/1 até 1/%i é igual a %f"%(number, result)

        if opcao == 28:
            print '28- Programa calcula o fatorial de um numero.'
            number = input('Entre com o número: ')
            result = Number2(number).factorial()
            print "Fatorial de %i é igual a %i"%(number, result)

        if opcao == 29:
            print '29- Programa imprima a série de Fibonacci.'
            number = input('Entre com o número: ')
            result = Number2(number).fibonacci_set()
            print "A série Fibonacci com %i dígitos é: %s"%(number, result)

        if opcao == 30:
            print '30- Programa calcula o pagamento do Monge.'
            result = Number2(64).pay_grains()
            print "O pagamento do monge é %f grãos"%(result)

        if opcao == 31:
            print '31- Programa apura uma eleição.'
            e = Eleicao()
            e.apuracao()

        if opcao == 32:
            print '32- Programa calcula equivalencia de altura.'
            s_height = input('Entre com a primeira altura em Centímetros: ')
            s_development = input('Entre com o primeiro desenvolvimento cm/ano: ')
            other_height = input('Entre com a segunda altura em Centímetros: ')
            other_development = input('Entre com o segundo desenvolvimento cm/ano: ')
            print Measure2().same_height(s_height, s_development, other_height, other_development)

        if opcao == 33:
            print '33- Programa pergunta 10 números e informar a soma, a média e o maior dos números lidos.'
            result = Number2().media_varios()
            print "Soma.................: %i"%(result[0])
            print "Média................: %2.1f"%(result[1])
            print "Maior número digitado: %i"%(result[2])

        if opcao == 34:
            print '34- Programa identifica qual foi o maior número digitado, entre vários.'
            print 'Para encerrar digite (-1)'
            result = Number2().maior_com_repeticao()
            print "Maior número digitado: %i"%(result)

        if opcao == 35:
            print '35- Programa compara vários números.'
            result = Number2().maior_com_repeticao_35()
            print "Soma........: %i"%(result[0])
            print "Média.......: %2.1f"%(result[1])
            print "Maior Número: %i"%(result[2])
            print "Menor Número: %i"%(result[3])

        if opcao == 36:
            print '36- Programa informar a média de alturas, a mais baixa e a mais alta entre 20 pessoas.'
            result = Dados().maior_altura()
            print "Average of heights: %1.1f"%(result[0])
            print "More height.......: %1.1f"%(result[1])
            print "Minor height......: %1.1f"%(result[2])

        if opcao == 37:
            print '37- Programa apura o sexo e a idade de 40 pessoas.'
            print Dados().sexo_idade()

        if opcao == 39:
            print '39- Programa de Caixa Eletrônico.'
            print Caixa().caixa_eletronico()

        if opcao == 40:
            print '40- Programa pesquisa de opinião.'
            Resposta().apresentacao()

        if opcao == 41:
            print '41- Programa pesquisa de opinião do Mercado.'
            Dados().processamento()

        if opcao == 42:
            print '42- Programa calcula a área de figuras geométricas.'
            Medidas().area()

        if opcao == 43:
            print '43- Programa trabalha com prismas triangulares regulares.'
            Medidas().prisma()

        ##################_____retorno_do_loop____##########
    loop = raw_input('Para continuar digite S: ').upper()
    os.system('clear')

print "Programa feito pelos Aspiras Felipe Norato Lacerda e João Felipe Roque Moraes"
print "'Nos mostrou que além de fazer café, estamos aprendendo também a programar!'"
print "Abraços"
input()

