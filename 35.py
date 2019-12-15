def rps_game(player1, player2):
    if player1=='rock' and player2=='scissors':
        return('1')
        print('congratulations')
    if player1=='rock' and player2=='paper':
        return('2')
        print('congratulations')
    if player1=='paper' and player2=='scissors':
        return('2')
        print('congratulations')
    if player1=='paper' and player2=='rock':
        return('1')
        print('congratulations')
    if player1=='scissors' and player2=='rock':
        return('2')
        print('congratulations')
    if player1=='scissors' and player2=='paper':
        return('1')
        print('congratulations')
    if player1==player2:
        return('draw')
        print('It’s a draw!')