#!/usr/bin/env bash
# Run every check for the FontLab writing skills. Exits non-zero if any fails.
set -u
cd "$(dirname "$0")/../.." || exit 2
status=0
python3 tools/scripts/sync_shared.py --check || status=1
python3 tools/scripts/check_paths.py || status=1
# A dash inside a blockquote is a quoted example, usually of the tell itself.
# Everywhere else in house prose it is a defect.
for f in fontlab-*/SKILL.md fontlab-*/references/*.md tools/house-rules.md; do
    [ -f "$f" ] || continue
    if grep -v '^>' "$f" | grep -q '[—–]'; then echo "FAIL     dash in $f"; status=1; fi
done
for d in fontlab-*/; do
    [ -f "${d}SKILL.md" ] || { echo "FAIL     ${d} has no SKILL.md"; status=1; }
done
[ $status -eq 0 ] && echo "all checks passed"
exit $status
