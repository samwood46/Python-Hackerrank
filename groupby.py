
def group_by_owners(files):
	result = {}
	for file, owner in files.items():  # use files.iteritems() on Python 2.x
	    print(file)

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    group_by_owners(files)