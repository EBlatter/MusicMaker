# Project description and plan

## Motivation

The goal is that a program written in this language will sound the way it looks, which will not only make it easier to write music, especially for those who can't read typical music notation, and would also be a fun way to make music. A DSL is an appropriate solution because music notation could already be considered to be a DSL, and this will simply be a different, more specific version of that.

## Language domain

The domain this language addresses is the domain of music. The people who will benefit most from this language are those who want to have fun creating music or recreating songs they know despite not knowing how to write music. There are other DSLs for this domain, such as normal music notation and guitar tabs. Because these are very standard, well-known languages for writing music, these could influence how I structure the syntax. For example, I plan to have words that are higher than others be higher in pitch, which is similar to how typical sheet music looks.

## Language design

In one sentence, my DSL will take in text that is formatted by the user and output music based on characteristics of the text. A program in my language consists of a text file (probably RTF). When this file is run, the output should be music notes that match the text. The output will be entirely audio. I am not sure of what data or control structures would be useful for this. I expect that the length of the notes will mostly be determined by the number of repeated vowels in a word, so it seems that most syntax errors would be due to not enough vowels in a note/word. It seems like there are not many opportunities for compile-time or run-time errors, though the problem with vowels might be a compile-time error instead. When the user tries to compile a program that does not have enough vowels per note, I could throw an error that explains this and stop compiling.

## Example computations

I have included some sample programs in the sample programs folder under documents. When batman.rtf is run, the output should be sound that is similar to the Batman theme. The notes should change in pitch with the text, going up when it goes up and going down when it goes down. The part where it actually says "batman" should be held for longer than the previous "nana" notes. The music should also get louder for the larger texts, so this program should gradually crescendo. 'we are never ever getting back together.rtf' is similar. When it is run, the out put should sound similar to two lines of melody from Taylor Swift's "We Are Never Ever Getting Back Together". Though this doesn't show the changes in dynamics, it shows the changes in pitch and length of note well, especially with the 'oooooo' parts.



