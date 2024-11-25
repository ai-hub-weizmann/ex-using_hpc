# ex-using_hpc
Learn to rewrite your python code for submission as a job, and use a linux-based HPC


# Introduction
## Overview
In this tutorial we will learn how to fully utilize the resources available to us, be it a personal computer (PC) or a high-performance computiong cluster (HPC) to facilitate our AI (and generally computer-related) research. We will do this by leaving behind the jupyter notebook in favour of the python scripts, and delving into the world of the command-line interfaces.

## So what's wrong with notebooks?
Notebooks are a great tool for fast prototyping, testing, and exploring your data, but they are also very slow and inefficient in executing code.
When we train an AI model, but also when we infer from it, the speed of execution may become a substantial bottleneck. There are many ways of optimizing the performance of any code, but the first and probably easiest is to transfer the code into the form of python scripts (or python modules).
Scripts have many benefits. Not only do they run faster than notebooks, they also allow us to reuse pieces of code thus reducing the amount of code we actually have to write and rewrite.
Unlike notebooks, scripts execute in a linear manner – from the top of the file to the bottom of it. 
This often results in less bugs and errors during runtime, since we can’t “jump back” and rerun a cell after changing some variable in a later cell.
On the other hand, scripts also have some drawbacks. 
They are less “comfortable” as they are not interactive (in general), they take more time to run, and debugging them is usually more time-consuming.
The best approach, usually, is using a mixture of the two:
Notebooks should be used at first to play with the code, explore the data, and test algorithms.
When your project runs into “production mode” – when you have to train your model or analyze a large dataset, the code should be migrated to script form and be used from there.

## OK, but what will we do?
The tutorial is divided into multiple chapters. Most chapters can be done independently of previous chapters, but for the most in-depth understanding it is recommendedto follow the tutorial from start to finish.
1. **Chapter 1 - Writing Python scripts**
    In this chapter we will learn how to write and run a python script.
    We will rewrite and run the KNN tutorial in the form of a script.

2. **Chapter 2 - Introduction to the linux command line**
    We will learn about the linux command line, how to navigate our file system without a graphical user intervace, and some other useful written commands.

3. **Chapter 3 - Basic Bash**
    We will learn to write simple bash scripts to automate some of the work for us. This will be very important when submitting jobs to the HPC later.

3. **Chapter 4 - HPC theory and application**
    On the theoretical side, we will learn what is an HPC, how it is built, what is the meaning of the different elements of it's architecture, and also why we care about all of this.
    We will learn about resource management and the scheduler, together with some common good practices.
    Then on to the practical side 

4. **Chapter 5 - Advanced python scripting**
    We will learn to create, define, and use our own python environment. ***- Under construction***

5. **Dealing with errors**
    It is inevitable that while writing, training, or using any python code (sometimes many) errors and warning messages will pop up.
    We will, therefore, try to see and deal with as many common errors and wornings as possible.
    This is not a chapter in itself, because we will encounter, and deal with, these errors throughout the whole tutorial.
    Our main goal in this respect is to familiarize with pythons errors, and see them as friends instead of foes.

#### A note
The goal of this tutorial is not to learn the best practices of writing python code (even though we will try to write good and readable code), but rather to have a simple yet instructing hands-on example of how to break free of the jupyter notebook, as well as utilizing high-performance computing resources.
For a better, in-depth, tutorial on writing good python and packagin your code see [this tutorial on coding practices](https://github.com/ai-hub-weizmann/ex-coding-practices/tree/master).