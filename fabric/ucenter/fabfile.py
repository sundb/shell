from fabric.api import *
from fabric.contrib import project, console

env.hosts = 'root@106.75.84.107:57321'

local_app_dir = '/Users/macbookpro/dev/git/ucenter/app'
local_db_dir = '/Users/macbookpro/dev/git/ucenter/db'
online_dir = '/data/ucenter'

def update():
    with cd('/data/ucenter'):
        project.rsync_project(
            remote_dir=online_dir,
            local_dir=local_app_dir,
            default_opts='-avczp',
            delete=True
        )

        project.rsync_project(
            remote_dir=online_dir,
            local_dir=local_db_dir,
            default_opts='-avczp',
            delete=True
        )

        run('kill -9 $(cat tmp/pids/server.pid)')
        run('rails s -b 0.0.0.0 -p 80 -d')

        run('cat tmp/pids/server.pid')
