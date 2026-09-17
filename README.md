<h1>Conway's Game of Life</h1>
My attempt at Conway's Game of Life.
<br/>
You can find details about the game as a whole here: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life.
<br/><br/>
Here are the rules that determine what happens in the game in general: <br />
<list>
<li>Any live cell with fewer than two live neighbors dies, as if by underpopulation.</li> 
<li>Any live cell with two or three live neighbors lives on to the next generation.</li> 
<li>Any live cell with more than three live neighbors dies, as if by overpopulation.</li> 
<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li> 
</list>
<br/>
<img src="https://github.com/mhaynes121/ConwaysGameOfLife/blob/main/Capture.JPG" />

<h3>Note:</h3>
This does not follow the standard rule set for Conway's Game of Life. That was the starting point but due to <br/>
general nature of those rules you could end up with several oscillating conditions. I added additional logic, <br/>
such as a generation counter and the concept of generationsLived along with a required 'dead' period, to help <br/>
alleviate some of those conditions. It's still possible to end up in an oscillator but it should be pretty rare <br/>
at this point. 

