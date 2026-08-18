#!/bin/bash
export BC_LINE_LENGTH=0
HERE="$(readlink -f "$(dirname "$0")")"
chmod +x "$HERE"/bc
echo "scale=15; $*" | "$HERE"/bc 2>&1
