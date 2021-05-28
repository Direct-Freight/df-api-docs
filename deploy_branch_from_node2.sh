#!/bin/bash
export TRAVIS_BRANCH='swaggerhub'
git remote -v
git remote set-url origin https://github.com/Direct-Freight/df-api-docs.git
git remote -v

../set_gh_token.df
npm run deploy-branch
