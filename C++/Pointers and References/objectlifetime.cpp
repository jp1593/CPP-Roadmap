/*
Object lifetime refers to the time during which an object exists, from the moment it is created until it is destroyed, it has 4 stages:
- Static Storage Duration:
    Objects with static storage duration exist for the entire run of the program. These objects are allocated at the beginning of the program’s run and
    deallocated when the program terminates. Global variables, static data members, and static local variables fall into this category.

    Ex:
    int global_var;            // Static storage duration
    class MyClass {
    static int static_var;   // Static storage duration
    };
    void myFunction() {
    static int local_var;    // Static storage duration
    }

- Thread Storage Duration: 
    Objects with thread storage duration exist for the lifetime of the thread they belong to. 

    Thread storage duration can be specified using the thread_local keyword: 
    thread_local int my_var;   // Thread storage duration

- Automatic Stoarge Duation: 
    Objects with automatic storage duration are created at the point of definition and destroyed when the scope in which they are declared is exited. 

    These objects are also known as “local” or “stack” objects. 

    Ex: Function variables

- Dynamic Storage Duration:
    Objects with dynamic storage duration are created at runtime, using memory allocation functions such as new or malloc. The lifetime of these objects must be managed manually,
    as they are not automatically deallocated when the scope is exited. 

    Programmer has the responsability to destroy this objects. 




*/