from tkinter import *
import os
root = Tk()
root.title('Car Statistics')
root.geometry('530x350')
windowWidth = 530
windowHeight = 350
position_x = int(root.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(position_x, position_y))
root.config(background='#DCDCDC')

def fuel_type_analysis():
	os.system('python3 fuel_type_plot.py')
	#os.system('eog fuel_type_analysis.png')
def best_price():
	os.system('python3 best_price.py')
def best_mileage():
	os.system('python3 best_mileage.py')
def best_price_mileage():
	os.system('python3 best_price_mileage.py')

button3 = Button(root, text='Fuel Type Analysis', command = fuel_type_analysis, font=('',20))
button3.place(x=165, y=20)
button1 = Button(root, text='Best Priced Cars', command = best_price, font=('',20))
button1.place(x=180, y=90)
button2 = Button(root, text='Best Mileage Cars', command = best_mileage, font=('',20))
button2.place(x=170, y=160)
button3 = Button(root, text='Best Price with Mileage', command = best_price_mileage, font=('',20))
button3.place(x=140, y=230)

back_button = Button(root, text = 'BACK', command = root.destroy, font=('',15), bd=-2, fg='yellow', bg='#252525')
back_button.place(x=20,y=300)


root.mainloop()
