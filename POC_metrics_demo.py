#!/usr/bin/env python3
# Produce a tiny metrics.json for demo (stdlib only)
import json, time, random
m = {
  "stability_avg": round(random.uniform(0.85, 0.95), 3),
  "latency_p95": int(random.uniform(120, 380)),
  "rollbacks": int(random.uniform(0, 3)),
  "propagation_index": round(random.uniform(0.3, 0.9), 3)
}
print(json.dumps(m, ensure_ascii=False, indent=2))
