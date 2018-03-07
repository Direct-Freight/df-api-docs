#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs
if ! diff -q web_deploy/swagger-nocode.yaml /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml; then
        cp /home/catalyst/Dropbox/directfreight/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        npm run restlet2repo
   if test "$1" = "PUSH"; then
        git commit -m "dropbox2repo" -a
        git push
   else
        echo "not pushing"
   fi
fi
