import csv
import os

os.chdir("D:\\1. Works\\2021\\2. UNESCAP\\UNESCAP(2020-12-18~)\\3. Phnom Penh(Cambodia)_Data\\8. Route_Analysis\\2. Google_API\\")
File_List = os.listdir()

Result_Directory = "D:\\1. Works\\2021\\2. UNESCAP\\UNESCAP(2020-12-18~)\\3. Phnom Penh(Cambodia)_Data\\8. Route_Analysis\\3. Result\\"

n = 0

for file in File_List:
    n += 1

    open_data = open(file, 'r', encoding='utf-8')
    write_data = open(Result_Directory + '[google_out]ODfile_num' + str(n) + '.csv', 'w', newline="", encoding='utf-8')

    data = csv.reader(open_data)
    csv_writer = csv.writer(write_data)
    csv_writer.writerow(['num', 'origin_FID', 'destin_FID', 'origin_coor_x', 'origin_coor_y', 'destination_coor_x', 'destination_coor_y', 'departure_time', 'arrival_time',
                         'distance', 'start_address', 'end_address', 'start_location_x', 'start_location_y', 'end_location_x', 'end_location_y', 'steps', 'traffic_speed_entry'])

    col = 0

    for line in data:
        if col > 0:
            OD = line[1].split('--')
            csv_writer.writerow([0, OD[0], OD[1], "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])

        col += 1

    write_data.close()
    open_data.close()

