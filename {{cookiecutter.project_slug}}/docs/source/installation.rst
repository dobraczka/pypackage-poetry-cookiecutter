Installation
============

The easiest way to get {{ cookiecutter.project_name }} is via pip:

.. code-block:: bash

   pip install {{ cookiecutter.module_name }}

To build kiez from source use `poetry <https://python-poetry.org/>`_ 

.. code-block:: bash

   git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git 
   cd {{ cookiecutter.project_slug }} 
   poetry install
