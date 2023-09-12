# General

- What is Conda?
- Why should I use a package and environment management system as part of my research workflow?
- Why use Conda ?


## Packages and Environments

## Modules, packages, libraries

- **Module**: a collection of functions and variables, as in a script
- **Package**: a collection of modules with an `init.py` file, as in a directory with scripts
- **Library**: a collection of packages with related functionality

## Dependencies

Many packages do not do everything on their own; instead of reinventing the wheel they _depend_ on other packages for their functionality. `Scipy` uses `numpy` and `matplotlib` so they are *dependances* for `Scipy`.

```ad-danger 
collapse: close
Problems can often occur, when packages update - functions may be altered or removed and if another package has it as a dependancy it can cause errors. So its important to ensure versions correctly work together, for example Scipy depends on numpy version >= 1.6 and matplotlib version >= 1.1



Other issues can arise from older software requiring earlier package versions to run, or a different Python (or language) version.
```
```ad-success
collapse: closed
_environments_ are one solution to the problem. Nowadays there are several environment management systems following a similar idea: Instead of having to use multiple computers or virtual machines to run different versions of the same package, you can install packages in isolated environments
```
## Environment management

There are many *situations* when using `envs` can be beneficial:
- An application you need for a research project requires different versions of your base programming language or different versions of various third-party packages from the versions that you are currently using.
- An application you developed as part of a previous research project that worked fine on your system six months ago now no longer works.
- Code that was written for a joint research project works on your machine but not on your collaborators’ machines.
- An application that you are developing on your local machine doesn’t provide the same results when run on your remote cluster.

`Envs` enable you to:
- Environment management systems help resolve dependency issues by allowing you to use different versions of a package for different projects.
- Make your projects self-contained and reproducible by capturing all package dependencies in a single requirements file.
- Allow you to install packages on a host on which you do not have admin privileges.

```ad-info
collapse: closed
title: Environment management systems for Python
Conda is not the only way; Python for example has many more ways of working with environments:

- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [venv](https://docs.python.org/3/library/venv.html)
- [pyenv](https://github.com/pyenv/pyenv)
- …
```
```ad-info
title: Package management systems for Python
collapse: closed
Also here, Conda is not the only way; Python for example has many more ways of working with packages:
- [pip](https://pip.pypa.io/en/stable/)
- [Poetry](https://python-poetry.org/)
```

## Why should use a package and environment management system?

Installing software can be hard. 
Installing scientific software is often even more challenging. 

To minimize the burden of installing and updating software we often install software packages **system-wide**.

Installing software **system-wide** has a number of drawbacks:

- It can be difficult to figure out what software is required for any particular research project.
- It is often impossible to install different versions of the same software package at the same time.
- Updating software required for one project can often “break” the software installed for another project.

Installing software system-wide creates complex dependencies between your research projects that shouldn’t really exist -  wouldn’t it be great if we could install software separately for each research project?

```ad-question
title: Discussion
collapse: closed
What are some of the _potential_ benefits from installing software separately for each project? What are some of the _potential_ costs?
```
```ad-success
title: Solution
collapse: closed
You may notice that many of the potential benefits from installing software separately for each project require the ability to isolate the projects’ software environments from one another (i.e., solve the environment management problem). Once you have figured out how to isolate project-specific software environments, you will still need to have some way to manage software packages appropriately (i.e., solve the package management problem).
```

# Conda

From the [official Conda documentation](https://conda.io/projects/conda/en/latest/index.html). Conda is an open source package and environment management system that runs on Windows, Mac OS and Linux.

- Conda can quickly install, run, and update packages and their dependencies.
- Conda can create, save, load, and switch between project specific software environments on your local computer.
- Although Conda was created for Python programs, Conda can package and distribute software for any language such as R, Ruby, Lua, Scala, Java, JavaScript, C, C++, FORTRAN.

Conda as a _package manager_ helps you find and install packages. 
If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because Conda is also an _environment manager_

## Conda vs. Miniconda vs. Anaconda
![[Pasted image 20230911122809.png]]
`Conda` is a tool for managing environments and installing packages. 
`Miniconda` combines `Conda` with Python and a small number of core packages
`Anaconda` includes `Miniconda` as well as a large number of the most widely used Python packages.

Benefits of using Conda:
- prebuild packages, installing from source can be a pain..
- cross platform, enhancing reproducibility
- can use other package managers inside a Conda `env`, such as `pip`

Anaconda provides many data science related packages already installed
```ad-danger
title: But
collapse: closed
Anaconda can be very slow at package resolution and can feel bloated
```
# Working with Environments

- What is a Conda environment?
- How do I create/delete an environment?
- How do I activate/deactivate an environment?
- How do I install packages into existing environments using Conda (+pip)?
- Where should I create my environments?
- How do I find out what packages have been installed in an environment?
- How do I find out what environments that exist on my machine?
- How do I delete an environment that I no longer need?


```ad-note
title: Workspace for Conda envs
collapse: closed
Create a new `conda_temp` directory on your Desktop in order to maintain a consistent workspace for all your conda environment.


On Mac OSX and Linux running following commands in the Terminal will create the required directory on the Desktop.

`$ cd ~/Desktop`

`$ mkdir conda_temp`

`$ cd conda_temp`

For Windows users you may need to reverse the direction of the slash and run the commands from the command prompt.

`> cd ~\Desktop`

`> mkdir conda_temp`

`> cd conda_temp`


Alternatively, you can always “right-click” and “create new folder” on your Desktop. 
```

## What is a Conda environment

A [Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) is a directory that contains a specific collection of Conda packages that you have installed

```ad-danger
title: Important
collapse: closed
## Avoid installing packages into your `base` Conda environment
Conda has a default environment called `base` that include a Python installation and some core system libraries and dependencies of Conda. It is a “best practice” to avoid installing additional packages into your `base` software environment. Additional packages needed for a new project should always be installed into a newly created Conda environment.
```
## Creating environments

Before we start lets look at the installed Conda information:

```
$ conda info

$ conda info -e
```
Setttings can usually be found in `.condarc`

To create a new environment for Python development using `conda` you can use the `conda create` command.
```
$ conda create --name python3-env python
```

Give your environment a meaningful **name** in order to help yourself remember the purpose of the environment. 

While naming things can be difficult, `$PROJECT_NAME-env` is a good convention to follow. 

Sometimes also the specific version of a package why you had to create a new environment is a good name

The command above will create a new Conda environment called  `python3-env` and install the most recent version of Python. 

If you wish, you can specify a particular version of packages for `conda` to install when creating the environment.

````
$ conda create --name python36-env python=3.6
````

Commands for keeping this tidy:
```
$ conda create --prefix ~/Desktop/conda_temp/py3.10_env python=3.10
```

```ad-danger
title: Always specify a version number for each package you wish to install
collapse: closed

To make results more reproducible and to make it easier for research colleagues to recreate your Conda environments on their machines it is a `best practice` to always explicitly specify the version number for each package that you install into an environment. 

If you are not sure exactly which version of a package you want to use, then you can use search to see what versions are available using the `conda search` command.

`$ conda search $PACKAGE_NAME`

For example, if you wanted to see which versions of [Scikit-learn](https://scikit-learn.org/stable/), a popular Python library for machine learning, were available, you would run the following.


`$ conda search scikit-learn`

As always you can run `conda search --help` to learn about available options.
```

You can create a Conda environment and install **multiple** packages by listing the packages that you wish to install.

```
$ conda create --name basic-scipy-env ipython=7.13 matplotlib=3.1 numpy=1.18 scipy=1.4
```

When `conda` installs a package into an environment it also installs any required dependencies. For example, even though Python is not listed as a packaged to install into the `basic-scipy-env` environment above, `conda` will still install Python into the environment because it is a required dependency of at least one of the listed packages.

```ad-question
title: Creating a new environment
collapse: closed
Create a new environment called “machine-learning-env” with Python and the most current versions of [IPython](https://ipython.org/), [Matplotlib](https://matplotlib.org/), [Pandas](https://pandas.pydata.org/), [Numba](https://numba.pydata.org/) and [Scikit-Learn](https://scikit-learn.org/stable/index.html).
```
```ad-success
title: Solution
collapse: closed
In order to create a new environment you use the `conda create` command as follows.


`$ conda create --name machine-learning-env \`

 `ipython \`
 
 `matplotlib \`
 
 `pandas \`
 
 `python \`
 
 `scikit-learn \`
 
 `numba`


Since no version numbers are provided for any of the Python packages, `conda` will download the most current, mutually compatible versions of the requested packages. 
However, since it is best practice to always provide explicit version numbers:


`$ conda create --name machine-learning-env \`

 `ipython=7.19 \`
 
` matplotlib=3.3 \`
 
` pandas=1.2 \`
 
 `python=3.8 \`
 
` scikit-learn=0.23 \`
 
` numba=0.51`



However, please be aware that the version numbers for each packages may not be the latest available and would need to be adjusted.
```

## Activating an existing environment

Activating environments is essential to making the software in environments work well (or sometimes at all!). Activation of an environment does two things.
1. Adds entries to `PATH` for the environment.
2. Runs any activation scripts that the environment may contain.
Step 2 is particularly important as activation scripts are how packages can set arbitrary environment variables that may be necessary for their operation. Aou activate the `basic-scipy-env` environment by name using the `activate` command.

```
$ conda activate basic-scipy-env
```
You can see that an environment has been activated because the shell prompt will now include the name of the active environment.
```
(basic-scipy-env) $
```
## Deactivate the current environment

To deactivate the currently active environment use the conda `deactivate` command:.

```
(basic-scipy-env) $ conda deactivate
```

You can see that an environment has been deactivated because the shell prompt will no longer include the name of the previously active environment.

```
$
```
```ad-info
title: warning
collapse: closed
## Returning to the `base` environment[](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html#returning-to-the-base-environment)

To return to the `base` Conda environment, it’s better to call `conda activate` with no environment specified, rather than to use `deactivate`. If you run `conda deactivate` from your `base` environment, you may lose the ability to run `conda` commands at all.
```

 ```ad-question
title: Activate an existing env by name
collapse: closed
Activate the `machine-learning-env` environment created in the previous challenge by name.
```
```ad-success
title: Solution
collapse: closed
In order to activate the env by name use `conda activate` : 

`$ conda activate machine-learning-env`
```
 ```ad-question
title: Deactivate an existing env by name
collapse: closed
Deactivate the `machine-learning-env` environment created in the previous challenge by name.
```
```ad-success
title: Solution
collapse: closed
In order to deactivate the env by name use `conda deactivate` : 

(active-environment-name) $ conda deactivate

```

## Installing a package into an existing environment

You can install a package into an existing environment using the `conda install` command.

By default the `conda install` command will install packages into the current, active environment.

The following would activate the `basic-scipy-env` we created above and install [Numba](https://numba.pydata.org/)

```
$ conda activate basic-scipy-env
$ conda install numba
```
```ad-danger
title: Freezing installed packages
collapse: closed
To prevent existing packages from being updating when using the `conda install` command, you can use the `--freeze-installed` option. This may force Conda to install older versions of the requested packages in order to maintain compatibility with previously installed packages. Using the `--freeze-installed` option does not prevent additional dependency packages from being installed.
```

 ```ad-question
title: Installing a package into a specific env
collapse: closed
Have a read through the [official documentation](https://docs.conda.io/projects/conda/en/latest/commands/install.html) for the `conda install` command and see if you can figure out how to install **Dask** into the `machine-learning-env` that you created in the previous challenge.
```
```ad-success
title: Solution
collapse: closed
You can install DASK into the `machine-learning-env` using `conda install`:

`$ conda install --name machine-learning-env dask=2.16`

or by activating the `env`:

`$conda activate machine-learning-env`

`(machine-learning-env)$ conda install dask=2020.12`

```

## Where do Conda environments live ?

Environments created with `conda`, by default, live in the `envs/` folder of your `miniconda3` (or `anaconda3`) directory the absolute path to which will look something the following: `/Users/$USERNAME/miniconda3/envs` or `C:\Users\$USERNAME\Anaconda3`

Running `ls` (linux) / `dir` (Windows) on your anaconda `envs/` directory will list out the directories containing the existing Conda environments.

You can also use:
`$ conda env list`

## How do I specify a location for a Conda environments ?

You can control where a conda environment lives by providing a `path` to a target directory when creating the environment. 

For example to following command will create a new environment in a sub-directory of the current working directory called `env`.

```
$ conda create --prefix ./env ipython=7.13 matplotlib=3.1 pandas=1.0 python=3.6
```

You activate an environment created with a prefix using the same command used to activate environments created by name.

```
$ conda activate ./env
```

It is often a good idea to specify a path to a sub-directory of your project directory when creating an environment.

1. Makes it easy to tell if your project utilizes an isolated environment by including the environment as a sub-directory.
2. Makes your project more self-contained as everything _including the required software_ is contained in a single project directory.

An additional benefit of creating your project’s environment inside a sub-directory is that you can then use the same name for all your environments; if you keep all of your environments in your `~/miniconda3/env/` folder, you’ll have to give each of them a different name.

```ad-note
title: Conda environment sub-directory naming convention
collapse: closed
In order to be consistent with the convention used by tools such as `venv` and `Pipenv`, I recommend using `env` as the name of the sub-directory of your project directory that contains your Conda environment. A benefit of maintaining the convention is that your environment sub-directory will be automatically ignored by the default Python `.gitignore` file used on [GitHub](https://github.com/github/gitignore/blob/master/Python.gitignore).


Whatever naming convention you adopt it is important to be consistent! Using the same name for all of your Conda environments allows you to use the same `activate` command as well.


`$ cd my-project/`
`$ conda activate ./env`
```

 ```ad-question
title: Creating a new environment as a sub-directory within a project directory
collapse: closed
First create a project directory called `project-dir` using the following command.


`$ mkdir project-dir`
`$ cd project-dir`


Next, create a new environment inside the newly created `project-dir` in a sub-directory called `env` an install Python 3.6, version 3.1 of Matplotlib, and version 2.0 of [TensorFlow](https://www.tensorflow.org/).
```
```ad-success
title: Solution
collapse: closed

`project-dir $ conda create --prefix ./env \`

`python=3.6 \`

`matplotlib=3.1 \`

`tensorflow=2.0 \`
```

Placing Conda environments outside of the default `~/miniconda3/envs/` folder comes with a couple of minor drawbacks. 

First, `conda` can no longer find your environment with the `--name` flag; you’ll generally need to pass the `--prefix` flag along with the environment’s full path to find the environment.

Second, the command prompt is now prefixed with the active environment’s absolute path rather than the environment’s name

```
(/absolute/path/to/env) $
```

This can quickly get out of hand.

```
(/Users/USER_NAME/research/data_projects/PROJECT_NAME/env) $
```

There is a quick fix: modify the `env_prompt` setting in your `.condarc` file, which you can do with the following command.

```
$ conda config --set env_prompt '({name})'
```
This will either edit `~/.condarc` file or create a `~/.condarc` file if not found. The command prompt will display the active environment’s generic name.

```
$ cd project-directory
$ conda activate ./env
(env) project-directory $
```


 ```ad-question
title: Conda can create environments for R projects too
collapse: closed
First create a project directory called `r-project-dir` using the following command.


`$ cd ~/Desktop/conda_temp`

`$ mkdir r-project-dir`

`$ cd r-project-dir`

Next, take a look through the [list of R packages](https://anaconda.org/r/repo) available by default for installation using `conda`. Create a new environment inside the newly created `r-project-dir` in a sub-directory called `env` and install `r-base`, `r-tidyverse` and `r-sparklyr`.
```
```ad-success
title: Solution
collapse: closed
`project-dir $ conda create --prefix ./env \`

` r-base \`

` r-tidyverse \`

` r-sparklyr \`
```


## Listing existing environments

````
$ conda env list
````

## Listing the contents of an environment
To list the contents of the `basic-scipy-env` that you created above, run the following command.

````
$ conda list --name basic-scipy-env
````

If you created your Conda environment using the `--prefix` option to install packages into a particular directory, then you will need to use that prefix in order for `conda` to locate the environment on your machine.

```
$ conda list --prefix /path/to/conda-env
```

 ```ad-question
title: Listing the contents of a particular environment
collapse: closed
List the packages installed in the `machine-learning-env` environment that you created in a previous question.
```
```ad-success
title: Solution
collapse: closed
You can list the packages and their versions installed in machine-learning-env using the conda list command as follows.

`$ conda list --name machine-learning-env`

To list the packages and their versions installed in the active environment leave off the ``--name` or ``--prefix` option.

`$ conda list`
```

## Deleting entire environments

You may want to delete an entire environment. 

```
$ conda remove --name my-first-conda-env --all
```
If you wish to delete and environment that you created with a `--prefix` option, then you will need to provide the prefix again when removing the environment.
```
$ conda remove --prefix /path/to/conda-env/ --all
```

 ```ad-question
title: Delete an entire environment
collapse: closed
Delete the entire `basic-scipy-env` environment.
```
```ad-success
title: Solution
collapse: closed
In order to delete an entire environment you use the `conda remove` command.

`$ conda remove --name basic-scipy-env --all --yes`

This command will remove all packages from the named environment before removing the environment itself. The use of the `--yes` flag short-circuits the confirmation prompt (and should be used with caution).
```

```ad-info
title: Key points
collapse: closed
- A Conda environment is a directory that contains a specific collection of Conda packages that you have installed.
    
- You create (remove) a new environment using the `conda create` (`conda remove`) commands.
    
- You activate (deactivate) an environment using the `conda activate` (`conda deactivate`) commands.
    
- You install packages into environments using `conda install`; you install packages into an active environment using `pip install`.
    
- You should install each environment as a sub-directory inside its corresponding project directory
    
- Use the `conda env list` command to list existing environments and their respective locations.
    
- Use the `conda list` command to list all of the packages installed in an environment.
```

# If time
## What are Conda channels?

`conda` packages ([Conda documentation](https://conda.io/en/latest/)) are downloaded from remote channels, which are `URLs` to directories containing `conda` packages. The `conda` command searches a default set of channels, and packages are automatically downloaded and updated from the [Anaconda Cloud channels](https://repo.anaconda.com/pkgs/).

Anaconda managed channels are referred to as the `defaults` channel because, unless otherwise specified, packages installed using `conda` will be downloaded from these channels.

### The `conda-forge` channel
 There is another channel called that also has a special status. The [Conda-Forge](https://github.com/conda-forge) project “is a community led collection of recipes, build infrastructure and distributions for the conda package manager.”

There are a few reasons to use the `conda-forge` channel:

1. Packages on `conda-forge` may be more up-to-date.
2. There are packages on the `conda-forge` channel that aren’t available from `defaults`.

## How do I install a package from a specific channel

You can install a package from a specific channel into the currently activate environment by passing the `--channel` option to the `conda install` command.

```
$ conda activate machine-learning-env
$ conda install scipy=1.6 --channel conda-forge
```

You can also install a package from a specific channel into a named environment (using `--name`) or into an environment installed at a particular prefix (using `--prefix`). 

For example, the following command installs the `scipy` package from the `conda-forge` channel into the environment called `my-first-conda-env`.

```
$ conda install scipy=1.6 --channel conda-forge --name machine-learning-env
```

This command would install `tensorflow` package from `conda-forge` channel into an environment installed into the `env/` sub-directory.

```
$ conda install tensorflow=1.14 --channel conda-forge --prefix ./env
```

Here is another example for R users. The following command would install [`r-tidyverse`](https://anaconda.org/r/r-tidyverse) package from the `conda-forge` channel into an environment installed into the `env/` sub-directory.

```
$ cd ~/Desktop/conda_temp
$ conda install r-tidyverse=1.3 --channel conda-forge --prefix ./env
```
#### Channel priority

You may specify multiple channels for installing packages by passing the `--channel` argument multiple times.

```
$ conda install scipy=1.6 --channel conda-forge --channel bioconda
```

## My package isn’t available on the `defaults` channel! What should I do?

It may very well be the case that packages (or often more recent versions of packages!) that are needed for a project are not available on the `defaults` channel. Options

1. `conda-forge`: the `conda-forge` channel contains a large number of community curated conda packages. Typically the most recent versions of packages that are generally available via the `defaults` channel are available on `conda-forge` first.
2. `bioconda`: the `bioconda` channel also contains a large number of Bioinformatics curated conda packages. `bioconda` channel is meant to be used with `conda-forge`, you should not worried about using the two channels when installing your prefered packages.
3. `pip`: only if a package is not otherwise available via `conda-forge` (or some domain-specific channel like `bioconda`) should a package be installed into a conda environment from PyPI using `pip`.


## A Python package isn’t available on any Conda channel! What should I do?

Use the default Python package manager [Pip](https://pip.pypa.io/en/stable/) to install this package from [PyPI](https://pypi.org/). However, there are a few [potential issues](https://www.anaconda.com/blog/using-pip-in-a-conda-environment) that you should be aware of when using Pip to install Python packages when using Conda.

First, Pip is sometimes installed by default on operating systems where it is used to manage any Python packages needed by your OS. **You do not want to use this `pip` to install Python packages when using Conda environments.**

```
(base) $ conda deactivate
$ which python
/usr/bin/python
$ which pip # sometimes installed as pip3
/usr/bin/pip
```

Second, Pip is also included in the Miniconda installer where it is used to install and manage OS specific Python packages required to setup your base Conda environment. **You do not want to use this `pip` to install Python packages when using Conda environments.**

```
$ conda activate
(base) $ which python
~/miniconda3/bin/python
$ which pip
~/miniconda3/bin/pip
```


# Sharing Environments
- Why should I share my Conda environment with others?
- How do I share my Conda environment with others?
- How do I create a custom kernel for my Conda environments inside JupyterLab?

## Creating an environment file
In order to make sure that your environment is truly shareable, you need to make sure that that the contents of your environment are described in such a way that the resulting environment file can be used to re-create your environment on Linux, Mac OS, and Windows.

Conda uses YAML (“YAML Ain’t Markup Language”) for writing its environment files. YAML is a human-readable data-serialization language that is commonly used for configuration files and that uses Python-style indentation to indicate nesting.

Creating your project’s Conda environment from a single environment file is a Conda **best practice**. Not only do you have a file to share with collaborators but you also have a file that can be placed under version control which further enhancing the reproducibility of your research project and workflow.
### Default `environment.yml` file

 Note that by convention Conda environment files are called `environment.yml`. As such if you use the `conda env create` sub-command without passing the `--file` option, then `conda` will expect to find a file called `environment.yml` in the current working directory and will throw an error if a file with that name can not be found.

Example `environment.yml` files to give you an idea of how to structure them.

```
name: machine-learning-env

dependencies:
  - ipython
  - matplotlib
  - pandas
  - pip
  - python
  - scikit-learn
```

This `environment.yml` file would create an environment called `machine-learning-env` with the most current and mutually compatible versions of the listed packages (including all required dependencies). The newly created environment would be installed inside the `~/miniconda3/envs/` directory, unless we specified a different path using `--prefix`.

Since explicit versions numbers for all packages should be preferred a better environment file would be the following.

```
name: machine-learning-env

dependencies:
  - ipython=7.13
  - matplotlib=3.1
  - pandas=1.0
  - pip=20.0
  - python=3.6
  - scikit-learn=0.22
```

Note that we are only specifying the major and minor version numbers and not the patch or build numbers. Defining the version number by fixing only the major and minor version numbers while allowing the patch version number to vary allows us to use our environment file to update our environment to get any bug fixes whilst still maintaining significant consistency of our Conda environment across updates.

Let’s suppose that you want to use the `environment.yml` file defined above to create a Conda environment in a sub-directory of some project directory. Here is how you would accomplish this task.

```
$ cd ~/Desktop/conda_temp
$ mkdir project-dir
$ cd project-dir
```

Once your project folder is created, create `environment.yml` using your favourite editor for instance `nano`. Finally create a new conda environment:

```
$ conda env create --prefix ./env --file environment.yml
$ conda activate ./env
```

Note that the above sequence of commands assumes that the `environment.yml` file is stored within your `project-dir` directory.

## Automatically generate an `environment.yml`

To export the packages installed into the previously created `machine-learning-env` you can run the following command:

```
$ conda env export --name machine-learning-env 
```

When you run this command, you will see the resulting YAML formatted representation of your Conda environment streamed to the terminal. Recall that we only listed five packages when we originally created `machine-learning-env` yet from the output of the `conda env export` command we see that these five packages result in an environment with roughly 80 dependencies!

To export this list into an environment.yml file, you can use `--file` option to directly save the resulting YAML environment into a file.

```
$ conda env export --name machine-learning-env --file environment.yml
```

 ```ad-question
title: Create a new environment from a YAML file
collapse: closed
Create a new project directory and then create a new environment.yml file inside your project directory with the following contents.

name: scikit-learn-env

dependencies:
  - ipython=7.13
  - matplotlib=3.1
  - pandas=1.0
  - pip=20.0
  - python=3.6
  - scikit-learn=0.22
Now use this file to create a new Conda environment. Where is this new environment created? Using the same environment.yml file create a Conda environment as a sub-directory called env/ inside a newly created project directory. Compare the contents of the two environments.
```
```ad-success
title: Solution
collapse: closed
To create a new environment from a YAML file use the conda env create sub-command as follows.

`$ mkdir scikit-learn-project-dir`

`$ cd scikit-learn-project-dir`

`$ nano environment.yml`

`$ conda env create --file environment.yml`

The above sequence of commands will create a new Conda environment inside the ~/miniconda3/envs directory. In order to create the Conda environment inside a sub-directory of the project directory you need to pass the --prefix to the conda env create command as follows.

`$ conda env create --file environment.yml --prefix ./env`

You can now run the conda env list command and see that these two environments have been created in different locations but contain the same packages.
```






(inspired from the [Carpentries for DS]([Introduction to Conda for (Data) Scientists (carpentries-incubator.github.io)](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)))
