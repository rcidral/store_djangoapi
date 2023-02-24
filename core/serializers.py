from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Usuario, Estoque, Pedido

class UsuarioSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "is_totem",
            "email",
            "username",
            "password",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("esse email já está cadastrado")}
            )
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("esse nome de usuario já está em uso")}
            )
        
        return args


class UsuarioCreateSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "is_totem",
            "email",
            "username",
            "password",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("esse email já está cadastrado")}
            )
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("esse nome de usuario já está em uso")}
            )
        return super().validate(args)

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        newUser = Usuario.objects.create_user(**validated_data)
        newUser.foto = None
        newUser.save()
        return newUser

class EstoqueSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Estoque
        read_only_fields = ("id",)
        fields = (
            "id",
            "coca",
            "cerveja",
            "hamburguer",
        )

class PedidoSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Pedido
        read_only_fields = ("id",)
        fields = (
            "id",
            "usuario",
            "coca",
            "cerveja",
            "hamburguer",
            "data",
        )

