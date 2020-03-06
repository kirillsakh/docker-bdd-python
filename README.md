Test Automation
===============

Create a Gherkin test (https://cucumber.io/docs/installation/) using JavaScript or Python,
that verifies basic operations of index.html.

Bonus
-----

Run the test in Docker on Travis or similar CI service


Solution
-----

<ol>
  <li>git clone  https://github.com/kirillsakh/docker-bdd-python.git</li>
  <li>docker build -t gherkin-test .</li>
  <li>docker run -it --rm gherkin-test</li>
</ol>
