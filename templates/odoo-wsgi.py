# WSGI Handler configuration file.

import odoo

#----------------------------------------------------------
# Common
#----------------------------------------------------------
odoo.multi_process = True # Nah!

# Equivalent of --load command-line option
odoo.conf.server_wide_modules = {{ odoo_config_server_wide_modules }}
conf = odoo.tools.config

conf['addons_path'] = "{{ odoo_config_addons_path.__class__.__name__ == 'list' and odoo_config_addons_path | join(',') or odoo_config_addons_path }}"
conf['db_name'] = "{{ odoo_config_db_name }}"
conf['db_host'] = {{ odoo_config_db_host and '"{0}"'.format(odoo_config_db_host) }}
conf['db_user'] = "{{ odoo_config_db_user }}"
conf['db_port'] = {{ odoo_config_db_port }}
conf['db_password'] = {{ odoo_config_db_passwd }}
conf['list_db'] = {{ odoo_config_list_db }}
conf['dbfilter'] = "{{ odoo_config_dbfilter }}"
conf['data_dir'] = "{{ odoo_config_data_dir }}"
conf['without_demo'] = {{ odoo_config_without_demo }}

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = odoo.service.wsgi_server.application
odoo.service.server.load_server_wide_modules()