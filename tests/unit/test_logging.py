import argparse
import logging

import pytest
from sudoku_ocr.logging import setup_logging, setup_parser


class TestSetupLogging:
    def test_root_logger_level(self) -> None:
        setup_logging()
        logger = logging.getLogger("root")
        assert logger.getEffectiveLevel() == logging.WARNING
    
    def test_default_main_level(self) -> None:
        setup_logging()
        logger = logging.getLogger("__main__")
        assert logger.getEffectiveLevel() == logging.INFO

    def test_default_sudoku_ocr_level(self) -> None:
        setup_logging()
        logger = logging.getLogger("sudoku_ocr")
        assert logger.getEffectiveLevel() == logging.INFO

    def test_explicit_main_level(self) -> None:
        setup_logging(level=logging.DEBUG)
        logger = logging.getLogger("__main__")
        assert logger.getEffectiveLevel() == logging.DEBUG

    def test_explicit_sudoku_ocr_level(self) -> None:
        setup_logging(level=logging.DEBUG)
        logger = logging.getLogger("sudoku_ocr")
        assert logger.getEffectiveLevel() == logging.DEBUG


class TestSetupParser:
    def test_default_level(self) -> None:
        parser = argparse.ArgumentParser()
        setup_parser(parser)
        args = parser.parse_args([])
        assert args.logging_level == logging.INFO

    def test_debug_level(self) -> None:
        parser = argparse.ArgumentParser()
        setup_parser(parser)
        args = parser.parse_args(["--debug"])
        assert args.logging_level == logging.DEBUG

    def test_quiet_level(self) -> None:
        parser = argparse.ArgumentParser()
        setup_parser(parser)
        args = parser.parse_args(["--quiet"])
        assert args.logging_level == logging.WARNING

    def test_debug_and_quiet(self) -> None:
        parser = argparse.ArgumentParser()
        setup_parser(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["--quiet", "--debug"])
