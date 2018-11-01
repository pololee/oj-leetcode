http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=215056 


6 File System
Write a file system class, which has two functions: create, and get

create("/a",1)
get("/a") //get 1
create("/a/b",2)
get("/a/b") //get 2
create("/c/d",1) //Error, because "/c" is not existed
get("/c") //Error, because "/c" is not existed


follow up 是写一个 watch 函数，比如 watch("/a",new Runnable(){System.out.println("helloword");}) 后，每当 create("/a/b"，1) 等在/a 之下的目录不产生 error 的话，都会执行绑在“/a”上的 callback 函数
比如 watch("/a",System.out.println("yes")) watch("/a/b",System.out.println("no"))
