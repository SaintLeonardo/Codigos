FROM python:3.8-alpine AS builder

WORKDIR /data

COPY generate-database.py .

RUN python generate-database.py

FROM alpine:latest

COPY --from=builder /data/perguntasbd2.db /data/perguntasbd2.db

RUN apk --no-cache add sqlite

WORKDIR /data

VOLUME /data

CMD ["sqlite3", "perguntasbd2.db"]
