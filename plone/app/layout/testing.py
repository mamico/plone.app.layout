# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.content import HAS_PLONE_APP_RELATIONFIELD
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.layout
        self.loadZCML(package=plone.app.layout)
        # check for relationfield support
        if HAS_PLONE_APP_RELATIONFIELD:
            # we need behaviors setup
            import plone.app.dexterity
            self.loadZCML(package=plone.app.dexterity)
            # and the behavior we want to test
            import plone.app.relationfield
            self.loadZCML(package=plone.app.relationfield)

    def setUpPloneSite(self, portal):
        if HAS_PLONE_APP_RELATIONFIELD:
            applyProfile(portal, 'plone.app.relationfield:default')


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='plone.app.layout:Integration',
)
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='plone.app.layout:Functional',
)