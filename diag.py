import json, os, time
from pypresence import Presence

print("=== RPC DIAG ===")
print("Folder:", os.path.abspath(os.getcwd()))

with open("config.json","r",encoding="utf-8") as f:
    cfg = json.load(f)

cid = cfg.get("client_id")
img = cfg.get("large_image")
print("client_id:", cid)
print("large_image:", img)

try:
    rpc = Presence(cid)
    print("Connecting...")
    rpc.connect()
    print("✅ CONNECTED. Updating presence...")
    rpc.update(details=cfg.get("details"),
               state=cfg.get("state"),
               large_image=img,
               large_text=cfg.get("large_text"),
               buttons=cfg.get("buttons"),
               start=int(time.time()))
    print("✅ OK. (Ctrl+C to quit)")
    while True:
        time.sleep(15)
except Exception as e:
    print("❌ ERROR:", repr(e))