
// Pipeline parameters
tests_selection = params.TESTS_SELECTION ?: "test_search.py"
test_branch = params.TEST_BRANCH ?: "main"
tests_timeout = params.TESTS_TIMEOUT ? params.TESTS_TIMEOUT.toInteger() : 60

runStage("Checkout", 10) {
    // Checkout the test repository
    checkoutWithCredentials(git_rtlab_qaa_tests_remote, "", test_branch, rtlab_qaa_credentialsId)
}

runStage("Setup Python Environment", 10) {
    // Setup virtual environment with dependencies
    bat """
        python -m venv .venv
        .\\.venv\\Scripts\\activate
        pip install -r requirements_frozen.txt
    """
}

try {
    runStage("Execute Tests", tests_timeout) {
        // Run pytest
        currentBuild.description = "Running tests: ${tests_selection}"
        bat "pytest tests/${tests_selection} -s"
    }
} finally {
    runStage("Archive Results", 10) {
        archiveArtifacts allowEmptyArchive: true, artifacts: '**/*.log', fingerprint: true, onlyIfSuccessful: false
        junit(allowEmptyResults: true, testResults: '**/test_report.html')
    }

    runStage("Cleanup", 5) {
        cleanWs()
    }
}

def runStage(String stageName, int timeoutMinutes, Closure stageBody) {
    stage(stageName) {
        timeout(time: timeoutMinutes, unit: 'MINUTES') {
            stageBody()
        }
    }
}
