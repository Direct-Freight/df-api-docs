#!/bin/bash
if test "$1" = "swaggerhub"; then
    export TRAVIS_BRANCH='swaggerhub'
elif test "$1" = "master"; then
    export TRAVIS_BRANCH='master'
else
    echo "invalid branch '$1'"
    exit
fi
git pull
git commit -a -m "saving modified files"
git checkout $TRAVIS_BRANCH
git remote -v
git remote set-url origin https://github.com/Direct-Freight/df-api-docs.git
git remote -v

source ../set_gh_token.df  #set the GH_TOKEN

if test "$1" = "master"; then
    npm run deploy
else
    npm run deploy-branch
fi
