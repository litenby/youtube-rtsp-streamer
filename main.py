

import tkinter as tk
from tkinter import *
import subprocess 
from subprocess import Popen, PIPE, STDOUT, call
import threading
import re
import time
import os
import json

with open('config.json') as config_file:
    config = json.load(config_file)

cam1_ip = config["camera1"]["ip"]
cam1_key = config["camera1"]["stream_key"]

cam2_ip = config["camera2"]["ip"]
cam2_key = config["camera2"]["stream_key"]

cam1_program_location = config["camera1"]["program_location"]
cam2_program_location = config["camera2"]["program_location"]

top = tk.Tk()
t = None

# Enable auto restart for individual cameras

cam1 = 1
cam2 = 0
# Time of last restart
c1lastRestartTime = time.time()
c2lastRestartTime = time.time()

c1RecordUptime = 0
c2RecordUptime = 0
# Counts to keep track of how many times cameras restart

cam1RestartCount = 0
cam2RestartCount = 0

# Disabled by default, enabled using button
autoRestart = 0

ffmpeg1_avg = [0, 0]
ffmpeg2_avg = [0, 0]
cam1UploadAvg = 0
cam2UploadAvg = 0

def calculate_average_bandwidth(file_path):
    global ffmpeg1_avg, ffmpeg2_avg
    global cam1UploadAvg
    global cam2UploadAvg
    ffmpeg1_sent = []
    ffmpeg1_received = []
    ffmpeg2_sent = []
    ffmpeg2_received = []

    # Open the file and read line by line
    beginningCounterCam1 = 4
    beginningCounterCam2 = 4
    with open(file_path, 'r') as file:
        for line in file:
            # Look for lines that contain ffmpeg1 or ffmpeg2
            if cam1_program_location in line:
                parts = line.split()
                if(beginningCounterCam1 !=0): beginningCounterCam1 -= 1
                if len(parts) > 2 and beginningCounterCam1 == 0:  # Ensure the line has the expected number of parts
                    print("parts[-2]", parts[-2])
                    sent_bandwidth = float(parts[-2]) * 10 # Sent bandwidth in KB/sec
                    received_bandwidth = float(parts[-1]) * 10  # Received bandwidth in KB/sec
                    ffmpeg1_sent.append(sent_bandwidth)
                    ffmpeg1_received.append(received_bandwidth)
            
            elif cam2_program_location in line:
                parts = line.split()
                if(beginningCounterCam2 !=0): beginningCounterCam2 -= 1
                if len(parts) > 2 and beginningCounterCam2 == 0:  # Ensure the line has the expected number of parts
                    sent_bandwidth = float(parts[-2]) * 10  # Sent bandwidth in KB/sec
                    received_bandwidth = float(parts[-1]) * 10  # Received bandwidth in KB/sec
                    ffmpeg2_sent.append(sent_bandwidth)
                    ffmpeg2_received.append(received_bandwidth)

    # Calculate averages only if there is data
    if ffmpeg1_sent and ffmpeg1_received:
        ffmpeg1_avg = [sum(ffmpeg1_sent) / len(ffmpeg1_sent), sum(ffmpeg1_received) / len(ffmpeg1_received)]
    #else:
        #ffmpeg1_avg = [0, 0]  # Handle the case where no data is available for ffmpeg1

    if ffmpeg2_sent and ffmpeg2_received:
        ffmpeg2_avg = [sum(ffmpeg2_sent) / len(ffmpeg2_sent), sum(ffmpeg2_received) / len(ffmpeg2_received)]

    #else:
        #ffmpeg2_avg = [0, 0]  # Handle the case where no data is available for ffmpeg2

def Start1():
  global c1lastRestartTime
  global cam1RestartCount
  timeNow = time.time()
  delay = timeNow - c1lastRestartTime
  print(delay)
  if delay > 20:
    c1lastRestartTime = time.time()
    cam1RestartCount = cam1RestartCount + 1
    Stop1()
    myUrl=f'xterm -geometry 80x25+50+20 -fg green -hold -e "{cam1_program_location} -rtsp_transport tcp -thread_queue_size 5096 -i \"{cam1_ip}\" -rtbufsize 200M -f lavfi -f dshow -c:a copy -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/{cam1_key}\""'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 1 started.")

def Start2():
  global c2lastRestartTime
  global cam2RestartCount
  timeNow = time.time()
  delay = timeNow - c2lastRestartTime
  print(delay)
  if delay > 20:
    c2lastRestartTime = time.time()
    cam2RestartCount = cam2RestartCount + 1
    Stop2()
    myUrl=f'xterm -geometry 80x25+50+20 -fg green -hold -e "{cam2_program_location} -rtsp_transport tcp -thread_queue_size 5096 -i \"{cam2_ip}\" -rtbufsize 200M -f lavfi -f dshow -c:a copy -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/{cam2_key}\""'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 2 started.")

def StartAll():
    Start1()
    Start2()
    
def Stop1():
    call("ps -ef | grep ffmpeg1 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 1 stopped.")

def Stop2():
    call("ps -ef | grep ffmpeg2 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 2 stopped.")
    
def StopAll():
    call("ps -ef | grep ffmpeg | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("All cameras stopped.\n")

def getUptime(camNum):
    global c1lastRestartTime
    global c1RecordUptime
    global c2lastRestartTime
    global c2RecordUptime
    currentTime = time.time()
    if camNum == 1:
      compareTime = c1lastRestartTime
      upTime = currentTime - compareTime
      upTime = int(upTime)
      if upTime > c1RecordUptime:
        c1RecordUptime = upTime
    if camNum == 2:
      compareTime = c2lastRestartTime
      upTime = currentTime - compareTime
      upTime = int(upTime)
      if upTime > c2RecordUptime:
        c2RecordUptime = upTime
    return upTime

def check():
  global t
  global cam1
  global cam2
  
  global autoRestart
  global c1RecordUptime
  global c2RecordUptime
  global cam1UploadAvg
  global cam2UploadAvg
  
  call("sudo timeout 20 nethogs -t > output.txt", shell=True)
  calculate_average_bandwidth('output.txt')
  
  #totalUploadAvg = ffmpeg1_avg[0] + ffmpeg2_avg[0]
  
  print(f"Camera 1 - Avg Speed: {ffmpeg1_avg[0]:.0f}kbps Uptime: ",getUptime(1)," Restarts: ",cam1RestartCount,"Record Uptime: ",c1RecordUptime)
  print(f"Camera 2 - Avg Speed: {ffmpeg2_avg[0]:.0f}kbps Uptime: ",getUptime(2)," Restarts: ",cam2RestartCount,"Record Uptime: ",c2RecordUptime)
  #print("           Total UL:  ",totalUploadAvg)

  if autoRestart == 1:
    if cam1 == 1:
      if ffmpeg1_avg[0] < 26000:
        Start1()
    if cam2 == 1:
      if ffmpeg2_avg[0] < 6000:
        Start2()

  t = threading.Timer(25, check)
  t.start()

check()

def AutoRestartOn():
  global autoRestart
  t = threading.Timer(20, check)
  t.start()
  autoRestart = 1
  print("Auto restart ON")

def AutoRestartOff():
  global autoRestart
  t.cancel()
  autoRestart = 0
  print("Auto restart OFF")

def exit_program():
    global t
    print("Exiting program.")
    StopAll()
    try:
      if t is not None:
        t.cancel()
    except:
      pass
    top.destroy()
    os._exit(0)


B = tk.Button(top, text ="Cam 1 Start", command = Start1)
B.pack()
B = tk.Button(top, text ="Cam 1 Stop", command = Stop1)
B.pack()
B = tk.Button(top, text ="Cam 2 Start", command = Start2)
B.pack()
B = tk.Button(top, text ="Cam 2 Stop", command = Stop2)
B.pack()
B = tk.Button(top, text ="Start All", command = StartAll)
B.pack()
B = tk.Button(top, text ="Stop All", command = StopAll)
B.pack()
B = tk.Button(top, text ="Auto Restart Off", command = AutoRestartOff)
B.pack()
B = tk.Button(top, text ="Auto Restart On", command = AutoRestartOn)
B.pack()
B = tk.Button(top, text="Exit", fg="red", command=exit_program)
B.pack()
top.mainloop()