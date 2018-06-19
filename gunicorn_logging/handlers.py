from logstash_async.handler import AsynchronousLogstashHandler
from . import settings


class LogstashHandler(AsynchronousLogstashHandler):
    def __init__(self, port=None, host=None, database_path=None, transport=None,
                 ssl_enable=None, ssl_verify=None, keyfile=None, certfile=None, ca_certs=None,
                 enable=True, event_ttl=None, encoding=None):

        host = str(host or settings.LOGSTASH_HOST)
        port = int(port or settings.LOGSTASH_PORT)
        database_path = database_path or settings.LOGSTASH_DB_PATH
        transport = str(transport or settings.LOGSTASH_TRANSPORT)
        ssl_enable = bool(ssl_enable or settings.LOGSTASH_SSL_ENABLE)
        ssl_verify = bool(ssl_verify or settings.LOGSTASH_SSL_VERIFY)
        keyfile = keyfile or settings.LOGSTASH_KEYFILE
        certfile = certfile or settings.LOGSTASH_CERTFILE
        ca_certs = ca_certs or settings.LOGSTASH_CA_CERTS
        enable = bool(enable or settings.LOGSTASH_ENABLEs)
        event_ttl = event_ttl or settings.LOGSTASH_EVENT_TTL
        encoding = str(encoding or settings.LOGSTASH_ENCODING)

        super(LogstashHandler, self).__init__(host=host, port=port, database_path=database_path, transport=transport,
                 ssl_enable=ssl_enable, ssl_verify=ssl_verify, keyfile=keyfile, certfile=certfile, ca_certs=ca_certs,
                 enable=enable, event_ttl=event_ttl, encoding=encoding)