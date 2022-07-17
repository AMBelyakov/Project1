import re
import datetime
from datetime import datetime


def main():
    receive=input('Поиск дня недели')

    all_objects=receive.split()
    print(all_objects)

    data_list = []                       # поиск числа и года
    for index in range (len(all_objects)):
            if all_objects[index].isdigit()  :
                data_list.append(all_objects[index])
    print(data_list)
    try:
        if len(data_list)>2:
            raise IndexError
        else:
            a=data_list[0]
            b=data_list[1]
            if int(b)//100!=0:
                year_intext=b
                day_intext=a
            else:
                year_intext=a
                day_intext=b
            print('Day=',day_intext,'Year=',year_intext)
    except IndexError :
        print('Incorrect input')




    day_find = re.findall(r'(?i)(понедельник|вторник|среда|четверг|пятница|суббота|восресенье]+)',receive)  # поиск дня недели

    current_date = datetime.now()
    current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')
    print(current_date_string)

    month=current_date_string[1]
    day = current_date_string[3:5]
    year=current_date_string[6:8]

    match = re.search(r'\d{2}.\d{2}.\d{4}', receive)  # находим дату
    date = datetime.strptime(match.group(), '%d.%m.%Y').date()
    print (date)

    time = re.findall(r'[0-2]\d:[0-5]\d+', receive)
    if time:
        time_str=time[0]
        hour = time_str[:2:]
        minute = time_str[3:5:]
        print(time_str)

    else:
        hour=current_date_string[9:11]
        minute=current_date_string[12:14]

    status='SUCCESS'
    out = re.sub('[0-2]\d:[0-5]\d', '', receive)
    try:
        day_given = day_find[0]
        if day_given==None:
            print("Message:{", "'STATUS':", status, ",", "'DATE':{'year':", year, ",", "'month':", month, ",", "'day':", day, ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}", sep='')
        else:
            print("Message:{","'STATUS':",status,",","'DATE':{'year':",year,",","'month':",month,",","'day':",day_given,",","'hour':",hour,",","'minute':",minute,"}",",","'TEXT':",out,"}",sep='')
    except IndexError:
        #print('Enter a day')
        pass


if __name__ == '__main__':
    main()