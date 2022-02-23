import urllib.request
import json
import csv
import bingmaps
import time
import datetime

#Suhwan, 20200504

###################################### Directory ######################################
directory = "F:\\Bing\\"       #TODO. to revise
filename = "ODfile_num1.csv"     #TODO. to revise

###################################### Result ########################################
outf = directory + "[bing_out]" + filename.split(".")[0] + ".csv"
f = open(outf, 'w', newline="",encoding='utf-8')
kk = csv.writer(f)
fieldname = ["num", "stage_count", "O_FID", "D_FID", "O_x", "O_y", "D_x", "D_y", "Total_Travel_Distance(km)", "Total_Travel_Time(h)","travel_Speed(kph"]
kk.writerow(fieldname)

###################################### Key ###########################################
bingMapsKey = "AgxjxkP_g7loQcHy3OXvp4gy-ZV6WjJckCwkmfWPti4FzjzPEWIFBIKzJmwpuU57"  #TODO. to revise
######################################################################################

# KEY LIST #
#1 임수환 AgxjxkP_g7loQcHy3OXvp4gy-ZV6WjJckCwkmfWPti4FzjzPEWIFBIKzJmwpuU57
#2 이세련 AkG7htncbUqeE0z6zLcj6jrYBt6VoOj5QfCKlo7PWjndFvnhwpQxbfH0Wl52w5y6
#3 김용준 AsIi4gAvTnvu9Cg-LFbYD6t5aekT3zojI78_vngLK9nr6W8zWui2j4JeqsI9QQqz
#4 문상미 An3hJDXRUGMdQ_HUbXjq3IzOt6cVlRDS2uE454HCTNmGEbf8UV2Shx2Jy-Gpvpc0
#5 이찬주 AjIFbVfeyGQTcJxcLClkhdbye9_tSFvGRp6PPX2PryboLCCEgTjvCh_aekuEGDwR
#6 김동준 AnFDQ7D4yYBaXDz70GZt8-S1NXkpV8d28wvWpJkCg67L3vn4qjZdyucr2Q3AcUVa
#7 이지훈 Any-Vy-2VTbRIr2gnFMeIxDT8GzOfwiM3j9g99RTJDD0MTOPRNFu8Z0JxMo45xYp
#8 이혜린 Aqymbd8qOfwSHYIBg-05Ir7R66dYn2JZUIHVh1k15MI5mRsHEzSB1SwT5opmP_OA
#9 조재현 7cVqS3p9fJ0SMh00lKiq~BJZbKGKpD0vmI-2rauucrA~AsuE_78Z1GBonX8BlKyJsyN74srkYE_nSp7qmiMJk_AuWBRIqG_F-dZ9YF9CppY5
#10 신호성 NTKNkbRIGnegqzipbHCR~Rk1yqZ-R_GhcKKsfje1dgA~AvX0Rp4VZtClQy5LZ0ZoIjAzjuoBFt5ARwIIZ4-BllQENl2CspgLt7accTTJD9WU 
#11 이서윤 zK5Y2XU0J0pUZXIAOYT2-E9ToMIp4ysW4tsHrRiOQ9Q~Ai6fnVZsPMuKcgzcPm_kdenXkDTFAIcrzrUBsAYNN_uCAAJtmSGrT1ptORiQ9dUr
#12 박예린 skX7iYhrKXO4gOK5WhOg~g8vVr9SgEcL3Lchble5DCQ~AjUTDZrcCZwO5jx2IT9mT1mft74DnYnynKqDvQ2uS4zJ6h5eZnQblFLuFaVZZNis

def Create_Datetime(self):
    now = datetime.datetime.now()
    self.Departureday = '2021_v1-05-12'  # TODO. to revise
    self.Departuretime = '19:00:00'  # TODO. to revise

with open(directory + filename) as f:
    k = csv.reader(f)
    for i, row in enumerate(k):
        if i > 0:
            num = int(row[0]); OD = row[1]
            O = OD.split("--")[0]; D = OD.split("--")[1]
            O_x = float(row[2]); O_y = float(row[3])
            D_x = float(row[4]); D_y = float(row[5])

            # input information
            O_longitude = O_x; O_latitude = O_y
            D_longitude = D_x; D_latitude = D_y

            traveldt = '12/05/2021_v1'
            #encodedDest = urllib.parse.quote(destination, safe='')

            try:
                routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(O_latitude) + "," + str(O_longitude) + \
                           "&wp.1=" + str(D_latitude) + "," + str(D_longitude) + "&" + "routeAttributes=routePath&optimize=timeWithTraffic" #+ "&key=" + bingMapsKey

                now = datetime.datetime.now()
                crawling_date = now.strftime('%m/%d/%Y')
                crawling_time = now.strftime("%H:%M:%S")

                #Input_departure_Set = "&dateTime=" + crawling_date + " " + crawling_time
                Input_Key = "&key=" + bingMapsKey
                DATETIME = "&dateTime" + "%3D" + crawling_date + "%20" + "21" + "%3A" + "00" + "%3A" + "00"
                URL = routeUrl + DATETIME + Input_Key
                #print(URL)

                request = urllib.request.Request(URL)
                response = urllib.request.urlopen(request)
                r = response.read().decode(encoding="utf-8")
                result = json.loads(r)

                resourceItems = result["resourceSets"][0]["resources"]
                itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
                stage_count = len(itineraryItems)

            except:
                pass

            n = 0
            for item in resourceItems:

                if item is not None:
                    itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
                    n+=1
                    stage = str(num) + "_" + str(n)
                    travel_dt = item["travelDistance"]
                    travel_dur= round(item["travelDuration"] / 3600, 2)

                    try:
                        total_travel_speed = round(travel_dt / travel_dur, 2)   #km/h
                    #print(total_travel_speed)
                    except ZeroDivisionError:
                        total_travel_speed = "0"

                    INFO = [num, stage_count, O, D, O_x, O_y, D_x, D_y, travel_dt, travel_dur, total_travel_speed]
                    print(INFO)
                    kk.writerow(INFO)

                if item is None:
                    n+=1
                    print(n, "############ Fail")
                    continue