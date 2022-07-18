import re                                                                                                               #regular expressions
from datetime import datetime
import time


def main():
    global day_intext, month_intext, year_intext, date_intext,date_intext_str,year,month,day,out,hour,minute
    receive=input('Введите событие:')

    all_objects=receive.split()                                                                                         #деление на подсторки
    print(all_objects)

    if ('в понедельник' or 'каждый понедельник' or 'понедельник' or'Понедельник' or 'по понедельникам') in receive:     # поиск дня недели
        day = 'Monday'

    if ('во вторник' or 'каждый вторник' or 'вторник' or 'Вторник' or 'по вторникам') in receive:
        day = 'Tuestday'

    if ('в среду' or 'каждую среду' or 'среда' or 'Среда' or 'по средам') in receive:
        day = 'Wednsday'

    if ('в четверг' or 'каждый четверг' or 'четверг' or 'Четверг' or 'по четвергам') in receive:
        day = 'Thursday'

    if ('в пятницу' or 'каждую пятницу' or 'пятница' or 'Пятница' or 'по пятницам') in receive:
        day = 'Friday'

    if ('в субботу' or 'каждую субботу' or 'суббота' or 'Суббота' or 'по субботам') in receive:
        day = 'Saturday'

    if ('в воскресенье' or 'каждое воскресенье' or 'воскресенье' or 'Воскресенье' or 'по воскресеньям') in receive:
        day = 'Sunday'


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

    else:                                                                                                               # иначе см 15 сторка
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

    current_date = datetime.now().replace(microsecond=0)                                                                #задержка вывода
    text_date = datetime(Year,Month,Day,Hour,Minute)
    delta = text_date - current_date
    sec = delta.total_seconds()
    seconds = int(sec)
    time.sleep(seconds)
    print(out)

    if year and month and day and hour and minute and out:                                                              #самый конец
        status='SUCCESS'
        print("Message:{","'STATUS':",status,",","'DATE':{'year':",year,",","'month':",month,",","'day':",day,",","'hour':",hour,",","'minute':",minute,"}",",","'TEXT':", out,"}",sep='')
    else:
        status='ERROR'
        print('Ошибка',status)

if __name__ == '__main__':
    main()