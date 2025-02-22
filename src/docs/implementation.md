# implementation

In this documentation we discuss how one implements our [systematics](systematics) in the `f-utils` framework.

## entities

In `f-utils`, we will deal with `f-system` that have four kinds of entities:
1. `types`: are the types that can be passed to (or returned by) a function;
2. `operations`: are functions that receive types and return another types, i.e., are ways to build new types from given ones;
3. `spectra`: are the "generic functions", which implements parametric polymorphisms, hence that can be applied to different types;
4. `dynamic spectra`: are the variations of spectra that deals with _variable_ generic functions, in the sense that they can have a variable number of objects.

## classes

Each kind of entity is an object of a class, which comes endowed with an alias:

```rst
class      alias     entities        
--------------------------------------    
Types      t         types
Ops        o         operations
Spec       s         spectra
DSpec      ds        dynamic spectra
```

## methods

The structural operations on the entities are implemented as _methods_ in the corresponding classes.

```rst
method                 meaning
-------------------------------------------------------------------------------------
Types.database()       initialize a Types database
Ops.init()             initialize an operation in some Ops database
Spec.add()             add some metadata to some spectra in some Spec database
DSpec.update()         update some info of some dynamic spectra in some DSpec database
```

## state

The state of an entity is given by a _dictionary entry_, which contains the metadata part and a specialized data part. 

For example, for operations in `Ops`:
```python
some_ops: {
    metadata: {
        desc: "some description",
        tags: ["tag1", "tag2", ...],
        comments: ["comment 1", "comment 2", ...]
    },
    op: {
        func: some_function,
        repr: human_readable_reprentation_of_some_function
    }
}
```

## database

Our databases are just class-level dictionaries containing the states (i.e, the dictionary entries) of the entities.

For example, for `Ops`:
```python
some_Ops_dict = {
    some_ops: {
        metadata: {
            desc: "some description",
            tags: ["tag1", "tag2", ...],
            comments: ["comment 1", "comment 2", ...]
        },
        op: {
            func: some_function,
            repr: human_readable_reprentation_of_some_function
        }
    },
    ...
}
```
