#!/usr/bin/env python3
"""Validate canonical report JSON against bundled Draft 2020-12 schemas.

No network access and no dependency on the source checkout are required.
"""
from pathlib import Path
import argparse
import json
import sys

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


def validate_file(path: Path, assets: Path):
    documents = {}
    for name in ("report.schema.json", "finding.schema.json", "review-process.schema.json"):
        file = assets / name
        if not file.is_file():
            raise ValueError(f"Missing required bundled schema: {file}")
        documents[file.resolve().as_uri()] = json.loads(file.read_text(encoding="utf-8"))
    root_uri = (assets / "report.schema.json").resolve().as_uri()
    registry = Registry().with_resources(
        (uri, Resource.from_contents({**schema, "$id": uri}))
        for uri, schema in documents.items()
    )
    root = {**documents[root_uri], "$id": root_uri}
    Draft202012Validator.check_schema(root)
    report = json.loads(path.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(root, registry=registry).iter_errors(report),
                    key=lambda err: tuple(str(x) for x in err.absolute_path))
    if errors:
        for err in errors:
            location = "/" + "/".join(str(x) for x in err.absolute_path)
            print(f"SCHEMA ERROR {location}: {err.message}", file=sys.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    args = parser.parse_args()
    scripts = Path(__file__).resolve().parent
    assets = scripts.parent / "assets"
    if not (assets / "report.schema.json").is_file():
        assets = scripts.parent / "schemas"
    try:
        if not validate_file(Path(args.input_json).resolve(), assets):
            return 1
    except Exception as exc:
        print(f"SCHEMA VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1
    print("REPORT SCHEMA VALIDATION OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
