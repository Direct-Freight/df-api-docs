#!/bin/bash
export TRAVIS_BRANCH='swaggerhub'
git remote -v
git remote set-url origin https://github.com/Direct-Freight/df-api-docs.git
git remote -v

source ../set_gh_token.df  #set the GH_TOKEN

npm run deploy-branch
