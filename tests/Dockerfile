FROM python:3.12-slim-bookworm@sha256:8a7e7cc04fd3e2bd787f7f24e22d5d119aa590d429b50c95dfe12b3abe52f48b

COPY test.sh /tests/test.sh
COPY grader.py /tests/grader.py

RUN chmod 0555 /tests/test.sh /tests/grader.py
