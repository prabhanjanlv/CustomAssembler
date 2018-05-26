import sys			#library used to take/give a file as input/output(sys.argv)
import struct		#library used to convert and generate binary output

inputfile = sys.argv[1]	#input filename
ofile = inputfile.split(".")
outputfilep = ofile[0]+".psd"  #output filename for hexadecimal code
outputfileo = ofile[0]+".o"	   #output filename for object code(binary code)

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def convertline(parm,ocode):	#function call 
	
	ins = parm.split(" ")	#split the instruction to seperate the function and operands
	operator = ins[0]	#operator will contain function
	inst = ins[1]	#Rest of the instruction without operator will be stored in inst	
	
	if (operator == 'add') or (operator == 'sub') or (operator == 'slt') or (operator == 'and') or (operator == 'nor'): #R-Type instructions are handled here
		binins = 00000000000	#Combination of function and Shamt for R-Type
		operands = inst.split(",") #split the instruction to seperate the operands
		rd = operands[0][1:]	#decimal values of registers
		rs = operands[1][1:]
		rt = operands[2][1:]
		brd = bin(int(rd))[2:].zfill(5)	#Binary values of registers
		brs = bin(int(rs))[2:].zfill(5)
		brt = bin(int(rt))[2:].zfill(5)
		if operator == 'add':		#opcode for different functions of R-Type
			opc = bin(10)[2:].zfill(6)
		
		elif operator == 'sub':
			opc = bin(20)[2:].zfill(6)
		
		elif operator == 'slt':
			opc = bin(30)[2:].zfill(6)

		elif operator == 'and':
			opc = bin(40)[2:].zfill(6)
		
		elif operator == 'nor':
			opc = bin(50)[2:].zfill(6)
	
		Interba = str(binins) + str(brd) + str(brs) + str(brt) + str(opc)	#Binary value of the assembly instruction
		Interb1 = Interba.zfill(32)	#Binary value of assembly instruction in 32 bits
	
		ocode.append(Interb1)
		
		decimal = int(Interb1, 2)	#decimal equivalent of the binary
		
		Interh = hex(decimal)[2:].zfill(8)	#Hexadecimal value of the assembly instruction
		Hexa = '0x'+Interh.upper() #Hexadecimal value of the assembly instruction in Upper case
		
		out = open(outputfilep, "a")	#output file to open for hexadecimal
		out.write(Hexa + "\n")	#output file to write for hexadecimal
		
	elif (operator == 'lwd') or (operator == 'swd'):	#I-Type Instructions lwd and swd
		
		offset_start = inst.split(",")
		offset_end = offset_start[1].split("(")
		offset = offset_end[0]	#Offset value of the instruction in decimal
		
		rt = offset_start[0][1:]	#register values
		rtinter = offset_end[1].split(")")
		rs = rtinter[0][1:]
				
		if operator == 'lwd':		#Opcode value for I-Type lwd and swd
			opc = bin(35)[2:].zfill(6)		
		elif operator == 'swd':
			opc = bin(43)[2:].zfill(6)			
		boffset = bin(int(offset))[2:].zfill(16)	#offset for I-type Binary
		brs = bin(int(rs))[2:].zfill(5)	#RS registers
		brt = bin(int(rt))[2:].zfill(5)	#RT registers
		
		Interbb = str(boffset) + str(brs) + str(brt) + str(opc) #Binary value of the assembly instruction
		Interb2 = Interbb.zfill(32)	#Binary value of assembly instruction in 32 bits
		
		ocode.append(Interb2)
		
		decimal = int(Interb2, 2)	#decimal equivalent of the binary		
		
		Interh = hex(decimal)[2:].zfill(8)	#Hexadecimal value of the assembly instruction
		Hexa = '0x'+Interh.upper()	#Hexadecimal value of the assembly instruction in Upper case
		
		out = open(outputfilep, "a")	#output file to open for hexadecimal
		out.write(Hexa + "\n")	#output file to write for hexadecimal
	
	elif (operator == 'beq'):			#I-Type Instruction beq
		operands = inst.split(",")	
		rt = operands[0][1:]	#get register values in decimal
		rs = operands[1][1:]
		offset = operands[2]
		
		brt = bin(int(rt))[2:].zfill(5)	#get values in binary
		brs = bin(int(rs))[2:].zfill(5)
		boffset = bin(int(offset))[2:].zfill(16)
		opc = bin(4)[2:].zfill(6)

		Interbc = str(boffset) + str(brs) + str(brt) + str(opc)	#Binary value of the assembly instruction
		Interb3 = Interbc.zfill(32)	#Binary value of assembly instruction in 32 bits
		
		ocode.append(Interb3)
		
		decimal = int(Interb3, 2)	#decimal equivalent of the binary
		
		Interh = hex(decimal)[2:].zfill(8)		#Hexadecimal value of the assembly instruction	
		Hexa = '0x'+Interh.upper()	#Hexadecimal value of the assembly instruction in Upper case
		
		out = open(outputfilep, "a")	#output file to open for hexadecimal
		out.write(Hexa + "\n")	#output file to write for hexadecimal
		
	elif(operator == 'j'):	#J-Type Instruction jump
		offset = (int(inst))/4.0	#generate the offset which can be used in Opcode later
		address = bin(int(offset))[2:].zfill(26)	#address of jump location in binary
		opc = bin(2)[2:].zfill(6)	#opcode for jump 2
	
		Interbd = str(address) + str(opc)	#Binary value of the assembly instruction
		Interb4 = Interbd.zfill(32)	#Binary value of assembly instruction in 32 bits
		
		ocode.append(Interb4)
		
		decimal = int(Interb4, 2)	#decimal equivalent of the binary
		
		Interh = hex(decimal)[2:].zfill(8)	#Hexadecimal value of the assembly instruction
		Hexa = '0x'+Interh.upper()	#Hexadecimal value of the assembly instruction in Upper case
		
		out = open(outputfilep, "a")	#output file to open for hexadecimal
		out.write(Hexa + "\n")	#output file to write for hexadecimal
		
print"\nExecution complete\n"
print"The output Hexadecimal code is stored in file","'",outputfilep,"'","available in current working directory\n"
print"The output binary code is stored in file","'",outputfileo,"'","available in current working directory\n"
		
infile = open(inputfile, "r")	#inputfile to read from input argument
lines = infile.read().strip().split("\n")	#Extract each instruction from file
infile.close()	#close the input file


leng = len(lines)
i = 0
ocode = []
while i<leng:
	convertline(lines[i],ocode)	#function call
	i += 1

objectcode = ''.join(ocode)

objectfile = bitstring_to_bytes(objectcode)
out = open(outputfileo, "a")	#output file to open for binary
out.write(objectfile)	#output file to write for binary
