from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivelastmodifiedLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.lastmodified
        xmlconfig.file(
            'configure.zcml',
            collective.lastmodified,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.lastmodified:default')

COLLECTIVE_LASTMODIFIED_FIXTURE = CollectivelastmodifiedLayer()
COLLECTIVE_LASTMODIFIED_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_LASTMODIFIED_FIXTURE,),
    name="CollectivelastmodifiedLayer:Integration"
)
COLLECTIVE_LASTMODIFIED_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_LASTMODIFIED_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectivelastmodifiedLayer:Functional"
)
