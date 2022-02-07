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

    all_note = graphene.List(NoteType)

    def resolve_all_note(root, info):
        return Note.objects.all()

    count_of_notes_created_today = graphene.Int()

    def resolve_count_of_notes_created_today(root, info):
        try:
            return Note.objects.filter(created__date=datetime.date.today()).count()
        except Note.DoesNotExist:
            return None

    count_of_notes_completed_today = graphene.Int()

    def resolve_count_of_notes_completed_today(root, info):
        try:
            return Note.objects.filter(
                created__date=datetime.date.today(), complete=True
            ).count()
        except Note.DoesNotExist:
            return None

    all_complete_notes = graphene.List(NoteType)

    def resolve_all_complete_notes(root, info):
        try:
            return Note.objects.filter(complete=True)
        except Note.DoesNotExist:
            return None

    count_complete_notes_this_week = graphene.Int()

    def resolve_count_complete_notes_this_week(root, info):
        try:
            return Note.objects.filter(
                created__week=datetime.date.today().isocalendar()[1], complete=True
            ).count()
        except Note.DoesNotExist:
            return None

    count_complete_notes_this_month = graphene.Int()

    def resolve_count_complete_notes_this_month(root, info):
        try:
            return Note.objects.filter(
                created__month=datetime.date.today().month, complete=True
            ).count()
        except Note.DoesNotExist:
            return None

    count_all_notes = graphene.Int()

    def resolve_count_all_notes(root, info):
        try:
            return Note.objects.all().count()
        except Note.DoesNotExist:
            return None

    note_by_id = graphene.Field(NoteType, id=graphene.Int(required=True))

    def resolve_note_by_id(root, info, id):
        try:
            return Note.objects.get(id=id)
        except Note.DoesNotExist:
            return None

    search_notes = graphene.List(NoteType, search=graphene.String())

    def resolve_search_notes(root, info, search):
        try:
            return Note.objects.filter(
                Q(title__icontains=search) | Q(memo__icontains=search)
            )
        except Note.DoesNotExist:
            return None

    todays_notes = graphene.List(NoteType)

    def resolve_todays_notes(root, info):
        try:
            return Note.objects.filter(created__date=datetime.date.today())
        except Note.DoesNotExist:
            return None

    yesterdays_notes = graphene.List(NoteType)

    def resolve_yesterdays_notes(root, info):
        try:
            return Note.objects.filter(
                created__date=datetime.date.today() - datetime.timedelta(days=1)
            )
        except Note.DoesNotExist:
            return None

    count_notes_this_month = graphene.Int()

    def resolve_count_notes_this_month(root, info):
        try:
            return Note.objects.filter(
                created__month=datetime.date.today().month
            ).count()
        except Note.DoesNotExist:
            return None

    count_incomplete_notes_this_week = graphene.Int()

    def resolve_count_incomplete_notes_this_week(root, info):
        try:
            return Note.objects.filter(
                created__week=datetime.date.today().isocalendar()[1],
                complete=False,
            ).count()
        except Note.DoesNotExist:
            return None

    count_notes_this_week = graphene.Int()

    def resolve_count_notes_this_week(root, info):
        try:
            return Note.objects.filter(
                created__week=datetime.date.today().isocalendar()[1]
            ).count()
        except Note.DoesNotExist:
            return None

    count_incomplete_notes_this_month = graphene.Int()

    def resolve_count_incomplete_notes_this_month(root, info):
        try:
            return Note.objects.filter(
                created__month=datetime.date.today().month, complete=False
            ).count()
        except Note.DoesNotExist:
            return None

    total_notes_created_today = graphene.Int()

    def resolve_total_notes_created_today(root, info):
        try:
            return Note.objects.filter(created__date=datetime.date.today()).count()
        except Note.DoesNotExist:
            return None

    notes_this_month = graphene.List(NoteType)

    def resolve_notes_this_month(root, info):
        try:
            return Note.objects.filter(created__month=datetime.date.today().month)
        except Note.DoesNotExist:
            return None

    notes_this_week = graphene.List(NoteType)

    def resolve_notes_this_week(root, info):
        try:
            return Note.objects.filter(
                created__week=datetime.date.today().isocalendar()[1]
            )
        except Note.DoesNotExist:
            return None

    incomplete_notes_this_week = graphene.List(NoteType)

    def resolve_incomplete_notes_this_week(root, info):
        try:
            return Note.objects.filter(
                created__week=datetime.date.today().isocalendar()[1],
                complete=False,
            )
        except Note.DoesNotExist:
            return None

    incomplete_notes_this_month = graphene.List(NoteType)

    def resolve_incomplete_notes_this_month(root, info):
        try:
            return Note.objects.filter(
                created__month=datetime.date.today().month, complete=False
            )
        except Note.DoesNotExist:
            return None

    count_complete_notes = graphene.Int()

    def resolve_count_complete_notes(root, info):
        try:
            return Note.objects.filter(complete=True).count()
        except Note.DoesNotExist:
            return None


class CompleteNote(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id):
        note = Note.objects.get(id=id)
        note.complete = True
        note.save()
        return CompleteNote(note=note)


class InCompleteNote(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id):
        note = Note.objects.get(id=id)
        note.complete = False
        note.save()
        return InCompleteNote(note=note)


class ImportantNote(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id):
        note = Note.objects.get(id=id)
        note.important = True
        note.save()
        return ImportantNote(note=note)


class NotImportantNote(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id):
        note = Note.objects.get(id=id)
        note.important = False
        note.save()
        return NotImportantNote(note=note)


class CreateNote(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        memo = graphene.String(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, title, memo):
        note = Note(title=title, memo=memo)
        note.save()
        return CreateNote(note=note)


class UpdateNote(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        memo = graphene.String(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id, title, memo):
        note = Note.objects.get(id=id)
        note.title = title
        note.memo = memo
        note.save()
        return UpdateNote(note=note)


class DeleteNote(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id):
        note = Note.objects.get(id=id)
        note.delete()
        return DeleteNote(note=note)


class UpdateMemo(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        memo = graphene.String(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id, memo):
        note = Note.objects.get(id=id)
        note.memo = memo
        note.save()
        return UpdateMemo(note=note)


class UpdateTitle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)

    note = graphene.Field(NoteType)

    def mutate(self, info, id, title):
        note = Note.objects.get(id=id)
        note.title = title
        note.save()
        return UpdateTitle(note=note)


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
    update_note = UpdateNote.Field()
    delete_note = DeleteNote.Field()
    complete_note = CompleteNote.Field()
    incomplete_note = InCompleteNote.Field()
    update_title = UpdateTitle.Field()
    update_memo = UpdateMemo.Field()
    important_note = ImportantNote.Field()
    not_important_note = NotImportantNote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
