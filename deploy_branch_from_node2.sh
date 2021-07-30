#!/bin/bash
if test "$1" = "swaggerhub"; then
    export TRAVIS_BRANCH='swaggerhub'
elif test "$1" = "master"; then
    export TRAVIS_BRANCH='master'
else
    echo "invalid branch '$1'"
    exit
fi
git checkout $TRAVIS_BRANCH
git remote -v
git remote set-url origin https://github.com/Direct-Freight/df-api-docs.git
git remote -v

source ../set_gh_token.df  #set the GH_TOKEN

npm run deploy-branch
