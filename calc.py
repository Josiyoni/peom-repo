def add(x,y):
	x=x+y	
	return x+y
def sub(x,y):
	return x-y
def mult(x,y):
	return x*y
def div(x,y):
	if y==0:
		raise ValueError("can't divide by zelo")
	else:
		return x/y

def main():
	print(add(4,5))
	print(sub(5,3))
if __name__=='__main__':
	main()
