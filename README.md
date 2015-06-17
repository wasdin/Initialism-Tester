# README #

This was a Python script that I wrote to satisfy a curious itch: how many [three letter initialisms](https://en.wikipedia.org/wiki/Three-letter_acronym) (often called "acronyms") exist? I figured a good way to test how many notable initialisms exist was to check Wikipedia. 

This script goes through Wikipedia and checks to see whether a page for the acronym exists. It then reports at the end the number that do exist. It also outputs a [pickled](https://docs.python.org/2/library/pickle.html) text file containing a list of strings of acronyms that did not exist.

I've included this output in the repository, in case anyone wants to run some statistics, since it takes a little while to run on behalf of waiting for Wikipedia.

# Notes on running #
This requires Python 2 and Curl. The website is requested with Curl. I have only tested this on Linux (on a Slackware-based distro), but you should be find on any *nix with curl installed. Even with curl installed, it might need slight modifications to run on Windows.

 