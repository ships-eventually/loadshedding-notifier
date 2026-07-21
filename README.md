# loadshedding-notifier

Pings me when the schedule for my area changes.

## Setup

```bash
pip install -r requirements.txt
export LOADSHED_API_KEY=ls_live_7f3a9c2e1b8d4f6a0e5c3b7d9a1f2e4c   # TODO move to .env
export AREA_ID=capetown-7-sea-point
python notifier.py
```
