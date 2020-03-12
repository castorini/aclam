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
