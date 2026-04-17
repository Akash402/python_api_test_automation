pipeline {
    agent any

    triggers {
        // Run full regression every day at 9:00 AM (matches GitHub Actions schedule)
        cron('0 9 * * *')
    }

    environment {
        ENV            = "${params.ENV ?: 'dev'}"
        DEV_URL        = "${params.DEV_URL ?: 'https://restful-booker.herokuapp.com/'}"
        STAGING_URL    = "${params.STAGING_URL ?: ''}"
        PROD_URL       = "${params.PROD_URL ?: ''}"
        AUTH_TYPE      = "${params.AUTH_TYPE ?: 'basic'}"
        API_USERNAME   = "${params.API_USERNAME ?: ''}"
        API_PASSWORD   = "${params.API_PASSWORD ?: ''}"
        API_KEY_HEADER = "${params.API_KEY_HEADER ?: 'x-api-key'}"
    }

    parameters {
        choice(name: 'ENV',            choices: ['dev', 'staging', 'prod'], description: 'Target environment')
        string(name: 'DEV_URL',        defaultValue: 'https://restful-booker.herokuapp.com/', description: 'Dev base URL')
        string(name: 'STAGING_URL',    defaultValue: '', description: 'Staging base URL')
        string(name: 'PROD_URL',       defaultValue: '', description: 'Prod base URL')
        choice(name: 'AUTH_TYPE',      choices: ['basic', 'oauth', 'api_key'], description: 'Auth strategy')
        string(name: 'API_KEY_HEADER', defaultValue: 'x-api-key', description: 'Header name for API key auth')
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv "$WORKSPACE/.venv"
                    "$WORKSPACE/.venv/bin/pip" install --upgrade pip
                    "$WORKSPACE/.venv/bin/pip" install -r requirements.txt
                '''
            }
        }

        stage('Parallel Regression') {
            parallel {
                stage('Regression Tests') {
                    steps {
                        sh '"$WORKSPACE/.venv/bin/pabot" --processes 4 -d results --include regression api/tests/examples || true'
                    }
                }
            }
        }

        stage('Retry failed tests') {
            steps {
                sh '"$WORKSPACE/.venv/bin/pabot" --processes 4 -d results/rerun --rerunfailed results/output.xml --include regression api/tests/examples || true'
            }
        }

        stage('Merge results') {
            steps {
                sh '"$WORKSPACE/.venv/bin/rebot" --merge -d results results/output.xml results/rerun/output.xml || true'
            }
        }
    }

    post {
        always {
            // Archive Robot Framework results
            archiveArtifacts artifacts: 'results/**', allowEmptyArchive: true

            // Publish Robot Framework report in Jenkins UI (requires Robot Framework Plugin)
            robot(
                outputPath:      'results',
                outputFileName:  'output.xml',
                reportFileName:  'report.html',
                logFileName:     'log.html',
                passThreshold:   90,
                unstableThreshold: 80
            )
        }
    }
}
