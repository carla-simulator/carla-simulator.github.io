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

if [ "$CHECK_INTERNAL_LINKS" = true ]; then
  bundle exec htmlproofer -t ./_site
else
  bundle exec htmlproofer --external_only --internal-domains carla.org ./_site
  echo "WARNING: Ignored internal links because we are not in 'master' branch"
fi
