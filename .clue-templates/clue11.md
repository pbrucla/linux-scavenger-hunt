### Clue 11: Editing Files ###

#### Opening and Editing Files ####

To edit files on the command line, you can use various text editors such as `nano`. It's simple to use and widely available. To open a file for editing, such as a `README.md` file, you can use:

    nano README.md

This will open the file in the `nano` editor. Once the file is open, you can start editing directly.

#### Editing text in Nano ####

The cool thing about nano is that you can use it almost exactly like a normal text editor: you just use the arrow keys to move around, and type whenever you want to add/remove/edit text.

#### Searching for Text in Nano ####

To search for a specific word or phrase in the file, press `Ctrl + W`. A prompt will appear at the bottom of the screen where you can type the word or phrase you're looking for. Once you press `Enter`, nano will jump to the first instance of that word. You can press `Ctrl + W` again and press `Enter` to move to the next occurrence of the word.

#### Saving and Exiting in Nano ####

Once you’ve made your changes, you can save and exit the file by pressing `Ctrl + X` (the letter "X" for "eXit"). Nano will ask if you want to save, so type `y` for "yes". Nano will then ask for confirmation of the filename - simply press `Enter` to confirm.

#### Finding Clue 12 ####

Your final task is to edit the `README.md` file and add the phrase `cats are better than dogs` anywhere in the file. You can open the file in `nano` with the following command:

    nano README.md

Navigate to where you want to add the phrase, type it in, save the file with `Ctrl + O`, and then exit with `Ctrl + X`.

Once you are done, simply run `next_clue.py` with the answer `done` like so:

    python next_clue.py 12 done
