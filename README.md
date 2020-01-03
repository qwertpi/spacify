# spacify
This program takes text and attempts to add spaces to it in order to form words. The word list included is the common words from [Molby Words 2](https://en.wikipedia.org/wiki/Moby_Project#Words) sourced from [here](https://www.gutenberg.org/files/3201/files/COMMON.TXT) but lacks some words and contains some archaic and obscure words so modifying it is an ongoing effort, help with this would be very much appreciated.

In essence the main algorithm used builds up the longest word it can using consective letters from the text starting from the first letter in the text, removes this word from the unspaced text and then repeats until all words have been extracted from the unspaced text. 

Feedback and pull requests (particularly those removing or adding words) are very welcome


## Copyright
Copyright © 2019-20  Rory Sharp All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If you have not received this, see <http://www.gnu.org/licenses/gpl-3.0.html>.

For a summary of the licence go to https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)


## Use 
-1\. Clone the repo  
0\. (Optional) Create a file called input.txt and put your text in it  
1\. (Optional) Replace words.txt with your own word file of the same name if you have when which would be better suited to your text  
2\. Run the code and if you didn't create the input.txt file enter the text you wish to have spacified. This text may contain spaces however these will be removed as part of text preprocessing.  
3\. If any words are used for spacing that are incorrect and are likely to never be correct, remove them from words.txt, re-run the program, and then create a PR with your modified words.txt  
