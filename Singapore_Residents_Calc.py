import csv
import datetime

Start = datetime.datetime.now()
print("시작시간: ", Start)

open_data = open('C:/Users/planning/Desktop/Singapore Residents by Subzone, 2011-2019.csv', 'r', encoding="EUC-KR")
data = csv.reader(open_data)

dataset = {}
Output = []

n = 0

for line in data:
    if n > 0:
        if line[3] not in dataset:
            dataset[line[3]] = {}

        if line[0] not in dataset[line[3]]:
            dataset[line[3]][line[0]] = {}

        if line[1] not in dataset[line[3]][line[0]]:
            dataset[line[3]][line[0]][line[1]] = int(line[2])

        else:
            dataset[line[3]][line[0]][line[1]] += int(line[2])

    n += 1

Year = list(set(dataset.keys()))
Year.sort()

for x in Year:
    Planning_Zone = list(set(dataset[x].keys()))
    Planning_Zone.sort()

    for y in Planning_Zone:
        Sub_Zone = list(set(dataset[x][y].keys()))
        Sub_Zone.sort()

        for z in Sub_Zone:
            Residents = 0
            Residents += dataset[x][y][z]

            Output.append([x, y, z, Residents])

#Case 1: 모든 연도에 대하여 출력하고자 하는 경우
'''write_data = open('C:/Users/planning/Desktop/Singapore Residents by Subzone_Output, 2011-2019.csv', 'w', encoding="EUC-KR", newline="")
csv_writer = csv.writer(write_data)

column_names = ['Year', 'Planning_Area', 'Sub_Zone', 'Residents']
csv_writer.writerow(column_names)

for line in Output:
    csv_writer.writerow(line)'''

#Case 2: 원하는 연도에 대하여만 출력하고자 하는 경우
write_data = open('C:/Users/planning/Desktop/Singapore Residents by Subzone_Output, 2019.csv', 'w', encoding="EUC-KR", newline="")
csv_writer = csv.writer(write_data)

column_names = ['Planning_Area', 'Sub_Zone', 'Residents']
csv_writer.writerow(column_names)

for line in Output:
    if line[0] == "2019":
        csv_writer.writerow([line[1], line[2], line[3]])

End = datetime.datetime.now()
print("종료시간: ", End)