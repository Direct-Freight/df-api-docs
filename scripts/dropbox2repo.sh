#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs
if ! diff -q web_deploy/swagger-nocode.yaml /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml; then
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        git pull --no-edit #just in case
        npm run restlet2repo
        git diff spec
        git commit -m "dropbox2repo" -a
        git push
elif ! diff -q web_deploy/swagger-nocode.yaml restlet_studio/swagger.yaml; then
        cp restlet_studio/swagger.yaml web_deploy/swagger-nocode.yaml
        git pull --no-edit #just in case
        npm run restlet2repo
        git diff spec
        git commit -m "dropbox2repo" -a
        git push
fi
