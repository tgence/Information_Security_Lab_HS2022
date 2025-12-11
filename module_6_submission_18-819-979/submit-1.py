import os
import subprocess
import time

def main():
    ##########
    # FLAG 1 #
    ##########
    os.chdir("/home/isl/t1")
    os.system("/home/isl/t1/run.sh")
    os.system("kill -9 $(lsof -t -i:5111)")
    process_gdb = subprocess.Popen(["gdb", "python3"], stdin=subprocess.PIPE)

    process_gdb.stdin.write(b"set breakpoint pending on\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"b gcm_crypt_and_tag\n") 
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"run sp_server.py\n")
    process_gdb.stdin.flush()
    time.sleep(3)
    subprocess.Popen(["sh", "/home/isl/t1/start.sh"])
    time.sleep(3)
    process_gdb.stdin.write(b"c\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b'set variable input="<mes><action type=\\"key-update\\"/></mes>"\n')
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"c\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"q\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.close()
    time.sleep(5)
    process_gdb.terminate()

    ##########
    # FLAG 2 #
    ##########

    os.system("/home/isl/t1/run.sh")
    os.system("kill -9 $(lsof -t -i:5111)")

    process_gdb = subprocess.Popen(["gdb", "python3"], stdin=subprocess.PIPE)
    process_gdb.stdin.write(b"set breakpoint pending on\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"b gcm_setkey\n") 
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"run sp_server.py\n")
    process_gdb.stdin.flush()
    time.sleep(3)    
    subprocess.Popen(["sh", "/home/isl/t1/start.sh"])
    time.sleep(3)
    process_gdb.stdin.write(b"c\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b'set variable redirectAdmin=0x7d316c\n')
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b'b *stringParser+0x677\n')
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"c\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b'set $rax=redeemer[3]\n')
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b'b *stringParser+0x697\n')
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"c\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b'set $al=0xff\n')
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"c\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.write(b"q\n")
    process_gdb.stdin.flush()
    process_gdb.stdin.close()
    time.sleep(5)
    process_gdb.terminate()


main()







