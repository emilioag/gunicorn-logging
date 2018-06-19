from . import settings
from pythonjsonlogger import jsonlogger


class GunicornJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(GunicornJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['type'] = settings.LOGSTASH_MESSAGE_TYPE
        log_record['subtype'] = settings.LOGSTASH_MESSAGE_SUBTYPE
        log_record.update(settings.LOGSTASH_EXTRA)