This directory contains a simple skeleton of a test file using pytest. The
purpose of this is to illustrate how you set up a test module, and how it
runs in practice.

To run the tests, you can use:

* `py.test`: just run the tests directly
* `py.test -v`: output the name of each test as it runs
* `py.test -s`: show the output (from stdout) with each test

The first way to run it is what you'll often do. The second way is useful to
see *which* test raises an error, if you have problems, and is how we run in
when we run regression tests as part of our continuous integration script.
In this particular example, one of the things to remember from the second
way is that the order in which tests are run is not guaranteed, so you
shouldn't have side effects in tests. The third way of running it is useful
when debugging tests, but here is primarily to help you understand the order
in which fixtures are used.

In addition, you can choose to only run part of the test suite. Using the
`-v` option, as above, will show you which tests are running:

* `py.test -v test_flow.py`: run everything in `test_flow.py`
* `py.test -v test_flow.py::TestClassA`: run all the tets in test class
  `TestClassA`
* `py.test -v test_flow::TestClassA::test_that`: only run the test
  `test_that` (within `TestClassA`)
