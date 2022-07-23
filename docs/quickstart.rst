:orphan:

.. _quickstart:

.. currentmodule:: pyspapi

Quickstart
==========

This page gives a brief introduction to the library. It assumes you have the library installed,
if you don't check the :ref:`installing` portion.

A Minimal Bot
-------------

Let's make a bot that responds to a slash command and walk you through it.

It looks something like this:

.. code::

  import pyspapi

  print(pyspapi.SPAPI(card_id='card_id', token='token').balance)

Make sure not to name it ``pyspapi`` as that'll conflict with the library.


You can find more examples in the `examples directory <https://github.com/deesiigneer/pyspapi/tree/main/examples/>`_ on GitHub.