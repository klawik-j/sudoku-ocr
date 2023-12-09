"""Logging utils."""

import logging
import logging.config
from argparse import ArgumentParser


def setup_logging(level: int = None) -> None:
    """Setups logging.

    :param level: logging level
    """
    if level is None:
        level = logging.INFO
    level_name = logging.getLevelName(level)

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "brief": {
                "format": "%(message)s",
            },
            "extended": {
                "format": "%(asctime)s - %(thread)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console_INFO": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "brief",
            },
            "console_WARNING": {
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "brief",
            },
            "console_DEBUG": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "extended",
            },
        },
        "root": {
            "level": "WARNING",
        },
        "loggers": {
            "__main__": {
                "level": level_name,
                "handlers": [f"console_{level_name}"],
            },
            "sudoku_ocr": {
                "level": level_name,
                "handlers": [f"console_{level_name}"],
            },
        },
    }
    logging.config.dictConfig(config)


def setup_parser(root_parser: ArgumentParser) -> None:
    """Setups parser.

    :param root_parser: parser to extend
    """
    logging_group = root_parser.add_argument_group("logging")
    level_group = logging_group.add_mutually_exclusive_group()
    level_group.add_argument(
        "--quiet",
        action="store_const",
        const=logging.WARNING,
        default=logging.INFO,
        dest="logging_level",
        help="log just error and warning messages",
    )
    level_group.add_argument(
        "--debug",
        action="store_const",
        const=logging.DEBUG,
        default=logging.INFO,
        dest="logging_level",
        help="log debug messages",
    )
