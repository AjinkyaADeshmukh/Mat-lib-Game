import time # For time delay
# First creating variables of a story. And removing the words whichever you want.
line1 = '''Once upon a time, there lived a shepherd boy who was bored watching his flock of ______ on the hill. 
To amuse himself, he shouted, “Wolf! Wolf! The sheep are being chased by the wolf!” The villagers came running to help the boy and save the sheep. 
They found nothing and the boy just laughed looking at their angry faces.'''
line2 = '''Don’t cry ‘____’ when there’s no wolf boy!”, they said angrily and left. The boy just laughed at them.'''
line3 = '''After a while, he got bored and cried ‘wolf!’ again, fooling the villagers a second time. 
The angry villagers warned the boy a second time and left. 
The boy continued watching the flock. After a while, he saw a _____ wolf and cried loudly, 
“Wolf! Please help! The wolf is chasing the sheep. Help!”'''
line4 = '''But this time, no one turned up to help. By evening, when the boy didn’t return home, the villagers wondered what happened to him and went up the hill. 
The boy sat on the hill weeping. “Why didn’t you come when I called out that there was a wolf?” he asked angrily. 
“The flock is _____ now”, he said.'''
line5 = '''An old villager approached him and said, “People won’t believe _____ even when they tell the truth. 
We’ll look for your sheep tomorrow morning. Let’s go home now”.'''
line6 = '''Moral
Lying breaks trust. Nobody trusts a liar, even when he is telling the truth.'''
info = '''Welcome to the Mad Lib Game. You have to give an appropriate word for the missing word in the line.
At the end you will get a surprise and the a valuable lesson. You will get three chances to guess the word.'''
# Create list of variables.
lines = [line1,line2,line3,line4,line5]
# List of options to print.
options = ["a) wolf\nb) sheep\nc) goat", "a) lionn\nb) wolf\nc) goat", "a) fake\nb) sheep\nc) real", "a) scattered\nb) combine\nc) goat", "a) faith\nb) trustworth\nc) liars"]
# Create list of answers.
words = ["sheep", "wolf", "real", "scattered", "liars"]
# Use two variables and set their value as zero.
y=0
count=0
print(info)
time.sleep(5) # 5 seconds delay.
# For loop is used 
for (x,z) in zip(lines, options):
    if count == 3:  # If condition used first so that if user give 3 wrong answers it will break the loop first without 4th iteration.
        break
    print(x)
    print(z)
    ans = input()   # User Input.
    # If condition to check wheather user input is correct or not.
    if ans == words[y]:
        y=y+1
        print("correct")
    # Else condition if the input is not correct.                
    else:
        while True:     # While loop 
            count += 1  # Every time user input is incorrect count will be incremented. 
            if count == 3:
                print("Game Over")
                break
                
            ans1 = input("Wrong!!! please try again\n")    
            if ans1 == words[y]:    # If the answer is coreect break the loop or continue the while loop.
                y=y+1
                break

# Complete story in a variable.
story="""Once upon a time, there lived a shepherd boy who was bored watching his flock of sheep on the hill. To amuse himself, 
he shouted, “Wolf! Wolf! The sheep are being chased by the wolf!” The villagers came running to help the boy and save the sheep. 
They found nothing and the boy just laughed looking at their angry faces.
“Don’t cry ‘wolf’ when there’s no wolf boy!”, they said angrily and left. The boy just laughed at them.
After a while, he got bored and cried ‘wolf!’ again, fooling the villagers a second time. The angry villagers warned the boy a second time and left. 
The boy continued watching the flock. After a while, he saw a real wolf and cried loudly, “Wolf! Please help! The wolf is chasing the sheep. Help!”
But this time, no one turned up to help. By evening, when the boy didn’t return home, the villagers wondered what happened to him and went up the hill. 
The boy sat on the hill weeping. “Why didn’t you come when I called out that there was a wolf?” he asked angrily. “The flock is scattered now”, he said.
An old villager approached him and said, “People won’t believe liars even when they tell the truth. We’ll look for your sheep tomorrow morning. Let’s go home now”."""            
moral="""Lying breaks trust. Nobody trusts a liar, even when he is telling the truth."""
if count < 3:   # If only user gets all answers within 3 chances.
    print(story)  
    time.sleep(2)  
    print(moral)