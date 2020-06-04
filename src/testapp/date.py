import re
import datetime
import collections
# import pytz
# import parsing_log

# cur_date = '17/May/2015'
def date_ch():
    with open('Apache_log.txt', 'r') as fp:
        line = fp.readline()
        date = []
        for line in fp:
            date_str = line.split(']')[0]
            date_n = date_str.rsplit('[')[-1]
            date_tot = date_n.split(' ')[0]
            date_obj = datetime.datetime.strptime(date_tot, '%d/%b/%Y:%H:%M:%S')
            date.append(date_obj)
    return print(date)
# def date_ch(cur_date):
#     while True:    
#         date_obj = datetime.datetime.strptime(cur_date, '%d/%b/%Y').date()
#         td = datetime.timedelta(days=1)
#         date_now = date_obj + td
#         curr_date = date_now.strftime('%d/%b/%Y')
#         print(curr_date)
#         return curr_date


# v = '17/May/2015'
# b = '18/May/2015'
# n = '19/May/2015'
# m = '20/May/2015'

# def date_pars(cur_date):
#     with open('Apache_log.txt', 'r') as fp:
#         line = fp.readline()
#         date = []
#         for line in fp:
#             if cur_date in line:
#                 date.append(line)
#         total = (cur_date + ' total ' + str(len(date)))

#         uni = []
#         for line in date:
#             uni_line = line.split(" ")[0]
#             if uni_line not in uni:
#                 uni.append(uni_line)
#         unique = (' unique ' + str(len(uni)))

#         safari = []
#         firefox = []
        
#         for line in date:
#             select = line.rsplit(' ')[-1]
#             s_sel = select.split('/')[0]
#             saf = 'Safari'
#             ff = 'Firefox'
#             ch = 'Chrome'
#             ice = 'Iceweasel'
#             tri = 'Trident'
#             if saf in select:
#                 safari.append(s_sel)
#             elif ff in select:
#                 firefox.append(s_sel)
#     bro_saf = (' Браузер Safari: ' + str(len(safari)))
#     bro_fire = (' Браузер Firefox: ' + str(len(firefox)))
#     print(str(total) + str(unique) + bro_saf + bro_fire)

def main():
    print('Парсинг по дате 17/05/2015: ')
    date_ch()
    # date_pars(b)
    # date_pars(n)
    # date_pars(m)
    
    # cur_date = '17/May/2015'
    # curr_date = date_ch(cur_date)  
    # date_pars(cur_date)
    # date_ch(cur_date)
    # date_pars(curr_date)
    # print(curr_date)






if __name__ == "__main__":
    main()