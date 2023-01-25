from nox_poetry import Session, session


@session()
def tests(session: Session) -> None:
    args = session.posargs or ["--cov", "--cov-report=xml"]
    session.install(".[all]")
    session.install("pytest")
    session.install("pytest-cov")
    session.install("pytest-mock")
    session.run("pytest", *args)


locations = ["{{ cookiecutter.module_name }}", "tests", "noxfile.py"]


@session()
def lint(session: Session) -> None:
    args = session.posargs or locations
    session.install("black", "isort")
    session.run("black", *args)
    session.run("isort", *args)


@session()
def style_checking(session: Session) -> None:
    args = session.posargs or locations
    session.install(
        "pyproject-flake8",
        "flake8-eradicate",
        "flake8-isort",
        "flake8-debugger",
        "flake8-comprehensions",
        "flake8-print",
        "flake8-black",
        "darglint",
        "pydocstyle",
    )
    session.run("mypy", "--install-types", "--non-interactive")
    session.run("pflake8", "--docstring-style", "sphinx",  *args)


@session()
def pyroma(session: Session) -> None:
    session.install("poetry", "pyroma")
    session.run("pyroma", "--min", "10", ".")


@session()
def type_checking(session: Session) -> None:
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", "--ignore-missing-imports", *args)


@session()
def doctests(session: Session) -> None:
    session.install(".[all]")
    session.install("xdoctest")
    session.install("pygments")
    session.run("xdoctest", "-m", "{{ cookiecutter.module_name }}")


@session()
def build_docs(session: Session) -> None:
    session.install(".")
    session.install("sphinx")
    session.install("insegel")
    session.cd("docs")
    session.run("make", "clean", external=True)
    session.run("make", "html", external=True)
