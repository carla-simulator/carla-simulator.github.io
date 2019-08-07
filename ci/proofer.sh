#!/usr/bin/env bash

set -e

CHECK_INTERNAL_LINKS=false

if [[ "${TRAVIS_PULL_REQUEST_BRANCH}" = "" ]]; then
  # This is a "push" job.
  if [[ "${TRAVIS_BRANCH}" = "master" ]]; then
    CHECK_INTERNAL_LINKS=true
  fi
fi

bundle exec jekyll build

EXTRA_ARGS="--only-4xx"

if [ "$CHECK_INTERNAL_LINKS" = true ]; then
  bundle exec htmlproofer ${EXTRA_ARGS} -t ./_site --file-ignore /Doxygen/
else
  bundle exec htmlproofer ${EXTRA_ARGS} --external_only --internal-domains carla.org ./_site --file-ignore /Doxygen/
  echo "WARNING: Ignored internal links because we are not in 'master' branch"
fi
