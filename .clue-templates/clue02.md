### Clue 2: The Lay of the Land ###

#### `pwd` ####

What if we get lost and need to know where we are? Just type `pwd` (print
working directory). This should print something like this:

    /home/e1-attack/linux-scavenger-hunt/clues/12345

We are five folders deep, in a folder named `12345`.

#### `cd` ####

Change directory is extremely useful, but it can also be confusing. We
already saw how you can move out of the current directory (`cd ..`) or into a directory
(`cd [dir]`). However, you can move out or in any number of directories in a single
command by separating each one with a `/`, like this (won't actually work here):

    cd ../../../one/two/

You would navigate to the location exiting 3 directories relative to where you are,
then into the directories `one` and then `two`. This is what's known as a relative path: it
depends on where you start where you will end up. The other way to change
directories is with absolute paths, which is a path that starts with a `/`. Try this:

    cd /

Look around and see what's there. This is known as the `root` of the files here - all files
and folders are in this folder! In fact, if you `cd /home/e1-attack`, you'll notice you'll be right back at home!

Lastly, if you get lost, run the cd command with no arguments to return to your home directory!
Your home directory is where we have the `linux-scavenger-hunt` folder, as well as your Downloads folder,
Documents folder, etc, and is where all of your account's files are stored.

#### Find Clue 3 ####

To find the next clue, go to the `/usr` directory (note the slash at the start - what kind of path is this?)
and count the number of subdirectories. This is a hint to your next clue location. Go to the
`linux-scavenger-hunt` directory (remember, we can do `cd` if we get lost and want to return to our home first!), and type

    python next_clue.py [next clue number] [answer]

So, if there were 5 directories in the `/usr` folder, and we looking for clue 3, we would type

    python next_clue.py 3 5

since we want to find clue 3 and our answer is 5.
The number of our next clue should be printed. If you get the hint wrong,
an incorrect clue will be printed.

Once we have the next clue's number, remember that we then need to go into the `clues` directory and then
the directory with the number given to us. If your answer was correct, then you should see clue 3!
