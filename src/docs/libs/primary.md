# primary libs

In this documentation we introduce the __primary__ libs of `f-utils` framework.

## description

The primary libs are the context-based `f-utils` libraries, which are built directly from the [primitive](primitive) libs. They construct the main utilities implemented in `f-utils`. 

## libs

1. [f-ansi](../../libs/f-ansi): deals with ANSI code
2. [f-log](../../f-log): deals with logging systems
3. [f-path](../../f-path): deals with filepaths
4. [f-re](../../f-re): deals with regex
5. [f-json](../../f-json): deals with json
6. [f-os](../../f-os): deals with operating system level stuff
7. [f-cli](../../f-cli): deals with the construction of command line interfaces

## classes

Each primary lib provides a single __global class__ that corresponds and ais named according to the underlying lib context. The classes also come endowed with an alias: a single uppercase letter - typically the first letter of the class name.
```rst
lib        context              class     alias
----------------------------------------------
f-ansi     ansi code            Ansi      A
f-log      logging systems      Log       L
f-path     filepaths            Path      P
f-re       regex and patterns   Re        R
f-json     json data            Json      J
...        ...                  ...       ...
```

Each of them lib also comes with a subclass `{Lib}.Err`, where the custom error classes are defined.
