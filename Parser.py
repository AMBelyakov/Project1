import re  # regular expressions
import time
from datetime import datetime


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
def long_delayed_action(years,months,days,Year,Month,Day,Hour,Minute):                                                  #через n лет n месяцев n дней
    delayed_year = int(find_delayed_year)
    delayed_month = int(find_delayed_month)
    delayed_day=int(find_delayed_day)
    try:
        dt1 = datetime(Year,Month, Day, Hour, Minute)
        dt2 = datetime(Year+delayed_year, Month+delayed_month, Day+delayed_day, Hour, Minute)
        tdelta = dt2 - dt1
        tdelta_string=str(tdelta)
        print(str(tdelta))
        tdelta_objects=tdelta_string.split()
        print(tdelta_objects)
        days_tosec=tdelta_objects[0]
        print(days_tosec)
        sec =days_tosec*86400
        seconds = int(sec)
        for a in range(0,seconds,4800):
            time.sleep(4800)
        print(out)

    except  OverflowError:
        pass
        print('Неправильный ввод')
def main():
    global day_intext, month_intext, year_intext, date_intext,date_intext_str,year,month,day,out,hour,minute\
        ,find_delayed_hour,find_delayed_minute,find_delayed_year, find_delayed_month,find_delayed_day,day_week,n,\
        string_month

    receive = input('Введите событие:')
    all_objects = receive.split()  # деление на подсторки
    print(all_objects)

    Mondays=['в понедельник','каждый понедельник' , 'понедельник' ,'Понедельник' , 'по понедельникам' ,'понедельник']
    Tuesdays=['во вторник' , 'каждый вторник' , 'вторник' , 'Вторник' , 'по вторникам']
    Wendsdays=['в среду' , 'каждую среду' , 'среда' , 'Среда' , 'по средам' , 'среду']
    Thursdays=['в четверг' , 'каждый четверг' , 'четверг' , 'Четверг' , 'по четвергам']
    Fridays=['в пятницу' , 'каждую пятницу' , 'пятница' , 'Пятница' , 'по пятницам']
    Saturdays=['в субботу' , 'каждую субботу' , 'суббота' , 'Суббота' , 'по субботам']
    Sundays=['в воскресенье' , 'каждое воскресенье' , 'воскресенье' , 'Воскресенье' , 'по воскресеньям']

    Septembers=['сентябрь' , 'сентября']
    Octobers=['октябрь' , 'октября']
    Novembers=['ноябрь' , 'ноября']
    Decembers=['декабрь' , 'декабря']
    Januarys=['январь' , 'января']
    Februarys=['февраль' , 'февраля']
    Marchs=['март' , 'марта']
    Aprils=['апрель' , 'апреля']
    Mays=['май' , 'мая']
    Junes=['июнь' , 'июня']
    Julys=['июль' , 'июля']
    Augusts=['август' , 'августа']



    for i in range(len(all_objects)):                                                                                   #поиск дня недели
        if all_objects[i] in Mondays:
            day_week='Monday'
        elif all_objects[i] in Tuesdays:
            day_week='Tuesday'
        elif all_objects[i] in Wendsdays:
            day_week='Wendsday'
        elif  all_objects[i] in Thursdays:
            day_week='Thursday'
        elif all_objects[i] in Fridays:
            day_week='Friday'
        elif  all_objects[i] in Saturdays:
            day_week='Saturday'
        elif  all_objects[i] in Sundays:
            day_week='Sunday'

    for k in range(len(all_objects)):                                                                                   #поиск месяца
        if all_objects[k] in Januarys:
            string_month = '01'
            n = 31
        elif all_objects[k] in Februarys:
            string_month = '02'
            n = 28
        elif all_objects[k] in Marchs:
            string_month = '03'
            n = 31
        elif all_objects[k] in Aprils:
            string_month = '04'
            n = 30
        elif all_objects[k] in Mays:
            string_month = '05'
            n = 31
        elif all_objects[k] in Junes:
            string_month = '06'
            n = 30
        elif all_objects[k] in Julys:
            string_month = '07'
            n = 31
        elif all_objects[k] in  Augusts:
            string_month = '08'
            n = 31
        elif all_objects[k] in Septembers:
            string_month = '09'
            n = 30
        elif all_objects[k] in Octobers:
            string_month = '10'
            n = 31
        elif all_objects[k] in Novembers:
             string_month = '11'
             n = 30
        elif all_objects[k] in Decembers:
            string_month = '12'
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
                if 'через' in all_objects:
                    index=all_objects.index('через')
                elif 'Через' in all_objects:
                    index=all_objects.index('Через')
                else:
                    raise ValueError ('Try again')
                if (all_objects[index]=='Через' or all_objects[index]=='через') and 0<=int(all_objects[index+1])<60 and (all_objects[index+2]=='минуту'or  all_objects[index+2]=='минуты'
                   or all_objects[index+2]=='минут'):
                    find_delayed_minute=all_objects[index+1]
                    find_delayed_hour=0
                    print('Через',find_delayed_hour,'час','через',find_delayed_minute,'минут')

                if (all_objects[index]=='Через' or all_objects[index]=='через') and 0<=int(all_objects[index+1])<24 and (all_objects[index+2]=='час'or  all_objects[index+2]=='часа' or
                   all_objects[index+2]=='часов'):
                    find_delayed_minute = 0
                    find_delayed_hour= all_objects[index + 1]
                    print('Через',find_delayed_hour,'часов','через',find_delayed_minute,'минут')

                if len(all_objects)==5:
                    if (all_objects[index]=='Через' or all_objects[index]=='через') and 0<=int(all_objects[index+1])<24 and (all_objects[index+2]=='час'or  all_objects[index+2]=='часа' or
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
                if 'через' in all_objects:
                    index = all_objects.index('через')
                elif 'Через' in all_objects:
                    index = all_objects.index('Через')
                else:
                    raise ValueError ('Try again')
                if  (all_objects[index] == 'Через' or all_objects[index] == 'через') and 0 <= int(all_objects[index + 1]) < 365 and (all_objects[index + 2] == 'день' or all_objects[index + 2] == 'дня'
                        or all_objects[index + 2] == 'дней'):
                    find_delayed_year=0
                    find_delayed_month = 0
                    find_delayed_day = all_objects[index + 1]
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев','через',find_delayed_day,'дней')

                if (all_objects[index] == 'Через' or all_objects[index] == 'через') and 0 <= int(all_objects[index + 1]) < 12 and (all_objects[index + 2] == 'месяц' or all_objects[index + 2] == 'месяца' or
                        all_objects[index + 2] == 'месяцев'):
                    find_delayed_year = 0
                    find_delayed_month = all_objects[index + 1]
                    find_delayed_day = 0
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через', find_delayed_day, 'дней')

                if (all_objects[index] == 'Через' or all_objects[index] == 'через') and 0 <= int(all_objects[index + 1]) < 101 and (
                        all_objects[index + 2] == 'год' or all_objects[index + 2] == 'года' or
                        all_objects[index + 2] == 'лет'):
                    find_delayed_year = all_objects[index + 1]
                    find_delayed_month = 0
                    find_delayed_day = 0
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через', find_delayed_day,
                    'дней')

                if len(all_objects)==7:
                    if (all_objects[index] == 'Через' or all_objects[index] == 'через') and 0 <= int(all_objects[index + 1]) < 101 and (all_objects[index + 2] == 'год' or all_objects[index + 2] == 'года' or
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
            long_delayed_action(find_delayed_year, find_delayed_month,find_delayed_day,Year,Month,Day,Hour,Minute)

    if year and hour and minute and out:                                                                                #самый конец
        status='SUCCESS'
        day_out=''
        month_out=''

        try:
            if day_week:
                day_out=day_week
                month_out=month

            elif day:
                day_out=day
                month_out=month

        except NameError:
            day_week=None
        else:
            print(day_out)

        try:
            if string_month:
                day_out=day
                month_out=string_month
            elif month:
                day_out=day
                month_out=month
        except NameError:
            string_month=None
        else:
            print(month_out)

        try:
            if string_month and day_week:
                day_out=day_week
                month_out=string_month
            elif month:
                day_out=day
                month_out=month
        except NameError:
            string_month=None
            day_week=None
        else:
            print(month_out)
            print(day_week)
        print("Message:{","'STATUS':",status,",","'DATE':{'year':",year,",","'month':",month_out,",","'day':",day_out,",","'hour':",hour,",","'minute':",minute,"}",",","'TEXT':", out,"}",sep='')

    else:
        status='FAILURE'
        print('Ошибка',status)

if __name__ == '__main__':
    main()


