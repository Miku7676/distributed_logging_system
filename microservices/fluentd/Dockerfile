FROM fluent/fluentd:v1.17.1-debian-1.1
USER root
RUN ["gem", "install", "fluent-plugin-kafka", "--no-document"]
COPY fluent.conf /fluentd/etc/fluent.conf
USER fluent