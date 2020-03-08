import matplotlib.pyplot as plt,csv

fo = open('data1_clean.csv')
data = csv.reader(fo,delimiter='|')
headers = next(data)

cng=diesel=petrol=0
for row in data:
	if row[6]=="Petrol":
		petrol+=1
	elif row[6]=="Diesel":
		diesel+=1
	else:
		cng+=1

labels = "CNG","Petrol","Diesel"
sizes = [cng,petrol,diesel]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.2, 0.1, 0.2)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.legend(labels, loc="best")
plt.axis('equal')
plt.title("Fuel Type Analysis")
plt.show()