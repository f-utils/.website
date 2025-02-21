# structure

In this documentation we talk about the _structure_ of the `f-utils` project.

## libs

The framework provided by `f-utils` consists of a collection of libs, organized into three main categories:

1. **primitive**: these are the generic and context free libs, in which the `f-utils` concepts and systematics are implemented, and their main concrete examples are constructed;
2. **primary**: the context based libs, which are built by making use of the primitive libs;
3. **secondary**:  the derivated and more involved libs, constructed from multiple primary libs.

## repository

Independently of the category, all libs are given by a repository in the Github organization [f-utils](https://github.com/f-utils) under the name `f-{lib}`. The only exception is `f`, which has no suffix. It is a primitive lib and the principal one, being used in each other lib.

## primitive

We have three _primitive_ libs:
1. `f`: the main library, implementing the systematics
2. `f-core`: constructing concrete examples of the concepts
3. `f-mon`: building useful monads, so that allowing a more functional approach

Each primitive lib provides certain _fundamental classes_, which are always represented by a single lowercase letter, as follows.

```rst
lib        class     scope
-------------------------------------------------
f          f         systematics implementation
.................................................
f-core     t         fundamental types
f-core     o         main type operations
f-core     s         basic spetra examples
f-core     g         principal global tests
..................................................
f-mon      m         useful monads
```

## primary

We have many _primary_ libs, each of them covering a small context. Their suffix in `f-{lib}` are determined precisely by their context:
```rst
lib        context
---------------------------
f-ansi     ansi code
f-log      logging systems
f-path     filepaths
f-re       regex and patterns
f-json     json data
...        ...
```

These libraries provide a single _global class_ that corresponds and are named according to the underlying context. The classes also come endowed with an alias: a single uppercase letter - the first letter of the class name.
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

Each primary lib also comes with a subclass `{Lib}.Err`, where the custom error classes are defined. 

## secondary
