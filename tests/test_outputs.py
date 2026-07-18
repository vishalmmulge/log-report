import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load():
    return json.loads(REPORT.read_text(encoding="utf-8"))


# criterion 1: /app/report.json exists and is valid JSON with exactly the keys
# total_requests, unique_ips, top_path
def test_keys():
    report = load()
    assert isinstance(report, dict)
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}


# criterion 2: total_requests is the count of non-empty lines in the log
def test_total_requests():
    report = load()
    assert isinstance(report["total_requests"], int)
    assert report["total_requests"] == 6


# criterion 3: unique_ips is the count of distinct IP addresses
def test_unique_ips():
    report = load()
    assert isinstance(report["unique_ips"], int)
    assert report["unique_ips"] == 3


# criterion 4: top_path is the most frequent path from the quoted HTTP request field
def test_top_path():
    report = load()
    assert isinstance(report["top_path"], str)
    assert report["top_path"] == "/index.html"
