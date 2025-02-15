# Systematics

Our [philosophy](./philosophy) is realized through a _systematics_: a collection of practical and systematical steps to be used to build `f-systems`. In this documentation we describe some of the fundamental concepts that subsumes our systematics.

## Overview

Recall that a `f-system` is a system that uses the `f` library. Every `f-system` have a `state`, which is defined by all information we have on the system in a given moment. These "information" are given by the entities that the system have access in that given moment, hence by their `accessible entities`. 

In a `f-system` we have four kinds of entities:
1. `types`: are the types that can be passed to (or returned by) a function;
2. `operations`: are functions that receive types and return another types, i.e., are ways to build new types from given ones;
3. `spectra`: are the "generic functions", which implements parametric polymorphisms, hence that can be applied to different types;
4. `dynamic spectra`: are the variations of spectra that deals with _variable_ generic functions, in the sense that they can have a variable number of objects.

The flavored entities that are considered _accessible_ are stored in a corresponding `database` (which is just a dictionary), being then manipulated through `structural methods` (which are just CRUD operations). Thus, with these `structural methods` one controls the `state` of a `f-system`.

## Structure

The entities splits into two parts:
1. metadata
2. specialized data.

The metadata contains:
1. `description`: which briefly describes the entity
2. `tags`: which classify the entity
3. `comments`: which complement the entity

The specialized data vary from the entity kinds, but, in essence, they define the "body" of the entity, which is the part of an entity which is used to construct other things.

## Methods

After creating a `f-system`, the first step is to _initialize_ a `database` for the specific kind of entity we will use. This is done through the method `database()`. One can then _initialize_ an entity in the database, which is done through the method `init()`, that creates an entity with a minimum of metadata and with an "empty body". 

In the sequence, one can _extend_ the "body" of an entity, or add some additional metadata to it. This is done via the methods `extend()` and `add()`, respectively. Some metadata can then be _deleted_ with the `delete()`. Finally, at some moment one can _update_ some data with `update()` method.

## Accessibility

Recall that a principle of the `f-utils` is _accessibility_, which means that the entities of a `f-system` should be quickly accessed and must provide human readable info. This is implemented through additional methods `get()`, `search()` and `info()`. The first one allows us to get data from a given entity. The second one allows us to find a entity inside its database by providing some search string. Finally, the last one returns a human readable account of a provided entity.
