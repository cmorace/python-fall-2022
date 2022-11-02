# python-fall-2022

google meet link: [https://meet.google.com/zog-qgxm-dda](https://meet.google.com/zog-qgxm-dda)

![time](images/time.png)

install and/or update pycat

```
pip install git+https://bitbucket.org/dwhite0/pycat.git -U
```

clone pycat repo (optional)

```
git clone git@bitbucket.org:dwhite0/pycat.git
```

--------

## Lesson 1: 2022-10-30

1. Discuss the future of our class
    
    a. Independent Project-Based (self-directed) vs. Planned Lesson (teacher-led)
    
    b. More APCS practice/homework?
    
    c. New directions? C/C++, Unity, Web Programming, 3D Graphics, Computer Vision, Machine Learning, Visualization, Operating Systems/Multi-threading/interprocess-communication, etc.

2. Today's lesson

    a. Look at new pycat projects

    - Asteroids

    - GeoGuesser

    - Animal Crossings
    
    b. Choose a project and start working on it

3. Tests

    - pycat test

        ``` python
        from pycat.core import Window
        w = Window()
        w.run()
        ```

    - download assets from a markdown source with Github pages
       [asteriods.zip](https://github.com/cmorace/python-fall-2022/raw/main/asteriods.zip)

### Discussion

1. Start with planned lessons
    
    - Add some C programming

    - Add some multiprocess lessons (server/client). Maybe turn Asteroids into a remote two-player game?

    - Add some Linux (Feng-Jun)

2. Do an independent project

3. Continue some APCS (more APCS content closer to the next test date 2023-01-08)

### Homework (choose one)

1. Look at the most recent APCS problems [https://yuihuang.com/apcs/](https://yuihuang.com/apcs/). Then, work on the solutions and submit them to ZeroJudge. Review questions next class.

2. Continue working on your current Asteroids game.

3. Research/Design a two-player asteroid game.

    a. Two computers with different IP addresses (two clients). One server synchronizes data between the two clients. Therefore, we need two programs, one for the client and another for the server.

    b. Draw a diagram with the clients and server. What messages need to be sent and received for the game to work?

    c. Draw one state-transition diagram for the server application and another for the client applications.

    d. Explain your diagrams in the next class.

    e. Research what python functions can send/receive data between multiple processes?

----

## Lesson 1: 2022-10-30

### A mini Unix Shell lesson

create a file with `touch`

delete a file with `rm`

create a directory with `mkdir`

navigate the filesystem with `cd`

print the working directory with `pwd`

show the contents of a file with `cat`, `head`, and `tail`

show the contents of a directory with `ls`

how to use `help` and `man`

# A mini C lesson