# Selenium inside AWS

This is a template on how to run *Selenium* web browser, using *Chromium*, inside AWS *lambda*.

The lambda is configured to run a *Docker* container under the hood (this method is superior to the *layers* method of packaging requirements).

## Requirements

* Docker
* AWS
* Chromedriver downloaded and in PATH
* serverless installed globally

## Usage


3. Deploy using `sls deploy`

## Local development

Running this locally is tricky. For some reason, the docker container does not run as expected locally. It does run well on AWS though.

1. Build the container: `docker build . -t selenium-inside-aws`
2. Run the container: `docker run -p 9000:8080 selenium-inside-aws`
3. Call the container: `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'`