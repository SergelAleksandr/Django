import re
def pars_all():
    with open('Apache_log.txt', 'r') as fp:
        print('1. Количество строк в логе: ')
    return print(len(fp.readlines()))


def pars_unique():
    with open('Apache_log.txt', 'r') as fp:
        print('2. Количество уникальных ID: ')
        id_list = []
        line = fp.readline()
        for line in fp:
            unique = line.split(" ")[0]
            if unique not in id_list:
                id_list.append(unique)
    return print(len(id_list))
           
def pars_browser():
    with open('Apache_log.txt', 'r') as fp:
        print('3. Количество запросов от браузеров: ')
        safari = []
        firefox = []
        chrome = []
        iceweasel = []
        trident = []
        
        line = fp.readline()
        
        for line in fp:
            select = line.rsplit(' ')[-1]
            s_sel = select.split('/')[0]
            saf = 'Safari'
            ff = 'Firefox'
            ch = 'Chrome'
            ice = 'Iceweasel'
            tri = 'Trident'
            if saf in select:
                safari.append(s_sel)
            elif ff in select:
                firefox.append(s_sel)
            elif ch in select:
                chrome.append(s_sel)
            elif ice in select:
                iceweasel.append(s_sel)
            elif tri in select:
                trident.append(s_sel)

        print('Браузер Safari: ' + str(len(safari)))
        print('Браузер Firefox: ' + str(len(firefox)))
        print('Браузер Chrome: ' + str(len(chrome)))
        print('Браузер Iceweasel: ' + str(len(iceweasel)))
        print('Браузер Microsoft Trident: ' + str(len(iceweasel)))
    return print('Браузер Safari: ' + str(len(safari)) + 'Браузер Firefox: ' + str(len(firefox)))

if __name__ == "__main__":
    print('its OK')