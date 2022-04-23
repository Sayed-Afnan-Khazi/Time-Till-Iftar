import datetime,csv
current_time = datetime.datetime.now()
f = open("iftar-timings-2022.csv","r") #Add "Time-Till-Iftar/" before for VSCode
my_reader=csv.reader(f)
for x in my_reader:
    data=x[0].split('\t')
    if data[0]=="Date":
        continue
    data_day_tuple=(int(data[1]),int(data[2]),int(data[3])) #Day,Month,Year
    if data_day_tuple[0]==current_time.day and data_day_tuple[1]==current_time.month and data_day_tuple[2]==current_time.year:
        iftar_time=datetime.datetime(int(data[3]),int(data[2]),int(data[1]),int(data[-1][:2]),int(data[-1][3:]))
        # print(iftar_time)
        break
f.close()
print("Time till iftar:",iftar_time-current_time)