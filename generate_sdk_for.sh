#!/bin/bash
export lang=$1
rm -rf client-sdks/$lang/
mkdir -p client-sdks/$lang
java -jar ./swagger-codegen-cli-2.2.1.jar generate -i ./web_deploy/swagger.json -l $lang -o ./client-sdks/$lang/
