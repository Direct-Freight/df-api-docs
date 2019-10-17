#!/bin/bash
export repo=$1 #df-api-docs OR ts-api-docs
export project=$2 #directfreight OR truckersearch
cd /var/www/dfwdbi/api/$repo/
git pull --no-edit
npm run build
cp -f web_deploy/swagger-nocode.yaml /home/catalyst/Dropbox/directfreight/apidocs/$project/swagger20-with-extensions.yaml 
rm shelljs_*

