#!/usr/bin/env bash
# this_file: tools/scripts/check_all.sh
# Run every check for the FontLab writing skills. Exits non-zero if any fails.
set -u
cd "$(dirname "$0")/../.." || exit 2
status=0
python3 tools/scripts/sync_shared.py --check || status=1
python3 tools/scripts/check_paths.py || status=1
# Punctuation needs contextual review; it is not a structural failure.
python3 -m unittest discover -s tests || status=1
for d in fontlab-*/; do
    [ -f "${d}SKILL.md" ] || { echo "FAIL     ${d} has no SKILL.md"; status=1; }
done
[ $status -eq 0 ] && echo "all checks passed"
exit $status
