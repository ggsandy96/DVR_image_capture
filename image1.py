#version 20
#donot run this file at startup
#19th june 2016
#improvements: number of screenshots to be taken is not fixed
#the new csv file can be uploaded with the name camx_new.csv into the folder camx
#the automatic file deletion feature included
#forced screenshots added
#delete the old files once per day
#directly input values in camx.csv is also working
#camera power management
#fixed the problem of crash while instant image capture
#the name of the image will be the actual time of capture and not that of the csv
#camera power managed
#events folder added

import subprocess
import numpy as np
import csv
import datetime
import os
import signal
import sys
import time

def capture():
	with open('/sys/class/gpio/gpio148/value', 'r') as myfile:
		state=myfile.read().replace('\n', '')
	state=int(state)
	if(state==1):
		now = datetime.datetime.now()
        	year = now.year
        	day = now.day
        	month = now.month
        	hour = now.hour
        	minute = now.minute
        	second = now.second
        	year = str(year)
       		month=str(month).zfill(2)
        	day=str(day).zfill(2)
        	hour=str(hour).zfill(2)
        	minute=str(minute).zfill(2)
	        second=str(second).zfill(2)
		cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.11 -vframes 1 -vcodec png /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png"
		print cmd_instant
		os.system(cmd_instant)
		fline=open("/home/linaro/user/camera/ftppath.txt").readline().rstrip()
		split = fline.index('/')
        	path=fline[split+1:]
	        url = fline[:split]
		cmd_upload_instant="lftp -u sandeep,aia@123 -e 'cd " + path + ";cd cam1;put /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png;exit' " + url + " &"
		os.system(cmd_upload_instant)
	else:
		os.system("sudo /home/linaro/App/cameraapp/high.sh")
		time.sleep(10)
		count=0
		status = os.system("ping -c 1 192.168.1.11")
		while (status!=0):
			status = os.system("ping -c 1 192.168.1.11")
			time.sleep(5)
			count = count+1
			if(count>=5):
				status=0
		time.sleep(20)
		now = datetime.datetime.now()
        	year = now.year
        	day = now.day
        	month = now.month
        	hour = now.hour
        	minute = now.minute
        	second = now.second
        	year = str(year)
       		month=str(month).zfill(2)
        	day=str(day).zfill(2)
        	hour=str(hour).zfill(2)
	        minute=str(minute).zfill(2)
	        second=str(second).zfill(2)
		cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.11 -vframes 1 -vcodec png /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png"
                os.system(cmd_instant)
                fline=open("/home/linaro/user/camera/ftppath.txt").readline().rstrip()
                split = fline.index('/')
                path=fline[split+1:]
                url = fline[:split]
                cmd_upload_instant="lftp -u sandeep,aia@123 -e 'cd " + path + ";cd cam1;put /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png;exit' " + url + " &"
                os.system(cmd_upload_instant)
	os.system("sudo /home/linaro/App/cameraapp/low.sh")

def signal_handler(signal, frame):
	capture()

def signal_handler2(signal, frame):
        with open('/sys/class/gpio/gpio148/value', 'r') as myfile:
		state=myfile.read().replace('\n', '')
	state=int(state)
	if(state==1):
		now = datetime.datetime.now()
        	year = now.year
        	day = now.day
        	month = now.month
        	hour = now.hour
        	minute = now.minute
        	second = now.second
        	year = str(year)
       		month=str(month).zfill(2)
        	day=str(day).zfill(2)
        	hour=str(hour).zfill(2)
        	minute=str(minute).zfill(2)
	        second=str(second).zfill(2)
		cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.11 -vframes 1 -vcodec png /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png"
		os.system(cmd_instant)
	else:
		os.system("sudo /home/linaro/App/cameraapp/high.sh")
		time.sleep(10)
		count=0
		status = os.system("ping -c 1 192.168.1.11")
		while (status!=0):
			status = os.system("ping -c 1 192.168.1.11")
			time.sleep(10)
			count = count+1
			if(count>=5):
				status=0
		time.sleep(20)
		now = datetime.datetime.now()
        	year = now.year
        	day = now.day
        	month = now.month
        	hour = now.hour
        	minute = now.minute
        	second = now.second
        	year = str(year)
       		month=str(month).zfill(2)
        	day=str(day).zfill(2)
        	hour=str(hour).zfill(2)
	        minute=str(minute).zfill(2)
	        second=str(second).zfill(2)
		cmd_instant  = "ffmpeg -rtsp_transport tcp -y -i rtsp://admin:admin@192.168.1.11 -vframes 1 -vcodec png /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png"
                os.system(cmd_instant)
                fline=open("/home/linaro/user/camera/ftppath.txt").readline().rstrip()
                split = fline.index('/')
                path=fline[split+1:]
                url = fline[:split]
                cmd_upload_instant="lftp -u sandeep,aia@123 -e 'cd " + path + ";cd cam1;put /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png;exit' " + url + " &"
                os.system(cmd_upload_instant)
                cmd_trans= "cp /home/linaro/user/camera/cam1/cam1_"+year+"_"+month+"_"+day+"_"+hour+"_"+minute+"_"+second+".png /home/linaro/user/camera/cam1/event/"
                os.system(cmd_trans)
	os.system("sudo /home/linaro/App/cameraapp/low.sh")

signal.signal(signal.SIGUSR1, signal_handler)
signal.signal(signal.SIGUSR2, signal_handler2)

def read():
        f1 = file('/home/linaro/user/camera/cam1/cam1.csv', 'r')
        c1 = csv.reader(f1)
        return c1

def delete(str):
	print "delete loop entered"
	print old
	rem = "find /home/linaro/user/camera/cam1 -type f -mtime +" +old+ " -name '*.png' -exec rm -rf {} \;"
	os.system(rem)
	
try:
	c1 = read()
	c1=list(c1)
	arr1 = np.asarray(c1)
	upload = 0
	arr1 = arr1.astype(int)
	a1 = len(arr1)
	old = str(arr1[0][0])
	delete(old)

except:
	try:
		os.system("cp /home/linaro/user/camera/cam1/cam1.bak /home/linaro/user/camera/cam1/cam1.csv")
        	c1= read()
        	c1=list(c1)
        	arr1 = np.asarray(c1)
        	arr1 = arr1.astype(int)
        	a1 = len(arr1)
		old = str(arr1[0][0])
		delete(old)

	except:
		arr1 = [[30,10,10],[0,0,0]]
		arr1=list(arr1)
		arr1 = np.asarray(arr1)
		arr1 = arr1.astype(int)
		a1 = len(arr1)
		old = str(arr1[0][0])
		delete(old)
day1 = int(0)
print arr1
while(1):
	if (os.path.isfile("/home/linaro/user/camera/cam1/cam1_new.csv") == True ):
		out = subprocess.check_output("ps aux | grep ftpd", shell=True)
		if 'cam1_new.csv' in out:
       			print "csv file is being uploaded"
		else:
		       	print "cam1_csv upload complete"
			try:
				os.system("mv /home/linaro/user/camera/cam1/cam1.csv /home/linaro/user/camera/cam1/cam1.bak")
	                        os.system("mv /home/linaro/user/camera/cam1/cam1_new.csv /home/linaro/user/camera/cam1/cam1.csv")
				c1= read()
                        	c1=list(c1)
                	        arr1 = np.asarray(c1)
        	                arr1 = arr1.astype(int)
				try:
					old = str(arr1[0][0])
                                        delete(old)
				except:
					continue
				a1 = len(arr1)

			except:
				try:
			                os.system("cp /home/linaro/user/camera/cam1/cam1.bak /home/linaro/user/camera/cam1/cam1.csv")
                			c1= read()
                			c1=list(c1)
			                arr1 = np.asarray(c1)
        			        arr1 = arr1.astype(int)
                			a1 = len(arr1)
        			except:
                			arr1 = [[0,0,0],[0,0,0]]
                			arr1=list(arr1)
                			arr1 = np.asarray(arr1)
               				arr1 = arr1.astype(int)
                			a1 = len(arr1)
			print arr1
	now = datetime.datetime.now()
	year = now.year
	day = now.day
	month = now.month
        hour = now.hour
        minute = now.minute
        second = now.second
	if(int(day) != day1):
		print "entered loop"
		delete(old)
		day1=day
		print day1
	for i in range(a1):
		try:
			if(arr1[i+1][2] == second and arr1[i+1][1] == minute and arr1[i+1][0] == hour):
				capture()
		except:
			continue
