## ETL Workers 
It is my way to express my love for python and my life passion for data science in general and explicitly for data engineering.

### About the package name:
I named it after the famous data-engineering pipeline approach: Extract, Transform, and Load.
<hr>

### About the idea and package structure
It will contain multiple worker classes, And Each worker will fulfill certain data operations segmented by type. 

For example, now it contains one worker called FileWorker, And it is performing file-related operations.

In the future, I will add more workers and more functions per worker. So it can perform complex operations under any applicable built with python.

<hr>

### How to install & use
``` 
# In your terminal
pip install EtlWorkers

# In your python application
import EtlWorkers as ew
my_file = ew.workers.FileWorker('file_location_and_name.csv')
my_file.replace_a_word_in_each_line('old_word','new_word')
```

