#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A demo.taskapp beat -l INFO
