print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num': 5, 'team2_num': 6})
print("Команда Волшебники данных решила задач: {count}!".format(count=42))
print("Волшебники данных решили задачи за {time} с !".format(time=18015.2))
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'
if score_1 > score_2:
    print(f'"Результат битвы: победа команды {team_1}!"')
if score_1 < score_2:
    print(f'"Результат битвы: победа команды {team_2}!"')
if score_1 == score_2:
    print(f'"Результат битвы: баллы команд {team_1} и {team_2} равны - ничья!"')
tasks_total = score_1 + score_2
team1_time = 1552.512
team2_time = 2153.31451
time_avg = (team1_time + team2_time)/tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg.__round__(1)} секунды на задачу!')

