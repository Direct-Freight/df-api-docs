#!/bin/bash
cd /var/www/dfwdbi/api/df-api-docs
export DF_APIDOCS_PATH="/home/catalyst/Dropbox/directfreight/apidocs/directfreight"
if ! diff -q web_deploy/swagger-nocode.yaml $DF_APIDOCS_PATH/swagger20-with-extensions.yaml; then
        cp $DF_APIDOCS_PATH/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp $DF_APIDOCS_PATH/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        git pull --no-edit #just in case
        cp $DF_APIDOCS_PATH/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp $DF_APIDOCS_PATH/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        npm run restlet2repo
        git diff spec
        export dropbox_info=`scripts/dropbox_last_modifier.pl`
        export email=${dropbox_info%:*}
        export short_email=${dropbox_info%@*}
        export display_name=${dropbox_info#*:}
        git commit --author="$display_name <$email>" -m "dropbox2repo: $short_email/$display_name" -a
        git push
fi
