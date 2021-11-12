Quickstart
==========
Install Cookiecutter if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

If you want to use the custom code coverage badge:

1. Go to [gist.github.com](https://gist.github.com/) and create a new gist. You will need the ID of the gist (this is the long alphanumerical part of its URL) later.
2. Navigate to [github.com/settings/tokens](https://github.com/settings/tokens) and create a new token with the *gist* scope.
3. Go to the *Secrets* page of the settings of your repository and add this token as a new secret. Name it `GIST_SECRET`.

Generate a project:

```bash
cookiecutter https://github.com/dobraczka/pypackage-poetry-cookiecutter.git
```
With the post-gen hook this will also add base depencies and install them.
