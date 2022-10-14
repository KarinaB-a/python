'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"'''

import random
from unittest import skip

def input_candies(player_number):
    return int(input(f'{player_number} игрок забирает конфет: '))

def comp_move(comp_candies, candies, player_p_candies):
    take_comp_candies = random.randint(1,min(28, candies))
    print (f'Компьютер забирает {take_comp_candies} конфет')
    comp_candies = comp_candies + take_comp_candies
    candies = candies - take_comp_candies
    print(f'У компьютера {comp_candies} конфет')
    print(f'Конфет на столе осталось {candies} ')
    if candies == 0:
        comp_candies = comp_candies + player_p_candies
        print(f'Компьютер выйграл, с количеством конфет {comp_candies}')
    return comp_candies, candies  

def player_move(player_number, player_candies, candies, player2_candies):
    take_candies = input_candies(player_number)
    while take_candies <= 0 or take_candies > min(28, candies):
        print('За ход можно забрать не более 28 конфет и не более оставшихся конфет! ')
        take_candies = input_candies(player_number)
    else:
        player_candies = player_candies + take_candies
        candies = candies - take_candies
        print(f'У {player_number} игрока {player_candies} конфет ')
        print (f'На столе осталось {candies} конфет ')
        if candies == 0:
            player_candies = player_candies + player2_candies
            print(f'{player_number} игрок забирает все конфеты. {player_number} игрок выйграл с количеством конфет {player_candies}')
    return player_candies, candies

def pvp_mode():
    player1_candies = 0
    player2_candies = 0
    skip_first = random.randint(0,1) == 1
    if skip_first:
        print('Режим игрок2 против игрока1 ')
    else:
        print('Режим игрок1 против игрока2 ')
    candies = int (input('Введите количество конфет, лежащих на столе: '))
    while candies > 0:
        if not skip_first:
            player1_candies, candies = player_move(1, player1_candies, candies, player2_candies)
        skip_first = False     
        if candies == 0:
            return 
        player2_candies, candies = player_move(2, player2_candies, candies, player1_candies) 

def pvc_mode():
    comp_candies = 0
    player_p_candies = 0
    skip_first = random.randint(0,1) == 1
    print('Режим игрок против компьютера ')
    candies = int(input('Введите количество конфет, лежащих на столе: '))
    while candies > 0:
        if not skip_first:
            comp_candies, candies = comp_move(comp_candies, candies, player_p_candies)
        skip_first = False 
        if candies == 0:
            return
        player_p_candies, candies = player_move('', player_p_candies, candies, comp_candies) 

def mode_sel(mode):
    if mode == 1:
        pvp_mode()
    elif mode == 2:
        pvc_mode()
    else:
        print('Данного режима нет ')
mode_s = int(input('Выберите режим игры: "Против другого игрока или против компьютера": '))
mode_sel(mode_s)

        



    



