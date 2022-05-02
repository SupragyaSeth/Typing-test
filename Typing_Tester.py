import random
import time

#Functions
def WPM(l_textinput, l_timetaken):
    list_wordcount = l_textinput.split()
    temp_wordcount = len(list_wordcount)
    wpm = (temp_wordcount * 60) / l_timetaken
    wpm = round(wpm)
    return wpm

def FindAccurayOrTypingErrors(prompt, input, findAccuracy):

    promptlist = prompt
    inputlist = input.split()
    lenth = len(inputlist)
    errors = 0
    count = 0
    if (lenth == 0):
        return -1
    if(findAccuracy == 0):    
        for x in promptlist:
            if (count < lenth ): 
                if (x != inputlist[count]):
                    errors = errors + 1 
            else:
                    errors = errors + 1
            count = count + 1    
            
        return errors
    else:
        split_input = inputlist
        wordcount = len(prompt)
        accuracy = len(set(split_input) & set(prompt))
        accuracy = (accuracy/wordcount) * 100 
        accuracy = round(accuracy)
        return accuracy

#Passages that the user has to type
passage1 = "The big black cat walked down the road"
passage2 = "The green apple grows on the tall tree"
passage3 = "There are many birds in the sky"
passage4 = "The little mouse ate the cheese"
passage5 = "She was sad to hear that fireflies are facing extinction due to habitat loss"
passage6 = "He did not cheat on the test because it was not the right thing to do"

randlist = [passage1, passage2, passage3, passage4, passage5, passage6]
choice = random.choice(randlist)
value = choice.split()

print("\n" + "Type the following sentence")
print( "\n" + choice) 
input("\n Press Enter to start...")

#Finding time
time1 = time.time()
textinput = str(input("\n" + "Enter the sentence: "))
time2 = time.time()
timetaken = time2 - time1

#Output
num_errors = FindAccurayOrTypingErrors(value,textinput,0)
if (num_errors == -1):
    print("Invalid Input. Try Again" )
else:
    num_accuracy = FindAccurayOrTypingErrors(value,textinput, 1)
    print("\n" + "WPM:", WPM(textinput, timetaken), "Accuracy:", str(num_accuracy) + "%" , "Timetaken:", str(round(timetaken)) + "s", "Number of Errors:", str(num_errors))