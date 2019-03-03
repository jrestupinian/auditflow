from rest_framework import serializers
from .models import Process, MacroProcess

class MacroProcessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MacroProcess
        fields = ('id', 'url', 'name')

class ProcessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'url','macroprocess_name','name', 'objective','reach', 'applies_to', 'localization', 'leader')