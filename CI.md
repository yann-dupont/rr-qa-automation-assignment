# CI implementation

This document will outline an approach to implementing the test framework on CI.
This approach will use Jenkins to create automated pipelines for each of the tests.

### Jenkinsfile
This framework includes a Jenkinsfile. It is to be downloaded by Jenkins, and in turn it clones the present repo. It then sets up the necessary environment, and then runs the selected test.

### Setup
A Jenkins server will need to be set up, with pipelines for each of the test files in the repo. Each pipeline will run daily, so as to catch bugs and regressions as soon as they are inserted in the product. We could call pytest without specifying the test_selection parameter to run every test at once, but this would greatly reduce the readability of the results.
Ideally, this setup would be made using configuration as code, to not have to add every pipeline manually, and make bulk changes easier.

### Operation
Once this CI system is set up, the pipelines will have to be checked daily. To make this more practical, a system of alerts could be set up to send mails or messages when a pipeline fails. Alternatively, a Graphana dashboard could be created to keep track of failing pipelines, as well as to provide an overview on the global status of the tests, and its evolution in time.
