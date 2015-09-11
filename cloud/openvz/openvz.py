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
module: openvz
author: YAEGASHI Takeshi (@yaegashi)
short_description: Manage OpenVZ Containers
version_added: '2.0'
description:
  - 'Manage OpenVZ containers using vzctl/vzlist command line tools'
requirements:
  - 'vzctl >= 4.0'
notes:
  - vzctl/vzlist command line tools in the system must be new enough
    to support JSON outputs (C(vzlist --json)).
# OPTION DOC BEGIN
options:
    applyconfig:
        default: null
        description:
        - Parameter passed to C(vzctl set --applyconfig).
        required: false
    avnumproc:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --avnumproc).
        required: false
    capability:
        default: null
        description:
        - Parameter passed to C(vzctl set --capability).
        required: false
    config:
        default: null
        description:
        - Parameter passed to C(vzctl create --config).
        required: false
    cpulimit:
        default: null
        description:
        - Parameter passed to C(vzctl set --cpulimit).
        required: false
    cpumask:
        default: null
        description:
        - Parameter passed to C(vzctl set --cpumask).
        required: false
    cpus:
        default: null
        description:
        - Parameter passed to C(vzctl set --cpus).
        required: false
    cpuunits:
        default: null
        description:
        - Parameter passed to C(vzctl set --cpuunits).
        required: false
    ctid:
        description:
        - Container ID or name to manage.
        required: true
    dcachesize:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --dcachesize).
        required: false
    description:
        default: null
        description:
        - Parameter passed to C(vzctl set --description).
        required: false
    dgramrcvbuf:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --dgramrcvbuf).
        required: false
    disabled:
        choices:
        - 'yes'
        - 'no'
        default: null
        description:
        - Parameter passed to C(vzctl set --disabled).
        required: false
    diskinodes:
        default: null
        description:
        - Parameter passed to C(vzctl set --diskinodes).
        required: false
    diskspace:
        default: null
        description:
        - Parameter passed to C(vzctl set --diskspace).
        required: false
    features:
        default: null
        description:
        - Parameter passed to C(vzctl set --features).
        required: false
    hostname:
        default: null
        description:
        - Parameter passed to C(vzctl set --hostname).
        required: false
    iolimit:
        default: null
        description:
        - Parameter passed to C(vzctl set --iolimit).
        required: false
    ioprio:
        default: null
        description:
        - Parameter passed to C(vzctl set --ioprio).
        required: false
    iopslimit:
        default: null
        description:
        - Parameter passed to C(vzctl set --iopslimit).
        required: false
    ipadd:
        default: null
        description:
        - Parameter passed to C(vzctl set --ipadd).
        required: false
    ipaddr:
        default: null
        description:
        - IP address settings in the idempotent way.  Specify addresses in an array
            or a space delimited string.
        required: false
    ipdel:
        default: null
        description:
        - Parameter passed to C(vzctl set --ipdel).
        required: false
    iptables:
        default: null
        description:
        - Parameter passed to C(vzctl set --iptables).
        required: false
    kmemsize:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --kmemsize).
        required: false
    layout:
        default: null
        description:
        - Parameter passed to C(vzctl create --layout).
        required: false
    lockedpages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --lockedpages).
        required: false
    mount_opts:
        default: null
        description:
        - Parameter passed to C(vzctl set --mount_opts).
        required: false
    name:
        default: null
        description:
        - Parameter passed to C(vzctl set --name).
        required: false
    nameserver:
        default: null
        description:
        - Parameter passed to C(vzctl set --nameserver).
        required: false
    netif:
        default: null
        description:
        - Network interface settings in the idempotent way.  Specify interfaces in
            an array or a space delimited string.
        required: false
    netif_add:
        default: null
        description:
        - Parameter passed to C(vzctl set --netif_add).
        required: false
    netif_del:
        default: null
        description:
        - Parameter passed to C(vzctl set --netif_del).
        required: false
    nodemask:
        default: null
        description:
        - Parameter passed to C(vzctl set --nodemask).
        required: false
    numfile:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numfile).
        required: false
    numflock:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numflock).
        required: false
    numiptent:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numiptent).
        required: false
    numothersock:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numothersock).
        required: false
    numproc:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numproc).
        required: false
    numpty:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numpty).
        required: false
    numsiginfo:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numsiginfo).
        required: false
    numtcpsock:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --numtcpsock).
        required: false
    onboot:
        choices:
        - 'yes'
        - 'no'
        default: null
        description:
        - Parameter passed to C(vzctl set --onboot).
        required: false
    oomguarpages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --oomguarpages).
        required: false
    ostemplate:
        default: null
        description:
        - Parameter passed to C(vzctl create --ostemplate).
        required: false
    othersockbuf:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --othersockbuf).
        required: false
    physpages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --physpages).
        required: false
    private:
        default: null
        description:
        - Parameter passed to C(vzctl create --private).
        required: false
    privvmpages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --privvmpages).
        required: false
    quotatime:
        default: null
        description:
        - Parameter passed to C(vzctl set --quotatime).
        required: false
    quotaugidlimit:
        default: null
        description:
        - Parameter passed to C(vzctl set --quotaugidlimit).
        required: false
    ram:
        default: null
        description:
        - Parameter passed to C(vzctl set --ram).
        required: false
    root:
        default: null
        description:
        - Parameter passed to C(vzctl create --root).
        required: false
    searchdomain:
        default: null
        description:
        - Parameter passed to C(vzctl set --searchdomain).
        required: false
    shmpages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --shmpages).
        required: false
    state:
        choices:
        - started
        - stopped
        - present
        - absent
        default: present
        description:
        - Container target state.
        required: false
    swap:
        default: null
        description:
        - Parameter passed to C(vzctl set --swap).
        required: false
    swappages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --swappages).
        required: false
    tcprcvbuf:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --tcprcvbuf).
        required: false
    tcpsndbuf:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --tcpsndbuf).
        required: false
    userpasswd:
        default: null
        description:
        - Parameter passed to C(vzctl set --userpasswd).
        required: false
    vmguarpages:
        default: null
        description:
        - UBC parameter passed to C(vzctl set --vmguarpages).
        required: false
# OPTION DOC END
"""

EXAMPLES = """
- name: Create and start container foobar with CTID 1000
  openvz:
    ctid: 1000
    state: started
    ostemplate: ubuntu-14.04-x86_64-minimal
    ram: 1G
    swap: 512M
    diskspace: 2G
    hostname: foobar
    name: foobar
    ipaddr:
    - 192.168.0.100
    - 192.168.0.101
    nameserver: 192.168.0.1
    userpasswd: ansible:secret
    description: Ubuntu trusty amd64 container
"""

CREATE_PARAMS = set((
    'ostemplate', 'config', 'root', 'private', 'layout', 'diskspace',
    'diskinodes'
))

SET_PARAMS = set((
    'ram', 'swap', 'ipaddr', 'ipadd', 'ipdel', 'hostname', 'nameserver',
    'searchdomain', 'onboot', 'userpasswd', 'cpuunits', 'cpulimit', 'cpus',
    'cpumask', 'nodemask', 'diskspace', 'diskinodes', 'quotatime',
    'quotaugidlimit', 'mount_opts', 'capability', 'netif', 'netif_add',
    'netif_del', 'applyconfig', 'features', 'name', 'description', 'ioprio',
    'iolimit', 'iopslimit', 'iptables', 'disabled'
))

UBC_PARAMS = set((
    'kmemsize', 'lockedpages', 'privvmpages', 'shmpages', 'numproc',
    'physpages', 'vmguarpages', 'oomguarpages', 'numtcpsock', 'numflock',
    'numpty', 'numsiginfo', 'tcpsndbuf', 'tcprcvbuf', 'othersockbuf',
    'dgramrcvbuf', 'numothersock', 'dcachesize', 'numfile', 'numiptent',
    'swappages', 'avnumproc'
))

DIFF_PARAMS = set((
    'private', 'root', 'mount_opts', 'hostname', 'name', 'description', 'ip',
    'nameserver', 'searchdomain', 'status', 'cpulimit', 'cpuunits', 'cpus',
    'ioprio', 'iolimit', 'iopslimit', 'onboot', 'bootorder', 'layout',
    'features', 'disabled'
))

def docupdate():
    options = {}
    options.update(dict([
        (i, {'description': ['Parameter passed to C(vzctl create --%s).' % i],
             'required': False, 'default': None})
        for i in CREATE_PARAMS]))
    options.update(dict([
        (i, {'description': ['Parameter passed to C(vzctl set --%s).' % i],
             'required': False, 'default': None})
        for i in SET_PARAMS]))
    options.update(dict([
        (i, {'description': ['UBC parameter passed to C(vzctl set --%s).' % i],
             'required': False, 'default': None})
        for i in UBC_PARAMS]))
    options.update({
        'ctid': {
            'description': ['Container ID or name to manage.'],
            'required': True,
        },
        'state': {
            'description': ['Container target state.'],
            'choices': ['started', 'stopped', 'present', 'absent'],
            'required': False, 'default': 'present',
        },
        'onboot': {
            'description': ['Parameter passed to C(vzctl set --onboot).'],
            'choices': ['yes', 'no'],
            'required': False, 'default': None,
        },
        'disabled': {
            'description': ['Parameter passed to C(vzctl set --disabled).'],
            'choices': ['yes', 'no'],
            'required': False, 'default': None,
        },
        'ipaddr' : {
            'description': [
                'IP address settings in the idempotent way.  '
                'Specify addresses in an array or a space delimited string.'
            ],
            'required': False, 'default': None,
        },
        'netif' : {
            'description': [
                'Network interface settings in the idempotent way.  '
                'Specify interfaces in an array or a space delimited string.'
            ],
            'required': False, 'default': None,
        },
    })

    with open(__file__) as f:
        lines = f.readlines()
    n0 = n1 = -1

    for i, line in enumerate(lines):
        if line.startswith('# OPTION DOC BEGIN'): n0 = i
        if line.startswith('# OPTION DOC END'): n1 = i

    if n0 >= 0 and n1 >= 0 and n1 > n0:
        import yaml
        lines[n0+1:n1] = yaml.dump({'options': options},
                                   indent=4, default_flow_style=False)
        with open(__file__, 'w') as f:
            f.writelines(lines)
        print 'Updated documentation in %s' % __file__

def maint():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'docupdate':
            docupdate()
        else:
            print 'Unknown command: %s' % command
    else:
        program = sys.argv[0]
        print 'Usage: %s COMMAND' % program
        print 'COMMAND:'
        print '  docupdate - Update documentation in %s' % program

def main():

    def get_vzjson():
        (rc, out, err) = m.run_command([vzlist_path, '-j', ctid])
        if not rc:
            return json.loads(out)[0]
        elif out == '[]\n' or 'Container(s) not found' in err:
            return {}
        m.fail_json(msg='No JSON support, vzlist is too old?', err=err)

    def diff_vzjson(a, b):
        if not a and not b:
            return False
        if (a and not b) or (not a and b):
            return True
        for i in UBC_PARAMS:
            if (i in a and i not in b) or (i not in a and i in b):
                return True
            if i in a:
                if a[i]['barrier'] != b[i]['barrier'] or \
                   a[i]['limit'] != b[i]['limit']:
                    return True
        for i in ('diskspace', 'diskinodes'):
            if (i in a and i not in b) or (i not in a and i in b):
                return True
            if i in a:
                if a[i]['softlimit'] != b[i]['softlimit'] or \
                   a[i]['hardlimit'] != b[i]['hardlimit']:
                    return True
        for i in DIFF_PARAMS:
            if (i in a and i not in b) or (i not in a and i in b):
                return True
            if i in a:
                if type(a[i]) is list:
                    if sorted(a[i]) != sorted(b[i]):
                        return True
                elif a[i] != b[i]:
                    return True
        return False

    def get_vzargs(params):
        args = []
        for i in params:
            p = m.params[i]
            if not p: continue
            if i == 'ipaddr':
                args += ['--ipdel', 'all', '--ipadd']
                args.append(' '.join(p) if type(p) is list else str(p))
            elif i == 'netif':
                args += ['--netif_del', 'all', '--netif_add']
                args.append(' '.join(p) if type(p) is list else str(p))
            else:
                args.append('--%s' % i)
                if type(p) is bool:
                    args.append('yes' if p else 'no')
                else:
                    args.append(str(p))
        return args

    spec = dict([(i, dict()) for i in CREATE_PARAMS | SET_PARAMS | UBC_PARAMS])
    spec.update(
        ctid=dict(required=True),
        state=dict(choices=['started', 'stopped', 'present', 'absent']),
        onboot=dict(choices=BOOLEANS, type='bool'),
        disabled=dict(choices=BOOLEANS, type='bool'),
    )
    m = AnsibleModule(argument_spec=spec)

    vzctl_path = m.get_bin_path('vzctl', required=True)
    vzlist_path = m.get_bin_path('vzlist', required=True)

    ctid = str(m.params['ctid'])
    state = str(m.params['state'])
    vzjson = vzjson_original = get_vzjson()
    done = []

    if state in ('started', 'stopped', 'present'):
        if not vzjson:
            args = [vzctl_path, 'create', ctid]
            args += get_vzargs(CREATE_PARAMS)
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('created')
            vzjson = get_vzjson()

    if vzjson:
        args = get_vzargs(SET_PARAMS | UBC_PARAMS)
        if args:
            args = [vzctl_path, 'set', ctid, '--save'] + args
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('configured')

    if state == 'started':
        if vzjson and vzjson['status'] != 'running':
            args = [vzctl_path, 'start', ctid]
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('started')

    if state in ('stopped', 'absent'):
        if vzjson and vzjson['status'] != 'stopped':
            args = [vzctl_path, 'stop', ctid]
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('stopped')

    if state == 'absent':
        if vzjson:
            args = [vzctl_path, 'destroy', ctid]
            (rc, out, err) = m.run_command(args, check_rc=True)
            done.append('destroyed')

    vzjson = get_vzjson()
    if state == 'present' and not vzjson:
        m.fail_json(msg='Failed to make the container present')
    elif state == 'started' and vzjson and vzjson['status'] != 'running':
        m.fail_json(msg='Failed to make the container started')
    elif state == 'stopped' and vzjson and vzjson['status'] != 'stopped':
        m.fail_json(msg='Failed to make the container stopped')
    elif state == 'absent' and vzjson:
        m.fail_json(msg='Failed to make the container absent')

    changed = diff_vzjson(vzjson, vzjson_original)
    msg = ', '.join(done) if changed else 'nothing done'
    m.exit_json(changed=changed, msg=msg.capitalize())

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    if 'ansible.module_utils.basic' in sys.modules.keys():
        maint() # Run locally for the maintenance
    else:
        main()  # Run as a module
