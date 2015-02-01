import webbrowser
import time

#count = 0
#while(count < 3):
#    time.sleep(10)
#    webbrowser.open("https://www.youtube.com/watch?v=9aofoBrFNdg")
#    count = count + 1
#    print "Break's over"

total_breaks = 3
break_count = 0

print "This program started on "+time.ctime()
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=9aofoBrFNdg")
    break_count = break_count + 1
    print "Get to work"
