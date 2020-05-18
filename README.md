# Prompt generator in Finnish

A creative writing prompt generator in Finnish, inspired by online writing communities in English which have many challenges and generators supplying prompts, helping writers to jumpstart their creativity. This generator consists of a simple Python program and a list of prompts in a .txt file. 

The latest update to the code has been to separate it into functions and running the programme through a main() function. There are now separate functions for asking the user for the number of prompts they want (kysy_maara), reading the file of prompts into a prompt list (lue_lista) generating a list of the desired number of random prompts (arvo_ehdotukset), and printing out the prompts (tulosta_ehdotukset). This will also make it easier to implement the next planned update, which will be to allow the user to select specific types of prompts their list will be generated from.

The list of prompts included ("ehdotukset.txt") will be updated and extended from time to time. The application is currently used through the command line, but a user interface may be created later, to help others use the generator as well.