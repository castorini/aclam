#!/usr/bin/env sh

# remove old repository
rm -rf acl-anthology

# clone repository
git clone https://github.com/acl-org/acl-anthology.git

# install dependencies and create build folder
cd acl-anthology
mkdir -p build/data
pip3 install -r bin/requirements.txt

# modify script to generate abstracts without HTML
sed -i 's/data\[\"abstract_html\"\] = paper.get_abstract(\"html\")/data["abstract"] = paper.get_abstract("plain")/g' \
    bin/create_hugo_yaml.py

# generate YAML files
python3 bin/create_hugo_yaml.py

cd ..
