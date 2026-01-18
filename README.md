TASK: L-system fractal architect

Type of parallel rewriting system to model plant,bacterial growth and root systems
L-systems are recursive in nature
As you iterate, replace parts of string, a lot of self similarity arises

This project uses two libraries: turtle,turtle graphics and tkinter
Using both of these libraries we produce a canvas and a turtle on the canvas which acts as a drawing tool

First we figure out how many symbols we need which are essentially strings, and each symbol has the turtle doing different things like move forward/backward etc.
Starts with initial string(Axiom), and iteratively replaces symbols within it based on a specific rule 
This produces a long series of strings, and each string has its own meaning, which the turtle will perform on the canvas 

First part of project is making the canvas and desiging the input dashboard, using tkinter
Next is introducing the turtle in the tkinter canvas, positioning it and deciding its properties
Then it is defining the axioms and rule sets of symbols(strings) using dictionary which turtle follows, and decoding the meaning of each character in string sequence and drawing it in the canvas
Lastly we have to connect the button widget to draw the pattern and close the tkinter window by defining a function.

I found difficulty in the formation of the long string formation, which the axiom will formafter following the rules.
