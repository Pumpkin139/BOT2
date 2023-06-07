from random import choice
import time
import webbrowser as web
import os
import log
hello = ['orders?', 'here!', 'yes', 'yes im here.', 'now what?','Whatever you say']
edin = '0.0.21.5 bata'
botname = 'bot001'
stt = False
debug = False
bootsystem = False
system = False

def progress_bar(total):
    if total <= 0:
        raise ValueError("Wrong total number ...")
    # step = (100 // total if total <= 100 else total // 100)

    for i in range(0, total):
        time.sleep(0.05)
        step = int(100 / total * (i + 1))
        str1 = '\r[%3d%%] %s' % (step, '>' * step)
        print(str1, end='', flush=True)


print('\n')

progress_bar(20)
print()
progress_bar(110)
print()
log.add()
time.sleep(0.5)
ex2 = False
while ex2 == False:
    oder = input('$ ')
    if oder == "boot":
        print('boot code -<bot>-')
        boot = input()
        if boot == '-<bot>-':
            print('boot time:')
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print(choice(hello))
            while stt == False:
                cmd = input('bot~$ ')
                if cmd == "search":
                    print('navigation:')
                    print('wallpaper:https://www.toopic.cn/')
                    print('music:https://tool.liumingye.cn/music/?page=homePage#/')
                    print('bing:https://cn.bing.com/')
                    print('baidu:https://www.baidu.com/')
                    print('csdn:https://blog.csdn.net/')
                    print('lets search something...')
                    FWT = input()
                    url = 'baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='+FWT
                    web.open(url)
                    time.sleep(1)
                    print('[OK]')

                if cmd == "-<bot>-exit":
                    print("kill all...")
                    time.sleep(1)
                    print('exit code 0')
                    ex = input()
                    if ex == '0':
                        print('[OK]')
                        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                        ext = 1
                        ex2 = True
                        stt = True
                    else:
                        print("cancel...")

                if cmd == '-<bot>-edin':
                    print('bot edition:',edin)

                if cmd == 'boot-<debug>-':
                    debug = True
                while debug == True:
                    decmd = input('debug~$ ')#进入调试模式
                    if decmd == 'debug.open [all]':
                        print('loading...')
                        time.sleep(1)
                        print('made of PYTHON')
                        print('1970.01.01 ~ 2023.05.30')
                        time.sleep(0.7)
                        print(' ----------------------------------------------------------------')
                        print('| all user : root   administrator   user accessing               |')
                        print(' ----------------------------------------------------------------')
                        time.sleep(2)
                        print('')
                        print('')
                        print('bot edition:',edin)
                        print('')
                        print('Time of first startup:2023.05.31')
                        time.sleep(1)
                        print('show more type:help')
                    if decmd == 'help':#列出所有命令
                        print('format : command [parameter1] [parameter2] - value & for {user} /** note **/')
                        print('')
                        print('open bot : -<bot>-')
                        print('search : -<bot>-search')
                        print('show bot edition : -<bot>-edin')
                        print('update bot : -<bot>-update')
                        print('debug : -<debug>-')
                        print('print somthing : echo')
                        print("what's your name : show bot name")
                        print('change [] [] ... : Change parameter')
                        print('exit bot : -<bot>-exit')
                        print('exit debug : -<debug>-exit')
                #退出debug模式
                    if decmd == '-<debug>-exit':
                        print('kill all...')
                        time.sleep(1)
                        print('exit...')
                        time.sleep(0.5)
                        print('[OK]')
                        debug = False
                    if decmd == 'echo':
                        echo = input('echo:')
                        print(echo)
                    if decmd == "bot":
                        print("i'm BOT001")
                        print('i was born in 2023Y.05M.31TRD')
                        print('my father is bruce wilde and mother is PYTHON')
                        print('you can call me',botname)
                    if decmd == '-<debug>-change bot [name]':
                        botname = input("new name of your bot:")
                        time.sleep(1)
                        print('[OK]')
                        print('now my name is',botname,"that's a good name!")
                if cmd == 'boot-<system>-':
                    print('loading...')
                    time.sleep(1)


                    def progress_bar(total):
                        if total <= 0:
                            raise ValueError("Wrong total number ...")
                        # step = (100 // total if total <= 100 else total // 100)

                        for i in range(0, total):
                            time.sleep(0.05)
                            step = int(100 / total * (i + 1))
                            str1 = '\r[%3d%%] %s' % (step, '>' * step)
                            print(str1, end='', flush=True)


                    print('\n')

                    progress_bar(20)
                    print()
                    progress_bar(110)
                    print('')
                    system = True
                    while system == True:
                        syscmd = input('system~$ ')
                        if syscmd == 'new-built':
                            flieformat = input('format: ')
                            location = input('location: ')
                            name = input('file name: ')
                            content = input('write: ')

                            path = location+name+flieformat
                            with open(path,'a') as f:
                                f.write(content)

                            print('[OK]')
                        if syscmd == 'del':
                            dellocation = input('location: ')

                            os.remove(dellocation)
                            print("File removed successfully")
                        if syscmd == 'exit':
                            system = False
                            print('[OK]')

                        if syscmd == 'write':
                            wrlocation = input('location: ')
                            write = input('write: ')
                            with open(path,'a') as f:
                                f.write(write)
                                print('[OK]')

        else:
            print('cancel...')
            time.sleep(0.5)
            print('[OK]')
    else:
       print('***--bad command:',oder,'--***')