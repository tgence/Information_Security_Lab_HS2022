import sys
import os

def password_cracker(complete, validated_ones):
	pass_cracked = ""
	for i in range(1, max(validated_ones.keys()) + 1):
		if i in validated_ones:
			pass_cracked += validated_ones[i]
		else:
			complete = False
			pass_cracked += "_"
	pass_cracked += ",complete" if complete else ",partial"
	return pass_cracked

def exploit_2_1():
	valid_ones = {}
	length_of_pwd = 0
	
	for T in os.listdir(sys.argv[1]):
		char_pointer = 0
		magnitude = 0		
		g = False
		dir = sys.argv[1]+"/"+ T
	
		with open(dir) as binary:
			for cmd in binary:
				if "0x401292" in cmd:
					if magnitude > 0:
							if g:
								valid_ones[char_pointer] = chr(((ord(T[char_pointer - 1]) - ord('a') + magnitude - 1) % 26) + ord('a'))	
							else:	
								valid_ones[char_pointer] = chr(ord(T[char_pointer - 1]) + magnitude - 1)
					magnitude = 0
					g = False					
					char_pointer += 1
				if "0x40126f" in cmd:
					g = True
				if "0x401286" in cmd:
					magnitude += 1
				if "0x401211" in cmd:
					valid_ones[char_pointer] = T[char_pointer - 1]

	complete = length_of_pwd != -1
	os.makedirs(os.path.dirname(f"/home/isl/t2_1/output/oput_{sys.argv[2]}"), exist_ok=True)
	file_of_output = open(f"/home/isl/t2_1/output/oput_{sys.argv[2]}", 'w')
	file_of_output.write(password_cracker(complete, valid_ones))
	file_of_output.close()

if __name__ == "__main__":
	exploit_2_1()
