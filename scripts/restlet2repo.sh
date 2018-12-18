#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs
git pull --no-edit
cp restlet_studio/swagger.yaml /home/catalyst/Dropbox/directfreight/apidocs/directfreight/swagger20-with-extensions.yaml
cp restlet_studio/swagger.yaml web_deploy/swagger-nocode.yaml
npm run restlet2repo
git diff spec
git config --global user.email "$1"
git add spec/*/*
git commit -m "restlet2repo: $2" -a
git push
git config --global user.email "jondf@directfreight.com"
