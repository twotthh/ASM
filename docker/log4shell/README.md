Log4Shell Test Environment

Image:
vulhub/solr:8.11.0

Run:

docker run -d -p 8983:8983 --name solr-test vulhub/solr:8.11.0

Access:
http://127.0.0.1:8983/solr/