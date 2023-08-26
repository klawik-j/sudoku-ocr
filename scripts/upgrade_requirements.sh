#!/bin/bash

set -e

pip-compile --upgrade setup.py
pip-compile --upgrade requirements-dev.in