# ===================some imports==============
import random, sys
from tkinter import *
from tkinter.ttk import Separator
from tkinter.messagebox import showinfo
from time import time, strftime

# =========start making window==============
root = Tk()
root.geometry('700x500')
root.resizable(0, 0)
root.title('Quiz App Designed by: ')
# ==================set an image as icon of app
img = ('wm', 'iconphoto', root._w, PhotoImage(file='game.png'))
root.tk.call(img)  # add image as icon of game
root.config(bg='black')
i = 0
timeLeft = {'min': 5, 'sec': 10}  # 3 total time +30 waiting time for intro

intro = '''\t\t ::Instructons::
        ........................................................................
            1. Total Quiz Time is : 05:00 Min
            2. Total Questions : 05
            3. Total Score : 05 X 100 = 500
            4. Please select appropriate option at once
                as you have only one chance to select.
            \t\t Good Luck !
        ........................................................................
'''
print(intro)


def timeShow():
    global i, timeLeft
    if timeLeft['min'] == 5 and timeLeft['sec'] > 0:
        note.config(text='You can Start Quiz after {} Seconds.'.format(timeLeft['sec']))
        timeLeft['sec'] -= 1
    elif timeLeft['sec'] > 0:
        submit.config(state=NORMAL)
        instruction.config(text='')
        timeLeft['sec'] -= 1
        note.config(text='Time left: {}min:{}sec'.format(timeLeft['min'], timeLeft['sec']))

    elif timeLeft['min'] != 0 and timeLeft['sec'] == 0:
        timeLeft['min'] -= 1
        timeLeft['sec'] = 59
        note.config(text='Time left: {}min:{}sec'.format(timeLeft['min'], timeLeft['sec']))
    elif timeLeft['min'] == 0 and timeLeft['sec'] == 0:
        print('Time up!')
        result()
    showtime.config(text=strftime('%H:%M:%S'))
    showtime.after(1000, timeShow)


# ====================make student's Attendance===================
def getDetails():
    global name, roll, mainWindow, Name, Roll
    Name = name.get()
    Roll = roll.get()
    root.deiconify()
    timeShow()
    mainWindow.destroy()


def attendance():
    global name, roll, mainWindow
    mainWindow = Toplevel(root)
    mainWindow.geometry('700x500')
    mainWindow.resizable(0, 0)
    mainWindow.title('Quiz App Designed by:  [make attendence]')
    mainWindow.tk.call(img)  # add any image as icon of game
    mainWindow.config(bg='black')
    # ===============app name same as root====================
    appName = Label(mainWindow, text=title, font=('impact', 20, 'italic'),
                    justify=CENTER, bg='goldenrod2', fg='white')
    appName.pack(side=TOP, fill=BOTH)
    # ===========================label to show info of attendance==========
    info = Label(mainWindow, text='Enter Your Name and Roll Number', bg='black', fg='goldenrod1', font=('arial', 15))
    info.place(x=210, y=200)
    name = Entry(mainWindow, width=30)
    name.place(x=250, y=235)
    roll = Entry(mainWindow, width=30)
    roll.place(x=250, y=260)
    name.insert(END, 'Name')
    roll.insert(END, 'Roll')
    submit = Button(mainWindow, text='Confirm & Start', width=20, bg='goldenrod1', fg='green', command=getDetails)
    submit.place(x=265, y=300)
    mainWindow.mainloop()


# ==============================================toplevel finished=================================================

# ====================================quit game===================
def quit_function():
    answer = showinfo(title="Good luck", message="Good Luck For Your Future..\n We'll contact you soon.")
    if answer == 'ok':
        sys.exit(root.destroy())


# ================================= desable all buttons============
def desableAllButton():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)


# ================================== enable All buttons============
def enableAllButton():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)


# ================================== Show final Result=============
def result():
    global score, Name, Roll
    root.withdraw()
    top = Toplevel(root)
    top.tk.call('wm', 'iconphoto', top._w, PhotoImage(file='game.png'))  # add any image as icon of game
    top.geometry('300x300')
    top.resizable(0, 0)
    top.title('Quiz Result')
    top.config(bg='blue')
    top.protocol('WM_DELETE_WINDOW', quit_function)
    filename = Name + '_' + Roll + '.txt'
    data = '\nStudent: ' + Name + '\nRoll: ' + Roll + '\nScore: ' + str(score) + '\nCompleted quiz at: ' + strftime(
        '%d/%m/%y --%H:%M:%S')
    with open(filename, 'a') as file:
        file.write(data)

    label = Label(top, text='Quiz Over...\n Score: ' + str(score), font=30, fg='white', bg='blue').place(x=50, y=25)
    exitBtn = Button(top, text='Exit', width=10, bg='black', fg='red', command=quit_function).place(x=50, y=70)
    top.mainloop()


# ===================== questions and corresponding answers

questions = {'Who is the founder of Python?': 'Guido van Rossum ',
             'What is the Output of 13//3   ?': '4.0',
             '''i=0
             while i<3:
                 print(i)
                 i+=1
                 print(i+1)			// What is Output?''': '021324',
             '''What is the output of following code?
print("Welcome to exam ")[::-1]''': 'maxe ot emocleW',
             'What is the Output of 0.1+0.2==0.3 ?': 'False'}

# ==================== separate questions and answers from questions variable
que = []
ans = []
for key, value in questions.items():
    que.append(key)
    ans.append(value)
# ==================== corresponding answers with answers including at random
options = [
    ['van neuman', ans[0], 'James Gosling', 'Gudo van Rosom'],
    [ans[1], '4', '4.5', 'Error'],
    ['012345', '013214', ans[2], '012023'],
    [' to Welcome ', 'Welcome to ', ans[3], 'Error'],
    ['True', '0.6', 'SyntaxError', ans[4]]
]
# =============================================================================
currentQ = ''
queNo = None
currentA = ''
score = 0
qn = 1  # for printing no of question finished
var = StringVar()


def _next():
    global currentQ, currentA, queNo, score, i, qn
    i = 0
    # till last question is left===========
    if len(que) > 0:
        currentQ = random.choice(que)
        print(currentQ)
        q = Label(root, text='Que. ' + str(qn), font=('arial', 10)).place(x=20, y=80)
        qn += 1
        # ==================================================
        queNo = que.index(currentQ)  # total questions = 5 so queNos =5 , queNo 0 means first que
        print(options[queNo])
        currentA = questions[currentQ]
        # firstly change caption of button
        submit.config(text='Next')
        # print current question on quelabel
        queLabel.config(text=currentQ, fg='green', height=6)
        # print options for question on labels--- option 1 option2,.....
        enableAllButton()
        option1.config(text=options[queNo][0], bg='sky blue', value=options[queNo][0], bd=1, command=answer)
        option2.config(text=options[queNo][1], bg='sky blue', value=options[queNo][1], bd=1, command=answer)
        option3.config(text=options[queNo][2], bg='sky blue', value=options[queNo][2], bd=1, command=answer)
        option4.config(text=options[queNo][3], bg='sky blue', value=options[queNo][3], bd=1, command=answer)
        # remove question from list which are asked
        que.remove(currentQ)
        ans.remove(currentA)
        options.remove(options[queNo])
    elif len(que) == 0:
        result()


def answer():
    global currentQ, currentA, score
    # ==============print selected radiobutton
    a = var.get()
    if currentA == str(a):
        score += 100
        desableAllButton()
    else:
        desableAllButton()  # ===========desable all button


title = '''Enterance Exam for Admission'''
appName = Label(root, text=title, font=('impact', 20, 'italic'),
                justify=CENTER, bg='goldenrod2', fg='white')
appName.pack(side=TOP, fill=BOTH)

# ============= label to show current question
queLabel = Label(root, text='', justify=LEFT, font=25)
queLabel.pack(side=TOP, fill=BOTH)
s = Separator(root).place(x=0, y=195, relwidth=1)
# =============================options labels
option1 = Radiobutton(root, text='', bg='black', font=20, width=20, relief=FLAT,
                      indicator=0, value=1, variable=var, bd=0)
option1.place(x=150, y=250)
option2 = Radiobutton(root, text='', bg='black', font=20, width=20, relief=FLAT,
                      indicator=0, value=2, variable=var, bd=0)
option2.place(x=400, y=250)
option3 = Radiobutton(root, text='', bg='black', font=20, width=20, relief=FLAT,
                      indicator=0, value=3, variable=var, bd=0)
option3.place(x=150, y=300)
option4 = Radiobutton(root, text='', bg='black', font=20, width=20, relief=FLAT,
                      indicator=0, value=4, variable=var, bd=0)
option4.place(x=400, y=300)
# instruction of quiz
instruction = Label(root, text=intro, bg='black', fg='white',
                    font=('calibri', 15), justify=LEFT)
instruction.place(x=150, y=200)
# note to quiz
note = Label(root, text='', font=('impact', 10), bg='black', fg='red')
note.pack(side=BOTTOM)
# ==================== submit button
submit = Button(root, text='Start Quiz', bg='blue', fg='white', width=15, font=('impact', 15), state=DISABLED,
                command=_next)
submit.pack(side=BOTTOM)

# ==================show current time
showtime = Label(root, text='', font=20, fg='black', bg='goldenrod2')
showtime.place(x=620, y=50)
# =========progress bar for time left for each question
copyri8 = Label(root, text="Developed By: Harshad",
                font=('mistral', 12, 'bold'), fg='blue', bg='powder blue', width=25, justify=LEFT).place(x=0, y=480)

if __name__ == "__main__":
    root.withdraw()
    attendance()
    root.mainloop()

#===================some imports==============
# import random,sys
# from tkinter import *
# from tkinter.ttk import Separator
# from tkinter.messagebox import showinfo
# from time import time,strftime
# #=========start making window==============
# root = Tk()
# root.geometry('700x500')
# root.resizable(0,0)
# root.title('Quiz App Designed by: ')
# #==================set an image as icon of app
# img = ('wm','iconphoto',root._w,PhotoImage(file='game.png'))
# root.tk.call(img)   #add image as icon of game
# root.config(bg='black')
# i=0
# timeLeft = {'min':5,'sec':30}#3 total time +30 waiting time for intro
#
# intro = '''\t\t ::Instructons::
#         ........................................................................
#             1. Total Quiz Time is : 05:00 Min
#             2. Total Questions : 05
#             3. Total Score : 05 X 100 = 500
#             4. Please select appropriate option at once
#                 as you have only one chance to select.
#             \t\t Good Luck !
#         ........................................................................
# '''
# print(intro)
#
# def timeShow():
#     global i,timeLeft
#     if timeLeft['min']==5 and timeLeft['sec']>0:
#         note.config(text='You can Start Quiz after {} Seconds.'.format(timeLeft['sec']))
#         timeLeft['sec']-=1
#     elif timeLeft['sec']>0:
#         submit.config(state=NORMAL)
#         instruction.config(text='')
#         timeLeft['sec']-=1
#         note.config(text='Time left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
#
#     elif timeLeft['min']!=0 and timeLeft['sec']==0:
#         timeLeft['min']-=1
#         timeLeft['sec']=59
#         note.config(text='Time left: {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
#     elif timeLeft['min']==0 and timeLeft['sec']==0:
#         print('Time up!')
#         result()
#     showtime.config(text=strftime('%H:%M:%S'))
#     showtime.after(1000,timeShow)
#
# #====================make student's Attendance===================
# def getDetails():
#     global name,roll,mainWindow,Name,Roll
#     Name = name.get()
#     Roll = roll.get()
#     root.deiconify()
#     timeShow()
#     mainWindow.destroy()
#
# def attendance():
#     global name,roll,mainWindow
#     mainWindow = Toplevel(root)
#     mainWindow.geometry('700x500')
#     mainWindow.resizable(0,0)
#     mainWindow.title('Quiz App Designed by:  [make attendence]')
#     mainWindow.tk.call(img)   #add any image as icon of game
#     mainWindow.config(bg='black')
#     #===============app name same as root====================
#     appName = Label(mainWindow,text=title,font=('impact',20,'italic'),
#                 justify=CENTER,bg='goldenrod2',fg='white')
#     appName.pack(side=TOP,fill=BOTH)
#     #===========================label to show info of attendance==========
#     info = Label(mainWindow,text='Enter Your Name and Roll Number',bg='black',fg='goldenrod1',font=('arial',15))
#     info.place(x=210,y=200)
#     name = Entry(mainWindow,width=30)
#     name.place(x=250,y=235)
#     roll = Entry(mainWindow,width=30)
#     roll.place(x=250,y=260)
#     name.insert(END,'Name')
#     roll.insert(END,'Roll')
#     submit = Button(mainWindow,text='Confirm & Start',width=20,bg='goldenrod1',fg='green',command=getDetails)
#     submit.place(x=265,y=300)
#     mainWindow.mainloop()
# #==============================================toplevel finished=================================================
#
# #====================================quit game===================
# def quit_function():
#     answer =showinfo(title="Good luck",message="Good Luck For Your Future..\n We'll contact you soon.")
#     if answer=='ok':
#         sys.exit(root.destroy())
# #================================= desable all buttons============
# def desableAllButton():
#     option1.config(state=DISABLED)
#     option2.config(state=DISABLED)
#     option3.config(state=DISABLED)
#     option4.config(state=DISABLED)
# #================================== enable All buttons============
# def enableAllButton():
#     option1.config(state=NORMAL)
#     option2.config(state=NORMAL)
#     option3.config(state=NORMAL)
#     option4.config(state=NORMAL)
# #================================== Show final Result=============
# def result():
#     global score,Name,Roll
#     root.withdraw()
#     top = Toplevel(root)
#     top.tk.call('wm','iconphoto',top._w,PhotoImage(file='game.png'))   #add any image as icon of game
#     top.geometry('200x100')
#     top.resizable(0,0)
#     top.title('Quiz Result')
#     top.config(bg='blue')
#     top.protocol('WM_DELETE_WINDOW',quit_function)
#     filename =Name+'_'+Roll+'.txt'
#     data = '\nStudent: '+Name+'\nRoll: '+Roll+'\nScore: '+str(score)+'\nCompleted quiz at: '+strftime('%d/%m/%y --%H:%M:%S')
#     with open(filename,'a') as file:
#         file.write(data)
#
#     label = Label(top,text='Quiz Over...\n Score: '+str(score),font=30,fg='white',bg='blue').place(x=50,y=25)
#     exitBtn = Button(top,text='Exit',width=10,bg='black',fg='red',command=quit_function).place(x=50,y=70)
#     top.mainloop()
#
# # ===================== questions and corresponding answers
#
# questions = {'Who is the founder of Python?':'Guido van Rossum ',
#              'What is the Output of 13//3   ?':'4.0',
# '''i=0
# while i<3:
#     print(i)
#     i+=1
#     print(i+1)			// What is Output?''':'021324',
#              '''What is the output of following code?
# print("Welcome to exam")[::-1]''':'maxe ot emocleW',
#              'What is the Output of 0.1+0.2==0.3 ?':'False'}
#
#
#
# #==================== separate questions and answers from questions variable
# que = []
# ans= []
# for key,value in questions.items():
#     que.append(key)
#     ans.append(value)
# #==================== corresponding answers with answers including at random
# options = [
#     ['van neuman',ans[0],'James Gosling','Gudo van Rosom'],
#     [ans[1],'4','4.5','Error'],
#     ['012345','013214',ans[2],'012023'],
#     [' to Welcome ','Welcome to ',ans[3],'Error'],
#     ['True','0.6','SyntaxError',ans[4]]
#         ]
# #=============================================================================
# currentQ =''
# queNo=None
# currentA=''
# score = 0
# qn = 1  #for printing no of question finished
# var = StringVar()
# def _next():
#     global currentQ,currentA,queNo,score,i,qn
#     i=0
#     # till last question is left===========
#     if len(que)>0:
#         currentQ = random.choice(que)
#         print(currentQ)
#         q = Label(root,text='Que. '+str(qn),font=('arial',10)).place(x=20,y=80)
#         qn+=1
#         #==================================================
#         queNo = que.index(currentQ)   # total questions = 5 so queNos =5 , queNo 0 means first que
#         print(options[queNo])
#         currentA = questions[currentQ]
#         #firstly change caption of button
#         submit.config(text='Next')
#         #print current question on quelabel
#         queLabel.config(text=currentQ,fg='green',height=6)
#         #print options for question on labels--- option 1 option2,.....
#         enableAllButton()
#         option1.config(text=options[queNo][0],bg='sky blue',value=options[queNo][0],bd=1,command=answer)
#         option2.config(text=options[queNo][1],bg='sky blue',value=options[queNo][1],bd=1,command=answer)
#         option3.config(text=options[queNo][2],bg='sky blue',value=options[queNo][2],bd=1,command=answer)
#         option4.config(text=options[queNo][3],bg='sky blue',value=options[queNo][3],bd=1,command=answer)
#         # remove question from list which are asked
#         que.remove(currentQ)
#         ans.remove(currentA)
#         options.remove(options[queNo])
#     elif len(que)==0:
#         result()
# def answer():
#     global currentQ,currentA,score
#     #==============print selected radiobutton
#     a = var.get()
#     if currentA == str(a):
#         score+=100
#         desableAllButton()
#     else:
#         desableAllButton()#===========desable all button
#
#
# title='''Enterance Exam for Admission '''
# appName = Label(root,text=title,font=('impact',20,'italic'),
#                 justify=CENTER,bg='goldenrod2',fg='white')
# appName.pack(side=TOP,fill=BOTH)
#
# #============= label to show current question
# queLabel = Label(root,text='',justify=LEFT,font=25)
# queLabel.pack(side=TOP,fill=BOTH)
# s = Separator(root).place(x=0,y=195,relwidth=1)
# #=============================options labels
# option1=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,
#                     indicator=0,value=1,variable = var,bd=0)
# option1.place(x=150,y=250)
# option2=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,
#                     indicator=0,value=2,variable = var,bd=0)
# option2.place(x=400,y=250)
# option3=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,
#                     indicator=0,value=3,variable = var,bd=0)
# option3.place(x=150,y=300)
# option4=Radiobutton(root,text='',bg='black',font=20,width=20,relief=FLAT,
#                     indicator=0,value=4,variable = var,bd=0)
# option4.place(x=400,y=300)
# #instruction of quiz
# instruction = Label(root,text=intro,bg='black',fg='white',
#                     font=('calibri',15),justify=LEFT)
# instruction.place(x=150,y=200)
# #note to quiz
# note = Label(root,text='',font=('impact',10),bg='black',fg='red')
# note.pack(side=BOTTOM)
# #==================== submit button
# submit = Button(root,text='Start Quiz',bg='blue',fg='white',width=15,font=('impact',15),state=DISABLED,command=_next)
# submit.pack(side=BOTTOM)
#
# #==================show current time
# showtime = Label(root,text='',font=20,fg='black',bg='goldenrod2')
# showtime.place(x=620,y=50)
# #=========progress bar for time left for each question
# copyri8= Label(root,text="Developed By: Harshad",
#                font=('mistral',12,'bold'),fg='blue',bg='powder blue',width=25,justify=LEFT).place(x=0,y=480)
#
# if __name__ =="__main__":
#     root.withdraw()
#     attendance()
#     root.mainloop()