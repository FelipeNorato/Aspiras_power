#-*- encoding:UTF-8 -*-
import math
import os
class Number2(int):

        # Question 25
    def prime(self):
        div = 1
        if self == 1:
            return False
        for n in range(2,self+1):
            if self%n == 0:
                div += 1
        if div == 2:  return True
        return False

        # Question 27
    def formula(self):
        H = 0
        for N in range(1, self + 1):
            H += 1. / N
        return H

        # Question 28
    def factorial(self):
        if self == 0:
            return 1
        return self * Number2(self - 1).factorial()

        # Question 29
    def fibonacci_set(self):
        if self in (0, 1, 2):
            return [1] * self
        result = [1, 1]
        for n in range(2, self):
            result.append(result[n-2] + result[n-1])
        return result

        # Question 30
    def pay_grains(self):
        return (2**64) - 1

        # Question 33
    def media_varios(self):
        maior,soma = 0, 0
        for i in range(1 , 11):
            num = input('Número %i: '%(i))
            if num > maior:
                maior = num
            soma += num
        media = soma / 10
        return soma, media, maior

          # Question 34
    def maior_com_repeticao(self):
        maior = 0
        cont = 1
        num = input('Entre com numero: ')
        while num != -1 :
            if cont == 1:
                maior = num
            elif num > maior:
                maior = num
            cont += 1
            num = input('Entre com numero: ')
        return maior

             # Question 35
    def maior_com_repeticao_35(self):
        lista = []
        n = input('Quantidade de numeros: ')
        for i in range(1, n + 1):
            num = input("Número %i: "%(i))
            lista.append(num)
        sum_ = sum(lista)
        average = sum_ / n
        more = max(lista)
        minor = min(lista)
        return sum_, average, more, minor


class Temperature(int):
        # Question 26
    def to_Celsius(self, start, stop):
        self = []
        print "Fahrenheit ----------- Celsius"
        for temperature in range(start, stop + 1):
            value = float(5. / 9) * ( temperature - 32)
            print "    %i ---------------- %2.1f"%(temperature, value)
            self.append(value)
        return '' #self  # nao estamos retornando o objeto, pois estamos retornando uma tabela.

class Measure2(int):
        # Question 32
    def same_height(self):
        pedro_height, jose_height = 110, 150
        years = 0
        while pedro_height < jose_height:
            pedro_height += 3
            jose_height += 2
            years += 1
        return years

class Dados():
        # Question 36
    def maior_altura(self):
        heights = []
        for i in range(1, 5):
            height = input("Altura da pessoa %i: "%(i))
            heights.append(height)
        average = sum(heights) / 20.
        more_height = max(heights)
        minor_height = min(heights)
        return average, more_height, minor_height

        # Question 37
    def sexo_idade(self):
        cont, contM, contF, somaM, somaF = 0, 0, 0, 0, 0
        for i in range(1, 3):
            sex = raw_input('Entre com sexo: ')
            sexo = sex.upper()
            idade = float(input('Entre com Idade: '))
            if sexo == 'M':
                somaM += idade
                contM +=1
            elif sexo == 'F':
                somaF += idade
                contF +=1
            cont += 1
        media_idades = float(somaF + somaM) / 2
        media_homem = somaM / contM
        print "Média Idades.......: %2.1f"%(media_idades)
        print "Média Idades Homens: %2.1f"%(media_homem)
        print "Total Mulheres.....: %i"%(contF)

        # Question 41
    def _escolha(self):
        import os
        print "F ou M para Sexo"
        print "S ou N para Resposta"
        print ''
        sexo = raw_input("F ou M: ").upper()
        resposta = raw_input("S ou N: ").upper()
        os.system("clear")
        while ((sexo != "F") and (sexo != "M")) or ((resposta != "S") and (resposta != "N")):
            sexo = raw_input("Apenas F ou M: ").upper()
            resposta = raw_input("Apenas S ou N:").upper()
        return sexo, resposta

    def processamento(self):
        conth, contm, conts_h, conts_m, contn_h, contn_m = 0, 0, 0, 0, 0, 0
        for i in range(1,6):
            sexo, resposta = self._escolha()
            print
            if (sexo == "M"):
                conth = conth + 1
                if (resposta == "S"):
                    conts_h = conts_h + 1
                else:
                    contn_h = contn_h + 1
            else:
                contm = contm + 1
                if (resposta == "S"):
                    conts_m = conts_m + 1
                else:
                    contn_m = contn_m + 1
        if (contm == 0):
            pf = "NULO"
        else:
            pf = conts_m * 100 / contm
        if (conth == 0):
            pm = "NULO"
        else:
            pm = contn_h * 100 / conth
        sim = conts_h + conts_m
        nao = contn_h + contn_m
        print
        print "Numero total de pessoas.....................: %s"%(conth + contm)
        print "Numero de pessoas que responderam SIM.......: %i"%(sim)
        print "Numero de pessoas que responderam NAO.......: %i"%(nao)
        print "Porcentagem das mulheres que responderam SIM: %s %%"%(pf)
        print "Porcentagem dos homens que responderam NAO..: %s %%"%(pm)

class Eleicao(int):

        # Question 31
    def apuracao(self):
        voto = input('Entre com seu voto: ')
        votos = []
        while voto > 5:
            voto = input('Entre com um voto valido: ')
        while voto != 0:
            votos.append(voto)
            voto = input ('Entre com seu voto: ')
            while voto > 5:
                voto = input('Entre com um voto valido: ')
        votos_invalidos = votos.count(4) + votos.count(5)
        invalivos_total = (float(votos_invalidos)/len(votos)) * 100
        print 'candidato 1..................: %i'%(votos.count(1))
        print 'candidato 2..................: %i'%(votos.count(2))
        print 'candidato 3..................: %i'%( votos.count(3))
        print 'votos em branco..............: %i'%(votos.count(4))
        print 'votos nulos..................: %i'%(votos.count(5))
        print 'percentual de votos invalidos: %.2f %%'%(invalivos_total), '%'

class Caixa():
        # Question 39

    def _menu(self):
        print '1 - Depósito'
        print '2 - Retirada'
        print '3 - Saldo'
        print '4 - Sair do algoritmo'

    def _escolha(self):
        import os
        operacao = input('Operação: ')
        while (operacao != 1) and (operacao != 2) and (operacao !=3) and (operacao != 4):
            os.system("clear")
            self._menu()
            operacao = input('Apenas 1, 2, 3 ou 4: ')
        return operacao

    def caixa_eletronico(self):
        import os
        self._menu()
        operacao = self._escolha()
        conta = 0.00
        os.system("clear")
        while operacao != 4:
            if operacao == 1:
                valor = float(input('Entre como Valor do Depósito: '))
                conta += valor
                os.system("clear")
            elif operacao == 2:
                valor = float(input('Entre como Valor da Retirada: '))
                if valor <= conta: conta -= valor
                else:
                    print 'Operação indisponível!'
            elif operacao == 3:
                print '\n' * 1
                print 'Saldo: R$ %.2f'%(conta)
                print '\n' * 1
            self._menu()
            operacao = self._escolha()
            os.system("clear")
        return "Operação Encerrada"

class Resposta():
        # Question 40

    def _menu(self):
        print
        print "--- MENU ---"
        print "S - SIM"
        print "N - Nao"
        print "Outra letra para sair"
        print

    def _escolha(self):
        opcao = raw_input("Sua escolha: ").upper()
        os.system("clear")
        return opcao

    def processamento_x(self):
        conts, contn = 0, 0
        self._menu()
        opcao = self._escolha()
        while ((opcao == "S") or (opcao == "N")):
            if (opcao == "S"):
                conts += 1
            else:
                contn += 1
            self._menu()
            opcao = self._escolha()
        if (conts > contn):
            res = "Bom"
        elif (conts == contn):
            res = "Empate"
        else:
            res = "Ruim"
        return conts, contn, res

    def apresentacao(self):
        conts, contn, res = self.processamento_x()
        print
        print "--- --- --- Conclusão --- --- ---"
        print
        print("Quantidade Sim: " + str(conts))
        print("Quantidade Nao: " + str(contn))
        print("Resultado.....: " + res)

class Medidas():
    # Question 42
    def escolha_area(self):
        print
        print "--- --- ---   MENU   --- --- ---"
        print "1 - Calcular Área do Quadrado"
        print "2 - Calcular Área do Retângulo"
        print "3 - Calcular Área do Triângulo"
        print "4 - Calcular Área do Círculo"
        print "5 - Sair"
        opcao = input("Opcao: ")
        while (opcao <= 0) or (opcao > 5):
            opcao = input("Digite uma opção válida: ")
        return opcao

    def area(self):
        import os
        opcao = self.escolha_area()
        while (opcao != 5):
            os.system("clear")
            if (opcao == 1):
                print
                print("Calcular Área do Quadrado")
                print
                base = input("Base..: ")
                altura = input("Altura: ")
                aq = base * altura
                print("Área do Quadrado: " + str(aq))
            elif (opcao == 2):
                print("Calcular Área do Retângulo")
                base = input("Base..: ")
                altura = input("Altura: ")
                ar = base * altura
                print("Área do Retângulo: " + str(ar))
            elif (opcao == 3):
                print("Calcular Área do Triângulo")
                base = input("Base..: ")
                altura = input("Altura: ")
                at = (base * altura) / 2
                print("Area do Triângulo: " + str(at))
            elif (opcao == 4):
                print("Calcular Área do Círculo")
                raio = input("Raio.: ")
                ac = 3.14 * raio**2
                print("Área do Círculo: " + str(ac))
            opcao = self.escolha_area()
        print
        print("FIM do Programa")

    # Question 43
    def escolha(self):
        print "--- --- MENU --- ---"
        print("1 - Novo Volume")
        print("0 - Sair")
        print
        opcao = input("Opçao: ")
        while (opcao != 0) and (opcao != 1):
            opcao = input("Apenas O ou 1: ")
        print
        return opcao

    def prisma(self):
        import os
        cont, soma = 0, 0
        opcao = self.escolha()
        while opcao != 0:
            cont = cont + 1
            altura = input("Altura: ")
            lado = input("Lado: ")
            al = 3 * (altura * lado)
            ab = 1.7 * lado**2
            at = (2 * ab) + al
            vol = ab * altura
            if cont == 1:
                menor_al = al
                maior_ab = ab
                np = cont
            elif al < menor_al:
                menor_al = al
            if ab > maior_ab:
                maior_ab = ab
                np = cont
            soma = soma + at
            print "Volume do Prisma %i: %4.1f"%(cont, vol)
            print
            opcao = self.escolha()
            os.system("clear")
        if cont == 0:
            print("NENHUM VALOR INSERIDO")
        else:
            media = soma / cont
            print "Conclusões"
            print
            print "Número do Prisma de Maior Área da Base: %i"%(np)
            print "Valor da Menor Área Lateral...........: %2.1f"%(menor_al)
            print "Média das Áreas Totais................: %4.1f"%(media)

