===================
totally-average-bot
===================

This is a simple Discord bot used in the Totally Average Gamers discord server.

Requirements
============
* Python 3.8+

Installation
============
This project uses ``pipenv`` (https://pypi.org/project/pipenv/) to manage dependencies.

To install dependencies for the project:

.. code-block:: bash

    pipenv install

This will install dependencies into a virtual environment manage by ``pipenv``. All other
commands should be run from this environment, which can be accessed with:

.. code-block:: bash

    pipenv shell


Quick Start
===========
To connect to a Discord server, a dotenv file should be provided that includes the Discord token
needed to connect to a server. For example:

.. code-block:: bash

    DISCORD_TOKEN=this_is_a_token

Discord tokens can be found in the developer portal on https://discord.com. Follow instructions on
Discord developer portal to allow the bot to join a server.

To run the bot after it's connected to a server:

.. code-block:: bash

    python main.py


Linting
=======
This project uses ``flake8`` for linting. This should install with dev dependencies. To run the linter:

.. code-block:: bash

    flake8

Or to run on a specific path/file

.. code-block:: bash

    flake8 path/to/code

It is recommended to install flake8 into VSCode for live linting


Type Checking
=============
Type checking can be accomplished using the ``pyright`` library (https://github.com/microsoft/pyright)

To install, using ``npm``

.. code-block:: bash

    npm install -g pyright

And to run:

.. code-block:: bash

    pyright

It is recommended to install ``pylance`` in VSCode which will include ``pyright`` as a type checker
