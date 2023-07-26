import json
import datetime
import requests
import re
class Downloadproxies():
    def __init__(self) -> None:
        self.api = {
    'socks4':[
        "https://api.openproxylist.xyz/socks4.txt",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxyscan.io/download?type=socks4",
        "https://openproxy.space/list/socks4",
        "https://proxylist.live/nodes/socks4_1.php?page=1&showall=1",
        "https://proxyspace.pro/socks4.txt",
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks4_proxies.txt",
        "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
        "https://raw.githubusercontent.com/ObcbO/getproxy/master/socks4.txt",
        "https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
        "https://raw.githubusercontent.com/iptotal/free-proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
        "https://proxyspace.pro/socks4.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt"
        ],
    'socks5': [
        "https://api.openproxylist.xyz/socks5.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://www.proxyscan.io/download?type=socks5",
        "https://openproxy.space/list/socks5",
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt",
        "https://raw.githubusercontent.com/ObcbO/getproxy/master/socks5.txt",
        "https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks5.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
        "https://raw.githubusercontent.com/iptotal/free-proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://proxylist.live/nodes/socks5_1.php?page=1&showall=1",
        "https://proxyspace.pro/socks5.txt",
        "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
        "https://proxyspace.pro/socks5.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt"
        ],
    'http': [
        "http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http",
        "https://api.openproxylist.xyz/http.txt",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
        "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://proxyspace.pro/http.txt",
        "https://proxyspace.pro/https.txt",
        "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt",
        "https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt",
        "https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://proxyspace.pro/https.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
        "https://www.proxyscan.io/download?type=http",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://openproxy.space/list/http",
        "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
        "https://github.com/saisuiu/Lionkings-Http-Proxys-Proxies/blob/main/free.txt",
        "http://alexa.lr2b.com/proxylist.txt",
        "http://rootjazz.com/proxies/proxies.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "https://proxy-spider.com/api/proxies.example.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
        "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/unchecked.txt",
        "https://spys.me/proxy.txt",
        "https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/proxies.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://spys.me/proxy.txt",
        "https://proxylist.live/nodes/free_1.php?page=1&showall=1",
        "https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt",
        "https://rootjazz.com/proxies/proxies.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/connect.txt"
    
    ]}
        self.proxy_dict = {'socks4':[],'socks5':[],'http':[]}
        pass

    def get_special1(self):
        proxy_list = []
        try:
            r = requests.get("https://www.socks-proxy.net/",timeout=5)
            part = str(r.text)
            part = part.split("<tbody>")
            part = part[1].split("</tbody>")
            part = part[0].split("<tr><td>")
            proxies = ""
            for proxy in part:
                proxy = proxy.split("</td><td>")
                try:
                    if proxies != '':
                        proxies = proxies + proxy[0] + ":" + proxy[1] + "\n"
                        if proxies != '':
                            proxy_list += proxies.split('\n')
                except:
                    pass
                
            return proxy_list
        except:
            return []

    def get_special2(self):
        for i in range(json.loads(requests.get('https://proxylist.geonode.com/api/proxy-summary').text)["summary"]['proxiesOnline'] // 100):
            proxies = json.loads(requests.get('https://proxylist.geonode.com/api/proxy-list?limit=100&page={}&sort_by=lastChecked&sort_type=desc'.format(i)).text)
            for p in proxies['data']:
                if p['protocols'][0] == 'https':
                    protocol = 'http'
                else:
                    protocol = p['protocols'][0]
                self.proxy_dict[protocol] .append('{}:{}'.format(p['ip'],p['port']))
        return

    def get(self):
        self.proxy_dict['socks4'] += self.get_special1()
        #self.get_special2()
        self.get_extra()
        
        for type in ['socks4','socks5','http']:
            for api in self.api[type]:
                self.proxy_list = []
                try:
                    self.r = requests.get(api,timeout=5)
                    if self.r.status_code == requests.codes.ok :
                        self.proxy_list += re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}',self.r.text)
                        self.proxy_dict[type] += list(set(self.proxy_list))
                        print('> Get {} {} ips from {}'.format(len(self.proxy_list),type,api))
                except:
                    pass

        print('> Get {} proxies done'.format(type))

    def get_extra(self):
        for q in range(20):
            self.count = {'http':0,'socks5':0}
            self.day = datetime.date.today() + datetime.timedelta(-q)
            self.r = requests.get('https://checkerproxy.net/api/archive/{}-{}-{}'.format(self.day.year,self.day.month,self.day.day))
            if self.r.text != '[]': 
                self.json_result = json.loads(self.r.text)
                for i in self.json_result:
                    if i['ip'] == '172.23.0.1':
                        if i['type'] in [1,2] and i['addr'] in self.proxy_dict['http']:
                            self.proxy_dict['http'].remove(i['addr'])
                        if i['type'] == 4 and i['addr'] in self.proxy_dict['socks5']:
                            self.proxy_dict['socks5'].remove(i['addr'])
                    else:
                        if i['type'] in [1,2] :
                            self.count['http'] += 1
                            self.proxy_dict['http'].append(i['addr'])
                        if i['type'] == 4 :
                            self.count['socks5'] += 1
                            self.proxy_dict['socks5'].append(i['addr'])
                print('> Get {} http proxy ips from {}'.format(self.count['http'],self.r.url))
                print('> Get {} socks5 proxy ips from {}'.format(self.count['socks5'],self.r.url))
        
        self.proxy_dict['socks4'] = list(set(self.proxy_dict['socks4']))
        self.proxy_dict['socks5'] = list(set(self.proxy_dict['socks5']))
        self.proxy_dict['http'] = list(set(self.proxy_dict['http']))
        
        print('> Get extra proxies done')

    def save(self):
        all_proxies = []
        for type in ['socks4', 'socks5', 'http']:
            for proxy in self.proxy_dict[type]:
                if proxy not in all_proxies:
                    all_proxies.append(proxy)

        proxies_per_file = len(all_proxies) // 2
        for i in range(2):
            start_index = i * proxies_per_file
            end_index = (i + 1) * proxies_per_file if i < 1 else None
            proxies_chunk = all_proxies[start_index:end_index]

            with open(f'data{i + 1}.txt', 'w') as txt_file:
                for proxy in proxies_chunk:
                    txt_file.write(proxy + '\n')

        print("> Have already saved proxies in data1.txt and data2.txt")

if __name__ == '__main__':
    d = Downloadproxies()
    d.get()
    d.save()
    
