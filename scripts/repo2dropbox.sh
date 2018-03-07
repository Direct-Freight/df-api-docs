#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs/
git pull --no-edit
npm run build
cp -f web_deploy/swagger-nocode.yaml /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml 
rm shelljs_*

