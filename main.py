import os

VOW = "I vow to love you through every firmware update and low battery, and to keep a backup of your heart — in case a factory reset ever makes you forget me."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW + "\n")

if __name__ == "__main__":
    main()
