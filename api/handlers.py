from piston.handler import BaseHandler
from general.models import Resource, Organization, UserProfile

class ResourceHandler(BaseHandler):
    model = Resource

class OrganizationHandler(BaseHandler):
    model = Organization

class UserHandler(BaseHandler):
    model = UserProfile
