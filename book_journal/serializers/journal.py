from rest_framework import serializers
from book_journal.models.journal import Journal
from common.constants import JOURNAL_TYPE

class JournalSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, obj)->str: 
        return JOURNAL_TYPE[obj.type][1]
    
    class Meta:
        model = Journal
        fields = "__all__"