import re
from gradelib import *

r = Runner(save("xv6.out"))

@test(1, "find, in current directory")
def test_find_curdir():
    fn = random_str()
    r.run_qemu(shell_script([
        'echo > %s' % fn,
        'find . %s' % fn
    ]))
    r.match('./%s' % fn)
    
@test(1,"find same name file")
def test_find_curdir():
    directory_1_name = random_str()
    directory_2_name = random_str()
    file_name = random_str()
    r.run_qemu(shell_script([
        'mkdir %s' % directory_1_name,
        'echo > %s/%s' % (directory_1_name,file_name),
        'mkdir %s' % directory_2_name,
        'echo > %s/%s' % (directory_2_name,file_name),
        'find . %s' % file_name
    ]))    
    r.match('./%s/%s' % (directory_1_name, file_name),
            './%s/%s' % (directory_2_name, file_name))
 
 
    
@test(1, "find, recursive")
def test_find_recursive():
    needle = random_str()
    dirs = [random_str() for _ in range(3)]
    r.run_qemu(shell_script([
        'mkdir %s' % dirs[0],
        'echo > %s/%s' % (dirs[0], needle),
        'mkdir %s/%s' % (dirs[0], dirs[1]),
        'echo > %s/%s/%s' % (dirs[0], dirs[1], needle),
        'mkdir %s' % dirs[2],
        'echo > %s/%s' % (dirs[2], needle),
        'find . %s' % needle
    ]))
    r.match('./%s/%s' % (dirs[0], needle),
            './%s/%s/%s' % (dirs[0], dirs[1], needle),
            './%s/%s' % (dirs[2], needle))   
    
@test(1,"no matching file")
def test_no_matching():
    r.run_qemu(shell_script(["find . there_is_no_file"]))
    r.match(no=["there_is_no_file"])
    

 
    
run_tests()     