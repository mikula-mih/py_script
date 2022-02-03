import sys, os, time
import random
import re
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as mController
'''
1. create automated brave.exe opener  ---------------------------------------------------------DONE-------------
2. brave.exe first installation
3. playList for automation + randomizing choice  ----------------------------------------------DONE-------------
4. TASKLIST for checking exe & closing if necessary
5. TASKLIST for checking memmory usage(further C++ dev)
6. Logging with python time module(can be done with CMD)
7. Mouse movement + detection
8. Single & Multiple key pressing ---DICTIONARY -----------------------------------------------DONE--------------
'''
####################################################
def create_BASIC_UserList():
    userList = []
    for i in range(0, 1000, 1):
        if i < 10:
            userName = f'u00{str(i)}'
        elif i < 100:
            userName = f'u0{str(i)}'
        else:
            userName = f'u{str(i)}'
        userList.append(userName)
    return userList
def create_MIKE_UserList():
    userList = ['none']
    for i in range(1, 11):
        if i < 10:
            userName = f'mikeBrave_0{str(i)}'
        else:
            userName = f'mikeBrave_{str(i)}'
        userList.append(userName)
    return userList
def createAccount(accountName, adminGroup):
    # net user /add 'userName' 'password = 8598'
    addUser = f'net user /add {accountName} 8598'
    # net localgroup 'adminGROUP' 'userName' /add
    addGroup = f'net localgroup {adminGroup} {accountName} /add'
    # wmic useraccount where name='userName' set passwordexpires=false
    setPassExp = f'wmic useraccount where name=\'{accountName}\' set passwordexpires=false'
    # Command joiner
    cmd = ' && '.join([addUser, addGroup, setPassExp])
    return cmd
def deleteAccount(delAccount):
    # net user /delete 'userName'
    deleteUser = f'net user /delete {delAccount}'
    return deleteUser
def refreshUserList(txtPath):
    # wmic useraccount list > PATH
    refreshList = f'wmic useraccount list > {txtPath}'
####################################################
### PlayLists
def Queen():
    pl_queen = []
    a = r'https://www.youtube.com/watch?v=81t8mi5i0X0&list=PLBnJv6rImVe9XXPLwK2CvysVd_CnrYB81&index=1' #
    b = r'https://www.youtube.com/watch?v=nFORvjAMhKg&list=PLC5AB9190F21DFFFA&index=1' # A Day At The Races
    c = r'https://www.youtube.com/watch?v=ZaJT5lucoc8&list=PLBnJv6rImVe_RJ8-fSQ3OQkYnGxLDFYc-&index=1' #
    d = r'https://www.youtube.com/watch?v=Dr0Gf6OzdBM&list=PLBnJv6rImVe8bdTn3KfefBucmEbFE2OrL&index=1' #
    pl_queen = [a, b, c]
    pl_queen.append(d)
    return pl_queen
def Bach():
    pl_bach = [r'https://www.youtube.com/watch?v=6JQm5aSjX6g',
               r'https://www.youtube.com/watch?v=_ioc6sdgugo',
               r'https://www.youtube.com/watch?v=w3HCPVMtd8M',
               r'https://www.youtube.com/watch?v=h9uv7XgP8Io',
               r'https://www.youtube.com/watch?v=XiG8AGn5Qz8',
               r'https://www.youtube.com/watch?v=NCPM8DEsvmc',
               r'https://www.youtube.com/watch?v=5uEbVFAhqxk',
               r'https://www.youtube.com/watch?v=xzN6VwiZYMo',
               r'https://www.youtube.com/watch?v=hbQORqkStpk',
               r'https://www.youtube.com/watch?v=1AtOPiG5jyk',
               r'https://www.youtube.com/watch?v=3FLbiDrn8IE',
               r'https://www.youtube.com/watch?v=ZwVW1ttVhuQ',
               r'https://www.youtube.com/watch?v=7F7TVM8m95Y',
               r'https://www.youtube.com/watch?v=D5ttwUX4zWg']
    return pl_bach
def Megadeth():
    pl_megadeth = [r'https://www.youtube.com/watch?v=vo5BUWYWPvo&list=PLLHyHi7NUwSamE8YEEmIf43f6u4PkDEXC',
                   r'https://www.youtube.com/watch?v=roCMX0xfNho&list=PLLHyHi7NUwSaRwMVT0bsQuFHRxt32Hyv5',
                   r'https://www.youtube.com/watch?v=UuTq2PhsBk4&list=PLLHyHi7NUwSacwZD5fTcsEcudD5cYwo0x',
                   r'https://www.youtube.com/watch?v=p-yfXokl1l8&list=PL6ogdCG3tAWgSlx3GOZNBkOm0kw1iJUNt',
                   r'https://www.youtube.com/watch?v=-WGcyRcqx2A&list=PLLHyHi7NUwSakx0ONnipN-SoTRWxztStO',
                   r'https://www.youtube.com/watch?v=LOXrjUuXEn0&list=OLAK5uy_lBLXRW43EViiE9xRRCR6l1Ghtj1Ko6Mhc',
                   r'https://www.youtube.com/watch?v=ih-DEhLecMY&list=PLLHyHi7NUwSamqd8Xpi2taHkjL4pm1AAU&index=2']
    return pl_megadeth
def Metallica():
    pl_metallica = [r'https://www.youtube.com/watch?v=qfehFvmwQlo&list=OLAK5uy_kwDDSWKgSgMcCmR7XGOZ7KTyxK-XJO-fo',
                    r'https://www.youtube.com/watch?v=DtJzRErAJ3Q&list=PLokAorcvoBv9LAxeK6xwqn3rSEEMhGfGr',
                    r'https://www.youtube.com/watch?v=fwtJUR4t8io&list=PLf_v4I3SLUptaBedPSbvWI45j5GXPVkkb',
                    r'https://www.youtube.com/watch?v=hNXmKiEqVx4&list=PLE8F8DBAADF4DFD20',
                    r'https://www.youtube.com/watch?v=17E-zFb-0aE&list=PL6ogdCG3tAWiIOauDDXTvfTL-Gx4vz1Wt',
                    r'https://www.youtube.com/watch?v=ZnCFWlso-UQ&list=PL_Dm-xhk4f3HgEyYE9bC1YQsdHTMKmseP',
                    r'https://www.youtube.com/watch?v=zUYpCh8kpYM&list=PL5B1176DC06B14AF3',
                    r'https://www.youtube.com/watch?v=qQNYRTUwtWs&list=PL3OXlIjd29JOwq1oo0W0qz-fiJ1uPoJUD']
    return pl_metallica
def MISC():
    pl_misc = [r'https://www.youtube.com/watch?v=Tj0FQ1nhn7I',
               r'https://www.youtube.com/watch?v=5Yrlcvix8bE',
               r'https://www.youtube.com/watch?v=cmrbbfdvnGU',
               r'https://www.youtube.com/watch?v=43csxMbD5yk',
               r'https://www.youtube.com/watch?v=wRdE5ZRdKWI',
               r'https://www.youtube.com/watch?v=ZPaqCfIvGao',
               r'https://www.youtube.com/watch?v=HUHEPo_g0AQ',
               r'https://www.youtube.com/watch?v=xtLoaMfinbU',
               r'https://www.youtube.com/watch?v=NZ2NWXp-1Y4',
               r'https://www.youtube.com/watch?v=Q-B_ONJIEcE',
               r'https://www.youtube.com/watch?v=l7rRSDu9hB0',
               r'https://www.youtube.com/watch?v=6vaWug73kDs',
               r'https://www.youtube.com/watch?v=5fHngyN8Qhw',
               r'https://www.youtube.com/watch?v=lus-pRPpFok',
               r'https://www.youtube.com/watch?v=Da-2h2B4faU',
               r'https://www.youtube.com/watch?v=Unl1jXFnzgo',
               r'https://www.youtube.com/watch?v=KOKnWaLiL8w&list=PLgVx6YV8lTtylx-DI9YYI-get9pNST8Kv',
               r'https://www.youtube.com/watch?v=L3LMbpZIKhQ&list=PLB7540DEDD482705B',
               r'https://www.youtube.com/watch?v=PxCxlsl_YwY&list=PLm0X8hqw4lIotQB9ep0MKVkT2447Lk2ue',
               r'https://www.youtube.com/watch?v=wvXDB9dMdEo&list=PLUl4u3cNGP63ctJIEC1UnZ0btsphnnoHR',
               r'https://www.youtube.com/watch?v=7UJ4CFRGd-U&list=PLE7DDD91010BC51F8',
               r'https://www.youtube.com/watch?v=JzhlfbWBuQ8']
    return pl_misc
def plShuffled():
    pl_shuffled = Queen() + Bach() + Megadeth() + Metallica() + MISC()
    random.shuffle(pl_shuffled)
    return pl_shuffled
####################################################
### Press KeyBoard
def pressKey(firstKey, secondKey, rep, delay):
    # firstKey, secondKey - str, rep - intm delay - float
    kb = Controller()
    keys = {'shift': Key.shift, 'ctrl': Key.ctrl, 'tab': Key.tab, 'cmd': Key.cmd, 'esc': Key.esc,
            'f1': Key.f1, 'f2': Key.f2, 'f3': Key.f3, 'f4': Key.f4, 'f5': Key.f5, 'f6': Key.f6,
            'f7': Key.f7, 'f8': Key.f8, 'f9': Key.f9, 'f10': Key.f10, 'f11': Key.f11, 'f12': Key.f12,
            'enter': Key.enter, 'space': Key.space, 'backspcae': Key.backspace, 'delete': Key.delete,
            'up': Key.up, 'down': Key.down, 'left': Key.left, 'right': Key.right}
    fkey = firstKey
    sKey = secondKey

    for k in keys.keys():
        if k == firstKey:
            fKey = keys[firstKey]
        elif k == secondKey:
            sKey = keys[secondKey]

    if secondKey == 0:
        while rep:
            rep -= 1
            kb.press(fKey)
            time.sleep(delay)
            kb.release(fKey)
    else:
        while rep:
            rep -= 1
            with kb.pressed(fKey):
                kb.press(sKey)
                time.sleep(delay)
                kb.release(sKey)
    time.sleep(delay)
### each Key separately
def enter(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        kb.press(Key.enter)
        time.sleep(delay)
        kb.release(Key.enter)
    time.sleep(delay)
def shift_n(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.shift):
            kb.press('n')
            time.sleep(delay)
            kb.release('n')
    time.sleep(delay)
def ctrl_tab(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.ctrl):
            kb.press(Key.tab)
            time.sleep(delay)
            kb.release(Key.tab)
    time.sleep(delay)
def f5(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        kb.press(Key.f5)
        time.sleep(delay)
        kb.release(Key.f5)
    time.sleep(delay)
def alt_tab(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.alt):
            kb.press(Key.tab)
            time.sleep(delay)
            kb.release(Key.tab)
    time.sleep(delay)
def ctrl_t(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.ctrl):
            kb.press('t')
            time.sleep(delay)
            kb.release('t')
    time.sleep(delay)
def ctrl_f4(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.ctrl):
            kb.press(Key.f4)
            time.sleep(delay)
            kb.release(Key.f4)
    time.sleep(delay)
### MISC KeyBoard
def mute(delay):
    kb = Controller()
    time.sleep(delay)
    kb.press('m')
    kb.release('m')
    time.sleep(delay)
def wait(delay):
    time.sleep(delay)
###################################################
### Log functions

def routine_Log():
    # First you need to start reading log and writing
    smth = ''
    # {time_start, collecting-t/f, 0} - 0 --> time working

def browser_Log():
    smth = ''
    time.strftime("%H:%M:%S", time.localtime())

###################################################

def openCMD():
    # CMD can be opened with GUI
    os.system(f'cmd /c start /d "{os.getcwd()}"')
    wait(0.05)
def openBraveCMD(user):
    # requires user name - str
    os.system(f'echo {user}| "{os.getcwd()}\\openBraveCMD.bat"')
def openBrave(user, speed):
    openCMD()
    run_exe = runas_EXE(userList_MIKE[i], exePATH)
    wait(speed)
    kb.type(run_exe)
    enter(1, 0.25)
    kb.type('8598')
    enter(1, 0.25)
    wait(speed)
def openCMD_admin():
    # apperantly SCREEN BLOCKS KEY TYPING
    # USER SUPREVISION MANDATORY
    # arrow <- + enter
    os.system(f'"{os.getcwd()}\\cmd_Admin.bat"')
    wait(0.05)
    # & worst of all you can't autotype inside it
def runas_EXE(user, exePATH):
    # runas /user:'userName' "PATH\.exe"
    run_exe = f'runas /user:{user} \"{exePATH}\"'
    return run_exe

def tasklist():
    # tasklist /fi "imagename eq firefox.exe" /fo csv
    # tasklist /? - explore
    print('')

def taskkill():
    # taskill /pid 9214
    # taskkill /?
    print('')

####################################################################################################################
####### ROUTINES ###################################################################################################
####################################################################################################################

def routine_myPC(who, collecting, browsing):
    # who - str; collecting - boolean; browsing - int  ????? +SPEED ?????
    print('')
    # start of routine
    print('Your Orders, my liege')
    wait(1.0)
    # routine log
    routine_Log()
    # brave routine
    for U in range():
        openBrave(userList[U])
        # log
        browser_Log()
        #
        wait(1.0)
        #####################################
        opTABs = 1
        while collecting:
            f5(1, 1.0)
            wait(1.0)
        while browsing:
            ctrl_t(1, 1.0)
            opTABs += 1
            ###
            str = random.choice(plShuffled)
            kb.type(str)
            enter(1, 1.0)
            ###
            shift_n(10, 1.0)
            wait(1.0)
            # count opened TABs
        # closing Brave
        ctrl_f4(opTABs, 0.5)
        # log
        browser_Log()
        # wait(1.0) -- not required immediatle opens new Brave
    # routine log
    routine_Log()
    print('All is done, my liege')



def OLD_routine_myPC(who):
    # must set user || 'all' command
    currentUser = []
    if who != 'all':
        currentUser = ['none', who]
    else:
        currentUser = userList_MIKE
    # start of routine
    print('Your Orders, my liege')
    wait(3.0)
    for U in range(1, len(currentUser)):
        #######################################################
        run_exe = runas_EXE(userList_MIKE[U], exePATH)
        openCMD()
        kb.type(run_exe)
        enter(1, 0.3)
        kb.type('8598')
        enter(1, 0.3)
        wait(2.0)
        ##########################################################
        for i in range(4):
            ctrl_t(1, 1.0)
            kb.type(Queen[i])
            enter(1, 1.0)
            # if not i:
            #     mute(2.0)
        ctrl_tab(1, 1.0)
        f5(20, 0.5)
        wait(10)
        ctrl_f4(5, 0.5)
        ##########################################################
        wait(0.3)
        kb.type('exit')
        enter(1, 0.3)
        wait(0.3)
        #########################################################
    print('All is done, my liege')
def routine_fPC():
    print('')
def routine_fNote():
    print('')

#######################################################################################################################
#######################################################################################################################

kb = Controller()
mouse = mController()
userList = create_BASIC_UserList()
userList_MIKE = create_MIKE_UserList()
# Queen = Queen()
# Bach = Bach()
plShuffled = plShuffled()
# runas_EXE(u, exePATH)
exePATH = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'

#######################################################################################################################
#############################  WORK STARTS HERE #######################################################################
#######################################################################################################################


# for i in range(10):
#     openBraveCMD(userList_MIKE[i+1])
    # openBraveCMD(userList[i])
    # openBraveCMD(userList[i])

