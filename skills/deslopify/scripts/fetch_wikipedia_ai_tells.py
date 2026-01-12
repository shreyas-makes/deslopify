#!/usr/bin/env python3
import json
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen


API_URL = (
    "https://en.wikipedia.org/w/api.php"
    "?action=parse"
    "&page=Wikipedia:Signs_of_AI_writing"
    "&prop=wikitext"
    "&format=json"
)
FALLBACK_PATH = "skills/deslopify/references/ai_tells_fallback.txt"
OUTPUT_PATH = "skills/deslopify/references/ai_tells.wikitext"


def fetch_wikitext() -> str:
    request = Request(
        API_URL,
        headers={"User-Agent": "deslopify-skill-fetch/1.0 (contact: local)"},
    )
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload["parse"]["wikitext"]["*"]


def load_fallback() -> str:
    with open(FALLBACK_PATH, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def load_existing() -> str:
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main() -> int:
    used_fallback = False
    try:
        wikitext = fetch_wikitext()
    except Exception as exc:
        print(
            f"Warning: failed to fetch Wikipedia wikitext ({exc}); "
            "using cached list if available.",
            file=sys.stderr,
        )
        try:
            _ = load_existing()
            print(f"Using cached list at {OUTPUT_PATH}.", file=sys.stderr)
            return 0
        except OSError:
            try:
                wikitext = load_fallback()
                used_fallback = True
            except OSError as fallback_exc:
                print(
                    f"Error: failed to load fallback list: {fallback_exc}",
                    file=sys.stderr,
                )
                return 1

    timestamp = datetime.now(timezone.utc).isoformat()
    output = (
        f"Source: {FALLBACK_PATH if used_fallback else API_URL}\n"
        f"Retrieved: {timestamp}\n"
        "\n"
        f"{wikitext}\n"
    )

    try:
        with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
            handle.write(output)
    except OSError as exc:
        print(f"Error: failed to write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
