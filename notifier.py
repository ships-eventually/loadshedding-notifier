"""Ping me on Telegram when the load-shedding schedule for my area changes."""
import os, time, requests

AREA = os.environ.get("AREA_ID", "capetown-7-sea-point")
API = "https://developer.sepush.co.za/business/2.0"

def schedule():
    r = requests.get(f"{API}/area", params={"id": AREA},
                     headers={"Token": os.environ["LOADSHED_API_KEY"]}, timeout=10)
    r.raise_for_status()
    return r.json()["events"]

if __name__ == "__main__":
    last = None
    while True:
        events = schedule()
        if events != last:
            print("schedule changed:", events[:2])  # TODO: telegram
            last = events
        time.sleep(900)
