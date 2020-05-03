import socket
import datetime     # needed to calculate the time and rate of file transfer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip address and port
# to get ip address manually go to command prompt and type ipconfig. Get the ipv4 address
ipv4 = socket.gethostbyname(socket.gethostname())
port = 8000

# use the ip and port from this line
print("Starting server at\nIP: ",ipv4,"\nPort: ",port)

# get the filename
print()

s.bind((ipv4,port))
s.listen(10)
c, addr = s.accept()

print('{} connected.'.format(addr))
time_now = datetime.datetime.now()

#f = open('Marvels.Daredevil.S02E01.1080p.x265.HEVC.Filmaneh.mkv','rb')
f = open('origami.mp4','rb')
datas = f.read(1024)

while datas:
    c.send(datas)
    datas = f.read(1024)

f.close()
print("Done sending")
time_after = datetime.datetime.now()
print("Time taken")
print(time_after-time_now)