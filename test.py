import os, random, words, turtle as draw
from tkinter import messagebox

word = random.choice(words.hw_words)
word = word.upper()
reveal =list(len(word)*'_')
lives = 7
won = False

def drawbar():
     draw.color("black")
     draw.width(4)
     draw.backward(300)
     draw.left(90)
     draw.forward(300)
     draw.left(90)
     draw.backward(200)
     draw.left(90)
     draw.forward(50)
     draw.right(90)
 
def drawhead():
    draw.begin_fill()
    draw.circle(20)
    draw.end_fill()

def drawhand():
    draw.left(90)
    draw.forward(60)
    draw.left(30)
    draw.forward(30)
    draw.backward(30)
    draw.right(60)
    draw.forward(30)
    draw.backward(30)

def drawbody():
   draw.left(34)
   draw.forward(100)
 
def drawlegs():
    draw.left(30)
    draw.forward(30)
    draw.backward(30)
    draw.right(60)
    draw.forward(30)
    draw.hideturtle()

def drawlost():
    draw.up()
    draw.right(40)
    draw.fd(100)
    draw.right(90)
    draw.fd(100)
    draw.down()
    draw.color("red")
    draw.write("you lost !!!!!!")
    draw.up()
    draw.left(90)
    draw.fd(350)

def drawman(lives):
    if lives == 6:
        drawbar()
    if lives == 5:
        drawhead()
    if lives == 4:
        drawhand()
    if lives == 3:
        drawbody()
    if lives == 2:
        drawlegs()
    if lives == 1:
        drawlost()
        messagebox.showinfo("lost game","do you whant to exit")

def check_letter(letter,word):
        for i in range(0,len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
        if '_' not in reveal:
            return  True
        else:
            return  False

def status():
    os.system('clear')
    print(' '.join([str(e) for e in reveal]))
    print('')

while won == False and lives > 1:

        status()
        guess = input('one letter or full: ') 
        guess = guess.upper()
        if guess == word:
            won = True
        if len(guess) == 1 and guess in word:
            won = check_letter(guess,word)
        else:
            lives -= 1
            drawman(lives)


if won:
    print('win')
    messagebox.showinfo("you did win","do you whant to exit")

else:
    print('lost and the word was: ',word)
