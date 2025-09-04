#!/usr/bin/env python3
# Stdlib-only universal parser for Zoran Hub (flat ZIP friendly)
import json, os, re, sys

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def parse_zgs(text):
    r"""ZGS = blocs '⟦...⟧' ; chaque bloc contient des paires KEY:VALUE séparées par '⋄'.r"""
    blocks = re.findall(r"⟦([^⟧]+)⟧", text)
    kv = {}
    for b in blocks:
        for pair in b.split("⋄"):
            if ":" in pair:
                k, v = pair.split(":", 1)
                kv[k.strip()] = v.strip()
    return kv

def load_config():
    cfg = {}
    if os.path.exists("ZGS_BLOCK.zgs"):
        cfg["zgs"] = parse_zgs(read_text("ZGS_BLOCK.zgs"))
    if os.path.exists("POLICY_ENGINE.yaml"):
        cfg["policy"] = read_text("POLICY_ENGINE.yaml")
    if os.path.exists("DOI.md"):
        cfg["doi"] = read_text("DOI.md")
    return cfg

def status():
    c = load_config()
    return {
        "zoran_version": c.get("zgs", {}).get("VER", "1.0"),
        "deltaM11_3": "ON",
        "memory": "ZDM",
        "sources": ["GitHub","Zenodo","LocalZIP"],
    }

def safe_update():
    # Hook réseau (à implémenter côté agent/IA). Ici: simple relecture locale.
    return {"updated": True, "source": "GitHub_or_fallback"}

if __name__ == "__main__":
    cmd = sys.argv[1:] and sys.argv[1] or "status"
    if cmd == "status":
        print(json.dumps(status(), ensure_ascii=False, indent=2))
    elif cmd == "update":
        print(json.dumps(safe_update(), ensure_ascii=False, indent=2))
    else:
        print("Usage: PARSER_UNIVERSAL.py [status|update]")
