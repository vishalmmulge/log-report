#!/bin/bash
set -u

mkdir -p /logs/verifier

if [ ! -f /app/report.json ]; then
    echo "report.json not found" | tee /logs/verifier/test-stdout.txt
    echo 0 > /logs/verifier/reward.txt
    exit 0
fi

if pytest /tests/test_outputs.py -v --tb=short 2>&1 | tee /logs/verifier/test-stdout.txt; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi
