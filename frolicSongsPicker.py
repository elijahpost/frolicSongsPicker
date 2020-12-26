import sys
import time
from random import randint
from datetime import datetime

def main():
    animation = [
        '\,,/(>.<) \,,/   ',
        '\,,/ (>.<)\,,/   '
    ]
    animation_index = 0

    print('ok set the time you want the notification sent.')
    userDefinedHour = -1
    while userDefinedHour not in range(0,24):
        print('First, the HOUR of the day, 0-23 please')
        userDefinedHour = int(input())
        if 0 <= int(userDefinedHour) <= 23:
            break
    userDefinedMinute = -1
    while userDefinedMinute not in range(0,60):
        print('Second, the MINUTE of the day, 0-59 please')
        userDefinedMinute = int(input())
        if 0 <= int(userDefinedMinute) <= 59:
            break
    print('k, I\'ll go off every time the clock hits '+str(userDefinedHour)+':'+str(userDefinedMinute))
    print('just x this window out to reset.')

    while True:
        print(animation[animation_index % len(animation)], end='\r')
        animation_index += 1
        time.sleep(0.1)
        now = datetime.now()
        timeH = now.hour
        timeM = now.minute
        if timeH == userDefinedHour and timeM == userDefinedMinute:
            print('\,,/ (O.O) \,,/')
            dewIt()

def dewIt():
    import smtplib
    from songs import songs # in .gitignore, follow Frolic on IG if you wanna know ;)
    while True:
        track1 = songs[randint(0, len(songs)-1)]
        track2 = songs[randint(0, len(songs)-1)]
        if track1 != track2:
            break
    from creds import gmailaddress, gmailpassword, mailto #creds in .gitignore for security reasons
    message = '\n' + str(track1) + '\n' + str(track2)
    mailServer = smtplib.SMTP('smtp.gmail.com', 587) # or 485 if 587 doesn't work
    mailServer.starttls()
    mailServer.login(gmailaddress, gmailpassword)
    mailServer.sendmail(gmailaddress, mailto, message)
    now = datetime.now()
    print('Successfully sent a message at '+str(now)+' recommending '+str(track1)+' and '+str(track2)+'.')
    mailServer.quit()
    resetCounter = 60
    while resetCounter != 0:
        resetCounter -= 1
        print('Resetting in ' + str(resetCounter) + '...', end=' '+'\r')
        time.sleep(1)

main()




# Learning: VSCode: Cmd+K+C to comment out highlighted, Cmd+K+U to uncomment 

# animation_multiline = [
#     '\,,/(>.<)\,,/\n ||       || \n \\\\       // ',
#     '\,,/     \,,/\n || (>.<) || \n \\\\       // ',
#     '\,,/     \,,/\n ||       || \n \\\\ (>.<) // ',
#     '\,,/     \,,/\n || (>.<) || \n \\\\       // '
#     ]

#   taken out of DewIt when trying to remove SUBJECT
#   body = str(strSpace) + '\n' + str(track1) + '\n' + str(track2)
#   message = 'Subject: {}\n\n{}'.format(SUBJECT, body)
#   SUBJECT = 'Tracks Today'

# def timer(eitherHourOrMinute):
#     now = datetime.now()
#     choice = eitherHourOrMinute
#     if choice == 'hour':
#         choice = now.hour
#     elif choice == 'minute':
#         choice = now.minute
#     else:
#         print('Timer Error - Quitting')
#         sys.exit
#     return choice