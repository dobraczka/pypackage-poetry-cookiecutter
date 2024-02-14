#!/bin/zsh

poetry add --group dev ruff ipdb mypy pytest pytest-cov nox-poetry pytest-mock toml strawman pyroma
poetry add --optional mkdocs mkdocs-material "mkdocstrings[python]" mkdocs-literate-nav mkdocs-gen-files mkdocs-section-index
git init
pre-commit install
