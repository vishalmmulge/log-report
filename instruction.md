There is an Apache-style access log at `/app/access.log`. Read it and write a JSON summary to `/app/report.json`.

The task passes only when all of the following are true:

1. `/app/report.json` exists and is valid JSON with exactly these keys: `total_requests`, `unique_ips`, `top_path`.
2. `total_requests` is the count of non-empty lines in the log file.
3. `unique_ips` is the count of distinct IP addresses — the first field on each non-empty line.
4. `top_path` is the path that shows up most in the quoted HTTP request field, e.g. `"GET /index.html HTTP/1.1"`.

Both counts must be JSON numbers. `top_path` must be a JSON string.
