# prjman
a project viewer
## Install
**this program only works on linux.**
```
python configure.py && ./install.sh | source /dev/stdin
```
now just run
```
prjman
```
to configure the default editor and the paths to search for projects.
## Uninstall
```
./uninstall.sh
```
## Note
when adding a alias for the program i recommend to alias the `projman` instead of `prjman`.\
the program needs a function in order to work properly.
the problem comes when you have a alias and a function both with the same name, you have to define the function first and the alias second. that is okay if it's the first time that you are adding the alias but when you have made a change and for example you run 
```
source ~/.bashrc
``` 
the alias is already set from before and when the function is defined first you get errors like:
```
.bashrc:3: defining function based on alias `something'
.bashrc:3: parse error near `()'
```
### example
```
alias prjman="prjman --exclude-dir something" # Don't do this
alias projman="projman --exclude-dir something" # Do this instead
```
**this will not make any difference on the command that you need to use which is:**
```
prjman
```
