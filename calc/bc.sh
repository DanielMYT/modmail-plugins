#!/bin/bash
HERE="$(readlink -f "$(dirname "$0")")"
chmod +x "$HERE"/bc
echo "$*" | "$HERE"/bc -lzLS15 2>&1
exit 0
