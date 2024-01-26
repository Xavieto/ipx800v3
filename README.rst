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

    > pip install git+https://github.com/Xavieto/ipx800v3.git#egg=ipx800v3

Usage
-----

.. note:: The default API key of the device is `apikey`.

.. code-block:: python

    from ipx800v3 import ipx800v3

    ipx = ipx800v3(url="http://your-device-ip", username="username", password="password")

    out1 = ipx.output[0]
    out1.status  # => return a Boolean
    out1.on()
    out1.off()

Links
-----

* GCE IPX800V3 API: https://download.gce-electronics.com/data/007_IPX800_V3/IPX_API.pdf

Licence
-------

Licensed under Apache License Version 2.0
