from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

test_list = ["1"]*10

def check_list_len():
    global test_list
    while True:
        time.sleep(5)
        logger.info(f"check_list_len：{len(test_list)}")

@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_list_len, 'cron', second='*/5')
    scheduler.start()

@app.get("/pop")
async def list_pop():
    global test_list
    test_list.pop(1)
    logger.info(f"current_list_len:{len(test_list)}")


if __name__ == '__main__':
    uvicorn.run(app="main3:app", host="0.0.0.0", port=80, reload=False, debug=False)
