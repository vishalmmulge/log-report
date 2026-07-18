There is an Apache-style access log at `/app/access.log`. Read it and write a JSON object to `/app/report.json`.

The task passes only when all four of the following are true:

1. `/app/report.json` exists and is valid JSON containing exactly three keys: `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is an integer equal to the number of non-empty lines in `/app/access.log`.
3. `unique_ips` is an integer equal to the number of distinct IP addresses found in the first whitespace-separated field of each non-empty line.
4. `top_path` is a string containing the request path that appears most often inside the quoted HTTP request field (for example, in `"GET /index.html HTTP/1.1"` the path is `/index.html`).
