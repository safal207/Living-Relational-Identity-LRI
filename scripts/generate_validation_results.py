from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'VALIDATION_RESULTS.md'


def main() -> int:
    result = subprocess.run(
        [sys.executable, 'scripts/validate_project.py'],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    lines = [
        '# LRI Validation Results',
        '',
        'Tracked validation snapshot for the current LRI reference implementation and protocol assets.',
        '',
        '## Summary',
        '',
        f'- Validation command: `python scripts/validate_project.py`',
        f'- Exit status: **{"PASS" if result.returncode == 0 else "FAIL"}**',
        '',
        '## Output',
        '',
        '```text',
        (result.stdout + result.stderr).strip(),
        '```',
        ''
    ]

    OUTPUT.write_text('\n'.join(lines), encoding='utf-8')
    return result.returncode


if __name__ == '__main__':
    raise SystemExit(main())