from rest_framework import serializers

from .models import (User, ChatType, Channel, Message,
                     Tag, Reaction, CustomMessage)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'image',
            'title'
        )


class ChatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatType
        fields = ('name',)


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Message
        fields = (
            'timestamp',
            'user',
            'text'
        )


class ReactionSerializer(serializers.ModelSerializer):
    message_timestamp = serializers.SerializerMethodField()
    user = UserSerializer()

    def get_message_timestamp(self, obj):
        return obj.message.timestamp

    class Meta:
        model = Reaction
        fields = (
            'timestamp',
            'message_timestamp',
            'reaction',
            'user'
        )


class ActionSerializer(serializers.ModelSerializer):
    message_timestamp = serializers.SerializerMethodField()
    action_tag = serializers.SerializerMethodField()
    user = UserSerializer()

    def get_message_timestamp(self, obj):
        return obj.message.timestamp

    def get_action_tag(self, obj):
        return obj.action.action_tag

    class Meta:
        model = Reaction
        fields = (
            'timestamp',
            'message_timestamp',
            'action_tag',
            'user'
        )


class TagSerializer(serializers.ModelSerializer):
    original_message_timestamp = serializers.SerializerMethodField()
    user = UserSerializer()

    def get_original_message_timestamp(self, obj):
        return obj.message.timestamp

    class Meta:
        model = Tag
        fields = (
            'timestamp',
            'original_message_timestamp',
            'user',
            'key',
            'value'
        )


class CustomMessageSerializer(serializers.ModelSerializer):
    original_message_timestamp = serializers.SerializerMethodField()
    user = UserSerializer()
    action_tag = serializers.SerializerMethodField()
    flow = serializers.SerializerMethodField()

    def get_original_message_timestamp(self, obj):
        return obj.message.timestamp

    def get_action_tag(self, obj):
        return obj.message_markup.action_tag

    def get_flow(self, obj):
        return obj.message_markup.flow

    class Meta:
        model = CustomMessage
        fields = (
            'action_tag',
            'flow',
            'original_message_timestamp',
            'user',
            'content'
        )


class ChannelSerializer(serializers.ModelSerializer):
    chat_type = ChatTypeSerializer()
    messages = MessageSerializer(many=True)
    reactions = serializers.SerializerMethodField()
    actions = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    custom_messages = serializers.SerializerMethodField()

    def get_reactions(self, obj):
        reactions = []
        for message in obj.messages.all():
            for reaction in message.reactions.all():
                if not reaction.action:
                    serializer = ReactionSerializer(instance=reaction)
                    reactions.append(serializer.data)

        return reactions

    def get_actions(self, obj):
        actions = []
        for message in obj.messages.all():
            for reaction in message.reactions.all():
                if reaction.action:
                    serializer = ActionSerializer(instance=reaction)
                    actions.append(serializer.data)

        return actions

    def get_tags(self, obj):
        tags = []
        for message in obj.messages.all():
            for reply in message.tags.all():
                serializer = TagSerializer(instance=reply)
                tags.append(serializer.data)

        return tags

    def get_custom_messages(self, obj):
        custom_messages = []
        for message in obj.messages.all():
            for markup in message.custom_messages.all():
                serializer = CustomMessageSerializer(instance=markup)
                custom_messages.append(serializer.data)

        return custom_messages

    class Meta:
        model = Channel
        fields = (
            'name',
            'chat_type',
            'messages',
            'reactions',
            'actions',
            'tags',
            'custom_messages'
        )
