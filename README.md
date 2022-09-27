# prjman
when you hear the word *project manager* (i know it's not a word) you probably think of something like *[notion](https://notion.so/)* or *[trello](https://trello.com/)* or *[asana](https://asana.com/)*.
well this is nothing like them. i only named it this because i didn't had any other idea. i wrote this for myself to use and i have no idea if there is any better program like this out there. if i knew one i most likely wouldn't even start writing this but since i have no idea what this things are called i just didn't bothered to look and wrote this program.

what project in this program means is essentially  any directory that has code inside of it.

another thing that might be confusing about this program is that it has the word *manager* in it but it really doesn't manage anything.
all it does is gets one or multiple paths from you, makes a directory tree out of them, with a weird approach decides if it's a project directory or not and shows them with *[fzf](https://github.com/junegunn/fzf)*. and when you select one it just goes to that path and automatically opens your selected editor in that directory (or not).
so yeah call me lazy but i didn't had any other name for it and it really wasn't made to be on github i just put it here because i have too many private repositories and i wanted one to be public.
## Install
if you read what i wrote above and still decided to install this i don't know what to say to you.
### Requirements
 - fzf

other than the python packages that it uses (which will install automatically if you follow the instructions below) it only uses *fzf*. so figure out how you can install *fzf* from [fzf's github repository](https://github.com/junegunn/fzf).

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

