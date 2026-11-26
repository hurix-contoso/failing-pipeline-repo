"""Package step: assembles the artifact the deploy job will consume.

Copies environment.yml (and any adjacent asset files) into the output
directory so that a downstream job can download it and run
`az ml environment create --file ./dist/environment.yml`.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

FILES_TO_PACKAGE = ["environment.yml"]


def build(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in FILES_TO_PACKAGE:
        source = Path(name)
        if not source.exists():
            raise FileNotFoundError(f"Expected {source} in the repository root.")
        shutil.copy2(source, out_dir / source.name)
        print(f"Packaged: {source} -> {out_dir / source.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the release artifact.")
    parser.add_argument("--out", type=Path, default=Path("./dist"))
    args = parser.parse_args()
    build(args.out)
    print(f"Artifact ready in {args.out}.")


if __name__ == "__main__":
    main()
