def pars_all():
    with open('Apache_log.txt', 'r') as fp:
        pars_list = []
        line = fp.readline()
        for line in fp:
            pars_list.append(line)
    return pars_list

def pars_ip():
    with open('Apache_log.txt', 'r') as fp:
        ip_list = []
        line = fp.readline()
        for line in fp:
            ip_string = line.split(" ")[0]
            ip_list.append(ip_string)
    return ip_list
           
def pars_browser():
    with open('Apache_log.txt', 'r') as fp:
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
    pars_all()