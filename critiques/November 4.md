# Critique - 11/4
## By Sisi Cheng

* A possible parser you may look into is [pyPEG](http://fdik.org/pyPEG1/). I was similarly searching for a good parsing library, but I rejected pyPEG because of its limited custom error message structure. However, since the user of your language uses rtf editors, you may have significantly fewer syntax errors. pyPEG is relatively light-weight and it'll allow you to program in Python!

* What was your experience with creating the sample programs? I don't often use rtf and I wonder if the user would that find it intuitive and easy to use? User-testing would be great for this.

* Do you expect to run into any problem caused by different formattings by rtf editors? I opened your examples in Wordpad (the only rtf editor I have), and I don't think the programs look the same as they do on your computer.

* Is just several levels of superscript and subscript enough to accurate capture the variety of pitches, and how do you plan to resolve this? We were throwing some ideas around in class about somehow limiting the user's input. Also, to accurately recreate a song, the user will need to accurately count how many super- and sub-script they're adding to each word in the lyric, which may make the language harder to use.

* Have you thought about your AST at all? It seems to me that it could be fairly straight-forward to decide, since it's simply a representation of the audio data for a song. Perhaps you can decide that first, then add the concrete syntax. The concrete syntax can then evolve without significant changes to the AST.

* Your project seems to be largely design-oriented. The design concrete syntax of the language is especially important to the usefulness of the DSL.

* Just a side note, I believe you should have at least one goal every week in your Implementation Plan.

I look forward to seeing the progress of your DSL!