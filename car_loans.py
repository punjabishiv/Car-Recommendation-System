from tkinter import *
import os, webbrowser

######################## Basic Structure
root=Tk()
root.geometry('800x450')
windowWidth = 800
windowHeight = 450
position_x = int(root.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(position_x, position_y))
root.title('Car Loan')
######################## Images
image1 = PhotoImage(file = 'car_loans.gif')
background = Label(root, image=image1)
background.place(x=0, y=0)
#background.image = image1
########################
########################

######################## Functions
def buy_now(url):
    webbrowser.open(url)
    
link1 = Label(root, text='GET IT NOW',fg='red',bg='cyan',width=12,cursor='hand2',font=('',20))
link1.place(x=520,y=145	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.icicibank.com/Personal-Banking/loans/car-loan/index.page#'))

link1 = Label(root, text='GET IT NOW',fg='red',bg='yellow',width=12,cursor='hand2',font=('',20))
link1.place(x=520,y=183	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.sbi.co.in/portal/web/personal-banking/sbi-new-car-loan-scheme'))

link1 = Label(root, text='GET IT NOW',fg='red',bg='cyan',width=12,cursor='hand2',font=('',20))
link1.place(x=520,y=221	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.axisbank.com/retail/loans/car-loan/new-car-loan/features-benefits'))

link1 = Label(root, text='GET IT NOW',fg='red',bg='yellow',width=12,cursor='hand2',font=('',20))
link1.place(x=520,y=259	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.centralbankofindia.co.in/English/cent_vehicle.aspx'))

link1 = Label(root, text='GET IT NOW',fg='red',bg='cyan',width=12,cursor='hand2',font=('',20))
link1.place(x=520,y=297	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.pnbindia.in/carloaninnerpage.html'))

link1 = Label(root, text='GET IT NOW',fg='red',bg='yellow',width=12,cursor='hand2',font=('',20))
link1.place(x=520,y=335	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.hdfcbank.com/personal/borrow/popular-loans/new-car-loan'))

link1 = Label(root, text="Check for 'Other Banks'",fg='green',bg='pink',width=21,cursor='hand2',font=('',27))
link1.place(x=170,y=380	)
link1.bind('<Button-1>',lambda e:buy_now('https://www.myloancare.in/'))
	
	
back_button = Button(root, text = 'BACK', command = root.destroy, font=('',12), bd=-2, fg='yellow', bg='#252525')
back_button.place(x=50,y=400)

root.mainloop()
