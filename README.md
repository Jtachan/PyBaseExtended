# Python Base Extended

The `pybase_ext` modules serve three purposes:

* Enable the use of new base classes in older Python versions. For example, `enum.StrEnum` is new in Python 3.11, but `pybase_ext` allows users on previous versions to use it too.
* Enable experimental classes not implemented in other modules. For example, `enum.TupleEnum` is not implemented in `enum`, but `pybase_ext` allows users to create enumerations where its members are tuples.
* Provide of new classes containing commonly used constant values. For example, `pybase_ext.colors.BGR` provides a wrapper to commonly used BGR color codes, like `BGR.WHITE` to use the color code `(255, 255, 255)`

## TBD - WIP

This code is still a work in progress!
There are still required changes to do before the first release (v0.1.0):

- [ ] Define the `pybase_ext.colors` module.
- [ ] Enable GitHub actions (files should be almost ready).
- [ ] Create ~~mkdocs~~ sphinx documentation.
