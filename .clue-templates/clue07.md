### Clue 7: Make Me a Sandwich ###

https://xkcd.com/149/

#### `sudo` ####

Linux has the concept of a `root` user, which is similar to the administrator
user on Windows. This user is sometimes called the super user. If you want to
do something as the super user, but stay logged in as yourself, there is a 
command for that: `sudo`. It stands for "super-user do".

#### Installing Software ####

Sometimes you need a new program. To install software on some versions of Linux
(Ubuntu and Debian), including the one we use for this class, you use the command
`apt`. Let's install a rainbow text generating program called `lolcat`.

    apt install lolcat
    
You should get an error message asking if you are root. This means you don't
have the ability to install software. Instead, try

    sudo apt install lolcat
    
Now we have the ability to make rainbow text! Type `lolcat`, then start typing any text and
hit enter, and voila! Rainbox text!

To exit, hold the control key and then hit the `c` key.

#### Finding Clue 8 ####

The hint is the name of the first folder in `/sys/kernel/debug`.

Hint: you won't be able to use `cd` with `sudo`. Instead, use `ls`
and specify the directory you would like to list the files inside of.
