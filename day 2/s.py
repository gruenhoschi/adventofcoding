outcome_points = [1,3,6] # 0 => Lose, 3 => draw,  6 => win
shape_points   = {"X":1,"Y":2,"Z":3} # 1 => Rock, 2 => Paper, 3 => Scissor
shape_opponent = {"A":1,"B":2,"C":3} # Rock, Paper, Scissor
win_condition  = {1:3,2:1,3:2}


f = open("input.txt")

tot_score = 0
win = 0
draw = 0
lost = 0

player = [0,0]

for i in f:
    s = i.split(" ")
    player[0] = shape_opponent.get(s[0])
    player[1] = shape_points.get(s[1].strip())

    tot_score += player[1]

    if win_condition.get(player[1]) == player[0]:
        print("me winning",player[1],player[0])
        tot_score += 6
        win += 1
    elif player[0] == player[1]:
        print("draw")
        tot_score += 3
        draw += 1
    else:
        print("lost")
        tot_score += 0
        lost += 1
print("win",win)
print("draw", draw)
print("lost",lost)
print(win + draw + lost)
print(tot_score)