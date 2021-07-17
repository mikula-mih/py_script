import sys, os, time
import random
from pynput.keyboard import Key, Controller
'''
create automated brave.exe opener
and brave.exe first installation
+ playList for automation
'''

################################################

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
    print(cmd)
def deleteAccount(delAccount):
    # net user /delete 'userName'
    deleteUser = f'net user /delete {delAccount}'
    print(deleteUser)
def refreshUserList(txtPath):
    # wmic useraccount list > PATH
    refreshList = f'wmic useraccount list > {txtPath}'

####################################################
### PlayLists
def queen():
    Queen_playList = []
    a = r'https://www.youtube.com/watch?v=81t8mi5i0X0&list=PLBnJv6rImVe9XXPLwK2CvysVd_CnrYB81&index=1' #
    b = r'https://www.youtube.com/watch?v=nFORvjAMhKg&list=PLC5AB9190F21DFFFA&index=1' # A Day At The Races
    c = r'https://www.youtube.com/watch?v=ZaJT5lucoc8&list=PLBnJv6rImVe_RJ8-fSQ3OQkYnGxLDFYc-&index=1' #
    d = r'https://www.youtube.com/watch?v=Dr0Gf6OzdBM&list=PLBnJv6rImVe8bdTn3KfefBucmEbFE2OrL&index=1' #
    Queen_playList = [a, b, c]
    Queen_playList.append(d)
    return Queen_playList
def BACH():
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
####################################################

def enter(rep, delay):
    kb = Controller()
    while rep:
        kb.press(Key.enter)
        time.sleep(delay)
        kb.release(Key.enter)
        rep -= 1
    time.sleep(0.5)
def shift_n(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.shift):
            kb.press('n')
            time.sleep(delay)
            kb.release('n')
    time.sleep(0.5)
def ctrl_tab(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.ctrl):
            kb.press(Key.tab)
            time.sleep(delay)
            kb.release(Key.tab)
    time.sleep(0.5)
def f5(rep, delay):
    kb = Controller()
    while rep:
        kb.press(Key.f5)
        time.sleep(delay)
        kb.release(Key.f5)
        rep -= 1
    time.sleep(0.5)
'''
def oneKey(rep, delay):
    kb = Controller()
    def f5(rep, delay):
        k0 = Key.f5
    def enter(rep, delay):
        k0 = Key.enter

    while rep:
        kb.press(k0)
        time.sleep(delay)
        kb.release(k0)
        rep -= 1
    time.sleep(0.5)

def twoKey(prKey, rep, delay):
    kb = Controller()
    a = Key.ctrl
    b = Key.tab
    while rep:
        rep -= 1
        with kb.pressed(a):
            kb.press(b)
            time.sleep(delay)
            kb.release(b)
    time.sleep(0.5)
'''

def alt_tab(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.alt):
            kb.press(Key.tab)
            time.sleep(delay)
            kb.release(Key.tab)
    time.sleep(0.5)
def ctrl_t(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.ctrl):
            kb.press('t')
            time.sleep(delay)
            kb.release('t')
    time.sleep(0.5)
def ctrl_f4(rep, delay):
    kb = Controller()
    while rep:
        rep -= 1
        with kb.pressed(Key.ctrl):
            kb.press(Key.f4)
            time.sleep(delay)
            kb.release(Key.f4)
    time.sleep(0.5)

def mute(delay):
    kb = Controller()
    time.sleep(delay)
    kb.press('m')
    kb.release('m')
    time.sleep(0.5)
def wait(delay):
    # ...
    time.sleep(delay)

def openCMD():
    kb = Controller()
    kb.press(Key.cmd)
    kb.release(Key.cmd)
    w = 0.1
    wait(w)
    kb.type('cmd')
    wait(w)
    enter(1, w)

def openCMD_admin():
    print('')


####################################################

def open_CMD_Admin():
    # THIS WILL BE PROBLEMATIC


    print('')
def runas_EXE(user, exePATH):
    # runas /user:'userName' "PATH\.exe"
    run_exe = f'runas /user:{user} \"{exePATH}\"'
    return run_exe
    ############################################# NEED A PASSWORD ENTR() ROUTINE

####################################################
####### ROUTINES ###################################
####################################################

def routine_myPC(who):
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
        run_exe = runas_EXE(userList_MIKE[U], exePATH)
        openCMD()
        kb.type(run_exe)
        enter(1, 0.3)
        kb.type('8598')
        enter(1, 0.3)
        wait(2.0)
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
        wait(0.3)
        kb.type('exit')
        enter(1, 0.3)
        wait(0.3)
    print('All is done, my liege')

def routine_fPC():
    print('')

def routine_fNote():
    print('')

#####################################################

kb = Controller()
userList = create_BASIC_UserList()
userList_MIKE = create_MIKE_UserList()
Queen = queen()
Bach = BACH()

u = userList[99]
# deleteAccount(u)
# createAccount(u, 'Administrators')

exePATH = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
# runas_EXE(u, exePATH)

###################################################################################################
#############################  WORK STARTS HERE ###################################################
###################################################################################################

# routine_myPC('mikeBrave_07')


currentUser = userList_MIKE[8]

print('Your Orders, my liege')
wait(3.0)
while True:
    run_exe = runas_EXE(userList_MIKE[8], exePATH)
    openCMD()
    kb.type(run_exe)
    enter(1, 0.3)
    kb.type('8598')
    enter(1, 0.3)
    wait(2.0)
    for i in range(4):
        ctrl_t(1, 1.0)
        s = random.randint(0, len(Bach)-1)
        kb.type(Bach[s])
        enter(1, 1.0)
        # if not i:
        shift_n(5, 1.0)
        #     mute(2.0)
    ctrl_tab(1, 1.0)
    f5(20, 0.5)
    wait(0.5)
    break
print('All is done, my liege')

