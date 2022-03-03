#!/bin/bash

set -e

git tag $1
git push origin --tags