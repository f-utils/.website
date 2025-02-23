# primitive libs

In this documentation we introduce the __primitive__ `f-utils` libs.

## description

The __primitive__  libs are general and multi context. They contains the implementation of the main concepts, including our [systematics](../../docs/systematics.md). 

## libs

1. [f](f): implements the [systematics](systematics) and the `f-systems`
2. [f-core](f-core): constructs the main instances of the [systematics](systematics)
3. [f-mon](f-mon): with useful monads

## structure

Each primitive lib provides certain _fundamental classes_, which are always represented by a single lowercase letter, as follows.

```rst
lib        class     scope
-------------------------------------------------
f          f         systematics implementation
f-core     t         fundamental types
f-core     o         main type operations
f-core     s         basic spetra examples
f-core     g         principal global tests
f-mon      m         useful monads
```
