#!/bin/bash
export repo=$1 #df-api-docs OR ts-api-docs
export project=$2 #directfreight OR truckersearch
export branch=$3 #directfreight OR truckersearch
export email="$4"
export message="$5"
cd /var/www/dfwdbi/api/$repo
git checkout $branch
git pull --no-edit
#cp restlet_studio/swagger.yaml /home/catalyst/Dropbox/directfreight/apidocs/$project/swagger20-with-extensions.yaml
cp restlet_studio/swagger.yaml web_deploy/swagger-nocode.yaml
npm run restlet2repo
git diff spec
git config --global user.email "$email"
git add spec/*/*
git commit -m "restlet2repo: $message" -a
git push
#git config --global user.email "jondf/ts@directfreight.com"
