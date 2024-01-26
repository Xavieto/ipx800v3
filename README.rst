IPX800V3
==========

A python library to control a IPX800 V3 device build by GCE-Electronics through its light "API".

* Python 3.8+ support
* WTFPL License

IPX800V3 features implemented
---------------------------

* Control:

  - outputs (``ipx.outputs[]``)
  - inputs (``ipx.intputs[]``)

Installation
------------

.. code-block:: console

    > pip install ipx800v3

Usage
-----

.. note:: The default API key of the device is `apikey`.

.. code-block:: python

    from ipx800v3 import ipx800v3

    ipx = ipx800("http://your-device-ip", "username", "password")

    out1 = ipx.output[0]

    out1.status  # => return a Boolean

    out1.on()

    out1.off()

Links
-----

* GCE IPX800V3 API: 

Licence
-------

Licensed under Apache License Version 2.0
