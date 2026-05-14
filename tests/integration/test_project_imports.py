def test_project_modules_importable():
    import src.config  # noqa: F401
    import src.logging_config  # noqa: F401
    import api.app  # noqa: F401
