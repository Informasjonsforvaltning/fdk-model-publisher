"""Nox sessions."""
import sys
import tempfile

import nox
from nox.sessions import Session
import nox_poetry

locations = "src", "tests", "noxfile.py"
nox.options.sessions = (
    "lint",
    "mypy",
    "safety",
    # "unit_tests",
    "integration_tests",
    # "contract_tests",
)


@nox.session
def integration_tests(session: Session) -> None:
    """Run the integration test suite."""
    args = session.posargs
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(
        session,
        "coverage[toml]",
        "pytest",
        "pytest-cov",
        "requests-mock",
        "pytest-mock",
        "aioresponses",
        "pytest-aiohttp"
    )

    print(sys.path)
    session.run(
        "pytest",
        "-m integration",
        "-rA",
        *args,
        env={},
    )


@nox.session
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    nox_poetry.install(session, "black")
    session.run("black", *args)


@nox.session
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    nox_poetry.install(
        session,
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


@nox.session
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
        nox_poetry.install(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    nox_poetry.install(session, "mypy")
    session.run("mypy", *args)


@nox.session
def coverage(session: Session) -> None:
    """Upload coverage data."""
    nox_poetry.install(session, "coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)
