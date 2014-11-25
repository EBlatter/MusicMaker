# Critique - 11/25
## By Sisi Cheng

* After looking at the input .xls files for the 3 sample songs, I think the output is pretty good and match what I expect! Call Me Maybe sounds particiularly good (I think the song style lends itself well to the midi format.).

* I didn't recognize the song from the Someone Like You midi output. I think it's because you have not yet implemented note duration? It seems like a held note is being output as a series of notes of the same pitch. Did you make any implementation decisions on that? I talked to Chloe during UX review today and she has to handle a similar situation, although I believe your input method makes note duration much easier to handle.

* It seems it would take a lot of trial and error to determine which cells each word would go in. In the Call Me Maybe sample, how would the user know "hey" and "i" are 8 cells apart? What would it sound like if the user places a word one cell too high or too low? I imagine it would be difficult for a user with no musical background or who can't come up with the pitch of a note by ear.

* Do you have any instructions on how to build and run your projects? I can get a better idea of how easy it is to input a program if I can create a piece from scratch myself or make modifications to your sample programs.

* If input is challenging for a user to get right, is there a way to add something to the UI to make it easier? Chloe is thinking about adding pitch information to each row (color-code each row in an Excel file according to the pitch they correspond to?). If input requires repeated trial and error, you can also think about how to make it simple for the user to input something (even a partially complete program), then run the program and get quick feedback on what it sounds like.
