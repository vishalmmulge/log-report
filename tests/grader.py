import json
import time
from pathlib import Path

EXPECTED = {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
REPORT = Path("/app/report.json")
CTRF = Path("/logs/verifier/ctrf.json")


def write_ctrf(status: str, message: str, started: float) -> None:
    passed = int(status == "passed")
    CTRF.write_text(json.dumps({"results": {"tool": {"name": "log-report-grader"}, "summary": {"tests": 1, "passed": passed, "failed": 1 - passed, "pending": 0, "skipped": 0, "other": 0, "start": started, "stop": time.time()}, "tests": [{"name": "report_matches_expected_summary", "status": status, "message": message}]}}))


def main() -> int:
    started = time.time()
    try:
        with REPORT.open(encoding="utf-8") as report_file:
            report = json.load(report_file)
        if not isinstance(report, dict):
            raise ValueError("report must be a JSON object")
        if set(report) != set(EXPECTED):
            raise ValueError("report must contain exactly total_requests, unique_ips, and top_path")
        if type(report["total_requests"]) is not int or type(report["unique_ips"]) is not int:
            raise ValueError("request counts must be JSON integers")
        if type(report["top_path"]) is not str:
            raise ValueError("top_path must be a JSON string")
        if report != EXPECTED:
            raise ValueError(f"unexpected report values: {report!r}")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        write_ctrf("failed", str(error), started)
        return 1
    write_ctrf("passed", "report matches the expected summary", started)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
