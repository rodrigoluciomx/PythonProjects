import random

def random_word():
    randomnum=int(random.uniform(0,170))
    word = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word.append(line.strip("\n"))
    randomword = word.pop(randomnum-1)
    print(randomnum)
    return randomword

def run():
    word = random_word()    
    divided_word = [letters for letters in word]
    result = False
    display=[]
    
    for i in range(0,len(divided_word)):
        display.append("_ ")
    
    while result == False:
        try_letter = input("Escribe una letra: " + "\n")
        for i in range(0,len(divided_word)):
            if try_letter == divided_word[i]:
                display[i] = try_letter
            else:
                result = False
        print(display)
        if display == divided_word:
            print("Felicidades")
            result = True
        else:
            result = False

if __name__ == "__main__":
    run()