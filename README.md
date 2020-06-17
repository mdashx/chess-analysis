# chess-analysis

A sample app to demonstrate various aspects of testing using pytest
and other tools

To illustrate various testing techniques, I’m going to use a simple
sample project named chess-analysis.

The basic behavior of this Python system will be to download portable
game notation (PGN) files from chessgames.com, analyze each position
with the Stockfish chess engine, save position as Forsyth–Edwards
Notation (FEN) in database with stockfish analysis, and allow querying
the database by the FEN string to get the Stockfish analysis.

The software will not be feature-complete, it will contain just enough
code to verify that we can perform the basic capabilities of the
system. This will also demonstrate how testing allows us to develop
significant parts of the system before we worry about non-core
features like user input or showing output.

- Simple tests for imperative code

Downloading a PGN file is written in imperative style to demonstrate
how to write simple tests for imperative code.

- Simple tests for OO code

A chess game as a PGN file and series of FEN strings is written in
object-oriented style to demonstrate writing simple tests for OO code.

- Testing external resources

Using Requests to query chessgames.com gives us an opportunity to test
code that depends on a network connection.

Using Stockfish gives us an opportunity to test code that depends on
an external resource.

- Testing with fixture data

We can save some PGN files as fixture data.

We can dump the database in a known state to create database fixture
data for testing database reads.

- Mocking out resources

We can mock out the code that connects to chessgames.com.

We can mock out the code that connects to Stockfish.

- Testing with a database

The ChessGame class will write to the database.

A `get_position` function will read from the database.

- Using conf.test



- Skipping tests

We can skip the tests that depend on external resources.

We can create tests for features we don't have yets, and then xfail
those tests.
