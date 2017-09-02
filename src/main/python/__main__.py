from frontEnd.app import app
from priceComparer.core.RetrieveData import RetrieveData
from threading import Thread
import schedule
import time


def run_every_10_seconds():
    print("Running periodic task!")


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    schedule.every(10).seconds.do(run_every_10_seconds)
    t = Thread(target=run_schedule)
    t.start()
    print ('Start time: ' + str(time.time()))
    app.run(debug=True)