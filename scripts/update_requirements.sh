#!/bin/bash

set -e

pip-compile setup.py
pip-compile requirements-dev.in