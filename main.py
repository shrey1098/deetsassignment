x = "Medvedev:Thiem:6-3,4-6,6-3,6-4"

main = []
winner = ""
loser = ""
colon_counter = 0
first_colon_index = 0
game_counter = 0
no_of_bo5 = 0
no_of_bo3 = 0
no_of_setsW = 0
no_of_gamesW = 0
no_of_setsL = 0
no_of_gamesL = 0
for i in range(0, len(x)):

    if x[i] == ":":
        colon_counter = colon_counter + 1
        if colon_counter == 1:
            winner = x[0:i]
            first_colon_index = first_colon_index + i
        elif colon_counter == 2:
            loser = x[first_colon_index+1:i]

    elif x[i] == "-":
        game_counter = game_counter + 1
        if x[i-1] > x[i+1]:
            no_of_gamesW = no_of_gamesW + 1

list = [winner, no_of_bo5, no_of_bo3, no_of_setsW, no_of_gamesW, no_of_setsL, no_of_gamesL]
main.append(list)
print("winner- " + winner)
print("loser- " + loser)
print("game-", game_counter)
print("games won-", no_of_gamesW)

print(main)