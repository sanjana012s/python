import random

def game():
    print("you are playing the game..")
    score = random.randint(1, 50)

    # create file if it doesn't exist, then read safely
    with open("cha_9_file_io/highscore.txt", "a+") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print("your score:", score)

    if score > hiscore:
        with open("cha_9_file_io/highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
