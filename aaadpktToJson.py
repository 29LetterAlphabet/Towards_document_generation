import dpkt
import math
from dpkt.ip import IP
import socket    
import sys   
import datetime 
import os


results = "" 
input_fnames = [x for x in os.listdir(os.getcwd()) if x.endswith("cap")]




def protocolString(x):
    global z

    if ip.p==dpkt.ip.IP_PROTO_TCP: #ip.p == 6: 
        tcp = x.data
        z = "TCP"

        # HTTP uses port 80
        if tcp.dport == 80 or tcp.sport == 80:
            return "HTTP"

        # HTTPS uses port 443
        elif tcp.dport == 443 or tcp.sport == 443:
            return "HTTPS"

        elif tcp.dport == 445 or tcp.sport == 445:
            return "LDAP"

        elif tcp.dport == 19 or tcp.sport == 19:
              return "CHARGEN"

        # SSH uses port 22
        elif tcp.dport == 22 or tcp.sport == 22:
            return "SSH"

        # SMTP uses port 25
        elif tcp.dport == 25 or tcp.sport == 25:
            return "SMTP"

        # telnet uses port 23
        elif tcp.dport == 23 or tcp.sport == 23:
            return "telnet"

        # whois uses port 43
        elif tcp.dport == 43 or tcp.sport == 43:
            return "whois"

        elif tcp.dport == 53 or tcp.sport == 53:
            return "DNS"

        # rsync uses port 873
        elif tcp.dport == 873 or tcp.sport == 873:
            return "rsync"

        # FTP uses port 21
        elif tcp.dport == 21 or tcp.sport == 21:
                return "FTP"

        elif tcp.dport == 1433 or tcp.sport == 1433:
                return "MSSQL"

        elif tcp.dport == 1723 or tcp.sport == 1723:
                return "PPTP"

        elif tcp.dport == 3389 or tcp.sport == 3389:
                return "RDP"

        elif tcp.dport == 5060 or tcp.sport == 5060:
                return "SIP"

        elif tcp.dport == 5900 or tcp.sport == 5900:
                return "VNC"

        else :
            return "Other TCP"

    # UDP packets
    elif ip.p==dpkt.ip.IP_PROTO_UDP: #ip.p==17:
        udp=x.data
        z = "UDP"

        if udp.dport == 19:
              return "CHARGEN"

        elif udp.dport == 22:
            return "SSH"

        elif udp.dport == 23:
            return "telnet"

        elif udp.dport == 53:
            return "DNS"

        # DHCP uses ports 67, 68
        elif udp.dport == 67 or udp.dport == 68:
            return "DHCP"

        # NTP uses port 123
        elif udp.dport == 123:
            return "NTP"

        elif udp.dport == 1723:
                return "PPTP"

        elif udp.dport == 3389:
                return "RDP"

        elif udp.dport == 5060:
                return "SIP"

        elif udp.dport == 5900:
                return "VNC"

        else :
            return "Other UDP"

    else :
        return "UNKNOWN"

print input_fnames
for fname in input_fnames:

	resar = []
	count = 1
	tsOne = 0
	z = ""

	outFile = open(str(fname[:-18])+'.json', 'w')
	filename = fname
	
	for ts, data in dpkt.pcap.Reader(open(filename, 'r')):

		lnth = len(data)
		resar.append('{\n')
		count += 1
		resar.append('"time" : "'+str(datetime.datetime.fromtimestamp(float(ts)).strftime('%d-%m-%Y %H:%M:%S'))+'",\n')


		try:
			eth=dpkt.ethernet.Ethernet(data)
		except dpkt.dpkt.NeedData:
			sys.exit()
		
		ip=eth.data
		try:
			tcp=ip.data
			udp=ip.data
		except AttributeError:
				resar.append('"source" : "-1",\n')
				resar.append('"destination" : "-1",\n')
				resar.append('"length" : "-1",\n')
				resar.append('"sourceAdr" : "-1",\n')
				resar.append('"destAdr" : "-1",\n')
				resar.append('"protocol" : "-1",\n')
				resar.append('"type" : "-1"\n}\n')
				continue
				
		srcAddr = socket.inet_ntoa(ip.src)
		dstAddr = socket.inet_ntoa(ip.dst)

		resar.append('"source" : "'+srcAddr+'",\n')
		resar.append('"destination" : "'+dstAddr+'",\n')
		packetLength = 0
		realPackLength = lnth
		if ip.p == dpkt.ip.IP_PROTO_TCP:
				
			try:
				packetLength = len(tcp.data)	#NBNBNBN try taking eth.data length
			except AttributeError: #generic error handler first is 107823
				resar.append('"length" : "'+str(realPackLength)+'",\n')
				resar.append('"sourceAdr" : "-1",\n')
				resar.append('"destAdr" : "-1",\n')
				resar.append('"protocol" : "Other TCP",\n')
				resar.append('"type" : "TCP"\n}\n')
				continue

		elif ip.p == dpkt.ip.IP_PROTO_UDP:
			try:
				packetLength = len(udp.data)
			except AttributeError: #generic error handler first is 107823
				resar.append('"length" : "'+str(realPackLength)+'",\n')
				resar.append('"sourceAdr" : "-1",\n')
				resar.append('"destAdr" : "-1",\n')
				resar.append('"protocol" : "Other UDP",\n')
				resar.append('"type" : "UDP"\n}\n')
				continue
		
		pktString = str(realPackLength)

		if ip.p == dpkt.ip.IP_PROTO_ICMP:
			resar.append('"length" : "'+pktString+'",\n')
			resar.append('"sourceAdr" : "-1",\n')
			resar.append('"destAdr" : "-1",\n')
			resar.append('"protocol" : "ICMP",\n')
			resar.append('"type" : "UDP"\n}\n')
			
			
		else:
			try:
				str(tcp.sport)
			except AttributeError:
				resar.append('"length" : "'+pktString+'",\n')
				resar.append('"sourceAdr" : "-1",\n')
				resar.append('"destAdr" : "-1",\n')
				resar.append('"protocol" : "-1",\n')
				resar.append('"type" : "TCP"\n}\n')
				continue
			else:
				resar.append('"length" : "'+pktString+'",\n')
				resar.append('"sourceAdr" : "'+str(tcp.sport)+'",\n') #try catch Attribute error here as well
				resar.append('"destAdr" : "'+str(tcp.dport)+'",\n')
				resar.append('"protocol" : "'+protocolString(ip)+'",\n')
				resar.append('"type" : "'+str(z)+'"\n}\n')
		s = ''.join(resar)
		outFile.write(s)
		resar = []
		if count%50000 == 0:
			print count
		if count%1000000 == 0:
			print filename
		
	outFile.close()

		
		
	
	








