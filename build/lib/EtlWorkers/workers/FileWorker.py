import time, uuid
from functools import wraps


def timer(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		start_point = time.time()
		results = func(*args,**kwargs)
		run_time = time.time() - start_point
		print("Func: {}, Runtime is:  {}".format(func.__name__,run_time))
		return results
	return wrapper

@timer
def end_lines_with_comma(file_path:str):
	"""Read a file as lines, add a comma to the end of each line, save it to a new file.

	Args:
		file_path (str): The source file destination and name
	
	Returns:
		new .txt file with a uuid4 name
	"""
	new_file_name = str(uuid.uuid4()) + '.txt'
	with open(file_path) as src_file:
		with open(new_file_name,'w') as dest_file:
			for line in src_file:
				dest_file.write(str(line.strip('\n')+','+'\n'))
