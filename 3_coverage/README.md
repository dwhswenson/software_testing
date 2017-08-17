This directory includes code that, in the tutorial, we will work together to
add tests until we have full coverage. The code, in
`pretty_print_seconds.py`, is a function that takes a number of seconds
(along with some optional arguments) and returns a string that will describe
the time remaining in days/hours/minutes etc. The purpose of this code is
that telling a user an amount of time remaining in seconds is not very
useful if the amount of time remaining can be measured in days.

The function used here is actual code from OpenPathSampling -- we make no
claim that this is the best way to write this particular function, but it
does give correct answers for its output. For this exercise, don't worry
about fully understanding the code; the point is to write tests that ensure
it behaves correctly under all circumstances.
