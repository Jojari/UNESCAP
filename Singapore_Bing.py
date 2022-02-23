import csv

open_Data = open("C:\\Users\\planning\\Downloads\\[CAR_out]Singapore_Car_Bing_0520.csv", 'r', encoding='utf-8')
data = csv.reader(open_Data)

write_data = open("C:\\Users\\planning\\Downloads\\[CAR_out]Singapore_Car_Bing_Statistics_0525.csv", 'w', newline="", encoding='utf-8')
csv_writer = csv.writer(write_data)

dict = {}
count = 0

for line in data:
    OD = line[2].split('-')

    O = OD[0]
    D = OD[2]

    if O not in dict:
        dict[0]['Stage'] = int(line[7])
        dict[0]['speed'] = ''

