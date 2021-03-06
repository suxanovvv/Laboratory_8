#Алгоритм лінійного пошуку.
while True:
    import numpy as np
    import random
    #Шукаємо наш x у рандомно заданому масиві.
    A=np.zeros(15, dtype=int)
    x=3 #Число, яке ми шукатимемо у лінійному масиві.
    counter=0 #Лічильник, який рахуватиме кількість порівнянь.
    
    for i in range(15):
        A[i]=random.randint(-5,5)#генеруємо рандомні числа для нашого масиву.
    print(A)

    n=len(A)#Якщо кількість порівнянь = n, то елемент не знайдено.
    i=0 #Елемент масиву, який буде порінюватися кожен раз з х.

    while i<n and A[i]!=x:
        i+=1
        counter+=1

    if i==n: #Якщо i = довжині послідовності, то в результаті ітерації не було\
        #знайдено співпадінь з х.
        print('Елемент не знайдений')
    else:
        print(f'На позиції {i} знайдений елемент {x}')
        print('Кількість ітерацій: ', counter)

    '''
    Елемент x=3 знайдеться на i-тій позиції. Наприклад, якщо дана послідовність:
    [0, 2, 1, 5, 6, 3, 2]. Програма буде порівнювати кожне число послідовності з x.
    На кожній ітерації тіла циклу програма буде йти до наступного числа, якщо воно
    не дорінює 3. Бачимо, що у нашому масиві число 3 розташоване на
    позиції 5(індексація з нуля). Отже, кількість порівнянь відбулось 6. Якщо ж
    у послідовності немає числа 3, то перейдемо до гілки else: Елемент не знайдений.
    Тобто, перевірка пройшла по всій довжині масиву n=len(A)і не зайшла жодного
    істинного елементу.
    '''
    #Випадок, коли x не буде знайдено.
    B=np.zeros(6, dtype=int)
    f=6
    count=0

    for j in range(6):
        B[j]= int(input('Введіть число, окрім 6: '))
    print(B)

    p=len(B)
    j=0
        
    while j<p and B[j]!=f:
        j+=1
        count+=1
    if j==p:
        print('Елемент не знайдений')
    else:
        print(f'На позиції {j} знайдений елемент {f}')
        print('Кількість iteration: ', count)
    

            
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
            



