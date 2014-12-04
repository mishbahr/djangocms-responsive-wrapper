from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import six

# South support.
try:
    from south.modelsinspector import add_introspection_rules
    SOUTH = True
except ImportError:
    SOUTH = False

# Try to be compatible with Django 1.5+.
try:
    import json
except ImportError:
    from django.utils import simplejson as json

# Basestring no longer exists in Python 3
try:
    basestring
except NameError:
    basestring = str


class JSONField(six.with_metaclass(models.SubfieldBase, models.TextField)):

    def to_python(self, value):
        if value == '':
            return None

        try:
            if isinstance(value, basestring):
                return json.loads(value)
            elif isinstance(value, bytes):
                return json.loads(value.decode('utf8'))
        except ValueError:
            pass
        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == '':
            return None
        if isinstance(value, dict) or isinstance(value, list):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return super(JSONField, self).get_db_prep_save(value, *args, **kwargs)

    def value_from_object(self, obj):
        value = super(JSONField, self).value_from_object(obj)
        if self.null and value is None:
            return None
        return json.dumps(value)

if SOUTH:
    add_introspection_rules([], ['^responsive_wrapper.fields.JSONField'])
