#!/usr/bin/env python3
"""
Module for filtering personally identifiable information (PII) from log messages.
"""

import re
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
