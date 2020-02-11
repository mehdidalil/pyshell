from parseLine import parseLine
from Exec import Exec
from Builtin import Builtin
from echo import echo

def main():
	while True:
		tab = parseLine("pyshell -> ")
		proc = Builtin(tab)
		ret = proc.run()
		if ret == None:
			proc = Exec(tab)
			ret = proc.run()

if __name__ == "__main__":
	main()