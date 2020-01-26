git clone  https://github.com/~.git
docker build -t gherkin-test .
docker run -it --rm gherkin-test
