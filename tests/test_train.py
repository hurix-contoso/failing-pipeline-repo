"""Unit tests for the synthetic training script."""

from train import load_config, train


def test_train_returns_expected_fields():
    config = {"learning_rate": 0.01, "max_iter": 100, "seed": 42}
    result = train(config)
    assert result["status"] == "trained"
    assert result["learning_rate"] == 0.01
    assert result["max_iter"] == 100
    assert result["seed"] == 42
    assert 0.0 <= result["metric"] <= 1.0


def test_load_config_returns_defaults_when_missing(tmp_path):
    missing = tmp_path / "does_not_exist.json"
    config = load_config(missing)
    assert config["learning_rate"] == 0.01
    assert config["max_iter"] == 100
    assert config["seed"] == 42
