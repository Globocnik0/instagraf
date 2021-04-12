# Instagraf
A web page that makes graphs from uploaded files, puts different fits on them and then it stores them.

# Setup

The required python modules are:

bottle

scipy

pandas

numpy

matplotlib

Make sure you have them installed (if not run `pip install numpy` or `sudo pip install numpy` and change name `numpy` to the missing module).

To start program move to root and run `python3 web_server.py`.
Older python releases may not work properly.

# Accepted file types

Only file extensions accepted by Instagraf are .txt, .csv and .xlsx. 

Data should be written in first two columns without any headers in the first row.

Examples of upload files can be seen in the example_upload_files folder.


# Sources
* web_server.py is built with the help of [Bottle documentation](https://bottlepy.org/docs/dev/)
* website design is made with [Bootstrap](https://getbootstrap.com/)
* source of Instagraph's icon was [this website](https://www.obfuscata.com/how-to-make-a-line-graph-7899.html) 
* A grave help was also doc. dr. Matija Pretnar Bottle course at FMF and people citing Bottle documentation on Stack Overflow.

# Possible future extensions
* Display fit parameters
* User can set colors and sytles of lines or points
* Different types of graphs
* User can add functions to the graphs


Project at elective class Računalništvo, 2. letnik, FMF UL.