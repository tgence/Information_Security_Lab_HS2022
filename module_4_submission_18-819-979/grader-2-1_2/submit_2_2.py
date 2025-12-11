import sys
import os

def password_cracker(validated_ones):
	pass_cracked = ""
	for i in range(1, max(validated_ones.keys()) + 1):
		pass_cracked += validated_ones[i]
	pass_cracked += ",complete"
	return pass_cracked

def exploit_2_2():
	valid_ones = {}
	for character in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
		os.makedirs(os.path.dirname(f"/home/isl/t2_2/samples/traces/trace_{character}"), exist_ok=True)
		os.system(f"/home/isl/pin-3.11-97998-g7ecce2dac-gcc-linux-master/pin -t /home/isl/pin-3.11-97998-g7ecce2dac-gcc-linux-master/source/tools/SGXTrace/obj-intel64/SGXTrace.so -o /home/isl/t2_2/samples/traces/trace_{character} -trace 1 -- /home/isl/t2_2/password_checker_2  {character * 31}")			
		
		char_pointer = 0
		with open(f"/home/isl/t2_2/samples/traces/trace_{character}") as binary:
			for cmd in binary:
				if "0x401d97" in cmd:
					char_pointer += 1
				if "0x401d83" in cmd:
					valid_ones[char_pointer] = character	

	os.makedirs(os.path.dirname(f"/home/isl/t2_2/output/oput_{sys.argv[1]}"), exist_ok=True)
	file_of_output = open(f"/home/isl/t2_2/output/oput_{sys.argv[1]}", 'w')
	file_of_output.write(password_cracker(valid_ones))
	file_of_output.close()


if __name__ == "__main__":
	exploit_2_2()