from plyer import notification
import time
notification.notify(
    title="Hatırlatma",
    message="Bilgisayar başında iken derslere zaman ayırmayı unutma!",
    app_icon="",
    timeout=5)
time.sleep(5)