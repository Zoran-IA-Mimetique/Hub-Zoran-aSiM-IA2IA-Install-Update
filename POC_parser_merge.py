#!/usr/bin/env python3
# Demonstrate ZGS+YAML merge (dry, illustrative)
import re

def parse_zgs(text):
    blocks = re.findall(r"⟦([^⟧]+)⟧", text)
    kv = {}
    for b in blocks:
        for pair in b.split("⋄"):
            if ":" in pair:
                k,v = pair.split(":",1)
                kv[k.strip()] = v.strip()
    return kv

zgs = open("ZGS_BLOCK.zgs","r",encoding="utf-8").read()
yaml = open("POLICY_ENGINE.yaml","r",encoding="utf-8").read()

print("ZGS keys:", sorted(parse_zgs(zgs).keys())[:6], "...")
print("YAML length:", len(yaml), "chars")
print("Merged view: ZGS governs anchors, YAML governs policies (demo).")
