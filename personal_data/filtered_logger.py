#!/usr/bin/env python3
"""
Module for filtering personally identifiable information (PII) from log messages.
"""

import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


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


# Define the fields considered Personally Identifiable Information
PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data' with redaction for PII fields.

    Returns:
        A logging.Logger object configured to filter out PII.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=list(PII_FIELDS)))

    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Establishes and returns a secure connection to the MySQL database.

    Environment Variables Used:
        - PERSONAL_DATA_DB_USERNAME (default: "root")
        - PERSONAL_DATA_DB_PASSWORD (default: "")
        - PERSONAL_DATA_DB_HOST (default: "localhost")
        - PERSONAL_DATA_DB_NAME (no default, required)

    Returns:
        A MySQLConnection object to the specified database.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    """
    Retrieves all rows from the 'users' table and logs each with PII fields redacted.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    field_names = [desc[0] for desc in cursor.description]
    logger = get_logger()

    for row in cursor:
        row_dict = dict(zip(field_names, row))
        message = "; ".join([f"{k}={v}" for k, v in row_dict.items()]) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
