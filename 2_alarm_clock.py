#print(f'{alarm_hour}---->{alarm_minute}---->{alarm_seconds}---->{alarm_period}')
#approch 1
def alarm():
    from datetime import datetime
    from playsound import playsound
    #take input from the user to set alarm time -
    try:
        alarm_time = input("Enter the time of alarm to be set:HH:MM:SS:(AM/PM) format is 12: HRS \n")
        alarm_hour=alarm_time[0:2]
        alarm_minute=alarm_time[3:5]
        alarm_seconds=alarm_time[6:8]
        alarm_period = alarm_time[9:11].upper()
        print("Setting up alarm..")
        while True:
            now = datetime.now()
            if alarm_period == now.strftime("%p"): #for checking am or pm
                if alarm_hour == now.strftime("%I"): #for checking hour in 12 hrs format
                    if alarm_minute == now.strftime("%M") and alarm_seconds == now.strftime("%S"):
                        print("Wake Up Baby!!! It's time to Code")
                        return playsound(r'C:\Users\UDCI.UDC-HYD-D-22\OneDrive - UDC\Smaple_Program_ML\Ring_Tone_Alarm\Husan - Ap Dhillon.mp3')
    except Exception as Ex:
        return Ex
    finally:
        return "Today is - " + now.strftime("%A")
# a = alarm()
# print(a)
#approch 2
try:
    from datetime import datetime
    from playsound import playsound
    alarm_time = input("Enter the time of alarm to be set:HH:MM format is 24: HRS \n")
    print("Setting up alarm..")
    while True:
        now = datetime.now()
        if alarm_time == now.strftime("%X"):
            print("Wake Up Baby!!! It's time to Code")
            playsound(r'C:\Users\UDCI.UDC-HYD-D-22\OneDrive - UDC\Smaple_Program_ML\Ring_Tone_Alarm\Husan - Ap Dhillon.mp3')
            break
except Exception as Ex:
    print(Ex)
finally:
    print("Today is - " + now.strftime("%A"))