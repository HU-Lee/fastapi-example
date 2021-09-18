from graphene import Interface, String, NonNull, Int

class Basic(Interface):
    date = NonNull(String)

class Korea(Basic):
    detected = NonNull(Int)
    death = NonNull(Int)

class Inter(Basic):
    japan = NonNull(Int)
    usa = NonNull(Int)