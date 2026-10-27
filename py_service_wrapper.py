import os
import time

import win32event
import win32service
import win32serviceutil


class PyBackgroundService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PyBackgroundService"
    _svc_display_name_ = "System Programming - Python Background Service"
    _svc_description_ = "Учебная служба Python для лабораторной работы."

    def __init__(self, args):
        super().__init__(args)

        # Событие, с помощью которого служба получает команду остановки.
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        # Сообщаем диспетчеру, что служба останавливается.
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        log_file = r"C:\py_service_log.txt"

        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            with open(log_file, "a", encoding="utf-8") as file:
                file.write(
                    f"[{timestamp}] Python service is running. "
                    f"PID: {os.getpid()}\n"
                )

            # Ждём 5 секунд или команду остановки.
            result = win32event.WaitForSingleObject(
                self.stop_event,
                5000
            )

            if result == win32event.WAIT_OBJECT_0:
                break


if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(PyBackgroundService)