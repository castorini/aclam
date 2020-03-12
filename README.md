# ACLAM: ACL Anthology Mirror

This repository contains YAML data files for the entire ACL Anthology, augmented with data from Semantic Scholar.

## Building the ACL Anthology YAML data

**IMPORTANT:** The ACL Anthology requires Python 3.7+; no, it won't work with Python 3.6.

Run the `build_acl_data.sh` script:

```bash
sh scripts/build_acl_data.sh
```

**OR**

To do this step-by-step, clone the ACL anthology repository containing the raw XML data:

```bash
git clone https://github.com/acl-org/acl-anthology.git
```
 
Next, navigate to the `acl-anthology` folder and install dependencies:

```bash
cd acl-anthology
```

```bash
pip3 install -r bin/requirements.txt
```

Create the data export directory:

```bash
mkdir -p build/data
```

Modify the YAML generation script to generate the abstracts without HTML tags:

```bash
sed -i 's/data\[\"abstract_html\"\] = paper.get_abstract(\"html\")/data["abstract"] = paper.get_abstract("plain")/g' \
    bin/create_hugo_yaml.py
```

Generate cleaned YAML data:

```bash
python3 bin/create_hugo_yaml.py
```

Generated ACL files can now be found in `acl-anthology/build/data/`

## Augmenting YAML files with Semantic Scholar data

First, download the latest [Semantic Scholar open corpus](http://s2-public-api-prod.us-west-2.elasticbeanstalk.com/corpus/download/) using the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html). This requires ~120GB of hard disk space.

```bash
aws s3 cp --no-sign-request --recursive s3://ai2-s2-research-public/open-corpus/LATEST-CORPUS-DATE/ SEMANTIC_SCHOLAR_PATH
```

Unzip all of the compressed files into JSON files using the following script. This requires ~300GB of additional hard disk space.

```bash
for file in *.gz; do
  gunzip -c "$file" > "${file/.gz*/.json}"
done
```

#### Filtering out ACL papers

We filter out all Semantic Scholar papers that are from venues in the ACL Anthology.

```bash
python3 scripts/semantic_scholar/filter_acl.py --semantic_scholar_path SEMANTIC_SCHOLAR_PATH --acl_data_path ACL_DATA_PATH
```
