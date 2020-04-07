# Prompt generator in Finnish

A creative writing prompt generator in Finnish, inspired by online writing communities in English which have many challenges and generators supplying prompts, helping writers to jumpstart their creativity. This generator consists of a simple Python program and a list of prompts in a .txt file. The generator requests the user to supply the number of prompts they want; the user can also ask for a random number of prompts by selecting 0, in which case the program generates the number randomly (between 1 and 12) using random.randint(). 

Once the number is selected, the application reads the .txt file using .readlines(), creating a list of the available prompts. Using random.sample() to prevent repeat numbers, the application generates the requested amount of random numbers from range covering the length of the list. With these numbers as indexes, it then returns prompts from the prompt list and prints them on the screen, one prompt per line.

The list of prompts included ("ehdotukset.txt") will be updated and extended with time. The application is currently used through the command line, but a user interface may be created later, to help others use the generator as well.

Other improvements planned include dividing the prompts into several lists based on the type or theme, and allowing the user to select the lists they wish to use for generating prompts, making the generator more useful for different kinds of writers.
