import time, json, sys, os
from pypresence import Presence

def load_cfg():
    with open("config.json","r",encoding="utf-8") as f:
        return json.load(f)

def main():
    cfg = load_cfg()
    cid = cfg.get("client_id")
    if not cid or cid.startswith("PASTE_"):
        print("⚠️ Please set your 'client_id' in config.json (Application ID).")
        sys.exit(1)

    print("=== Discord RPC ===")
    print("Folder:", os.path.abspath(os.getcwd()))
    print("Using client_id:", cid)
    print("Using large_image:", cfg.get("large_image"))

    rpc = Presence(cid)
    print("Connecting to Discord RPC...")
    rpc.connect()
    print("✅ CONNECTED. Updating presence...")

    payload = {
        "details": cfg.get("details"),
        "state": cfg.get("state"),
        "large_image": cfg.get("large_image"),
        "large_text": cfg.get("large_text"),
        "buttons": cfg.get("buttons")
    }
    if cfg.get("start_timestamp", True):
        payload["start"] = int(time.time())

    rpc.update(**payload)
    print("✅ Presence active. Leave this window open (Ctrl+C to quit).")
    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Stopping...")
        rpc.clear()
        rpc.close()

if __name__ == "__main__":
    main()