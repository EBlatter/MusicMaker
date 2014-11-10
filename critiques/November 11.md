# Critique - 11/11
## By Sisi Cheng

* I think switching to Excel is a great idea! It doesn't seem to be harder to parse than RTF, and it makes it's easier to use.

* The current input method is very intuitive! Although any additional linguistic knowledge the user is required to know would make it more difficult and time-consuming to input a song, so it may not be a good idea to expect the user to know about phoneme and or even reliably break words into syllables.

* Since you're now using Excel as the input interface for the language, a lot of syntax errors will be automatically handled. Though there might still be some other kinds of errors you'll have to handle.
  * How will you handle typo-ed words? What about numbers or special symbols?
  * If the program parses the user inputs in a way that some inputs are rejected (i.e. inputs with typos, non-words, etc), the program should output helpful messages to help the user debug their input. I'd expect to see a message about why the input was rejected and some marker pointing to the location of the error; perhaps even a suggestion about how to fix it.
  * The user might need to tweak their inputs several times to achieve the output they want. How easy is it for the user to figure out what's wrong with their inputs? You may decide that this requires the program to have musical intelligence that's outside the scope of the DSL project.

* As we discussed in class, you have some choices to make regarding how to support extending the duration of a note based on repeated letters. While there are lots of possibilities around parsing words, I think it's important to pick a design that's reasonable for you to implement in the timeframe you have, while keeping in mind that this design could be improved given more time. It's a good idea to do some research to see what's out there and what's reasonably easy to do. Maybe parsing syllables will be easy? Or maybe a simple heuristic for repeated letters will be good enough for now.

* It's super exciting to see something running and working! Now that you've decided on Excel as the input method, it'd be good to decide your abstract syntax. Once the IR is decided, you can get started with working on some part of your project and keep thinking about other parts that may not be decided yet.

