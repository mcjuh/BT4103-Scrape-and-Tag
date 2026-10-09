# -*- coding: utf-8 -*-
"""
Runs one pipeline stage and appends everything it prints to logs/<stage>.log,
so each stage keeps a single log file however many times it runs. The output
still shows on the console.

    python run.py extract --balance --limit 20
    python run.py crawl --concurrency 1

Everything after the stage name goes to the stage's script unchanged. Each run
starts with a "----- run <time>: <command>" line and ends with its exit code;
monitor/dashboard.py reads the latest run from that marker. The dashboard's
Start buttons append to the same files.
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
LOGS_DIR = ROOT_DIR / "logs"
RUN_MARK = "----- run "  # monitor/dashboard.py looks for this at the start of a line

STAGES = {
    "crawl": "scraper/crawl.py",
    "fetch": "scraper/fetch_urls.py",
    "classify": "classifier_extractor/classify.py",
    "industry": "classifier_extractor/industry.py",
    "extract": "classifier_extractor/extract.py",
    "manufacture": "classifier_extractor/manufacture_providers.py",
    "enrich": "enricher/enrich.py",
    "label": "labeller/label.py",
    "judge": "labeller/judge_pools.py",
    "grade": "labeller/grade_pairs.py",
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in STAGES:
        print("usage: python run.py <stage> [script arguments]\n\nstages:")
        for stage, script in STAGES.items():
            print(f"  {stage:<9} {script}")
        return 2
    stage, args = sys.argv[1], sys.argv[2:]
    cmd = [sys.executable, "-u", str(ROOT_DIR / STAGES[stage]), *args]
    # utf-8 output: page titles are printed and would crash a cp1252 console encoder
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1"}
    sys.stdout.reconfigure(errors="replace")

    LOGS_DIR.mkdir(exist_ok=True)
    with (LOGS_DIR / f"{stage}.log").open("a", encoding="utf-8") as log:
        log.write(f"\n{RUN_MARK}{datetime.now():%Y-%m-%d %H:%M:%S}: {' '.join(cmd)}\n")
        log.flush()
        proc = subprocess.Popen(cmd, cwd=ROOT_DIR, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                stdin=subprocess.DEVNULL, env=env, text=True, encoding="utf-8",
                                errors="replace", bufsize=1)

        console = [True]  # cleared if the console goes away (e.g. piped into head), so the log stays whole

        def echo(line: str) -> None:
            if console[0]:
                try:
                    sys.stdout.write(line)
                    sys.stdout.flush()
                except OSError:
                    console[0] = False
            log.write(line)
            log.flush()

        try:
            for line in proc.stdout:
                echo(line)
        except KeyboardInterrupt:
            # Ctrl+C reaches the stage too (same console), so keep logging what it
            # prints while it stops. A second Ctrl+C kills it outright.
            try:
                for line in proc.stdout:
                    echo(line)
            except KeyboardInterrupt:
                proc.kill()
        code = proc.wait()
        log.write(f"----- exit {code}\n")
    return code


if __name__ == "__main__":
    sys.exit(main())
