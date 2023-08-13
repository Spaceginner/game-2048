from game import game
import copy
import time

#Init indexes
currentSession = 0
sessions = []

def newSession():
    global sessions

    sessions.append(copy.copy(game(2)))

def closeSession():
    global sessions
    global currentSession

    sessions.pop(currentSession)
    currentSession -= 1

    input("Press ENTER to procceed")

def listSessions():
    global sessions

    print("Sessions:")
    for s in range(len(sessions)):
        print("\tSession number %2d" % (s + 1))

    input("Press ENTER to procceed")

def chooseSession():
    global currentSession
    global sessions

    i = input("Choose session (total %2d sessions, current %1d): " % (len(sessions), currentSession + 1))
    if (int(i) >= len(sessions) + 1):
        print("It seems like entered session index is out of range!")
    else:
        currentSession = int(i) - 1

    input("Press ENTER to procceed")

#Print the board
def print_board(board, score):
    #Clear console
    print("\033[H\033[J", end="")
    print("== SCORE: %8d ==" % score)
    print("+----+----+----+----+")
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if board[i][j] == 0:
                print("    |", end="")
            else:
                print("%4d|" % board[i][j], end="")
        print("\n+----+----+----+----+")

#Play the game
def play():
    global currentSession

    newSession()

    while True:
        if (len(sessions) == 0):
            print("Quiting...")
            time.sleep(1)
            return

        print_board(sessions[currentSession].getBoard(), sessions[currentSession].getScore())
        if (sessions[currentSession].getCheckVars()["isGameOver"]):
            print("##### GAME OVER #####")
            print("# You did %3d moves #" % sessions[currentSession].getMoveCount())
            closeSession()

        move = input("Enter a move: ").upper()
        if move == "W":
            sessions[currentSession].move_up()
        elif move == "S":
            sessions[currentSession].move_down()
        elif move == "D":
            sessions[currentSession].move_right()
        elif move == "A":
            sessions[currentSession].move_left()
        elif move == "Q":
            print("Closing session...")
            time.sleep(1)
            closeSession()
            continue
        elif move == "N":
            newSession()
            print("Created new session")
            input("Press ENTER to procceed")
            continue
        elif move == "C":
            chooseSession()
            continue
        elif move == "L":
            listSessions()
            continue
        elif move == "H":
            print("Help:")
            print("\tUp = W")
            print("\tDown = S")
            print("\tRight = D")
            print("\tLeft = A")
            print("\tClose Session = Q")
            print("\tHelp = H")
            print("\tReset = R")
            print("\tNew Session = N")
            print("\tChoose Session = C")
            print("\tList Sessions = L")
            input("\nPress ENTER to procceed...")
            continue
        elif move == "R":
            sessions[currentSession] = copy.copy(game(2))
        else:
            print("Invalid move! Type H to get help...")
            time.sleep(0.5)
            continue

        sessions[currentSession].update()

if __name__ == "__main__":
    #Run the game
    play()
