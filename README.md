# derico.odoo

Ansible role to install and configure multiple Odoo instances on one host. It uses by default the OCB repository from the OCA.

## Minimum Ansible Version:

2.9

## Supported versions and systems

| System / Odoo       | 12.0 | 13.0 |
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

