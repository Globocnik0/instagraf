# Instagraf
A web page that makes graphs from uploaded files and puts different fits on them.
User must first register in order to save uploaded files to his account, later he can download his graphs by clicking on them. 
In order to save precious storage only uploaded files are stored on server while graphs are deleted and produced on command from saved data.

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

# Fitting 

User can choose to fit functions to uploaded data. Current available functions are:

* Linear fit
* Quadratic fit
* Cubic fit
* Exponential fit
* Logarithmic fit

# Accepted file types

Instagraf can accept multiple file extensions as .txt, .xlsx and .csv (with ; as separator). 

Data should be written in first two columns without any headers in the first row.

Examples of upload files can be seen in the database/uploaded_files folder. They belong to user "ales" as it can be seen in database/accounts.json.


# Sources
* web_server.py is built with the help of [Bottle documentation](https://bottlepy.org/docs/dev/)
* website design is made with [Bootstrap](https://getbootstrap.com/)
* source of Instagraph's icon was [this website](https://www.obfuscata.com/how-to-make-a-line-graph-7899.html) 
* A grave help was also doc. dr. Matija Pretnar Bottle course at FMF and people citing Bottle documentation on Stack Overflow.

# Possible future extensions
* Displaying errorbars on graphs
* Displaying fit parameters
* User can set colors and sytles of lines or points
* Different types of graphs
* User can add functions to the graphs or manually edit data
* Checking whether graph is already made and not remaking it for a faster web page


Project at elective class Računalništvo, 2. letnik, FMF UL.