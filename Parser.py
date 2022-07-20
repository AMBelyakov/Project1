import re                                                                                                               #regular expressions
from datetime import datetime
import time

def delayed_action(hours,minutes):                                                                                      #через n часов n минут
    delayed_minute = int(find_delayed_minute)
    delayed_hour = int(find_delayed_hour)
    try:
        sec = delayed_hour*3600+delayed_minute*60
        seconds = int(sec)
        time.sleep(seconds)
        print(out)

    except  OverflowError:
        print('Неправильный ввод')
def long_delayed_action(years,months,days):                                                                             #через n лет n месяцев n дней
    delayed_year = int(find_delayed_year)
    delayed_month = int(find_delayed_month)
    delayed_day=int(find_delayed_day)
    try:
        sec =delayed_month*30.5*3600+delayed_day*3600
        if delayed_year:
            sec1=delayed_year*365*3600
            for _ in range (24):
                seconds1=float(sec1)
                time.sleep(seconds1)
        seconds = float(sec)
        time.sleep(seconds)
        print(out)

    except  AttributeError:
        print('Неправильный ввод')
def main():
    global day_intext, month_intext, year_intext, date_intext,date_intext_str,year,month,day,out,hour,minute,find_delayed_hour,find_delayed_minute,find_delayed_year, find_delayed_month,find_delayed_day,day_week

    receive=input('Введите событие:')

    all_objects=receive.split()                                                                                         #деление на подсторки
    print(all_objects)

    if ('в понедельник' or 'каждый понедельник' or 'понедельник' or'Понедельник' or 'по понедельникам') in receive:     # поиск дня недели
        day_week = 'Monday'

    if ('во вторник' or 'каждый вторник' or 'вторник' or 'Вторник' or 'по вторникам') in receive:
        day_week = 'Tuestday'

    if ('в среду' or 'каждую среду' or 'среда' or 'Среда' or 'по средам') in receive:
        day_week = 'Wednsday'

    if ('в четверг' or 'каждый четверг' or 'четверг' or 'Четверг' or 'по четвергам') in receive:
        day_week = 'Thursday'

    if ('в пятницу' or 'каждую пятницу' or 'пятница' or 'Пятница' or 'по пятницам') in receive:
        day_week = 'Friday'

    if ('в субботу' or 'каждую субботу' or 'суббота' or 'Суббота' or 'по субботам') in receive:
        day_week = 'Saturday'

    if ('в воскресенье' or 'каждое воскресенье' or 'воскресенье' or 'Воскресенье' or 'по воскресеньям') in receive:
        day_week = 'Sunday'

    if 'январь' or 'января' in receive:
        month = '01'
        n = 31
    elif 'февраль' or 'февраля' in receive:
        month = '02'
        n = 28
    elif 'март' or 'марта' in receive:
        month = '03'
        n = 31
    elif 'апрель' or 'апреля' in receive:
        month = '04'
        n = 30
    elif 'май' or 'мая' in receive:
        month = '05'
        n = 31
    elif 'июнь' or 'июня' in receive:
        month = '06'
        n = 30
    elif 'июль' or 'июля' in receive:
        month = '07'
        n = 31
    elif 'август' or 'августа' in receive:
        month = '08'
        n = 31
    elif 'сентябрь' or 'сентября' in receive:
        month = '09'
        n = 30
    elif 'октябрь' or 'октября' in receive:
        month = '10'
        n = 31
    elif 'ноябрь' or 'ноября' in receive:
        month = '11'
        n = 30
    elif 'декабрь' or 'декабря' in receive:
        month = '12'
        n = 31

    current_date = datetime.now()                                                                                       #текущие: month day year hour minute
    current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')                                                    #hour и minute далее
    print("Текущие значения:",current_date_string)

    month_current=current_date_string[1]
    day_current = current_date_string[3:5]
    year_current=current_date_string[6:8]


    try:
        match = re.search(r'\d{2}.\d{2}.\d{4}', receive)                                                                # находим день месяц год из сообщения  в формате даты
        date_intext = datetime.strptime(match.group(), '%d.%m.%Y').date()
    except  (AttributeError,ValueError):
        print('Нет даты в формате dd.mm.yyyy или ошибка ввода даты')
        year=year_current
        month=month_current
        day=day_current
    else:
        date_intext_str=str(date_intext)
        print ("Значения из сообщения:",date_intext_str)
        year_intext=date_intext_str[:4]
        month_intext=date_intext_str[5:7]
        day_intext=date_intext_str[8:10]
        year=year_intext
        month=month_intext
        day=day_intext
        print(year_intext)
        print(month_intext)
        print(day_intext)


    Time = re.findall(r'[0-2]\d:[0-5]\d+', receive)                                                                     #поиск времени в формате dd:dd
    if Time:                                                                                                            #если найдено, то режем
        Time_str=Time[0]
        hour_intext = Time_str[:2:]
        minute_intext = Time_str[3:5:]
        print(Time_str)
        hour=hour_intext
        minute=minute_intext

    else:                                                                                                               # иначе см 15 строка
        hour_current=current_date_string[9:11]
        minute_current=current_date_string[12:14]
        hour=hour_current
        minute=minute_current


    out_1 = re.sub('[0-2]\d:[0-5]\d', '', receive)                                                                      #удаление времени формата dd:dd из сообщения
    out_2=re.sub('\d{2}.\d{2}.\d{4}', '', out_1)                                                                        #удаление даты
    out_2_str=str(out_2)
    out=out_2_str

    Minute=int(minute)
    Hour=int(hour)
    Day=int(day)
    Month=int(month)
    Year=int(year)
    try:
        current_date = datetime.now().replace(microsecond=0)                                                            #задержка вывода
        text_date = datetime(Year,Month,Day,Hour,Minute)
        delta = text_date - current_date
        sec = delta.total_seconds()
        seconds = int(sec)
        time.sleep(seconds)
    except  OverflowError:
        print('Неправильный ввод')
    else:
        print(out)

    match_find_delay_minute=re.findall('минут',receive)
    match_find_delay_hour = re.findall('час', receive)
    if match_find_delay_minute or match_find_delay_hour or(match_find_delay_minute and match_find_delay_hour):
        try:
            #for index in range(len(all_objects)):
                index=0
                if all_objects[index]=='Через' or all_objects[index]=='через':
                    print(all_objects[index])



                if 0<=int(all_objects[index+1])<60 and (all_objects[index+2]=='минуту'or  all_objects[index+2]=='минуты'
                   or all_objects[index+2]=='минут'):
                    find_delayed_minute=all_objects[index+1]
                    find_delayed_hour=0
                    print('Через',find_delayed_hour,'час','через',find_delayed_minute,'минут')

                if 0<=int(all_objects[index+1])<24 and (all_objects[index+2]=='час'or  all_objects[index+2]=='часа' or
                   all_objects[index+2]=='часов'):
                    find_delayed_minute = 0
                    find_delayed_hour= all_objects[index + 1]
                    print('Через',find_delayed_hour,'часов','через',find_delayed_minute,'минут')

                if len(all_objects)==5:
                    if 0<=int(all_objects[index+1])<24 and (all_objects[index+2]=='час'or  all_objects[index+2]=='часа' or
                    all_objects[index+2]=='часов') and 0<=int(all_objects[index+3])<60 and (all_objects[index+4]=='минуту'
                    or all_objects[index+4]=='минуты' or all_objects[index+4]=='минут'):
                        find_delayed_hour = all_objects[index + 1]
                        find_delayed_minute = all_objects[index +3]
                        print('Через',find_delayed_hour,'час','через',find_delayed_minute,'минут')

        except IndexError:
            print('Необходимо ввести в формате: Через (число) часов (число) минут ИЛИ Через (число) часов ИЛИ Через (число) минут')

        else:
            delayed_action(find_delayed_hour, find_delayed_minute)

    match_find_delay_day=re.search('ден',receive)
    match_find_delay_month = re.search('месяц', receive)
    match_find_delay_year=re.search('год',receive)
    if match_find_delay_day or match_find_delay_month or match_find_delay_year or (match_find_delay_day and match_find_delay_month) or (match_find_delay_day and match_find_delay_year ) or (match_find_delay_month and match_find_delay_year):
        try:
            #for index in range(len(all_objects)):
                index=0
                if all_objects[index] == 'Через' or all_objects[index] == 'через':
                    print(all_objects[index])

                if 0 <= int(all_objects[index + 1]) < 365 and (all_objects[index + 2] == 'день' or all_objects[index + 2] == 'дня'
                        or all_objects[index + 2] == 'дней'):
                    find_delayed_year=0
                    find_delayed_month = 0
                    find_delayed_day = all_objects[index + 1]
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев','через',find_delayed_day,'дней')

                if 0 <= int(all_objects[index + 1]) < 12 and (all_objects[index + 2] == 'месяц' or all_objects[index + 2] == 'месяца' or
                        all_objects[index + 2] == 'месяцев'):
                    find_delayed_year = 0
                    find_delayed_month = all_objects[index + 1]
                    find_delayed_day = 0
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через', find_delayed_day, 'дней')

                if 0 <= int(all_objects[index + 1]) < 101 and (
                        all_objects[index + 2] == 'год' or all_objects[index + 2] == 'года' or
                        all_objects[index + 2] == 'лет'):
                    find_delayed_year = all_objects[index + 1]
                    find_delayed_month = 0
                    find_delayed_day = 0
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через', find_delayed_day,
                    'дней')

                if len(all_objects)==7:
                    if 0 <= int(all_objects[index + 1]) < 101 and (all_objects[index + 2] == 'год' or all_objects[index + 2] == 'года' or
                        all_objects[index + 2] == 'лет') and 0 <= int(
                        all_objects[index + 3]) < 12 and (all_objects[index + 4] == 'месяц'
                        or all_objects[index + 4] == 'месяца' or all_objects[index + 4] == 'месяцев') and \
                        0 <= int(all_objects[index + 5]) < 365 and (all_objects[index + 6] == 'день' or
                        all_objects[index + 6] == 'дня'or all_objects[index + 6] == 'дней') :
                        find_delayed_year = all_objects[index + 1]
                        find_delayed_month = all_objects[index + 3]
                        find_delayed_day = all_objects[index + 5]
                        print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через', find_delayed_day,
                        'дней')
        except IndexError:
            print('Необходимо ввести в формате: Через (число) лет (число) месяцев (число) дней ')

        else:
            long_delayed_action(find_delayed_year, find_delayed_month,find_delayed_day,)




    if year and month and day and hour and minute and out:                                                              #самый конец
        status='SUCCESS'
        print("Message:{","'STATUS':",status,",","'DATE':{'year':",year,",","'month':",month,",","'day':",day,",","'hour':",hour,",","'minute':",minute,"}",",","'TEXT':", out,"}",sep='')
        #if day_week:
        #    day=day_week
        #    print("Message:{", "'STATUS':", status, ",", "'DATE':{'year':", year, ",", "'month':", month, ",", "'day':",
        #          day, ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}", sep='')
    else:
        status='ERROR'
        print('Ошибка',status)

if __name__ == '__main__':
    main()


