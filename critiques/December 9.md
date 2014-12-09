# Critique - 12/9
## By Sisi Cheng

* It sounds like the program is not handling a blank column as a pause. Did it do that in a previous version?

* When there are multiple notes in a column, the program plays them in sequence and throws a warning. This is pretty counter-intuitive, since I would expect all notes in a column would be played simultaneously. If you don't get to implement simultaneous notes, I would prefer the program to either refuse to generate the midi or pick one note from each column to play (perhaps the highest one since that one is mostly likely to carry the melody?). This way, I can still hear what my music sounds like overall with the expected tempo and length.

* I think the way you're handling note duration is a quick and easy way to do it. Adding more vowels in a row makes the note longer, and the user should be able to easily experiment with the duration by adding different numbers of vowels. If the user can be instructed to put each note/syllable in its own cell, you can put most of the work on the user.

* As we discussed in class today, it would be really cool if there is a way for the user to more quickly try out an input without the user having to compile and re-open the midi file.