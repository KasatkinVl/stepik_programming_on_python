n = int(input())
match_list = []
big_dic = {}
count_of_games, wins, draws, loses, total = 0, 0, 0, 0, 0

for i in range(n):
    match_list.append(input().split(';'))

for i in range(len(match_list)):

    big_dic[match_list[i][0]] = [count_of_games, wins, draws, loses, total]
    big_dic[match_list[i][2]] = [count_of_games, wins, draws, loses, total]

for i in range(len(match_list)):

    if int(match_list[i][1]) > int(match_list[i][3]):

        big_dic[match_list[i][0]][0] += 1
        big_dic[match_list[i][0]][1] += 1
        big_dic[match_list[i][0]][2] += 0
        big_dic[match_list[i][0]][3] += 0

        big_dic[match_list[i][2]][0] += 1
        big_dic[match_list[i][2]][1] += 0
        big_dic[match_list[i][2]][2] += 0
        big_dic[match_list[i][2]][3] += 1


    elif int(match_list[i][1]) < int(match_list[i][3]):

        big_dic[match_list[i][0]][0] += 1
        big_dic[match_list[i][0]][1] += 0
        big_dic[match_list[i][0]][2] += 0
        big_dic[match_list[i][0]][3] += 1


        big_dic[match_list[i][2]][0] += 1
        big_dic[match_list[i][2]][1] += 1
        big_dic[match_list[i][2]][2] += 0
        big_dic[match_list[i][2]][3] += 0


    else:
        big_dic[match_list[i][0]][0] += 1
        big_dic[match_list[i][0]][1] += 0
        big_dic[match_list[i][0]][2] += 1
        big_dic[match_list[i][0]][3] += 0

        big_dic[match_list[i][2]][0] += 1
        big_dic[match_list[i][2]][1] += 0
        big_dic[match_list[i][2]][2] += 1
        big_dic[match_list[i][2]][3] += 0

for i in big_dic:
    big_dic[i][4] = (3*big_dic[i][1]) + (big_dic[i][2])


# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

for q, w in big_dic.items():
    print((q+':'), *w, end='\n')