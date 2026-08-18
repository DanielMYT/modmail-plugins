#!/bin/bash
HERE="$(readlink -f "$(dirname "$0")")"
chmod +x "$HERE"/bc
echo "$*" | "$HERE"/bc -zLS15 2>&1
