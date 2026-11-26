"""Contoso Health Analytics: synthetic training script.

This is an instructional placeholder used to demonstrate a GitHub Actions
release path (validate, package, deploy). It does not represent a real
model. The workspace and data references are synthetic.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_config(path: Path) -> dict:
    """Load a training config from a JSON file, or return defaults."""
    if path.exists():
        return json.loads(path.read_text())
    return {"learning_rate": 0.01, "max_iter": 100, "seed": 42}


def train(config: dict) -> dict:
    """Return a synthetic training result. No real model is fitted."""
    return {
        "status": "trained",
        "learning_rate": config["learning_rate"],
        "max_iter": config["max_iter"],
        "seed": config["seed"],
        "metric": 0.87,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Synthetic training script.")
    parser.add_argument("--config", type=Path, default=Path("config.json"))
    parser.add_argument("--out", type=Path, default=Path("./dist/metrics.json"))
    args = parser.parse_args()

    config = load_config(args.config)
    result = train(config)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2))
    print(f"Training complete. Metrics written to {args.out}.")


if __name__ == "__main__":
    main()
