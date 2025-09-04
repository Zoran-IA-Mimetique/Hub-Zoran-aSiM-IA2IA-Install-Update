#!/usr/bin/env python3
from PARSER_UNIVERSAL import status
if __name__ == "__main__":
    import json
    print(json.dumps(status(), ensure_ascii=False, indent=2))
