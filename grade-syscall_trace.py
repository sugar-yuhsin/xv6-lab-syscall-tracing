import re
from gradelib import *

r = Runner(save("xv6.out"))


@test(1, "strace echo test")
def test_strace_echo():
    r.run_qemu(shell_script(["strace echo hello"]))
    r.match(r'\[pid \d+\] exec\("echo"\) = \d+')
    r.match(r'\[pid \d+\] write\(1\) = 5')
    r.match(r'\[pid \d+\] write\(1\) = 1')  

    
@test(2, "mkdir and rm test")
def test_mkdir_rm():
    fn = random_str()
    r.run_qemu(shell_script(["strace mkdir %s" % fn,"strace rm %s" % fn]))
    r.match(r'\[pid \d+\] exec\("mkdir"\) = \d+')
    r.match(r'\[pid \d+\] mkdir\(\"%s\"\) = 0' % fn)    
    r.match(r'\[pid \d+\] exec\("rm"\) = \d+')
    r.match(r'\[pid \d+\] unlink\(\"%s\"\) = 0' % fn)
    
@test(3, "grep test")
def test_grep():
    r.run_qemu(shell_script(["strace grep hello README"]))
    r.match(r'\[pid \d+\] exec\("grep"\) = \d+')
    r.match(r'\[pid \d+\] open\("README"\) = \d+')
    r.match(r'\[pid \d+\] read\(\d+\) = 1023')
    r.match(r'\[pid \d+\] read\(\d+\) = 971')
    r.match(r'\[pid \d+\] read\(\d+\) = 298')
    r.match(r'\[pid \d+\] read\(\d+\) = 0')
    r.match(r'\[pid \d+\] close\(\d+\) = 0')    
    
@test(4, "trace nothing")
def test_trace_nothing():
    r.run_qemu(shell_script([
        'grep hello README'
    ]))
    r.match(no=[".* syscall .*"])
    

@test(5, "strace exec fail")
def test_strace_exec_fail():
    r.run_qemu(shell_script([
        "strace not_a_command"
    ]))
    r.match(r'\[pid \d+\] exec\("not_a_command"\) = -1')

@test(6, "echo and mkdir test")
def test_find_curdir():
    directory_name = random_str()
    sub_directory_name = random_str()
    file_name = random_str()
    r.run_qemu(shell_script([
        'strace mkdir %s' % directory_name,
        'strace echo > %s/%s' % (directory_name,file_name),
        'strace mkdir %s/%s' % (directory_name,sub_directory_name),
        'strace echo > %s/%s/%s' % (directory_name,sub_directory_name,file_name),
    ]))
    
    r.match(r'\[pid \d+\] exec\("mkdir"\) = \d+')
    r.match(r'\[pid \d+\] mkdir\(\"%s\"\) = 0' % directory_name)
    r.match(r'\[pid \d+\] exec\("echo"\) = \d+')
    r.match(r'\[pid \d+\] exec\("mkdir"\) = \d+')
    r.match(r'\[pid \d+\] mkdir\(\"%s/%s\"\) = 0' % (directory_name,sub_directory_name))
    r.match(r'\[pid \d+\] exec\("echo"\) = \d+')


run_tests()
