list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_players = len(list_players)

players_per_team = total_players // 2

team1 = list_players[:players_per_team]
team2 = list_players[players_per_team:]

print(team1)
print(team2)

# TODO Разделите участников на две команды
