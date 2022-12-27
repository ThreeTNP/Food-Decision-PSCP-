from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk
import csv
import pandas as pd
import matplotlib.pyplot as plt

bg_color = '#b47229'
real_bg = '#1E1E1E'
fn_color = '#D666FC'
dish = []
ls_food = []


def clear_widgets(frame):
    # clear widget each frame
    for widget in frame.winfo_children():
        widget.destroy()

def keepdata(name, ty_food, loca, food):
    #clear data if save error
    try:
        food[0]
    except:
        tkinter.messagebox.showinfo('Alert','Select Food !')
        clear_widgets(frame2)
        if loca == 'Gegi4':
            gegi(ty_food,name)
        elif loca == 'Billion':
            billion(ty_food, name)
    else:
        ls_food.clear()
        # Keep data in csv file
        with open('Data.csv', 'a',newline='') as mycsv:
            writer = csv.writer(mycsv)
            writer.writerow([name, ty_food, loca, food[0]])
        mycsv.close()
        tkinter.messagebox.showinfo('Save','Thank for Using!!')
        dish.clear()
        load_frame1('Type of Food', 'Name')
        

def show_stat(name):
    # Show stat on Pie Chart
    colnames = ['Name', 'Type Food', 'Place', 'Food']
    df = pd.read_csv('Data.csv', names=colnames)
    ls_type = []
    ls_food = []
    colors = ['#30FA26', '#26FAEE','#797BFA','#DECCFB']
    data1 = df.loc[df['Name']==name]
    for row in data1['Type Food']:
        if row not in ls_type:
            ls_type.append(row)

    for i in ls_type:
        num_food = data1.loc[data1['Type Food'] == i].count()[0]
        ls_food.append(num_food)    
    plt.pie(ls_food, labels=ls_type,autopct='%.2f %%', colors = colors[0:len(ls_type)])
    plt.title('Your Food Type',fontdict={'fontweight':'bold','fontsize':18})
    plt.show()


def select(res):
    # select food in list ls_food
    num = res.get()
    dish.clear()
    dish.append(ls_food[num-1])

def gegi(food,name):
    # frame2 with gegi restaurant
    clear_widgets(frame1)
    frame2.tkraise()
    try:
        if food == 'Thai':
            food1 = 'KapraoGe4'
            food2 = 'Stewed Chicken Noodles'
            food3 = 'Khaomankai'
            food4 = 'Omlet'
        elif food == 'Japanese':
            food1 = 'MeeZAA Ramen'
            food2 = 'Tenkuya'
            food3 = 'Takoyaki'
            food4 = 'Curry Meetiew'
        elif food == 'Other':
            food1 = 'steakhouse'
            food2 = 'Urban Street'
            food3 = 'Kebab'
            food4 = 'Tiger steak X the burgest'
        elif food == 'Drink and Dessert':
            food1 = 'Cold Crepe'
            food2 = 'Pooh PangPang Bakery'
            food3 = 'Soy Milk'
            food4 = 'FreeZTory'
        logo_img = ImageTk.PhotoImage(file='recom.png')
        logo_widget = Label(frame2, image=logo_img,bg=real_bg)
        logo_widget.image = logo_img
        logo_widget.pack()
        Label(frame2, text='Choose Only 1',bg=real_bg, fg='white',font=('TkHeadingFont',15)).place(x=50, y=150)
        ls_food.extend([food1, food2, food3, food4])
        # checkbutton with name of restaurant
        res = IntVar()
        Radiobutton(text=food1,variable=res,bg=real_bg,fg=fn_color,font=1,value=1,command=lambda:select(res)).place(x=50,y=180)
        Radiobutton(text=food2,variable=res,bg=real_bg,fg=fn_color,font=1,value=2,command=lambda:select(res)).place(x=50, y=230)
        Radiobutton(text=food3,variable=res,bg=real_bg,fg=fn_color,font=1,value=3,command=lambda:select(res)).place(x=50, y=280)
        Radiobutton(text=food4,variable=res,bg=real_bg,fg=fn_color,font=1,value=4,command=lambda:select(res)).place(x=50, y=330)
        bt1 = Button(frame2, height=2,width=10,text='BACK', command=lambda:load_frame1(food,name),bg='red',fg='white',font=2).place(x=75, y=375)
        bt2 = Button(frame2, height=2,width=10,text='SAVE',bg='green',fg='white',font=2,command=lambda:keepdata(name, food, 'Gegi4', dish)).place(x=325, y=375)
    except:
        tkinter.messagebox.showinfo('Alert','Select Type Food')
        load_frame1(food,name)

def billion(food, name):
    # frame2 with billion restaurant
    try:
        clear_widgets(frame1)
        frame2.tkraise()
        if food == 'Thai':
            food1 = 'Kaprao Billion'
            food2 = 'Yum Billion'
            food3 = 'Noodle'
            food4 = 'KhaoSoi'
        elif food == 'Japanese':
            food1 = 'Sho Ramen'
            food2 = 'ShabuN'
            food3 = 'Smooth Japanese food&dessert'
            food4 = 'Nan'
        elif food == 'Other':
            food1 = 'Zeedneez'
            food2 = 'Daeguemsong'
            food3 = 'PangPing'
            food4 = 'Fruit'
        elif food == 'Drink and Dessert':
            food1 = 'Nom Mahalai'
            food2 = 'Bingsu'
            food3 = 'Mo Milk'
            food4 = 'Smooth Japanese food&dessert'
        logo_img = ImageTk.PhotoImage(file='recom.png')
        logo_widget = Label(frame2, image=logo_img,bg=real_bg)
        logo_widget.image = logo_img
        logo_widget.pack()
        Label(frame2, text='Choose Only 1',bg=real_bg, fg='white',font=('TkHeadingFont',15)).place(x=50, y=150)
        # checkbutton with name of restaurant
        ls_food.extend([food1, food2, food3, food4])
        # checkbutton with name of restaurant
        res = IntVar()
        Radiobutton(text=food1,variable=res,bg=real_bg,fg=fn_color,font=1,value=1,command=lambda:select(res)).place(x=50,y=180)
        Radiobutton(text=food2,variable=res,bg=real_bg,fg=fn_color,font=1,value=2,command=lambda:select(res)).place(x=50, y=230)
        Radiobutton(text=food3,variable=res,bg=real_bg,fg=fn_color,font=1,value=3,command=lambda:select(res)).place(x=50, y=280)
        Radiobutton(text=food4,variable=res,bg=real_bg,fg=fn_color,font=1,value=4,command=lambda:select(res)).place(x=50, y=330)
        bt1 = Button(frame2, height=2,width=10,text='BACK', command=lambda:load_frame1(food, name),bg='red',fg='white',font=2).place(x=75, y=375)
        bt2 = Button(frame2, height=2,width=10,text='SAVE',bg='green',fg='white',font=2, command=lambda:keepdata(name, food, 'Billion', dish)).place(x=325, y=375)
    except:
        tkinter.messagebox.showinfo('Alert','Select Type Food')
        load_frame1(food, name)

def load_frame1(re_food, re_name):
    # load frame1
    clear_widgets(frame2)
    ls_food.clear()
    frame1.tkraise()
    frame1.pack_propagate(False)
    # frame1 widget
    logo_img = ImageTk.PhotoImage(file='logo.png')
    logo_widget = Label(frame1, image=logo_img,bg=real_bg)
    logo_widget.image = logo_img
    logo_widget.pack()
    Label(frame1, text="Your Name:",bg=real_bg, fg='white', font=('TkMEnuFont', 16)).place(x=25, y=250)
    Label(frame1, text="Type Food:",bg=real_bg, fg='white', font=('TkMEnuFont', 16)).place(x=25, y=300)
    # input Name
    name = StringVar(value=re_name)
    myname = Entry(frame1, width=40, textvariable=name).place(x=140, y=255)
    # combo TypeFood
    food = StringVar(value=re_food)
    combo = ttk.Combobox(textvariable=food,width=30,state='readonly')
    combo['values'] = ('Thai', 'Japanese', 'Other', 'Drink and Dessert')
    combo.place(x=140, y=305)
    #Button
    btn1 = Button(frame1, height=2,width=10, text="เกกี4", fg='white', bg=bg_color,font=2,command=lambda:gegi(food.get(), name.get())).place(x=75, y=375)
    btn2 = Button(frame1, height=2,width=10, text="บิลเลี่ยน", fg='white', bg=bg_color,font=2, command=lambda:billion(food.get(), name.get())).place(x=325, y=375)
    btn3 = Button(frame1, height=2,width=10, text="Stat", fg='white', bg=bg_color,font=2, command=lambda:show_stat(name.get())).place(x=200, y=375)

#initiallize app
root = Tk()
root.title('ร้านสุดโปรดกระแทกใจคุณ')
root.config(width=500, height=500)

frame1 = Frame(root, width=500, height=500, bg=real_bg)
frame2 = Frame(root, bg=real_bg)

for frame in (frame1, frame2):
    # for frame in root
    frame.grid(row=0, column=0, sticky='nesw')

load_frame1('Type of Food', 'Name')

root.mainloop()
