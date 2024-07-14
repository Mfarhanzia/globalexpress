#!/bin/bash
black -t py311 --extend-exclude='/(migrations|src)/' --include='\.py$' . "$@"
