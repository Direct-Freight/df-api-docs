#!/bin/sh
#Custom Build Script for Nevercode -- see https://intercom.help/nevercode/configuring-nevercode/custom-build-steps

#Magic Variables to disable build for Nevercode -- see https://intercom.help/nevercode/configuring-nevercode/magic-variables
export NC_SKIP_COCOAPODS=true  #nevercode downloading and installing Cocoapods is skipped.
export NC_TEST_ONLY=true  #nevercode build step will be skipped.

#other environment variables

#Commands to do a custom build
npm run deploy

