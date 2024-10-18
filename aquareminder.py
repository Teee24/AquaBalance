from win10toast_click import ToastNotifier
import webbrowser
import os
import webbrowser
import time
from datetime import datetime

# 獲取相對路徑中的 icon.ico 路徑
icon_path = os.path.join('icons', 'drop.ico')
play_path = os.path.join('icons', 'play.ico')
stop_path = os.path.join('icons', 'stop.ico')

# 定義打開 URL 的函數
def open_link():
    webbrowser.open("https://www.google.com.tw/?hl=zh_TW")

toaster = ToastNotifier()

def show_notification(title, message,icon):
    toaster.show_toast(
        "喝水提醒",
        "水喝多少惹，來記錄一下ㄅ~ \r[點擊]前往記錄",
        icon_path=icon_path,  
        duration=10,  # 通知顯示的時間（秒）
        threaded=True,
        callback_on_click=open_link  # 綁定點擊事件的函數
    )

# 定義允許通知的時間範圍
start_time = datetime.strptime("08:30", "%H:%M").time()
end_time = datetime.strptime("18:05", "%H:%M").time()

# 每隔 1 小時的指定通知時間，
notification_times = [datetime.strptime(t, "%H:%M").time() for t in [
    "09:05", "10:05", "11:05", "12:25", "13:25", "14:05", "15:05", "16:05", "17:05"]]

show_notification("喝水提醒程式啟動", "程式已經開始運行，提醒你喝水~",play_path)

while True:
    current_time = datetime.now().time()
    
    # 檢查當前時間是否在指定的時間範圍內
    if start_time <= current_time <= end_time:
        # 檢查當前時間是否與每小時的通知時間匹配
        if current_time in notification_times:
            show_notification("喝水提醒", "水喝多少惹，來記錄一下ㄅ~ \r[點擊]前往記錄",icon_path)
            
            # 等待通知顯示完畢
            while toaster.notification_active():
                time.sleep(0.1)  # 每 0.1 秒檢查一次通知是否仍在顯示

            # 等到下一個整點通知，避免在同一分鐘內重複顯示通知
            time.sleep(60)  # 等待 1 分鐘，防止在同一個時間內顯示多次通知
    else:
        # 如果當前時間不在指定範圍內，讓程式暫停一段時間後再檢查
        time.sleep(60)  # 每 1 分鐘檢查一次

    # 程式運行結束時間提醒
    if current_time >= end_time:
        show_notification("喝水提醒結束", "程式運行時間已過，明天見~",stop_path)
        break