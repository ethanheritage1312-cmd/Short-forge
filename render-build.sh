#!/usr/bin/env bash
set -e

pip install -r requirements.txt

curl -fsSL https://deno.land/install.sh | DENO_INSTALL=/opt/render/project/src/.deno sh

mkdir -p /opt/render/project/src/.chrome
cd /opt/render/project/src/.chrome

wget -q https://storage.googleapis.com/chrome-for-testing-public/153.0.8010.36/linux64/chrome-linux64.zip
unzip -q chrome-linux64.zip
