
def display_board(bl):
    print(f'  {bl [7]}  |   {bl [8]}   |   {bl [9]}')
    print('--------------------')
    print(f'  {bl [4]}  |   {bl [5]}   |   {bl [6]}')
    print('--------------------')
    print(f'  {bl [1]}  |   {bl [2]}   |   {bl [3]}')

    return


def mark_selection(p1, p2):
    p1 = ''
    while p1 not in ['X', 'O']:
        p1 = input('Please select mark for player1 (X,O) : ').upper()

        if p1 == 'X':
            p2 = 'O'
        elif p1 == 'O':
            p2 = 'X'
    return p1, p2


def player1(board, played):
    index_selected_p1 = 'wrong'
    while index_selected_p1 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        index_selected_p1 = input('P1 select index to place mark : ')
        if index_selected_p1 in played:
            index_selected_p1 = 'wrong'
            print('Already selected, select from remaining indexes ')
            continue
        else:
            if index_selected_p1.isdigit():
                played.pop(-0)
                played.append(index_selected_p1)
                played.sort()
                board[int(index_selected_p1)] = player_1
            else:
                index_selected_p1 = 'wrong'
    return board


def player2(board, played):
    index_selected_p2 = 'wrong'
    while index_selected_p2 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        index_selected_p2 = input('P2 select index to place mark : ')
        if index_selected_p2 in played:
            index_selected_p2 = 'wrong'
            print('Already selected, select from remaining indexes ')
            continue
        else:
            if index_selected_p2.isdigit():
                played.pop(-0)
                played.append(index_selected_p2)
                played.sort()
                board[int(index_selected_p2)] = player_2
            else:
                index_selected_p2 = 'wrong'
        return board


def game():

    return (board_list[1] == 'X' and board_list[2] == 'X' and board_list[3] == 'X') or\
           board_list[4] == 'X' and board_list[5] == 'X' and board_list[6] == 'X' or\
           board_list[7] == 'X' and board_list[8] == 'X' and board_list[9] == 'X' or\
           board_list[1] == 'O' and board_list[2] == 'O' and board_list[3] == 'O' or\
           board_list[4] == 'O' and board_list[5] == 'O' and board_list[6] == 'O' or\
           board_list[7] == 'O' and board_list[8] == 'O' and board_list[9] == 'O' or\
           board_list[1] == 'X' and board_list[4] == 'X' and board_list[7] == 'X' or\
           board_list[2] == 'X' and board_list[5] == 'X' and board_list[8] == 'X' or\
           board_list[3] == 'X' and board_list[6] == 'X' and board_list[9] == 'X' or\
           board_list[1] == 'O' and board_list[4] == 'O' and board_list[7] == 'O' or\
           board_list[2] == 'O' and board_list[5] == 'O' and board_list[8] == 'O' or\
           board_list[3] == 'O' and board_list[6] == 'O' and board_list[9] == 'O' or\
           board_list[1] == 'X' and board_list[5] == 'X' and board_list[9] == 'X' or\
           board_list[3] == 'X' and board_list[5] == 'X' and board_list[7] == 'X' or\
           board_list[1] == 'O' and board_list[5] == 'O' and board_list[9] == 'O' or\
           board_list[3] == 'O' and board_list[5] == 'O' and board_list[7] == 'O'


def play_again():
    play = 'wrong'
    while play not in ['Y', 'N']:
        play = input('Do you want to play game Y/N: ').upper()
    return play


playing = play_again()
while playing == 'Y':
    board_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    check_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    played_list = [''] * 9
    display_board(board_list)
    player_1 = ''
    player_2 = ''
    player_1, player_2 = mark_selection(player_1, player_2)
    continue_play = True
    while continue_play:
        if check_list != played_list:
            player1(board_list, played_list)
            display_board(board_list)
            if game():
                print('P1 You have won')
                play_again()
                continue_play = False

            elif check_list != played_list:
                player2(board_list, played_list)
                display_board(board_list)
                if game():
                    print('P2 You have won')
                    play_again()
                    continue_play = False

        else:
            continue_play = False
            print('No player succeeded in winning')
