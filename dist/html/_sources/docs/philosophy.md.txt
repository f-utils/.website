# philosophy

In this documentation we talk about the philosophy that subsumes the `f-utils` framework.

## f-systems

`f-utils` is about building `f-systems`. They are formed by `entities`, which are organized into `types`, and relations between them: the `constructions`. 

In the world of software development, one could think of these "entities" as variables that have some "type". This is the case, for example, of objects of some class. The "constructions" could be viewed as operations that receive entities, manipulate them, and return some other entity, hence as functions in some programming language.

## principles 

In a `f-system`, entities and constructions are subjected to the following principles:
1. **constructivism**: there are certain _primitive_ entities, from which everything is derived
2. **distinguishability**: entities can be easily distinguished one among each other
4. **intelligibility**: entities contains intelligible (i.e, human readable) information
5. **extensibility**: entities can be modified without affecting the constructions that already used them
6. **universality**: constructions are _general_ and can be applied to different contexts
7. **type safety**: constructions are parameterized by the type of the involved entities

All those specific principles are guided by a simple general principle:

> **minimalism**: to have only what is _really_ needed.

## state

One can give sense to the "extensibility" principle by assuming that:
1. the entities have not only a `type`, but also a `state`
2. the `state` can be modified
3. a construction depends not only of the `type` of the involved entities (as needed to ensure type safety), but also on their on `state`.

One could then talk about "stateful `f-systems`". 

> Notice that if one adopt states, this means that the entities are supposed to be _mutable_.

## polymorphisms

The "universality" principle assumes that there constructions that can be applied to different contexts. If one think of constructions as "functions", this means that certain functions can be used to different proposes. This is precisely the scope of _polymorphisms_.

On the other hand, the "type safety" principle assumes that there are constructions that depends on the type of entities. But polymorphisms which depend on types are _parametric polymorphisms_.

Thus:

> `f-systems` typically deals with constructions that are implemented by parametric polymorphisms.

## metadata

In turn, the "distinguishability" principle tell us that entities could be easily distinguished, while "intelligibility" principle tell us that this should be made using human readable info.

But the "distinguishable human readable" info of something is normally given by its _metadata_.

Therefore:

> In `f-systems`, entities typically have metadata.

## dependencies

Finally, the general "minimalism" principle tell us that one should avoid adding dependencies unless they are __really__ needed.
