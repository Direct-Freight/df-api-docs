#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs/
npm run build
cp -f web_deploy/swagger-nocode.yaml /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml 