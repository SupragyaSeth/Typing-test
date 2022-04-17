from random import random
import time
import random
import pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

randlist = ["come", "when", "it", "logo"]
random.shuffle(randlist)
wordcount = len(randlist)
print(*randlist)

#Starts pygame
def main():
    
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()

#Calculations
while True:
    t1 = time.time()
    textinput = str(input("Enter the Sentence:"))
    t2 = time.time()
    accuracy = len(set(textinput.split())&set(randlist))
    accuracy = (accuracy/wordcount) * 100
    timetaken = t2 - t1
    wpm = (wordcount * 60) / timetaken

    wpm = round(wpm)
    accuracy = round(accuracy)
    timetaken = round(timetaken)

    print("WPM", wpm, "Accuracy", accuracy , "Timetaken", timetaken)
    break