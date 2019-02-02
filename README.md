# spacify
This program takes text and attempts to add spaces to it. The list of valid words is sourced from [here](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) but contains lots of archaic and obscure words so removing these is an ongoing effort, help with this would be very much appreciated. The inclusion of all the letters of the alphabet on their own in words_alpha.txt is NOT a bug, without this the code would get "stuck" if there were no words that matched part of the text which is the only time at which a single letter will be outputted.

In essence the code builds up the longest word it can starting from the first character in the unspaced text, removes this word from the unspaced text and then repeats until all words have been extracted from the unspaced text. 

Feedback and pull requests (particularly those removing words) are very welcome


## Copyright
Copyright © 2019  Rory Sharp All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If you have not received this, see <http://www.gnu.org/licenses/gpl-3.0.html>.

For a summary of the licence go to https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)


## Use 
1\. Run the code and enter the text you wish to have spacified. This text may contain spaces however these will be removed as part of text preprocessing.
2\. If any words are used for spacing that are incorrect and are likely to never be correct, remove them from words_alpha.txt and then re-run the program
