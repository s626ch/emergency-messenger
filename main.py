import tkinter as tk
import smtplib
app = tk.Tk()
# email login details
emsrv = '' # smtp server
eml = '' # email
psw = '' # password

# actually obtain the input
def sndmsg():
    #login
    srvr = smtplib.SMTP(emsrv, 587) # define server, replace port with whatever port your email server uses
    # authenticate 
    srvr.starttls()
    srvr.ehlo() # hello call
    srvr.login(eml, psw) # auth with email and pw
    print("\n\nauthenticated!\n\n")
    # obtain numbers
    # to send with email, i have to actually concat each carrier's text addr
    phnone = str(numone.get())
    phnlist = phnone.split(",")
    # send it AYEEEEEEeeeeeee....
    sntmsg = msginp.get()
    #emlmsg = 'From: ' + str(eml) + '\nSubject: EMERGENCY' + '\n\n' + str(sntmsg)
    emlmsg = 'From: ' + str(eml) + '\n\n' + str(sntmsg)
    for j in phnlist:
        phncar = [  
            j + '@txt.att.net', #               AT&T SMS
            j + '@mms.att.net', #               AT&T MMS
            j + '@sms.myboostmobile.com', #     BOOST SMS
            j + '@myboostmobile.com', #         BOOST MMS
            j + '@mms.cricketwireless.net', #   CRICKET SMS & MMS
            j + '@msg.fi.google.com', #         GOOGLE FI SMS & MMS
            j + '@mymetropcs.com', #            METROPCS SMS & MMS
            j + '@text.republicwireless.com', # REPUBLIC SMS
            j + '@messaging.sprintpcs.com', #   SPRINT SMS
            j + '@pm.sprint.com', #             SPRINT MMS
            j + '@tmomail.net', #               TMOBILE SMS & MMS - (POSSIBLY ONLY MMS??)
            j + '@message.ting.com', #          TING SMS
            j + '@mmst5.tracfone.com', #        TRACFONE MMS
            j + '@email.uscc.net', #            US CELLULAR SMS
            j + '@mms.uscc.net', #              US CELLULAR MMS
            j + '@vtext.com', #                 VZW SMS
            j + '@vzwpix.com', #                VZW MMS
            j + '@vmobl.com', #                 VIRGIN MOBILE SMS
            j + '@vmpix.com' #                  VIRGIN MOBILE MMS
        ]
        srvr.sendmail(eml, phncar, emlmsg)
        print(eml, phncar, emlmsg)
    srvr.quit()
    print("\n\nstopping mail session\n\n")
# define
aphd = tk.Label(app, text="Emergency messenger!")
nseclb = tk.Label(app,text="Numbers:\nEx: 2345678910\n2345678910,3301119912,5558100281")

# number input
numone = tk.Entry(app)

# message area
msglb = tk.Label(app, text="Message:")
msginp = tk.Entry(app)

# button to send message!
sndbtn = tk.Button(app,text="Send message!",command=sndmsg)

# pack
aphd.pack(fill=tk.BOTH,expand=True)
nseclb.pack(fill=tk.BOTH,expand=True)

# pack sending functions
numone.pack(fill=tk.BOTH,expand=True)
msglb.pack(fill=tk.BOTH,expand=True)
msginp.pack(fill=tk.BOTH,expand=True)
sndbtn.pack(fill=tk.BOTH,expand=True)

# init app
app.title("Emergency messenger!")
app.geometry('346x157')
app.mainloop()