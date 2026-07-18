import json
import time
from pathlib import Path

EXPECTED = {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}

REPORT = Path("/app/report.json")
CTRF   = Path("/logs/verifier/ctrf.json")


def write_ctrf(status, message, started):
    passed = 1 if status == "passed" else 0
    data = {
        "results": {
            "tool": {"name": "log-report-grader"},
            "summary": {
                "tests": 1,
                "passed": passed,
                "failed": 1 - passed,
                "pending": 0,
                "skipped": 0,
                "other": 0,
                "start": started,
                "stop": time.time(),
            },
            "tests": [
                {
                    "name": "report_matches_expected_summary",
                    "status": status,
                    "message": message,
                }
            ],
        }
    }
    CTRF.write_text(json.dumps(data))


def main():
    started = time.time()
    try:
        with REPORT.open(encoding="utf-8") as f:
            report = json.load(f)

        if not isinstance(report, dict):
            raise ValueError("report.json must be a JSON object")

        if set(report.keys()) != set(EXPECTED.keys()):
            raise ValueError("wrong keys in report.json")

        if not isinstance(report["total_requests"], int) or not isinstance(report["unique_ips"], int):
            raise ValueError("total_requests and unique_ips must be integers")

        if not isinstance(report["top_path"], str):
            raise ValueError("top_path must be a string")

        if report != EXPECTED:
            raise ValueError(f"values don't match expected: got {report}")

    except (OSError, ValueError, json.JSONDecodeError) as e:
        write_ctrf("failed", str(e), started)
        return 1

    write_ctrf("passed", "report matches expected", started)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
