import pafy
link_list = ["https://www.youtube.com/watch?v=UDDMYw_IZnE&list=RDQMCuWWsgWD_mw&index=2",
             "https://www.youtube.com/watch?v=wV-uzm7Hfcw","https://www.youtube.com/watch?v=pqNCD_5r0IU","https://www.youtube.com/watch?v=EQ205a0P10Y"]
s=0
for link in link_list:
    url = link
    video = pafy.new(url)
    #print(video.length)
    s= s+video.length
H = s/3600
s = s%3600
M=s/60
S= s%60
from datetime import time
t= time(int(H),int(M),int(S))

#print(t.hour,t.minute,t.second)

print("{:0>2}:{:0>2}:{:0>2}".format(t.hour,t.minute,t.second))
