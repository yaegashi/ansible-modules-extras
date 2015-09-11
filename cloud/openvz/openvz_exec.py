#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015 YAEGASHI Takeshi <yaegashi@debian.org>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = """
---
module: openvz_exec
author: YAEGASHI Takeshi (@yaegashi)
short_description: Execute commands in OpenVZ container
version_added: '2.0'
description:
  - 'Execute commands in OpenVZ container'
options:
    ctid:
        required: true
        description:
        - Container ID or name to execute commands.
    exec:
        required: true
        aliases:
        - shell
        description:
        - Shell commands to execute in the container.
"""

EXAMPLES = """
- name: Execute commands in container with CTID 1000
  openvz_exec:
    ctid: 1000
    exec: |
      adduser --system --group --uid 999 ansible
      adduser ansible sudo
      echo ansible:secret | chpasswd
"""

def main():

    m = AnsibleModule(argument_spec={
        'ctid': {'required': True},
        'exec': {'required': True, 'aliases': ['shell']},
    })

    vzctl_path = m.get_bin_path('vzctl', required=True)

    ctid = str(m.params['ctid'])
    cmd = str(m.params['exec'])

    args = [vzctl_path, 'status', ctid]
    (rc, out, err) = m.run_command(args, check_rc=True)
    if 'exist' not in out:
        m.fail_json(msg='Container not found')
    if 'running' not in out:
        m.fail_json(msg='Container not running')

    args = [vzctl_path, 'exec2', ctid, '-']
    (rc, out, err) = m.run_command(args, data=cmd)
    m.exit_json(changed=True, rc=rc, cmd=cmd, stdout=out, stderr=err)

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
