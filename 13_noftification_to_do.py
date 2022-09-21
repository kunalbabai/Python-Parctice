def trun_notyfy():
    try:
        import time
        from plyer import notification
        from playsound import playsound
        while True:
            playsound(r"E:\Husan - Ap Dhillon.mp3")
            notification.notify(
                title = "ALERT!!!",
                message = "Take a break! It has been an hour!",
                timeout = 10,
                app_icon = r"C:\Users\UDCIND\Downloads\Treetog-I-Documents.ico",
                ticker = "",
                toast = False)
            playsound(r"E:\Husan - Ap Dhillon.mp3")
            time.sleep(120)
    except Exception:
        return Exception
trun_notyfy()