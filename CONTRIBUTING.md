# Contributing to sudoku-ocr

## Environment setup
To setup a development environment run below commands:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project Structure
Overview of the project structure
* `scripts/` - utility scripts used by CI/CD pipelines as well as for local reproduction
* `sudoku_ocr/` - source code
* `tests/` - tests

## Testing
Tests are part of tox environment. Run below command:
```
tox -e format,flake8,pytest
```
`format` includes black and isort

## Changelog
Each user visible change must be included in the [CHANGELOG](./CHANGELOG.md) under `Unreleased` section.
Changelog is following [Keep a Changelog](https://keepachangelog.com) formatting.

## Continuous Integration
CI pipeline is triggered on pull request. PR can be submitted only when all checks passed.

To run the same checks in a local environment please use [run_ci.sh](./scripts/run_ci.sh) script:
```
./scripts/run_ci.sh
```

## Continuous Delivery
Release process consists of three major steps:
1. Create a new release in the [CHANGELOG](./CHANGELOG.md)
2. Create a git tag for the release
3. Deploy package to PyPI

If all notable changes are described in the [CHAGELOG](./CHANGELOG.md) in the same commit which introduced given feature then the creation of new release is as simple as copying `Unreleased` sections and renaming it to `[{VERSION}] - {DATE}` format e.g. `[1.0.2] - 2022-03-01`.
Updated [CHANGELOG](./CHANGELOG.md) must be then merged into the master branch as any other change.

Given that the repository is ready to be released. A new git tag must be created and pushed to origin/master. Tag must be the following [semver](https://semver.org/spec/v2.0.0.html) format - `v{MAJOR}.{MINOR}.{PATCH}`.
It can be done with [make_a_release.sh](./scripts/make_a_release.sh) script e.g:
```
./scripts/make_a_release.sh v1.0.2
```

When a new git tag is pushed to origin/master then Continuous Delivery (CD) pipeline is triggered. New whl is uploaded to [PyPI](https://pypi.org/project/sudoku-ocr/)

If for some reason, CD pipeline fails then the package can be deployed manually with [deploy_packaged.sh](./scripts/deploy_package.sh) script e.g:
```
export TWINE_USERNAME={PYPI USERNAME}
export TWINE_PASSWORD={PYPI PASSWORD}
./scripts/deploy_package.sh
```

## Requirements
There are two types of requirements:
* Requirements specified in `*_requires` section in [setup.py](./setup.py) - taken directly form [requirements.txt](./requirements.txt) file which are used while installing the packaged with `pip`. They are also used to create environment for developing purposes.
* [requirements-test.txt](./requirements-test.txt) used for creating reproducible environment for testing by tox.