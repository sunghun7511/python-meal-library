#-*- coding: utf-8 -*-
import requests, datetime, re

__pattern = re.compile(r"(?<=[<]div[>])\d{1,}[<]br \/[>].*?(?=[<][/]div[>])", re.DOTALL)

# get meal
# schoolcode : school code (now basic value is Daedeok Meister High School)
# schooltype
#  - 1 : kindergarden
#  - 2 : elementary school
#  - 3 : middle school
#  - 4 : high school
def getMeal(
        year="{:04d}".format(datetime.datetime.now().year),
        month="{:02d}".format(datetime.datetime.now().month),
        schoolcode="G100000170",
        schooltype="4"):
    
    meal = dict()
    url = "http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=" + schoolcode + "&schulCrseScCode=" + schooltype + "&schulKndScCode=0" + schooltype + "&schYm=" + year + month
    global __pattern

    # request to server
    res = requests.get(url)
    data = res.text

    # print(data)

    # regex find
    findlist = __pattern.findall(data.encode("utf-8"))

    for find in findlist:
        lst = find.split("<br />")
        index = lst[0]
        meal[index] = dict()

        flag = "알 수 없음"
        for i in lst[1:len(lst)]:
            # remove . in end
            if i.endswith("."):
                i = i[0:-1]
            
            if i == "[조식]" or i == "[중식]" or i == "[석식]":
                flag = i[1:-1]
                if flag not in meal[index]:
                    meal[index][flag] = list()
            else:
                meal[index][flag].append(i)
                continue
    return meal


# test case
if __name__ == "__main__":
    # get today meal
    # meals = getMeal("{:04d}".format(datetime.datetime.now().year), "{:02d}".format(datetime.datetime.now().month), "G100000170", "4")
    meals = getMeal()

    # print meals
    for date in meals.keys():
        print(date + "일 : ")
        for time in meals[date]:
            print(" " + time)
            for meal in meals[date][time]:
                print("  " + meal)