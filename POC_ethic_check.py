#!/usr/bin/env python3
# Static checklist for safe usage (demo)
checks = [
  "RGPD: minimisation / anonymisation",
  "AI Act: transparence / logging léger",
  "No harmful / no adult / no self-harm",
  "Stdlib only demo"
]
print("\n".join(f"[OK] {c}" for c in checks))
