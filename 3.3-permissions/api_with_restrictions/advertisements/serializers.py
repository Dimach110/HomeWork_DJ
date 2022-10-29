from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', "updated_at" )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if Advertisement.objects.filter(creator=self.context["request"].user).filter(status="OPEN").count() >= 10:
            if self.context["request"].method in ["POST"]:
                raise ValidationError("Превышен лимит доступных вам открытых объявлений, "
                                      "для создания новых объявлений, сперва закройте старые.")
            if self.context["request"].method == "PATCH" and self.context["request"].data.get("status") != "OPEN":
                return data
            else:
                raise ValidationError("Превышен лимит доступных вам открытых объявлений")
        return data


        #
        # if self.context["request"].method in ["POST"] and Advertisement.objects.filter(
        #         creator=self.context["request"].user).filter(status="OPEN").count() >= 10:
        #     raise ValidationError("Превышен лимит доступных вам открытых объявлений")
        # if (self.context["request"].method in ["PATCH"] and
        #         self.context["request"].data.get("status") == "CLOSED" and Advertisement.objects.filter(
        #         creator=self.context["request"].user).filter(status="OPEN").count() >= 10):
        #     raise ValidationError("Вы не можете внести изменения, "
        #                           "превышен лимит доступных вам открытых объявлений")

    # if len([key for key in self.context["request"].data.keys() if key in ["title", "description"]]) > 0: