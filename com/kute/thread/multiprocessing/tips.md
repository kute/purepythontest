1. 父进程与子进程之间通信, 使用pool时须得使用 `multiprocessing.Manager().Queue()`, 其他情况则可以直接使用 `multiprocessing.Queue()`
2. 父进程启动子进程的方式
- spawn: 子进程不会全部继承父进程的资源,仅会继承运行是必要的资源,相较于其他启动方式 较慢
- fork : 子进程将会全部继承父进程的资源
- forkserver: 将会启动 `服务器进程`, 此后每次都会 fork一个新进程,单线程,线程安全, 非必须资源不会继承
- 使用 `multiprocessing.getContext().set_start_method('fork')`设置
3. 进程间数据交换
- `multiprocessing.Queue()`
- `multiprocessing.Pipe()`
4. 进程间共享状态
- `shared-memory`: 使用`multiprocessing.Value`或者`multiprocessing.Array`
- `Server-process`: 即使用`multiprocessing.Manager()`, 推荐使用, 支持较多类型,可被处于同一网络的其他计算机共享, 比shared-memory较慢



https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming