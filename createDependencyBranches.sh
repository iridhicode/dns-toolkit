#!/bin/bash

git config --global user.email "goyalridhima30@gmail.com"
git config --global user.name "Ridhima Goyal"

function executeCommand() {
    command="$1"
    echo "Executing: $command"
    eval $command
}

DEPENDENCIES=$(jq -r '.package | keys[]' outdated.json)

for DEPENDENCY in $DEPENDENCIES; do
    LATEST_VERSION=$(jq -r ".package[\"$DEPENDENCY\"].latest_version" outdated.json)
    BRANCH_NAME="update-$DEPENDENCY-$LATEST_VERSION"
    
    executeCommand "git checkout -b $BRANCH_NAME"
    executeCommand "pip install $DEPENDENCY==$LATEST_VERSION"
    
    # Update the requirements.txt file
    executeCommand "pip freeze > requirements.txt"
    
    # Rebase the branch to be up-to-date with the main branch and resolve conflicts in requirements.txt
    executeCommand "git fetch origin main"
    executeCommand "git rebase origin/main"  
    executeCommand "git add requirements.txt"
    executeCommand "git commit -m \"DependAware: Update $DEPENDENCY to $LATEST_VERSION\""
    executeCommand "git push https://${GH_PAT}@github.com/${GITHUB_REPOSITORY}.git $BRANCH_NAME"
    executeCommand "git checkout main"
done
