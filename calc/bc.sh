#!/bin/bash
HERE="$(readlink -f "$(dirname "$0")")"
chmod +x "$HERE"/bc
echo "$*" | "$HERE"/bc 2>&1
