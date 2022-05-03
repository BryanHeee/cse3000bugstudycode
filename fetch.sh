#! /bin/bash
DOWNLOADS=$1
GH_TOKEN=$2

if [ "$#" -ne 2 ]; then
    echo "usage: fetch.sh DOWNLOADS GH_TOKEN"
    exit
fi

echo "Fetching Salt Bugs..."
# python3 fetch_bugs.py $DOWNLOADS/bugs/salt.txt \
        # $DOWNLOADS/bugs/fixes/bug_issue_descriptions $DOWNLOADS/bugs/salt.json $GH_TOKEN

# echo "Cloning Compilers' Repositories..."
# ./scripts/fetch/clone.sh $DOWNLOADS/repos
# PHASE 2
echo "Finding Test Cases & Fixes (Post-Filtering)..."
echo "This requires some time. Please bear with us ..."
./find_fixes.sh $DOWNLOADS/bugs \
        $DOWNLOADS/bugs/fixes/bug_issue_descriptions $DOWNLOADS/repos \
        $DOWNLOADS/bugs/fixes $GH_TOKEN 2>&1 | tee $DOWNLOADS/logs
