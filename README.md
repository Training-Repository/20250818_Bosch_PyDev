## References
* [Pep-8  Python prog style guide](https://peps.python.org/pep-0008/)
* [Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html#lexical-analysis)
* [Zen of Python](https://peps.python.org/pep-0020/)
* [Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [Operator overloading](https://docs.python.org/3/library/operator.html#module-operator)

| `ctypes` Type      | C Equivalent        | Python Equivalent Type | Typecode | Description                                                      |
|--------------------|---------------------|------------------------|----------|------------------------------------------------------------------|
| `ctypes.c_bool`    | `_Bool`             | `bool`                 | `?`      | Boolean value (True or False)                                    |
| `ctypes.c_char`    | `char`              | `bytes` or `str`       | `c`      | Single character                                                 |
| `ctypes.c_wchar`   | `wchar_t`           | `str`                  | `u`      | Single wide character                                            |
| `ctypes.c_byte`    | `signed char`       | `int`                  | `b`      | Signed byte value                                                |
| `ctypes.c_ubyte`   | `unsigned char`     | `int`                  | `B`      | Unsigned byte value                                              |
| `ctypes.c_short`   | `short`             | `int`                  | `h`      | Signed short integer                                             |
| `ctypes.c_ushort`  | `unsigned short`    | `int`                  | `H`      | Unsigned short integer                                           |
| `ctypes.c_int`     | `int`               | `int`                  | `i`      | Signed integer                                                   |
| `ctypes.c_uint`    | `unsigned int`      | `int`                  | `I`      | Unsigned integer                                                 |
| `ctypes.c_long`    | `long`              | `int`                  | `l`      | Signed long integer                                              |
| `ctypes.c_ulong`   | `unsigned long`     | `int`                  | `L`      | Unsigned long integer                                            |
| `ctypes.c_longlong`| `__int64` or `long long` | `int`              | `q`      | Signed long long integer                                         |
| `ctypes.c_ulonglong`| `unsigned __int64` or `unsigned long long` | `int`   | `Q`      | Unsigned long long integer                                       |
| `ctypes.c_float`   | `float`             | `float`                | `f`      | Single precision floating point                                  |
| `ctypes.c_double`  | `double`            | `float`                | `d`      | Double precision floating point                                  |
| `ctypes.c_longdouble` | `long double`     | `float`                | `g`      | Extended precision floating point                                |
| `ctypes.c_char_p`  | `char *`            | `bytes` or `None`      | `z`      | Pointer to a string (C-style)                                    |
| `ctypes.c_wchar_p` | `wchar_t *`         | `str` or `None`        | `Z`      | Pointer to a wide string                                         |
| `ctypes.c_void_p`  | `void *`            | `int` or `None`        | `P`      | Pointer to any type (void pointer)                               |
| `ctypes.c_size_t`  | `size_t`            | `int`                  | `n`      | Unsigned integral type used for sizes                            |
| `ctypes.c_ssize_t` | `ssize_t`           | `int`                  | `N`      | Signed integral type used for sizes                              |
| `ctypes.POINTER`   | `*` (pointer)       | `ctypes` type          |          | Generic pointer type (used for creating pointers to other types) |
| `ctypes.Structure` | `struct`            | `class`                |          | Used for defining C-style structures                             |
| `ctypes.Union`     | `union`             | `class`                |          | Used for defining C-style unions                                 |
| `ctypes.Array`     | Array type          | `list` or `array`      |          | Used for defining C-style arrays                                 |


## Snippets
* Create a virt. env --> `python -m venv .venv-training`
* Enter into a virt. env --> 
    * Bash (Win) --> `source .venv-training/Scripts/activate`
    * Bash (Mac) --> `source .venv-training/bin/activate`
    * Cmd Prompt --> `.venv-training\Scripts\activate.bat`
    * Power Shell --> `.venv-training\Scripts\activate.ps1`
* Exit a virt. env. --> `deactivate`
* Pip Commands
    * `pip install <package_name>`
    * `pip list` to list the installed packages
    * `pip freeze > requirements.txt` to store the installed packages (and specific versions) into the file
    * `pip install -r requirements.txt` to install packages specified in the file

* Compare image resize project - Base to Latest
    * `git reset --hard b655c03`
    * `pytest _027_Concurrency_Revisit/`
    * `git reset --hard origin/main`
    * `pytest _027_Concurrency_Revisit/`


## Links
* [Trainer/Training Feedback](https://forms.gle/e5txJ6TQftBp6hQz9)

## Contact
* ramakant.s.debata@gmail.com

