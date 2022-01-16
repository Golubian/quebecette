# Francinette

A small and easy to use testing framework for the 42 projects.

Use `francinette` or `paco` inside a project folder to run it.


## Table of Contents
1. [Purpose](#purpose)
2. [Install](#install)
3. [Update](#update)
4. [Running](#Running)
5. [FAQ](#faq)
6. [Acknowledgments](#acknowledgments)

## Purpose:

This is designed to function as a kind of `moulinette` that you can execute in local.

That means that by executing `francinette` it will check `norminette`, compile the
code and execute the tests.

This will give you more time to look at the code when doing a review, instead of
worrying about compiling and executing tests on the cloned code.

You can also use it as a local test battery, so that you can test your own code.


## Install:
Francinette has an automatic installer.

Copy the line bellow to your console and execute it. It will automatically download the repo,
create the necessary folders and alias, and install a python virtual environment dedicated to
running this tool

```
bash -c "$(curl -fsSL https://raw.github.com/xicodomingues/francinette/master/utils/install.sh)"
```

The francinette folder will be under your `$HOME` directory (`/User/<you_username>/`)

## Update:
Normally francinette will prompt you when there is a new version, and you can then update it.

You can also force it from francinette itself:

```
~ $> francinette -u              # Forces francinette to update
```

If the above does not work you can also execute the command bellow:

```
bash -c "$(curl -fsSL https://raw.github.com/xicodomingues/francinette/master/utils/update.sh)"
```


## Runnning:

If you are on a root of a project, `francinette` should be able to tell which project
it is and execute the corresponding tests.

You can also use the shorter version of the command: `paco`

```
/C00 $> francinette                  # Execute the tests for C00

/C00/ex00 $> francinette             # Execute only the tests for ex00 in C00

/libft $> francinette                # Execute the tests for libft

~ $> francinette -h                  # Shows the help message

libft $> paco memset isalpha memcpy  # Executes only the specified tests
```

The name of the folder is not important. What is important is that you have a `Makefile`
that contains the name of the project (for example `libft`). If there is no `Makefile`
`francinette` will not know what project to execute.

```
~ $> francinette git@repo42.com/intra-uuid-234
```
This command clones the git repository present in `git@repo42.com/intra-uuid-234` into the
current folder and executes the corresponding tests

All the files are copied to the folder `~/francinette/temp/<project>`. In here is where the
norminette is checked, the code compiled and the tests executed. Normally you do not need to
access this directory for anything. But if you run into unexpected problems, this is where
the magic happens.

## FAQ

If you have any questions I am probably in the barcelona cluster. Also, you can reach me on
slack under `fsoares-`

#### I'm more advanced than the tests you have available. When are you adding more tests?

When I reach that exercise or project. You can also add them. For that you need to create a
`ProjectTester.py` file. and change the function `guess_project` in `main.py` to recognize
the project.

#### This test that you put up is incorrect!

Please contact me on slack (under `fsoares-`) indicating for what exercise which test fails,
and a description of what you think is wrong. You can also try to fix it and create a pull
request for that change!

## Acknowledgments

* To 42 for providing me this opportunity
* To [Tripouille](https://github.com/Tripouille) for their excellent [libftTester](https://github.com/Tripouille/libftTester)