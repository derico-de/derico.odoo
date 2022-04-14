# derico.odoo

Ansible role to install and configure multiple Odoo instances on one host. It uses by default the OCB repository from the OCA and installs addons from PyPi via Poetry.

## Structure

This role will create the following Odoo structure.

### odoo_rootdir

  /srv/odoo

### odoo_workdir

For every Odoo version we create a working directory.

  /srv/odoo/o14

### odoo_checkoutdir

Inside the workdir we checkout Odoo into the repo directory. This checkout is shared beetween all Odoo setups in this version.

  /srv/odoo/o14/repo

### odoo_setupdir

For every Odoo setup we create a folder with the name of the odoo_setups hostname in the workdir directory.
Inside this directory we will have the configuration and wsgi files for this Odoo setup.

  /src/odoo/o14/odoo14-demo.derico.de

## Minimum Ansible Version:

2.9

## Supported versions and systems

| System / Odoo       | 13.0 | 14.0 |
|---------------------|------|------|
| Debian 10 (buster)  | yes  | yes  |

## Usage

### Play

```yaml
- name: Odoo
    hosts: odoo_servers
    become: yes
    environment:
    LC_ALL: en_US.UTF-8

    roles:
    - role: derico.odoo
```

### host_vars/odoo01:

```yaml
odoo_setups:
  - name: 12.0
    version: 12.0
    odoo_user: odoo
    instances:
      - name: example1
        domain: example1.office.derico.de
        config_http_port: 8000
        config_longpolling_port: 9000
  - name: 13.0
    version: 13.0
    odoo_user: odoo
    instances:
      - name: example2
        domain: example2.office.derico.de
        config_http_port: 8010
        config_longpolling_port: 9010
```

### tags

Most of the time you want to use:

`--tags "addons,instance"` or just `--tags "instance"` if you don't have changes for the addons.

#### install

all tasks for the initial installation

#### addons

tasks for addon repositories checkouts

#### instance

Odoo instance configuration, like uWSGI Emperor files and Systemd services

