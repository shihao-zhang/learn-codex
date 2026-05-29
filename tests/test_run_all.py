from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RunAllTest(unittest.TestCase):
    def test_run_all_script(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "run_all.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK all mocks", result.stdout)
