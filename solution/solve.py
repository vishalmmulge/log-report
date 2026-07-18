import json
import re
from collections import Counter

total = 0
ip_set = set()
path_counts = Counter()

with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ip_set.add(line.split()[0])
        match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if match:
            path_counts[match.group(1)] += 1

out = {
    "total_requests": total,
    "unique_ips": len(ip_set),
    "top_path": path_counts.most_common(1)[0][0],
}

with open("/app/report.json", "w") as f:
    json.dump(out, f)
