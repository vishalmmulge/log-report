FROM python:3.12-slim-bookworm@sha256:8a7e7cc04fd3e2bd787f7f24e22d5d119aa590d429b50c95dfe12b3abe52f48b

RUN pip install --no-cache-dir pytest==8.2.2

COPY test.sh /tests/test.sh
COPY test_outputs.py /tests/test_outputs.py

RUN chmod 0555 /tests/test.sh /tests/test_outputs.py
