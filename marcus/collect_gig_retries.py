"""Collect source files whose latest gig manifest result is not structurally valid."""

import argparse
import json
import shutil
from pathlib import Path


EXPECTED_RESULT_KEYS = {"title", "description"}


def is_valid_result(record: dict) -> bool:
    status = record.get("status")
    result = record.get("result")

    if status == "not_a_gig":
        return result == {}

    if status != "ok" or not isinstance(result, dict):
        return False

    return (
        set(result) == EXPECTED_RESULT_KEYS
        and all(
            isinstance(result[key], str) and result[key].strip()
            for key in EXPECTED_RESULT_KEYS
        )
    )


def load_latest_records(manifest_path: Path) -> tuple[dict[str, dict], list[str]]:
    latest_records = {}
    malformed_lines = []

    with manifest_path.open("r", encoding="utf-8") as manifest:
        for line_number, line in enumerate(manifest, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                malformed_lines.append(f"line {line_number}: invalid JSON ({error.msg})")
                continue

            filename = record.get("file")
            if not isinstance(filename, str) or not filename:
                malformed_lines.append(f"line {line_number}: missing usable 'file' property")
                continue

            latest_records[filename] = record

    return latest_records, malformed_lines


def collect_retries(manifest_path: Path, source_dir: Path, retry_dir: Path) -> int:
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source directory not found: {source_dir}")

    latest_records, malformed_lines = load_latest_records(manifest_path)
    retry_dir.mkdir(parents=True, exist_ok=True)

    copied = []
    missing_sources = []
    for filename, record in latest_records.items():
        if is_valid_result(record):
            continue

        # Manifest filenames are expected to be flat names from big_crawl/gig.
        if Path(filename).name != filename:
            missing_sources.append(f"{filename} (not a filename)")
            continue

        source_file = source_dir / filename
        if not source_file.is_file():
            missing_sources.append(filename)
            continue

        shutil.copy2(source_file, retry_dir / filename)
        copied.append(filename)

    print(f"Latest manifest records checked: {len(latest_records)}")
    print(f"Files copied to retry folder: {len(copied)}")
    print(f"Retry folder: {retry_dir}")

    if malformed_lines:
        print(f"Manifest lines skipped: {len(malformed_lines)}")
        for detail in malformed_lines[:10]:
            print(f"  {detail}")
    if missing_sources:
        print(f"Retry sources not copied: {len(missing_sources)}")
        for filename in missing_sources[:10]:
            print(f"  {filename}")

    return len(copied)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Copy source files with invalid latest gig manifest results into a retry folder."
    )
    parser.add_argument("--manifest", type=Path, default=Path("big_crawl/gig_manifest.jsonl"))
    parser.add_argument("--source-dir", type=Path, default=Path("big_crawl/gig"))
    parser.add_argument("--retry-dir", type=Path, default=Path("big_crawl/gig_retry"))
    args = parser.parse_args()

    collect_retries(args.manifest, args.source_dir, args.retry_dir)


if __name__ == "__main__":
    main()
