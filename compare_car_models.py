from tkinter import *
import csv, os, webbrowser

root=Tk()
root.title('Compare Car Models')
root.config(background='#DCDCDC')
root.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(root.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(position_x, position_y))

fo = open('data1_clean.csv')
data = csv.reader(fo, delimiter = '|')
brand = StringVar()
model = StringVar()
variant = StringVar()
brand2 = StringVar()
model2 = StringVar()
variant2 = StringVar()


def buy_now(url):
    webbrowser.open(url)

def reset_frame():
	root.destroy()
	os.system('python3 compare_car_models.py')
	
def comparison():
	selected_brand = brand.get()
	selected_model = model.get()
	selected_variant = variant.get()
	selected_brand2 = brand2.get()
	selected_model2 = model2.get()
	selected_variant2 = variant2.get()
	cmp_result = 'Our Results :-\n'
	
	fo.seek(0)
	headers = next(data)
	for row in data:
		if row[1]==selected_brand and row[2]==selected_model and row[3]==selected_variant:
			engine1 = int(row[4])
			mileage1 = float(row[7])
			price1 = float(row[8])
			
	fo.seek(0)
	headers = next(data)
	for row in data:
		if row[1]==selected_brand2 and row[2]==selected_model2 and row[3]==selected_variant2:
			engine2 = int(row[4])
			mileage2 = float(row[7])
			price2 = float(row[8])
			
	if (engine1>engine2):
		cmp_result = cmp_result+'> Engine    :   Model I is better.\n'
	elif (engine1<engine2):
		cmp_result = cmp_result+'> Engine    :   Model II is better.\n'
	else:
		cmp_result = cmp_result+'> Engine    :   Both have similar powered engines.\n'
		
	if (mileage1>mileage2):
		cmp_result = cmp_result+'> Mileage   :   Model I is better.\n'
	elif (mileage1<mileage2):
		cmp_result = cmp_result+'> Mileage   :   Model II is better.\n'
	else:
		cmp_result = cmp_result+'> Mileage   :   Both offer the same mileage.\n'
		
	if (price1<price2):
		cmp_result = cmp_result+'> Price       :   Model I is light on your pocket.\n'
	elif (price1>price2):
		cmp_result = cmp_result+'> Price       :   Model II is light on your pocket.\n'
	else:
		cmp_result = cmp_result+'> Price       :   Both have the same price.\n'
		
	cmp_result = cmp_result + '\n>>> The ultimate decision is yours!'
		
	text_res = Text(root, height=6, width=50, bg='#DCDCDC', font=('',16), bd=-2)
	text_res.insert(5.0, cmp_result)
	text_res.config(state='disabled')
	text_res.place(x=300, y=420)
		

def variant_is_selected():
	selected_brand = brand.get()
	selected_model = model.get()
	selected_variant = variant.get()
	fo.seek(0)
	headers = next(data)
	for row in data:
		if row[1]==selected_brand and row[2]==selected_model and row[3]==selected_variant:
			str1='ENGINE                 :   '+row[4]+' CC'+'\nTRANSMISSION     :   '+row[5]+'\nFUEL                     :   '+row[6]+'\nMILEAGE               :   '+row[7]+' KMPL'+'\nPRICE                    :   '+row[8]+' Lacs'+'\nSEATS                   :   '+row[9]
			url1 = row[10]
			text1 = Text(root, height=7, width=35, bg='#DCDCDC', font=('',12), bd=-2)
			text1.insert(5.0, str1)
			text1.config(state='disabled')
			text1.place(x=60, y=230)
			
			link1 = Label(root, text='CHECK ONLINE',fg='red',bg='cyan',width=12,cursor='hand2',font=('',20))
			link1.place(x=80,y=350)
			link1.bind('<Button-1>',lambda e:buy_now(url1))

			
def variant2_is_selected():
	selected_brand2 = brand2.get()
	selected_model2 = model2.get()
	selected_variant2 = variant2.get()
	fo.seek(0)
	headers = next(data)
	for row in data:
		if row[1]==selected_brand2 and row[2]==selected_model2 and row[3]==selected_variant2:
			str1='ENGINE                 :   '+row[4]+' CC'+'\nTRANSMISSION     :   '+row[5]+'\nFUEL                     :   '+row[6]+'\nMILEAGE               :   '+row[7]+' KMPL'+'\nPRICE                    :   '+row[8]+' Lacs'+'\nSEATS                   :   '+row[9]
			url2 = row[10]
			text1 = Text(root, height=7, width=35, bg='#DCDCDC', font=('',12), bd=-2)
			text1.insert(5.0, str1)
			text1.config(state='disabled')
			text1.place(x=580, y=230)
			
			link2 = Label(root, text='CHECK ONLINE',fg='red',bg='cyan',width=12,cursor='hand2',font=('',20))
			link2.place(x=620,y=350)
			link2.bind('<Button-1>',lambda e:buy_now(url2))
			
			compare_button = Button(root, text = 'COMPARE',width = 7, font=('',18), bg='#252525', fg='yellow', borderwidth=5, command=comparison)
			compare_button.place(x=380,y=350)
			

def model_is_selected():
	selected_brand = brand.get()
	selected_model = model.get()
	fo.seek(0)
	headers = next(data)
	variants = set([])
	for row in data:
		if row[1]==selected_brand and row[2]==selected_model:
			variants.add(row[3])
	variants = list(variants)
	
	variant.set(variants[0])
	label3 = Label(root, text='Variant :', font=('',15), bg='#DCDCDC')
	label3.place(x=30,y=150)
	entry3=OptionMenu(root,variant,*variants)
	entry3.place(x=150,y=150,height=30,width=100)

	OK3 = Button(root, text = 'OK', font=('',10), fg='blue', bg='white', command=variant_is_selected)
	OK3.place(x=280,y=150)
	
def model2_is_selected():
	selected_brand2 = brand2.get()
	selected_model2 = model2.get()
	fo.seek(0)
	headers = next(data)
	variants = set([])
	for row in data:
		if row[1]==selected_brand2 and row[2]==selected_model2:
			variants.add(row[3])
	variants = list(variants)
	
	variant2.set(variants[0])
	label3 = Label(root, text='Variant :', font=('',15), bg='#DCDCDC')
	label3.place(x=550,y=150)
	entry3=OptionMenu(root,variant2,*variants)
	entry3.place(x=670,y=150,height=30,width=100)

	OK3 = Button(root, text = 'OK', font=('',10), fg='blue', bg='white', command=variant2_is_selected)
	OK3.place(x=800,y=150)
	

def brand_is_selected():
	selected_brand = brand.get()
	fo.seek(0)
	headers = next(data)
	models = set([])
	for row in data:
		if row[1]==selected_brand:
			models.add(row[2])
	models = list(models)
	
	
	model.set(models[0])
	label2 = Label(root, text='Model :', font=('',15), bg='#DCDCDC')
	label2.place(x=30,y=100)
	entry2=OptionMenu(root,model,*models)
	entry2.place(x=150,y=100,height=30,width=100)

	OK2 = Button(root, text = 'OK', font=('',10), fg='blue', bg='white', command=model_is_selected)
	OK2.place(x=280,y=100)
	
def brand2_is_selected():
	selected_brand2 = brand2.get()
	fo.seek(0)
	headers = next(data)
	models = set([])
	for row in data:
		if row[1]==selected_brand2:
			models.add(row[2])
	models = list(models)
	
	model2.set(models[0])
	label2 = Label(root, text='Model :', font=('',15), bg='#DCDCDC')
	label2.place(x=550,y=100)
	entry2=OptionMenu(root,model2,*models)
	entry2.place(x=670,y=100,height=30,width=100)

	OK2 = Button(root, text = 'OK', font=('',10), fg='blue', bg='white', command=model2_is_selected)
	OK2.place(x=800,y=100)


text1=Text(root, height=1, width=16, bg='#DCDCDC', font=('',20), bd=-2)
text1.insert(5.0, "Model I")
text1.config(state='disabled')
text1.place(x=200, y=15)
text1=Text(root, height=1, width=16, bg='#DCDCDC', font=('',20), bd=-2)
text1.insert(5.0, "Model II")
text1.config(state='disabled')
text1.place(x=700, y=15)

fo.seek(0)
headers = next(data)
brands = set([])
for row in data:
    brands.add(row[1])
brands = list(brands)

brand.set(brands[0])
label1 = Label(root, text='Brand :', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=50)
entry1=OptionMenu(root,brand,*brands)
entry1.place(x=150,y=50,height=30,width=100)

OK1 = Button(root, text = 'OK', font=('',10), fg='blue', bg='white', command=brand_is_selected)
OK1.place(x=280,y=50)
########################
brand2.set(brands[0])
label1 = Label(root, text='Brand :', font=('',15), bg='#DCDCDC')
label1.place(x=550,y=50)
entry1=OptionMenu(root,brand2,*brands)
entry1.place(x=670,y=50,height=30,width=100)

OK1 = Button(root, text = 'OK', font=('',10), fg='blue', bg='white', command=brand2_is_selected)
OK1.place(x=800,y=50)


reset_button=Button(root, text = 'RESET',width = 5, font=('',14), bg='white', command=reset_frame)
reset_button.place(x=30,y=480)
back_button=Button(root, text = 'BACK',width = 5, font=('',14), bg='white', command=root.destroy)
back_button.place(x=30,y=530)

root.mainloop()
