# Critique - 11/18
## By Sisi Cheng

* Since you've decided to use number of vowels as heuristic for note length, I think your IR is reasonable. You may want to think more specifically about the data structures you're using to represent each note. It's an important decision, since it splits the code between the parser and the evaluator. In Scala, I've found it easier to put the more coding-intensive portion of the program into the evaluator. The parser simply handles processing the input into the IR. Although you may have much more flexibility with this in Python!

* I have no expertise in music libraries in Python, but I think your demo in class was good and demonstrated that MIDIUtil should do all you need it to. It's perfectly reasonable for the program to output a MIDI file as the output.

* I would like to see more on how notes map from their Excel sheet cell indices to pitches in the output of the program. Choices made here may be key to ensure that the output of the program match the user's expectations. Or you may find that some songs are easier to get right in the program than others.

* Considering that we're getting close to a prototype, you may want to re-think about your timeline for the rest of the project. The design portion (which was important!) seems to have taken a bit longer than you expected. Do you still think you'll be on track for the goal you set for this weekend? What would your prototype look like? Which parts of the project do you think you'll finish by semester's end?

