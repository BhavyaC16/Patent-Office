import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('patents.xlsx')
    sh = wb.sheet_by_name('patents')
    your_csv_file = open('patents.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

def tune_csv():
	file = open("patents.csv","r")
	read = csv.reader(file)
	rows = []
	for i in read:
		rows.append([])
		for j in i:
			try:
				if float(j)==int(float(j)):
					rows[-1].append(str(int(float(j))))
				else:
					rows[-1].append(j)
			except:
				rows[-1].append(j)

	file = open("patents.csv","w")
	write = csv.writer(file)
	for i in rows:
		write.writerow(i)

# runs the csv_from_excel function:
csv_from_excel()
tune_csv()