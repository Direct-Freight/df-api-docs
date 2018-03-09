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
        export dropbox_info=`scripts/dropbox_last_modifier.pl`
        export email=${dropbox_info%:*}
        export short_email=${dropbox_info%@*}
        export display_name=${dropbox_info#*:}
        git config --global user.name "$display_name"
        git config --global user.email "$email"
        git config user.name "$display_name"
        git config user.email "$email"
        git commit --author="$display_name <$email>" -m "dropbox2repo: $short_email/$display_name" -a
        git push
fi
