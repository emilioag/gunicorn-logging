================
Gunicorn logging
================

Centralized logging for gunicorn ussing ELK besed on (python-logstash-async)[https://github.com/eht16/python-logstash-async].


Environment vars
----------------

- LOGSTASH_HOST: Logstash host.
- LOGSTASH_PORT: Logstash port.
- LOGSTASH_DB_PATH: The path to the file containing queued events. Use None to use a in-memory cache.
- LOGSTASH_TRANSPORT: Callable or path to a compatible transport class.
- LOGSTASH_SSL_ENABLE: Callable or path to a compatible transport class.
- LOGSTASH_SSL_VERIFY: Should the server's SSL certificate be verified?
- LOGSTASH_KEYFILE: The path to client side SSL key file.
- LOGSTASH_CERTFILE: The path to client side SSL key file.
- LOGSTASH_CA_CERTS: The path to the file containing recognized CA certificates.
- LOGSTASH_ENABLE: Flag to enable log processing. (default is True, disabling might be handy for local testing, etc.)
- LOGSTASH_EVENT_TTL: Amount of time in seconds to wait before expiring log messages in the database. (Given in seconds. Default is None, and disables this feature)
- LOGSTASH_ENCODING: 
- LOGSTASH_MESSAGE_TYPE: 
- LOGSTASH_MESSAGE_SUBTYPE: 
- LOGSTASH_EXTRA: 


Using Django settings
---------------------

Environment vars:

 - WORKSPACE: Django base directory.
 - DJANGO_SETTINGS_MODULE: Django settings module.
