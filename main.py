

import tkinter as tk
from tkinter import *
import subprocess 
from subprocess import Popen, PIPE, STDOUT, call
import threading
import re
import time

top = tk.Tk()
t = None

# Enable auto restart for individual cameras
cam0 = 0
cam1 = 1
cam2 = 1
cam3 = 1
cam4 = 1 
cam5 = 1
cam6 = 1
cam7 = 0 
cam8 = 0 
cam9 = 0

# Time of last restart
c0lastRestartTime = time.time()
c1lastRestartTime = time.time()
c2lastRestartTime = time.time()
c3lastRestartTime = time.time()
c4lastRestartTime = time.time()
c5lastRestartTime = time.time()
c6lastRestartTime = time.time()
c7lastRestartTime = time.time()
c8lastRestartTime = time.time()
c9lastRestartTime = time.time()

c0RecordUptime = 0
c1RecordUptime = 0
c2RecordUptime = 0
c3RecordUptime = 0
c4RecordUptime = 0
c5RecordUptime = 0
c6RecordUptime = 0
c7RecordUptime = 0
c8RecordUptime = 0
c9RecordUptime = 0

# Counts to keep track of how many times cameras restart
cam0RestartCount = 0
cam1RestartCount = 0
cam2RestartCount = 0
cam3RestartCount = 0
cam4RestartCount = 0
cam5RestartCount = 0
cam6RestartCount = 0
cam7RestartCount = 0
cam8RestartCount = 0
cam9RestartCount = 0

# defog toggle
cam1Defog = 0
cam2Defog = 0

# Disabled by default, enabled using button
autoRestart = 0

def Start0():
  global c0lastRestartTime
  global cam0RestartCount
  timeNow = time.time()
  delay = timeNow - c0lastRestartTime
  print(delay)
  if delay > 20:
    c0lastRestartTime = time.time()
    cam0RestartCount = cam0RestartCount + 1
    Stop0()
    myUrl='xterm -geometry 80x25+50+740 -fg green -hold -e /home/i7user/ffmpeg0 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.121:554\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 0 started.")

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
    if cam1Defog == 0:
      myUrl='xterm -geometry 80x25+50+20 -fg green -hold -e /home/i7user/ffmpeg1 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.60:554/Streaming/Channels/101/\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    elif cam1Defog == 1:
      myUrl='xterm -geometry 80x25+50+20 -fg green -hold -e /home/i7user/ffmpeg1 -re -rtsp_transport tcp -y -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.60:554\" -f lavfi -f dshow -rtbufsize 2000M -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -bufsize 5096k -c:v h264_nvenc -preset:v hq -rc cbr_hq -b:v 16M -buffer_size 10000k -vf curves=psfile=c22.acv -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
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
    if cam2Defog == 0:
      myUrl='xterm -geometry 80x25+50+380 -fg green -hold -e /home/i7user/ffmpeg2 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.102:554/VideoInput/1/h264/1\" -f lavfi -f dshow -rtbufsize 500M -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -threads 0 -bufsize 512k -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    elif cam2Defog == 1:  
      myUrl='xterm -geometry 80x25+50+380 -fg green -hold -e /home/i7user/ffmpeg2 -re -rtsp_transport tcp -y -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.102:554/VideoInput/1/h264/1\" -f lavfi -f dshow -rtbufsize 500M -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -bufsize 5096k -c:v h264_nvenc -preset:v hq -rc cbr_hq -b:v 5M -buffer_size 512k -vf curves=psfile=cam2.acv -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 2 started.")

def Start3():
  global c3lastRestartTime
  global cam3RestartCount
  timeNow = time.time()
  delay = timeNow - c3lastRestartTime
  print(delay)
  if delay > 20:
    c3lastRestartTime = time.time()
    cam3RestartCount = cam3RestartCount + 1
    Stop3()
    myUrl='xterm -geometry 80x25+50+740 -fg green -hold -e /home/i7user/ffmpeg3 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.121:554\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 3 started.")

def Start4():
  global c4lastRestartTime
  global cam4RestartCount
  timeNow = time.time()
  delay = timeNow - c4lastRestartTime
  print(delay)
  if delay > 20:
    c4lastRestartTime = time.time()
    cam4RestartCount = cam4RestartCount + 1
    Stop4()
    myUrl='xterm -geometry 80x25+560+20 -fg green -hold -e /home/i7user/ffmpeg4 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.121:554/Streaming/Channels/106\" -f lavfi -f dshow -rtbufsize 50M -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 4 started.")

def Start5():
  global c5lastRestartTime
  global cam5RestartCount
  timeNow = time.time()
  delay = timeNow - c5lastRestartTime
  print(delay)
  if delay > 20:
    c5lastRestartTime = time.time()
    cam5RestartCount = cam5RestartCount + 1
    Stop5()
    myUrl='xterm -geometry 80x25+560+380 -fg green -hold -e /home/i7user/ffmpeg5 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.122:554/Streaming/Channels/101/\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    #old myUrl='xterm -geometry 80x25+560+380 -fg green -hold -e /home/i7user/ffmpeg5 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.124:554/Streaming/Channels/101/\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 5 started.")

def Start6():
  global c6lastRestartTime
  global cam6RestartCount
  timeNow = time.time()
  delay = timeNow - c6lastRestartTime
  print(delay)
  if delay > 20:
    c6lastRestartTime = time.time()
    cam6RestartCount = cam6RestartCount + 1
    Stop6()
    myUrl='xterm -geometry 80x25+560+740 -fg green -hold -e /home/i7user/ffmpeg6 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.124:554/Streaming/Channels/101/\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 6 started.")

def Start7():
  global c7lastRestartTime
  global cam7RestartCount
  timeNow = time.time()
  delay = timeNow - c7lastRestartTime
  print(delay)
  if delay > 20:
    c7lastRestartTime = time.time()
    cam7RestartCount = cam7RestartCount + 1
    Stop7()
    myUrl='xterm -geometry 80x25+1050+20 -fg green -hold -e /home/i7user/ffmpeg7 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://192.168.1.168/0\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 7 started.")
def Start8():
  global c8lastRestartTime
  global cam8RestartCount
  timeNow = time.time()
  delay = timeNow - c8lastRestartTime
  print(delay)
  if delay > 20:
    c8lastRestartTime = time.time()
    cam8RestartCount = cam8RestartCount + 1
    Stop8()
    myUrl='xterm -geometry 80x25+1050+380 -fg green -hold -e /home/i7user/ffmpeg8 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://192.168.1.168/0\" -rtbufsize 1000M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 8 started.")
#yvx8-cdq3-frzs-4u7h-f1mh - Variable key for Nikon, 4k possible to upgrade to 8k in future
def Start9():
  global c9lastRestartTime
  global cam9RestartCount
  timeNow = time.time()
  delay = timeNow - c9lastRestartTime
  print(delay)
  if delay > 20:
    c9lastRestartTime = time.time()
    cam9RestartCount = cam9RestartCount + 1
    Stop9()
    myUrl='xterm -geometry 80x25+1050+740 -fg green -hold -e /home/i7user/ffmpeg9 -rtsp_transport tcp -thread_queue_size 5096 -i \"rtsp://user:password@192.168.1.127:554\" -rtbufsize 500M -f lavfi -f dshow -f alsa -i default -c:a libmp3lame -ab 192k -ar 48000 -map_channel 1.0.0 -c:v copy -f flv \"rtmp://a.rtmp.youtube.com/live2/x\"'
    subprocess.Popen(myUrl, shell=True)
    print("Camera 9 started.")

def StartAll():
    Start0()
    Start1()
    Start2()
    Start3()
    Start4()
    Start5()
    Start6()
    Start7()
    Start8()
    Start9()

def Stop0():
    call("ps -ef | grep ffmpeg0 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 0 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop1():
    call("ps -ef | grep ffmpeg1 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 1 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop2():
    call("ps -ef | grep ffmpeg2 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 2 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop3():
    call("ps -ef | grep ffmpeg3 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 3 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop4():
    call("ps -ef | grep ffmpeg4 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 4 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop5():
    call("ps -ef | grep ffmpeg5 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 5 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop6():
    call("ps -ef | grep ffmpeg6 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 6 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop7():
    call("ps -ef | grep ffmpeg7 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 7 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop8():
    call("ps -ef | grep ffmpeg8 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 8 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def Stop9():
    call("ps -ef | grep ffmpeg9 | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("Camera 9 stopped.")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)
def StopAll():
    call("ps -ef | grep ffmpeg | grep -v grep | awk '{print $2}' | xargs -r kill -9", shell=True)
    print("All cameras stopped.\n")
    #call("ps -ef | grep defunct | grep -v grep | cut -b8-20 | xargs kill -9", shell=True)

def getUptime(camNum):
  global c0lastRestartTime
  global c1lastRestartTime
  global c2lastRestartTime
  global c3lastRestartTime
  global c4lastRestartTime
  global c5lastRestartTime
  global c6lastRestartTime
  global c7lastRestartTime
  global c8lastRestartTime
  global c9lastRestartTime

  global c0RecordUptime
  global c1RecordUptime
  global c2RecordUptime
  global c3RecordUptime
  global c4RecordUptime
  global c5RecordUptime
  global c6RecordUptime
  global c7RecordUptime
  global c8RecordUptime
  global c9RecordUptime

  currentTime = time.time()
  if camNum == 0:
    compareTime = c0lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c0RecordUptime:
      c0RecordUptime = upTime
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
  if camNum == 3:
    compareTime = c3lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c3RecordUptime:
      c3RecordUptime = upTime
  if camNum == 4:
    compareTime = c4lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c4RecordUptime:
      c4RecordUptime = upTime
  if camNum == 5:
    compareTime = c5lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c5RecordUptime:
      c5RecordUptime = upTime
  if camNum == 6:
    compareTime = c6lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c6RecordUptime:
      c6RecordUptime = upTime
  if camNum == 7:
    compareTime = c7lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c7RecordUptime:
      c7RecordUptime = upTime
  if camNum == 8:
    compareTime = c8lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c8RecordUptime:
      c8RecordUptime = upTime
  if camNum == 9:
    compareTime = c9lastRestartTime
    upTime = currentTime - compareTime
    upTime = int(upTime)
    if upTime > c9RecordUptime:
      c9RecordUptime = upTime
  return upTime

def check():
  global t
  global cam0
  global cam1
  global cam2
  global cam3
  global cam4
  global cam5
  global cam6
  global cam7
  global cam8
  global cam9

  global autoRestart
  global c0RecordUptime
  global c1RecordUptime
  global c2RecordUptime
  global c3RecordUptime
  global c4RecordUptime
  global c5RecordUptime
  global c6RecordUptime
  global c7RecordUptime
  global c8RecordUptime
  global c9RecordUptime

  X_list = []
  Y_list = []
  cam0sum=0
  cam0avg=0
  cam0instances=0
  cam1sum=0
  cam1avg=0
  cam1instances=0
  cam2sum=0
  cam2avg=0
  cam2instances=0
  cam3sum=0
  cam3avg=0
  cam3instances=0
  cam4sum=0
  cam4avg=0
  cam4instances=0
  cam5sum=0
  cam5avg=0
  cam5instances=0
  cam6sum=0
  cam6avg=0
  cam6instances=0
  cam7sum=0
  cam7avg=0
  cam7instances=0
  cam8sum=0
  cam8avg=0
  cam8instances=0
  cam9sum=0
  cam9avg=0
  cam9instances=0
  totalUploadAvg=0
  call("timeout 20 sysdig -c topprocs_net > /home/i7user/test2.txt", shell=True)

  with open("/home/i7user/test2.txt") as catalog:
    for line in catalog:
        goodletters = ('1','2','3','4','5','6','7','8','9')
        if line.startswith(goodletters):
          column = line.split()
          x = str(column[0])
          y = str(column[1])
          if 'M' in x:
            x = re.sub("[^0-9\.]", "", x)
            xf = float(x)
            xf = xf * 4200
          elif 'KB' in x:
            x = re.sub("[^0-9\.]", "", x)
            xf = float(x)
            xf = xf * 42
          elif 'B' in x:
            x = re.sub("[^0-9\.]", "", x)
            xf = float(x)
            xf = xf * 42
            xf = xf / 100
          #x = x[:3]
          z = y[:6]
          #x = re.sub("[^0-9]", "", x)
          if z == 'ffmpeg':
            #xfloat = float(x)
            #xint = int(xfloat)
            X_list.append(xf)
            y = y[:7]
            Y_list.append(y)
          if y == 'ffmpeg0':
            cam0sum = cam0sum + xf
            cam0instances = cam0instances + 1
          if y == 'ffmpeg1':
            cam1sum = cam1sum + xf
            cam1instances = cam1instances + 1
          if y == 'ffmpeg2':
            cam2sum = cam2sum + xf
            cam2instances = cam2instances + 1
          if y == 'ffmpeg3':
            cam3sum = cam3sum + xf
            cam3instances = cam3instances + 1
          if y == 'ffmpeg4':
            cam4sum = cam4sum + xf
            cam4instances = cam4instances + 1
          if y == 'ffmpeg5':
            cam5sum = cam5sum + xf
            cam5instances = cam5instances + 1
          if y == 'ffmpeg6':
            cam6sum = cam6sum + xf
            cam6instances = cam6instances + 1
          if y == 'ffmpeg7':
            cam7sum = cam7sum + xf
            cam7instances = cam7instances + 1
          if y == 'ffmpeg8':
            cam8sum = cam8sum + xf
            cam8instances = cam8instances + 1
          if y == 'ffmpeg9':
            cam9sum = cam9sum + xf
            cam9instances = cam9instances + 1
  
  if cam0instances != 0:
    cam0avg = (cam0sum / cam0instances)
  if cam1instances != 0:
    cam1avg = (cam1sum / cam1instances)
  if cam2instances != 0:  
    cam2avg = (cam2sum / cam2instances)
  if cam3instances != 0:  
    cam3avg = (cam3sum / cam3instances)
  if cam4instances != 0:  
    cam4avg = (cam4sum / cam4instances) 
  if cam5instances != 0:  
    cam5avg = (cam5sum / cam5instances) 
  if cam6instances != 0:  
    cam6avg = (cam6sum / cam6instances) 
  if cam7instances != 0:  
    cam7avg = (cam7sum / cam7instances) 
  if cam8instances != 0:  
    cam8avg = (cam8sum / cam8instances) 
  if cam9instances != 0:  
    cam9avg = (cam9sum / cam9instances) 
  totalUploadAvg = cam0avg + cam1avg + cam2avg + cam3avg + cam4avg + cam5avg + cam6avg + cam7avg + cam8avg + cam9avg
  
  #print("Instances in file")
  #print("0:" + cam0instances + " 1:" + cam1instances + " 2:" + cam2instances + " 3:" + cam3instances + " 4:" + cam4instances + " 5:" + cam5instances + " 6:" + cam6instances + " 7:" + cam7instances + " 8:" + cam8instances + " 9:" + cam9instances)
  #print("")
  print("Camera 0 - Avg Speed: ",cam0avg," Uptime: ",getUptime(0)," Restarts: ",cam0RestartCount,"Record Uptime: ",c0RecordUptime)
  print("Camera 1 - Avg Speed: ",cam1avg," Uptime: ",getUptime(1)," Restarts: ",cam1RestartCount,"Record Uptime: ",c1RecordUptime)
  print("Camera 2 - Avg Speed: ",cam2avg," Uptime: ",getUptime(2)," Restarts: ",cam2RestartCount,"Record Uptime: ",c2RecordUptime)
  print("Camera 3 - Avg Speed: ",cam3avg," Uptime: ",getUptime(3)," Restarts: ",cam3RestartCount,"Record Uptime: ",c3RecordUptime)
  print("Camera 4 - Avg Speed: ",cam4avg," Uptime: ",getUptime(4)," Restarts: ",cam4RestartCount,"Record Uptime: ",c4RecordUptime)
  print("Camera 5 - Avg Speed: ",cam5avg," Uptime: ",getUptime(5)," Restarts: ",cam5RestartCount,"Record Uptime: ",c5RecordUptime)
  print("Camera 6 - Avg Speed: ",cam6avg," Uptime: ",getUptime(6)," Restarts: ",cam6RestartCount,"Record Uptime: ",c6RecordUptime)
  print("Camera 7 - Avg Speed: ",cam7avg," Uptime: ",getUptime(7)," Restarts: ",cam7RestartCount,"Record Uptime: ",c7RecordUptime)
  print("Camera 8 - Avg Speed: ",cam8avg," Uptime: ",getUptime(8)," Restarts: ",cam8RestartCount,"Record Uptime: ",c8RecordUptime)
  print("Camera 9 - Avg Speed: ",cam9avg," Uptime: ",getUptime(9)," Restarts: ",cam9RestartCount,"Record Uptime: ",c9RecordUptime)
  print("           Total UL:  ",totalUploadAvg)

  if autoRestart == 1:
    if cam0 == 0:
      if cam0avg < 10000 or cam0instances == 0:
        Start0()
    if cam1 == 1:
      if cam1avg < 10000 or cam1instances == 0:
        Start1()
    if cam2 == 1:
      if cam2avg < 4700 or cam2instances == 0:
        Start2()
    if cam3 == 1:
      if cam3avg < 9000 or cam3instances == 0:
        Start3()
    if cam4 == 1:
      if cam4avg < 200 or cam4instances == 0:
        Start4()
    if cam5 == 1:
      if cam5avg < 10000 or cam5instances == 0:
        Start5()
    if cam6 == 1:
      if cam6avg < 10000 or cam6instances == 0:
        Start6()
    if cam7 == 1:
      if cam7avg < 25000 or cam7instances == 0:
        Start7()
    if cam8 == 1:
      if cam8avg < 25000 or cam8instances == 0:
        Start8()
    if cam9 == 1:
      if cam9avg < 6000 or cam9instances == 0:
        Start9()

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

def ToggleDefog():
  global cam1Defog
  if cam1Defog == 0:
    cam1Defog = 1
    print("Cam 1 defog set to ON, restart cam 1 to enable changes.")
  elif cam1Defog == 1:
    cam1Defog = 0
    print("Cam 1 defog set to OFF, restart cam 1 to enable changes.")

def ToggleDefog2():
  global cam2Defog
  if cam2Defog == 0:
    cam2Defog = 1
    print("Cam 2 defog set to ON, restart cam 1 to enable changes.")
  elif cam2Defog == 1:
    cam2Defog = 0
    print("Cam 2 defog set to OFF, restart cam 1 to enable changes.")

B = tk.Button(top, text ="Cam 0 Start", command = Start0)
B.pack()
B = tk.Button(top, text ="Cam 0 Stop", command = Stop0)
B.pack()
B = tk.Button(top, text ="Cam 1 Start", command = Start1)
B.pack()
B = tk.Button(top, text ="Cam 1 Stop", command = Stop1)
B.pack()
B = tk.Button(top, text ="Cam 1 Defog", command = ToggleDefog)
B.pack()
B = tk.Button(top, text ="Cam 2 Start", command = Start2)
B.pack()
B = tk.Button(top, text ="Cam 2 Stop", command = Stop2)
B.pack()
B = tk.Button(top, text ="Cam 2 Defog", command = ToggleDefog2)
B.pack()
B = tk.Button(top, text ="Cam 3 Start", command = Start3)
B.pack()
B = tk.Button(top, text ="Cam 3 Stop", command = Stop3)
B.pack()
B = tk.Button(top, text ="Cam 4 Start", command = Start4)
B.pack()
B = tk.Button(top, text ="Cam 4 Stop", command = Stop4)
B.pack()
B = tk.Button(top, text ="Cam 5 Start", command = Start5)
B.pack()
B = tk.Button(top, text ="Cam 5 Stop", command = Stop5)
B.pack()
B = tk.Button(top, text ="Cam 6 Start", command = Start6)
B.pack()
B = tk.Button(top, text ="Cam 6 Stop", command = Stop6)
B.pack()
B = tk.Button(top, text ="Cam 7 Start", command = Start7)
B.pack()
B = tk.Button(top, text ="Cam 7 Stop", command = Stop7)
B.pack()
B = tk.Button(top, text ="Cam 8 Start", command = Start8)
B.pack()
B = tk.Button(top, text ="Cam 8 Stop", command = Stop8)
B.pack()
B = tk.Button(top, text ="Cam 9 Start", command = Start9)
B.pack()
B = tk.Button(top, text ="Cam 9 Stop", command = Stop9)
B.pack()
B = tk.Button(top, text ="Start All", command = StartAll)
B.pack()
B = tk.Button(top, text ="Stop All", command = StopAll)
B.pack()
B = tk.Button(top, text ="Auto Restart Off", command = AutoRestartOff)
B.pack()
B = tk.Button(top, text ="Auto Restart On", command = AutoRestartOn)
B.pack()

top.mainloop()