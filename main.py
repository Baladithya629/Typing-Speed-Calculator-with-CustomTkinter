
from customtkinter import *
from CTkMessagebox import CTkMessagebox

set_default_color_theme('green')


window=CTk()
timer=None
def time_update():
    txt=tm_label._text
    if txt=='01:00':
        
        calculate_speed(txt,box.get('0.0',END))
    else:
        m,s=map(int,txt.split(':'))
        s+=1
        if s==60:
            m+=1
            s=0
        s=str(s)
        m=str(m)
        if len(s)==1:
            s='0'+s
        if len(m)==1:
            m='0'+m
        
        tm_label.configure(text=f'{m}:{s}')
        global timer
        timer=window.after(1000,time_update)
        

    
def calculate_speed(time,text):
    tm_label.configure(text='00:00')
    button.configure(text='Start')
    box.delete('0.0',END)
    
    
    n_words=len(text.split())
    words=pgraph._text.split()[:n_words]
    
    c=0
    for o,t in zip(text.split(),words):
        if o!=t:
            c+=1
            
    accuracy= 100-c*100/n_words
            
    m,s=map(int,time.split(':'))
    t=m +  s/60
    CTkMessagebox(window,message=f'Your typing speed :{n_words/t :.2f} wpm\nAccuracy :{accuracy :.2f}',font=('tohima',20),icon='check')
    
    

def show_time():
    time = tm_label._text
    
    if time=='00:00':
        button.configure(text='Stop')
        time_update()
    else:
        global timer
        window.after_cancel(timer)
        tm=tm_label._text
        text=box.get('0.0',END)        
        calculate_speed(tm,text)
        

        


window.geometry('700x600+333+60')

window.title('Typing speed calculator')

timeframe=CTkFrame(window,height=50,width=200)
timeframe.pack(pady=10)

tm_label=CTkLabel(timeframe,180,45,text='00:00',font=('Palatino',30))
tm_label.pack()



textframe =CTkScrollableFrame(window,height=260,width=680)
textframe.pack(padx=10)

with open('textfile.txt','r') as file:
    pgraph=CTkLabel(textframe,text=file.read(),
             font=('Arial',20),text_color='green',
             wraplength=640)
    pgraph.grid(row=0,column=0,padx=10,pady=20)


textbox=CTkFrame(window,height=200,width=680)
textbox.pack(pady=10)

box = CTkTextbox(textbox,660,180,font=('palatino',20))
box.pack(padx=10,pady=10)

box.focus()



button = CTkButton(window,text='Start',command=show_time,font=('tohima',20))
button.pack()



window.mainloop()