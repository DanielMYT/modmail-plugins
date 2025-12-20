#!/bin/bash
HERE="$(readlink -f "$(dirname "$0")")"
chmod +x "$HERE"/minsandbox
"$HERE"/minsandbox "$@"
