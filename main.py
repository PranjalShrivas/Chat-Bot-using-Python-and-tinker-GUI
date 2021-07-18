
#print("Testing")
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk
from PIL import Image



bot = ChatBot("My Bot")
convo = [
    'hello', 'hi there!',
    'what is your name ?',
    'My name is Bot, I am created by Pranjal',
    'how are you',
    'I am doing great these days',
    'thank you',
    'In which city you live?',
    'I live in Kharsia',
    'Which language you talk',
    'I talk in English',
    'What you like',
    'I mostly like to play game, guitar',
    'Who is your favourite hero',
    'I like Tom Cruise',
    'What is your favourite song',
    'There are various songs but my favourite is Tu jane na',
    'What is your favourite study subject?',
    'I like Physics',
    'Which country and state do you live',
    'I live in India and Chhattisgarh state',
    'Are you student or do you work and do job',
    'Yes I am a student and currently I am not working',
    'Who is your favourite football player ?',
    ' My favourite football player is Leone Messi'

]
trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)
#answer=bot.get_response("what is your name")
#print(answer)

print("Talk to bot")
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer=bot.get_response(query)
#     print("bot :", answer)

main = Tk()

main.geometry("500x650")
main.title("Jarvis Chat Bot")

img = Image.open('Bot.png')
img = img.resize((10, 10))
img= ImageTk.PhotoImage(file="Bot.png")

photoL= Label(main, image=img)
photoL.pack(pady=20)

def ask_from_bot():
    query= textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END, "you: "+query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot :"+ str(answer_from_bot))
    textF.delete(0,END)
    msgs.yview(END)


frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
# creating text field

textF=Entry(main,font=("Courier",20))
textF.pack(fill=X, pady=10)
btn=Button(main,text='Ask from bot', font=('Verdana',16), command=ask_from_bot)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key...
main.bind('<Return>', enter_function)

main.mainloop()
