## Usage

First, import the `FileSystem` class from the `filesystem` module:

```python
from filesystem import FileSystem

# Instantiate the FileSystem
fs = FileSystem()

<!-- # Create a new directory named 'project'
fs.mkdir('project')

# Change to the 'project' directory
fs.cd('project')

# Create a new README.md file and write some content to it
fs.touch('README.md')
fs.echo('# My Project\n\nThis is a sample README file.', 'README.md')

# List the contents of the current directory to verify
fs.ls()

# Save the file system state to a JSON file (optional)
fs.save_state('filesystem_state.json') -->
# Creates a new directory named 'test'
fs.mkdir('test') 

 # Changes the current directory to 'test'
fs.cd('test') 

# Creates a new file named 'file.txt'
fs.touch('file.txt')  

# Writes 'Hello, world!' to 'file.txt'
fs.echo('Hello, world!', 'file.txt')  

# Displays the contents of 'file.txt'
fs.cat('file.txt')  

 # Renames 'file.txt' to 'new_file.txt'
fs.mv('file.txt', 'new_file.txt') 

# Creates a copy of 'new_file.txt' named 'copy.txt'
fs.cp('new_file.txt', 'copy.txt')  

# Removes 'copy.txt'
fs.rm('copy.txt')  

# Searches for 'world' in 'new_file.txt'
fs.grep('world', 'new_file.txt')

# Saves the current state to 'state.json'  
fs.save_state('state.json')  

# Loads the state from 'state.json'
fs.load_state('state.json')  
```

## Testing 
python test.py
