#  Написать тест по математике.
#  генерить примеры на +, -, *
#  проверки хранить в виде функций
#  к функции проверки обращаться по ключу-действию, собрав их в словарь!
#  внешний цикл предлагает решить ещё один пример, либо завершить тест.
#  выводится статистика.


# не получилось со словарем ,не так сделал задание 



import random

def main():
    vsego_primerov=0                       #подсчет количества примеров
    kolichestvo_oshibok=0                  #подсчет количества ошибок
    d='да'
    while d=='да':                          #цикл,предлагающий решить примеры  еще раз
        chislo_1=random.randint(1,10)       #рандомный выбор чисел
        chislo_2=random.randint(1,10)
        #primer = {'+': plus, 
        #           '-': minus,                           
        #          '*': umnojenie}


        def plus(param_1,param_2):           #функция  с примером на сложение
            return param_1 + param_2
        zzz= chislo_1,chislo_2
        res='''Сколько будет %i + %i ?'''    #выводится условие примера
        print(res%(
            chislo_1,
            chislo_2
        ))
        otvet= input('Ваш ответ')
        otvet=int(otvet)
        while otvet!=(plus(*zzz)):          #условие при несоответствии ответа
            print("неа,еще раз")
            kolichestvo_oshibok+=1           #прибавили ошибку
            otvet= int(input('Ваш ответ'))
        print('Браво')
        vsego_primerov+=1                    #прибавили пример


        def minus(param_1,param_2):         #функция  с примером на вычетание
            return param_1 - param_2
        zzz= chislo_1,chislo_2
        res='''Сколько будет  %i - %i='''   #выводится условие примера
        print(res%(
            chislo_1,
            chislo_2
        ))
        otvet= input('Ваш ответ')
        otvet=int(otvet)
        while otvet!=(minus(*zzz)):         #условие при несоответствии ответа
            print("неа,еще раз")
            kolichestvo_oshibok+=1          #прибавили ошибку
            otvet= int(input('Ваш ответ'))
        print('Браво')
        vsego_primerov+=1                   #прибавили пример

        
        def umnojenie(param_1,param_2):     #функция  с примером на умножение
            return param_1 * param_2
        zzz= chislo_1,chislo_2
        res='''Сколько будет %i * %i?'''    #выводится условие примера
        print(res%(
            chislo_1,
            chislo_2
        ))
        otvet= input('Ваш ответ')
        otvet=int(otvet)
        while otvet!=(umnojenie(*zzz)):      #условие при несоответствии ответа
            print("неа,еще раз")
            kolichestvo_oshibok+=1           #прибавили ошибку
            otvet= int(input('Ваш ответ'))
        print('Браво')
        vsego_primerov+=1                    #прибавили пример


        d=input('Еще раз?')                   #предложение о новых примерах
    total='''всего примеров: %i, сделано ошибок:%i''' 
    print(total%(
        vsego_primerov,
        kolichestvo_oshibok
    ))                     
main()  