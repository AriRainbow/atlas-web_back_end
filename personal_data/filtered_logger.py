#!/usr/bin/env python3
"""
Module for filtering personally identifiable information (PII) from log messages.
"""

import re
import logging
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscates the values of specified fields in a log message using regex.

    Args:
        fields: List of field names whose values should be obfuscated.
        redaction: String to replace the sensitive field values with.
        message: The original log message.
        separator: The character separating fields in the message.

    Returns:
        The log message with specified field values obfuscated.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class that obfuscates sensitive PII fields in log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the fields to redact.

        Args:
            fields: List of field names to redact from log messages.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format and redact sensitive fields in the log record.

        Args:
            record: A logging.LogRecord instance.

        Returns:
            A formatted log string with sensitive fields redacted.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)
