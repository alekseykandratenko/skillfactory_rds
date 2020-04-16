import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    low = 1
    high = 100
    count = 1
    predict = np.random.randint(1,100)
    
    while number != predict:
        count+=1
        '''Так как искомое число находится в определённом диапазоне от low до high, то при каждой
        итерации мы можем делить наш диапазон чисел на 2 чтобы понять в каком направлении искать число:
            - либо уменьшать предельный диапазон high если новое число больше искомого
            - либо увеличивать нижний диапазон low если новое число меньше искомого'''
        predict = (low+high)//2
        if predict > number:
            high = predict
        elif predict < number:
            low = predict + 1
    return(count) # выход из цикла, если угадали

score_game(game_core_v2)