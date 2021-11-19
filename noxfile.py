"""Nox sessions."""
import sys
import tempfile

import nox
from nox.sessions import Session
import nox_poetry

nox.options.envdir = ".cache"
nox.options.reuse_existing_virtualenvs = True
locations = "src", "tests", "noxfile.py"
nox.options.sessions = ("lint", "mypy", "safety", "integration_tests")


@nox_poetry.session
def integration_tests(session: Session) -> None:
    """Run the integration test suite."""
    args = session.posargs or ["--cov"]
    session.install(
        ".",
        "coverage[toml]",
        "pytest",
        "pytest-cov",
        "requests-mock",
        "pytest-mock",
        "aioresponses",
        "pytest-aiohttp",
    )

    session.run(
        "pytest",
        "-m integration",
        "-rA",
        *args,
        env={},
    )


@nox_poetry.session
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox_poetry.session
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "pep8-naming",
    )
    session.run("flake8", *args)


@nox_poetry.session
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox_poetry.session
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or ["--install-types", "--non-interactive", "src", "tests"]
    session.install(".")
    session.install("mypy", "pytest")
    session.run("mypy", *args)
    if not session.posargs:
        session.run("mypy", f"--python-executable={sys.executable}", "noxfile.py")


@nox_poetry.session
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)
