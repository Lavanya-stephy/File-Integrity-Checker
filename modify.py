
def compare_hashes(old, new):
    for file in old:
        if file in new:
            if old[file]!=new[file]:
                print(f"⚠ {file} --- modified")
            else:
                print(f"✔ {file} --- not modified")
        else:
            print(f"❌ {file} --- deleted")

    for file in new:
        if file not in old:
            print(f"➕ New file detected: {file}")
