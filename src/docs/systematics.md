# systematics

Our [philosophy](./philosophy) is realized through a _systematics_: a collection of practical and systematical steps to be used to build `f-systems`. 

## review

Recall that :
1. `f-systems` are composed by `entities` and by `constructions`
2. entities have a `type`
4. `f-systems` typically deals with _parametric polymorphisms_
3. the entities normally have _metadata_.

> In the following we will deal with "stateful `f-systems`", for with an entity have not only a `type`, but also a `state`.

## global state

The `state` of an entity is defined by all information we have on the system in a given moment. If the entities have a state, also has the `f-system`: it is given by the entities that the system have access in that given moment.

> These are the so-called _accessible entities_, which determines the _global state_ of the `f-system`.

## database

The entities should be created at some sort of "database", which stores the state of the entities and, therefore, which defines the "global state" of the `f-system`.

## structure

If entities have "metadata", this means that they split into two parts:
1. the metadata
2. other _specialized data_.

The metadata should contains, for example:
1. `description`: which briefly describes the entity
2. `tags`: which classify the entity
3. `comments`: which complement the entity

The specialized data may vary from the entity kind, but, in essence, they define the "body" of the entity, which is the part of an entity which is used to construct other things. 

> The "state" of an entity is defined by its _metadata_ and by its _specialized data_.

## methods

To modify the "state" of something we need certain CRUD operations. In our context, they could be viewed as _methods_:
1. `database()`: creates some empty database. In other words, _initialize_ the global state 
2. `init()`: creates (or _initialize_) an entity in some database with its _minimal state_
3. `add()`: add some metadata, as a "tag" or a "comment"
4. `delete()`: delete some metadata
5. `extend()`: add something to the "body" of the entity 
6. `update()`: change something in the metadata or in the body.

On the other hand, recall the principle of "distinguishability". According to them, one should be able to have a simplified access to the information that distinguishes an entity from the other entities. In other words, one needs two new methods:

- `find()`: localizes an entity inside a database from some given information
- `get()`: retrieves specific metadata or specialized data of an entity

Finally, we also have the principle of "intelligibility", so that we also need another method:

- `info()`: prints information of  an entity in a human readable way. 
