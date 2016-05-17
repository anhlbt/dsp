# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. `pushd` : create a directory, add it to the stack, and then go there
2. `popd` : go to the next directory on the stack
3. Pipe commands: output to command `|`, output to file `>`, input from file `<`, and append to file `>>`
4. Wildcards: all/any `*` and single character `?`
5. Find a file in current directory that matches given criteria: `find . -name '*.txt'` (I love find)
6. Search for text in a file and print matching lines plus two lines before and one after: `grep -B 2 -A 1 some_file 'my cat'`
7. Suggest manual pages for the word apropos: `apropos apropos`
8. Apply command to each line of input: `xargs` (I love xargs)
9. View contents of large files: `less `, `more some_file`, and the related `cat some_file`
10. List all environment variables (useful when debugging software installation): `env`

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 1. `ls`  : list directory contents
2. `ls -a`  : list *all* files, including invisible files whose name begins with "."
3. `ls -l`  : list files in long format, which includes additional data columns such as size, date modified, permissions
4. `ls -lh`  : list files in long format and use sensible units for respective file sizes
5. `ls -lah`  : list all files in long format with sensible units for file size
6. `ls -t`  : list files and sort by time modified
7. `ls -Glp` : list files in colorized, long format and print a slash after directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 1. `ls -ltr` : list files in long format sorted by reverse time modification (I used this all the time)
2. `ls -R`  : list files and recurse directories
3. `ls -x`  : display files as rows
4. `ls -1`  : display files as a single column
5. `ls -m`  : display files as a comma separated list


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` applies a command to every line of a given input pipe. One common way I use `xargs` is to search for a programming command in a given type of files. This example searches for the pivot_table command in  Jupyter notebooks: `find . -name '*.ipynb' | xargs grep 'pivot_table'

 

