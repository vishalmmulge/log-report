Analyze the Apache-style access log at `/app/access.log` and write a JSON report to
`/app/report.json`.

Your report is successful only if it meets all of the following criteria:

1. `/app/report.json` exists and is valid JSON containing exactly the keys
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the number of non-empty log lines in `/app/access.log`.
3. `unique_ips` is the number of distinct client IP addresses (the first
   whitespace-separated field of each non-empty line).
4. `top_path` is the request path occurring most often in the log. Parse the path
   from the HTTP request enclosed in double quotes (for example, `GET /index.html HTTP/1.1`).

Use JSON number values for the two counts and a JSON string for `top_path`.
