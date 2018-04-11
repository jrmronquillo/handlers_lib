import socket    # used for TCP/IP communication
import smtplib   # used to send email report
import time      # used to insert current date in email report
import sys
import requests

#if len(sys.argv) < 3:
#	print "Error: Need to Provide (rack, command, slot) as arguments"
#	sys.exit(0)

#key = sys.argv[2]


          
def keyPress(rack, key, slot):	
	if rack == "A00":
		rack = "00-80-A3-A2-D9-13"
	elif rack == "A01":
		rack = "00-80-A3-A9-E3-68"	
	elif rack == "A02":
		rack = "00-80-A3-A9-E3-6A"
	elif rack == "A03":
		rack = "00-80-A3-A9-E3-7A"
	elif rack == "A04": 
		rack = "00-80-A3-A9-DA-67"
	elif rack == "A05":
		rack = "00-80-A3-A9-E3-79"
	elif rack == "A06":
		rack = "00-80-A3-A9-E3-78"
	elif rack == "A07":
		rack= "00-80-A3-9E-67-37"
	elif rack == "A08":
		rack = "00-80-A3-9D-86-D5"
	elif rack == "A09":
		rack = "00-80-A3-9D-86-CF"
	elif rack == "A10":
		rack = "00-80-A3-9E-67-27"
	elif rack == "A11": 
		rack = "00-80-A3-9E-67-34"
	elif rack == "A12":
		rack = "00-80-A3-9E-67-35"
	elif rack == "B04":
		rack = "00-20-4A-BD-C5-1D"
	elif rack == "B05":
		rack = "00-80-A3-9D-86-D2"
	elif rack == "B06":
		rack = "00-80-A3-9E-67-3B"
	elif rack == "B07":
		rack = "00-80-A3-9E-67-36"
	elif rack == "B08":
		rack = "00-80-A3-9E-67-32"
	elif rack == "B09":
		rack = "00-80-A3-9D-86-D6"
	elif rack == "B10":
		rack = "00-80-A3-9D-86-D3"
	elif rack == "B11":
		rack = "00-80-A3-9D-86-D1"
	elif rack == "B12":
		rack = "00-80-A3-9D-86-D0"
	else:
		print "Invalid Rack number inputted for first argument"
		sys.exit(0)


#Prepare 3-byte control message for transmission
        TCP_IP = '10.23.223.36'
        TCP_PORT = 40000
        BUFFER_SIZE = 1024
        MESSAGE = 'MAC="' + rack + '" dataset="RC71" signal="' + key + '" output="' + slot + '" \n'
#Open socket, send message, close scoket
        p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        p.connect((TCP_IP, TCP_PORT))
        p.send(MESSAGE)
        data = p.recv(BUFFER_SIZE)
        p.close()
        print "Return Data: " + str(data) + key
#keyPressAPI(rack, key, "1-16")




def tune(channel, rack, slot):
	
	for i in channel:
		print i
		keyPress(rack, i, slot)
		time.sleep(1)
	# Delay to wait for info banner to disappear
	time.sleep(6)
	return "Function to tune to channel"

def dbEntry(entryText):
	if entryText:	
		URL = "http://127.0.0.1:5000/postTest/?name=%s" % entryText
		r = requests.get(url=URL)
	return

def verify_info_banner():
	# note: this only check if the info banner was detected, it does not validate the specific channel it was tuned to
	stbt.wait_for_match('/home/e2e/e2ehost29_local/sanityAutomation/images/info_banner_corner.png')
        # keyPress(rack, "prev", slot)
        time.sleep(6)


def image_verified(image, threshold):
	counter = 0
        for x in range(0, threshold):
		if stbt.detect_match(image).next().match:
			print "Detected True"
			counter += 1
		else:
			print "detected false"
	print "counter:"+str(counter)
	if counter < threshold:
		print "checked "+str(threshold)+"times did not find strong  match for image"
		return False
	else:
		return True

def init2(func, *args, **kwargs):
	try:
		t = func()
	except:
		print "error found"
		# when a test fails, store the result in the database		
		error = sys.exc_info()[1]
		dbEntry(error)




 
