#!/usr/bin/python
#-*- encoding:UTF-8 -*-

import os
from algoritmo import Age, Number, Measure, PersonalData, Fish, Ink, \
                        Year, Letter, Average, Price, Date_time, Salary
loop = 'SIM'
while loop == 'SIM':
    print 'Para melhor visualização maximize sua tela'
    escolha = input('Programa com seleção (1) ou com repetição (2): ')
    os.system('clear')
    #################____ menu____############
    if escolha == 1:
        print '\n'
        print '                   ESCOLHA UM PROGRAMA       '
        print '\n'
        print ' 1- Programa verifica idade do usuário'
        print ' 2- Programa verifica qual é o maior numero entre 3 digitados'
        print ' 3- Programa converte uma medida de metros para centímetros'
        print ' 4- Programa calcula e informe o volume da caixa'
        print ' 5- Programa calcula o peso ideal de uma pesoa'
        print ' 6- Programa calcula a multa para o peso excedente de peixes'
        print ' 7- Programa calcula as orçamento para pintura'
        print ' 8- Programa informa se o valor é negativo'
        print ' 9- Programa informa o sexo pela letra'
        print '10- Programa determina ano Bissexto'
        print '11- Programa verifique se uma letra digitada é vogal ou consoante'
        print '12- Programa calcula a média alcançada pelo aluno'
        print '13- Programa informa qual produto você deve comprar'
        print '14- Programa imprime mensagem simpática'
        print '16- Programa aumento no salário'
        print '17- Programa calcula folha de pagamento'
        print '18- Programa lê um número e exibe o dia correspondente da semana'
        print '19- Programa emite o preço junto de sua procedência'
        print '20- Programa que emite o conceito do aluno'
        print '21- Programa que emite o conceito final do aluno'
        print '22- Programa que define o tipo de trângulo'
        print '23- Programa imprime a quantidade de centenas, dezenas e unidades um numero'
        print '24- Programa classifica idade da turma'

        ##################_____seleçao____##########

        opcao = input('Entre com o numero do programa que deseja executar: ')
        os.system('clear')

        if opcao == 1:
            print ' 1- Programa verifica idade do usuário'
            if (Age(input('Entre com a idade: ')).adult()) == "Minor":
                print "Idade menor que 21 anos"
            else:
                print "Idade maior que 21 anos"

        if opcao == 2:
            print ' 2- Programa verifica qual é o maior numero entre 3 digitados'
            _number = Number(input('Entre com o primeiro numero: '))
            number2 = input('Entre com o segundo numero: ')
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
            width =  input('Entre com a largura: ')
            height = input('Entre com a altura: ')
            _volume =  Measure().cube_area(length, width, height)
            print "O volume da caixa é %2.f litros"%(_volume)

        if opcao == 5:
            print ' 5- Programa calcula o peso ideal de uma pesoa'
            sex = raw_input('Entre com seu sexo (M ou F): ')
            height = float(input('Entre com sua altura: '))
            result = PersonalData().ideal_weight(sex.upper(), height)
            print "Essa pessoa está %s"%(result)

        if opcao == 6:
            print ' 6- Programa calcula a multa para o peso excedente de peixes'
            print Fish(input('Entre com a quantidade de peixes: ')).penalty()

        if opcao == 7:
            print ' 7- Programa calcula as orçamento para pintura'
            tintas = Ink(input('Entre com a área a ser pintada (em metro): '))
            print tintas.amount()
            print tintas.buying_cans()
            print tintas.buying_gallons()

        if opcao == 8:
            print ' 8- Programa informa se o valor é negativo'
            print Number(input('Entre com um numero: ')).positive()

        if opcao == 9:
            print ' 9- Programa informa o sexo pela letra'
            print PersonalData(raw_input('Entre com seu sexo (M ou F): ')).sex_person()

        if opcao == 10:
            print '10- Programa determina ano Bissexto'
            print Year(input('Entre com um ano: ')).leap_year()

        if opcao == 11:
            print '11- Programa verifique se uma letra digitada é vogal ou consoante'
            print Letter(raw_input('Entre com a letra: ')).vowel()

        if opcao == 12:
            print '12- Programa calcula a média alcançada pelo aluno'
            Average(input('Entre com a primeira nota: '))
            other = input('Entre com a segunda nota: ')
            print Average().concept(other)

        if opcao == 13:
            print '13- Programa informa qual produto você deve comprar'
            price1 = Price(float(input('Entre com o primeiro preço: ')))
            price2 = float(input('Entre com o segundo preço: '))
            price3 = float(input('Entre com o terceiro preço: '))
            print price1.cheaper(price2, price3)

        if opcao == 14:
            print '14- Programa imprime mensagem simpática'
            print Date_time(raw_input('Entre com o período do dia( M , V     ou N): ')).day_shift()

        if opcao == 16:
            print '16- Programa aumento no salário'
            salario = Salary(float(input('Entre com seu salário: ')))
            print salario
            print salario.percentage()
            print salario.increase()
            print salario.new_salary()

        if opcao == 17:
            print '17- Programa calcula folha de pagamento'
            value_time = float(input('Entre com o valor da sua hora de trabalho: '))
            hour_months= input('Entre com o total de horas trabalhadas no mês: ')
            salario = Salary(value_time * hour_months)
            print salario
            print salario.IR_Discount()
            print salario.INSS_Discount()
            print salario.FGTS_Discount()
            print salario.total_Discounts()
            print salario.final_salary()

        if opcao == 18:
            print '18- Programa lê um número e exibe o dia correspondente da semana'
            print Date_time(input('Entre com o numero')).day_week()

        if opcao == 19:
            print '19- Programa emite o preço junto de sua procedência'
            price = Price(float(input('Entre com o preço do produto: ')))
            print price.provenance(input('Entre com o código procedência do produto: '))

        if opcao == 20:
            print '20- Programa que emite o conceito do aluno'
            nota = Average(input('Entre com a primeira parcial: '))
            print nota.letter_concept(input ('Entre com a segunda parcial: '))

        if opcao == 21:
            print '21- Programa que emite o conceito final do aluno'
            nota = Average(input('Entre com a primeira parcial: '))
            print nota.final_concetp(input ('Entre com a segunda parcial: '))

        if opcao == 22:
            print '22- Programa que define o tipo de trângulo'
            medida = Measure()
            side1 = float(input('Entre com a medida do lado 1: '))
            side2 = float(input('Entre com a medida do lado 2: '))
            side3 = float(input('Entre com a medida do lado 3: '))
            print medida.type_triangle(side1, side2, side3)

        if opcao == 23:
            print '23- Programa imprime a quantidade de centenas, dezenas e unidades um numero'
            print Number(input('Entre com o numero: ')).full_name()


        if opcao == 24:
            print '24- Programa classifica idade da turma'
            _age = Age(input('Entre com a primeira idade: '))
            age2 = input('Entre com a segunda idade: ')
            age3 = input('Entre com a terceira idade: ')
            print _age.mid_class(age2, age3)


    if escolha == 2:

        from algo_rep import Number2, Temperature, Eleicao, Measure2, Dados, Caixa

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
            print Number2(input('Entre com o número: ')).prime()

        if opcao == 26:
            print '26- Programa imprime a tabela de equivalência de graus Fahrenheit para Centígrados.'
            t = Temperature()
            start = input('Entre com a primeira temperatura em Fahrenheit: ')
            stop = input('Entre com a segunda temperatura em Fahrenheit: ')
            print t.to_Celsius(start,stop)

        if opcao == 27:
            print '27- Programa calcula somatória do inversos.'
            print Number2(input('Entre com o número: ')).formula()

        if opcao == 28:
            print '28- Programa calcula o fatorial de um numero.'
            print Number2(input('Entre com o número: ')).factorial()

        if opcao == 29:
            print '29- Programa imprima a série de Fibonacci.'
            print Number2(input('Entre com o número: ')).fibonacci_set()
        if opcao == 30:
            print '30- Programa calcula o pagamento do Monge.'
            print Number2(input('Entre com o número: ')).pay_grains()

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
            n = Number2()
            print n.media_varios()

        if opcao == 34:
            print '34- Programa identifica qual foi o maior número digitado, entre vários.'
            print 'Para encerrar digite (-1)'
            n = Number2()
            print n.maior_com_repeticao()

        if opcao == 35:
            print '35- Programa compara vários números.'
            n = Number2()
            print n.maior_com_repeticao_35()

        if opcao == 36:
            print '36- Programa informar a média de alturas, a mais baixa e a mais alta entre 20 pessoas.'
            print Dados().maior_altura()

        if opcao == 37:
            print '37- Programa apura o sexo e a idade de 40 pessoas.'
            print Dados().sexo_idade()
        if opcao == 39:
            print '39- Programa de Caixa Eletrônico.'
            print Caixa().caixa_eletronico()

#        if opcao == 40:
#            print '40- Programa pesquisa de opinião.'
#        if opcao == 41:
#            print '41- Programa pesquisa de opinião do Mercado.'
#        if opcao == 42:
#            print '42- Programa calcula a área de figuras geométricas.'
#        if opcao == 43:
#            print '43- Programa trabalha com prismas triangulares regulares.'


















        ##################_____retorno_do_loop____##########
    loop_num = raw_input('Para continuar digite (SIM)')
    loop = loop_num.upper()

    os.system('clear')

