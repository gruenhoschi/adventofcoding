outcome_points = [1,3,6] # 0 => Lose, 3 => draw,  6 => win
shape_points   = {"X":1,"Y":2,"Z":3} # 1 => Rock, 2 => Paper, 3 => Scissor
shape_opponent = {"A":1,"B":2,"C":3} # Rock, Paper, Scissor
win_condition  = {1:3,2:1,3:2}
lose_condition = {3:1,1:2,2:3}

f = open("input.txt")

tot_score = 0
win = 0
draw = 0
lost = 0

player = [0,0]

for i in f:
    s = i.split(" ")
    player[0] = shape_opponent.get(s[0])
    expected_outcome = s[1].strip()
    if expected_outcome == "X": #loose
        tot_score += win_condition.get(player[0])
    elif expected_outcome == "Y": #draw
        tot_score += 3 + player[0]
    else: #win
        tot_score += 6 + lose_condition.get(player[0])

print(tot_score)