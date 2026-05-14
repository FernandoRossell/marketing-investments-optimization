from pathlib import Path
from src.config import load_yaml_config


def test_load_yaml_config_returns_dict(tmp_path: Path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("a: 1
b: test
", encoding="utf-8")
    data = load_yaml_config(config_file)
    assert isinstance(data, dict)
    assert data["a"] == 1
    assert data["b"] == "test"
