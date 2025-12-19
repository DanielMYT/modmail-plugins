#!/bin/bash
HERE="$(readlink -f "$(dirname "$0")")"
chmod +x "$HERE"/bwrap
"$HERE"/bwrap "$@"
