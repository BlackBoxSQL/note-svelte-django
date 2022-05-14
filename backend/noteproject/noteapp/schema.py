import datetime
import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from .models import Note
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations


class NoteType(DjangoObjectType):
    class Meta:
        model = Note


class Query(UserQuery, MeQuery, graphene.ObjectType):
    me_notes = graphene.List(NoteType)

    def resolve_me_notes(self, info, **kwargs):
        user = info.context.user
        return Note.objects.filter(user=user)

    me_notes_complete = graphene.List(NoteType)

    def resolve_me_notes_complete(self, info, **kwargs):
        user = info.context.user
        return Note.objects.filter(user=user, complete=True)

    me_notes_important = graphene.List(NoteType)

    def resolve_me_notes_important(self, info, **kwargs):
        user = info.context.user
        return Note.objects.filter(user=user, important=True)


class CreateNote(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        memo = graphene.String(required=True)
        complete = graphene.Boolean(required=True)
        important = graphene.Boolean(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, title, memo, complete, important):
        user = info.context.user
        note = Note(
            user=user, title=title, memo=memo, complete=complete, important=important
        )
        note.save()
        return CreateNote(note=note)


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()  # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    create_note = CreateNote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
