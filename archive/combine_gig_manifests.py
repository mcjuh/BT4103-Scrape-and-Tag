"""Combine gig manifests, retaining the latest record for each source filename."""

import argparse
import json
from pathlib import Path


def default_manifests() -> list[Path]:
    """Find all generation manifests, including later structural or semantic retries."""
    combined_name = "gig_combined_manifest.jsonl"
    return sorted(
        path
        for path in Path("big_crawl").glob("gig*_manifest*.jsonl")
        if path.name != combined_name
    )


def combine(manifests: list[Path], output_path: Path) -> None:
    latest_records = {}
    invalid_lines = []

    for manifest_path in manifests:
        if not manifest_path.is_file():
            raise FileNotFoundError(f"Manifest not found: {manifest_path}")
        with manifest_path.open("r", encoding="utf-8") as manifest:
            for line_number, line in enumerate(manifest, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as error:
                    invalid_lines.append(f"{manifest_path}:{line_number}: {error.msg}")
                    continue
                filename = record.get("file")
                if not isinstance(filename, str) or not filename:
                    invalid_lines.append(f"{manifest_path}:{line_number}: missing usable 'file'")
                    continue
                latest_records[filename] = record

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output:
        for record in latest_records.values():
            output.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Combined records written: {len(latest_records)}")
    print(f"Output: {output_path}")
    if invalid_lines:
        print(f"Invalid input lines skipped: {len(invalid_lines)}")
        for detail in invalid_lines[:10]:
            print(f"  {detail}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Combine gig manifests, allowing later retry results to replace earlier ones."
    )
    parser.add_argument("--manifests", nargs="+", type=Path)
    parser.add_argument(
        "--output", type=Path, default=Path("big_crawl/gig_combined_manifest.jsonl")
    )
    args = parser.parse_args()
    combine(args.manifests or default_manifests(), args.output)


if __name__ == "__main__":
    main()