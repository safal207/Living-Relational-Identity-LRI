from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / 'README.md',
    ROOT / 'docs' / 'SECURITY_MODEL.md',
    ROOT / 'docs' / 'architecture' / 'lri-trust-model.md',
    ROOT / 'protocol' / 'VERSION.json',
    ROOT / 'protocol' / 'lri' / 'schema' / 'identity.yaml',
    ROOT / 'protocol' / 'lri' / 'schema' / 'lifecycle.yaml',
    ROOT / 'lri-reference' / 'main.py',
]

EXAMPLE_JSONS = [
    ROOT / 'lri-reference' / 'examples' / 'dmp_record_example.json',
    ROOT / 'lri-reference' / 'examples' / 'ltp_event_example.json',
    ROOT / 'lri-reference' / 'examples' / 'subject_example.json',
]


def run_pytest() -> tuple[str, str, int]:
    result = subprocess.run(
        [sys.executable, '-m', 'pytest', '-q'],
        cwd=ROOT / 'lri-reference',
        capture_output=True,
        text=True,
    )
    return 'lri-reference pytest', (result.stdout + result.stderr).strip(), result.returncode


def main() -> int:
    failures: list[str] = []
    outputs: list[tuple[str, str, int]] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            failures.append(f'missing required file: {path.relative_to(ROOT).as_posix()}')

    version_path = ROOT / 'protocol' / 'VERSION.json'
    if version_path.exists():
        try:
            version = json.loads(version_path.read_text(encoding='utf-8'))
            if 'version' not in version:
                failures.append('protocol/VERSION.json missing version field')
        except Exception as exc:
            failures.append(f'protocol/VERSION.json invalid JSON: {exc}')

    for path in EXAMPLE_JSONS:
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            failures.append(f'invalid example JSON {path.relative_to(ROOT).as_posix()}: {exc}')

    outputs.append(run_pytest())

    for name, output, code in outputs:
        print(f'[{name}] status={"PASS" if code == 0 else "FAIL"}')
        if output:
            print(output)
            print('')
        if code != 0:
            failures.append(f'{name} failed')

    if failures:
        print('Project validation failures:')
        for failure in failures:
            print(f'- {failure}')
        return 1

    print('Project validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())