#!/bin/bash
export repo=$1 #df-api-docs OR ts-api-docs
export project=$2 #directfreight OR truckersearch
cd /var/www/dfwdbi/api/$repo
pwd
export APIDOCS_PATH="/home/catalyst/Dropbox/directfreight/apidocs/$project"
if ! diff -q web_deploy/swagger-nocode.yaml $APIDOCS_PATH/swagger20-with-extensions.yaml; then
        #sed -i "s/example: [\"']\(\[.*\]\)[\"']$/example: \1/g" $APIDOCS_PATH/swagger20-with-extensions.yaml #remove extra quotes from examples
        perl -i ./scripts/clean_example.pl $APIDOCS_PATH/swagger20-with-extensions.yaml #remove extra quotes from examples
        cp $APIDOCS_PATH/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp $APIDOCS_PATH/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        git pull --no-edit #just in case
        cp $APIDOCS_PATH/swagger20-with-extensions.yaml web_deploy/swagger-nocode.yaml
        cp $APIDOCS_PATH/swagger20-with-extensions.yaml restlet_studio/swagger.yaml
        npm run restlet2repo
        git diff spec
        export dropbox_info=`scripts/dropbox_last_modifier.pl`
        export email=${dropbox_info%:*}
        export short_email=${dropbox_info%@*}
        export display_name=${dropbox_info#*:}
        git commit --author="$display_name <$email>" -m "dropbox2repo: $short_email/$display_name" -a
        git config --global push.default simple
        git push
        npm run build
fi
