#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs
if ! diff -q web_deploy/swagger-nocode.yaml /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml; then
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        git pull --no-edit #just in case
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        npm run restlet2repo
        git diff spec
        git config --global user.email "jondf@directfreight.com"
        git commit -m "dropbox2repo" -a
        git push
fi
