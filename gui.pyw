import tkinter
import time
import paramiko

# SSH INITIALIZATION
host = "192.168.0.176"
username = "pi"
password = "password"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)


# GUI INTIALIZATION
root = tkinter.Tk()
root.iconbitmap(r'C:\Users\LukeF\LED\favicon.ico')


# GUI BUTTON FUNCTIONS
def turnOn():
    _stdin, _stdout,_stderr = client.exec_command("python3 /home/pi/LED/LEDLightShow/LEDfuncs/turnOn.py")
    myLabel = tkinter.Label(root, text='test strand initiated')
    myLabel.pack()

def turnOff():
    _stdin, _stdout,_stderr = client.exec_command("python3 /home/pi/LED/LEDLightShow/LEDfuncs/turnOff.py")
    myLabel2 = tkinter.Label(root, text='test strand off or sumn')
    myLabel2.pack()
#def disconnect():
    # execute turn off file
    #client.close()

testButton = tkinter.Button(root, text='test strand', command = turnOn)
testButtonOff = tkinter.Button(root, text='test strand off', command = turnOff)
testButton.pack()


root.mainloop()
