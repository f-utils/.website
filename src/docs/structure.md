# structure

In this documentation we talk about the structure of the `f-utils` project, i.e, how it is organized.

## libs

The framework provided by `f-utils` consists of a collection of libs, organized into four main categories:

1. [primitive](../libs/primitive): these are the generic and context free libs, in which the `f-utils` concepts and [systematics](systematics) are [implemented](implementation), and in which their main concrete examples are constructed
2. [primary](../libs/primary): the context-based libs, which are built by making use of the primitive libs. These libs provides our main utilities
3. [secondary](../libs/secondary):  the derived and more involved libs, constructed from multiple primary libs
4. [other](../libs/other):  additional minor libraries

## repository

Independently of the category, all libs are given by a repository in the Github organization [f-utils](https://github.com/f-utils) under the name `f-{lib}`. The only exception is `f`, which has no suffix. It is a primitive lib and the principal one, being used in each other lib. It is in it that our [systematics](systematics) is implemented.

## dot repos

The [f-utils](https://github.com/f-utils) organization also has another kind of repositories: the __dot__ repos. As suggested, they are named under `.{name}` and have a non-lib context:

1. [.github](https://github.com/f-utils/.github): organization configuration files
2. [.issues](https://github.com/f-utils/.issues): issues of all libs
3. [.website](https://github.com/f-utils/.website): files of our website
4. [.template](https://github.com/f-utils/.template): template directory to build libs
