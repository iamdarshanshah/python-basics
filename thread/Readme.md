## How to create thread and start

### Using a function

```buildoutcfg
# Using Thread class
t = Thread(target=functionName, args)
t.start() # Starting the thread
```

### Extending Thread class
```buildoutcfg
class Mythread(Thread):
    override the run()
    
t.start()
```

### Without extending Thread class
```buildoutcfg
class MyThread:
    display()

t = Thread(target = mythread.display, args)
t.start()
```