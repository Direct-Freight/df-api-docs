#!/bin/bash
if test "$1" = "swaggerhub"; then
    export TRAVIS_BRANCH='swaggerhub'
elif test "$1" = "master"; then
    export TRAVIS_BRANCH='master'
else
    echo "invalid branch '$1'"
    exit
fi
source ../set_gh_token.df  #set the GH_TOKEN

/var/www/dfwdbi/api/df-api-docs/scripts/restlet2repo.sh df-api-docs directfreight master 'jon@directfreight.com' restlet2repo
git checkout $TRAVIS_BRANCH
git pull
lynx --source "https://app.swaggerhub.com/apiproxy/registry/jgabriels/Direct_Freight_API/1.0/swagger.yaml?resolved=true&flatten=false&pretty=false" >restlet_studio/swagger.yaml
git commit -a -m "saving modified files"
git push
git remote -v
git remote set-url origin https://github.com/Direct-Freight/df-api-docs.git
git remote -v

source ../set_gh_token.df  #set the GH_TOKEN

if test "$1" = "master"; then
    npm run deploy
else
    npm run deploy-branch
fi

./scripts/build.js
