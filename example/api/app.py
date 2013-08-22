
import urlparse

from keystoneclient.v3 import client

from oslo.config import cfg
import pecan

from example.api import config
from example.api import hooks
from example.api import middleware

CONF = cfg.CONF

# the endpoints of all openstack services that has been registered to Keystone
"""
ENDPOINTS = { # All of Endpoints
    "keystone": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "nova": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "glance": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "cinder": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "ceph": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "swift": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "quantum": {
        'admin': '',
        'public': '',
        'internal': '',
    },
    "ec2": {
        'admin': '',
        'public': '',
        'internal': '',
    }

}
"""
ENDPOINTS = {}



def get_pecan_config():
    # Set up the pecan configuration
    filename = config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app(config, extra_hooks=None):

    app_hooks = [hooks.DBHook()]

    if extra_hooks:
        app_hooks.extend(extra_hooks)

    if not config:
        config = get_pecan_config()

    app = pecan.make_app(
        config.app.root,
        static_root=config.app.static_root,
        template_path=config.app.template_path,
        debug=CONF.debug,
        force_canonical=getattr(config.app, 'force_canonical', True),
        hooks=app_hooks,
        wrap_app=middleware.FaultWrapperMiddleware,
    )
    pecan.conf.update({'wsme': {'debug': CONF.debug}})

    return app


class VersionSelectorApplication(object):
    def __init__(self):
        pc = get_pecan_config()
        self.v1 = setup_app(config=pc)

        # Load configuration
        AUTH_OPTIONS = [
            cfg.StrOpt('auth_host',
                       deprecated_group="AUTH",
                       default='localhost',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('auth_port',
                       deprecated_group="AUTH",
                       default='25257',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('auth_protocol',
                       deprecated_group="AUTH",
                       default='http',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('auth_api_version',
                       deprecated_group="AUTH",
                       default='v3',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('admin_user_domain_name',
                       deprecated_group="AUTH",
                       default='',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('admin_username',
                       deprecated_group="AUTH",
                       default='',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('admin_password',
                       deprecated_group="AUTH",
                       default='',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('admin_project_name',
                       deprecated_group="AUTH",
                       default='service',
                       help='Username to use for openstack service access'),
            cfg.StrOpt('admin_project_domain_name',
                       deprecated_group="AUTH",
                       default='Default',
                       help='Username to use for openstack service access'),
        ]

        CONF.register_opts(AUTH_OPTIONS)

        # Get api
        keystone_endpoint = "%s://%s:%s/%s" % (CONF.auth_protocol, CONF.auth_host, CONF.auth_port, CONF.auth_api_version)
        keystone = client.Client(user_domain_name=CONF.admin_user_domain_name, username=CONF.admin_username, password=CONF.admin_password, project_name=CONF.admin_project_name, project_domain_name=CONF.admin_project_domain_name, auth_url=keystone_endpoint)

        # Get services
        services = {}
        services_all = keystone.services.list()
        for service in services_all:
            services[service.id] = {}
            services[service.id]['name'] = service.name
            services[service.id]['type'] = service.type
            services[service.id]['description'] = service.description

        # Get endpoints and service name
        endpoints = keystone.endpoints.list()
        for endpoint in endpoints:
            service_name = services[endpoint.service_id]['type']
            ENDPOINTS[service_name] = {}
            url = urlparse.urlparse(endpoint.url)
            ENDPOINTS[service_name][endpoint.interface] = "%s://%s" % (url.scheme, url.netloc)
            # ENDPOINTS[service_name]['type'] = services[endpoint.service_id]['type']
            # ENDPOINTS[service_name]['description'] = services[endpoint.service_id]['description']


    def __call__(self, environ, start_response):
        return self.v1(environ, start_response)

