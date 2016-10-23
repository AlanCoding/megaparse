# megaparse
Python bundler for parsing methods (YAML, JSON, etc.) that won't give "no" for an answer.

If you can type it, we can parse it!

## Use

This should follow the same pattern that other parsing libraries do.
For example, it should adhere to basic "load" and "dump" operations.

```python
import megaparse
astr = "a: 4"
print megaparse.load(astr)
```

That code should print out simply `{'a': 4}`.
A second optional argument will always be the fallback option.
For example:

```python
import megaparse
astr = "{a: "
rock = Rock()
print megaparse.load(astr, rock)
```

That string is not a coherent dictionary in any markup system, so
we default to returning the fallback option, which is a rock in this case.
The above code may print `<__main__.Rock instance at 0x10c334518>`, but results
will vary based on what your individual rock looks like.

## Features (planned)

### Multi-parse

Attempt to parse the given string with all the available parsers. If successful
with any parser, return that result, with some restrictions. This will only
ever return a dictionary, and non-dictionary results from any given parser
will be rejected if they are not.

### Pretty Merge

Within the confines of certain formats, comments should be preserved when
merging multiple sources.

### Nested encrypted values

