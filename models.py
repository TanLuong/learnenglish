# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ieltsessay(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IELTSEssay'


class Ieltsstories(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IELTSStories'


class Ieltstest(models.Model):
    sublevel = models.IntegerField(db_column='SubLevel', blank=True, null=True)  # Field name made lowercase.
    qnumber = models.AutoField(db_column='QNumber', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    qcontent = models.TextField(db_column='QContent', blank=True, null=True)  # Field name made lowercase.
    answera = models.TextField(db_column='AnswerA', blank=True, null=True)  # Field name made lowercase.
    answerb = models.TextField(db_column='AnswerB', blank=True, null=True)  # Field name made lowercase.
    answerc = models.TextField(db_column='AnswerC', blank=True, null=True)  # Field name made lowercase.
    answerd = models.TextField(db_column='AnswerD', blank=True, null=True)  # Field name made lowercase.
    correctanswer = models.TextField(db_column='CorrectAnswer', blank=True, null=True)  # Field name made lowercase.
    passed = models.IntegerField(db_column='Passed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IELTSTest'


class Ieltswords(models.Model):
    keyword = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IELTSWords'


class Iverbsfull(models.Model):
    baseform = models.CharField(blank=True, null=True)
    pastsimple = models.CharField(blank=True, null=True)
    pastpart = models.CharField(blank=True, null=True)
    person3rd = models.CharField(blank=True, null=True)
    gerund = models.CharField(blank=True, null=True)
    definition = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVerbsFull'


class Idioms(models.Model):
    title = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Idioms'


class Listening(models.Model):
    title = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    audio = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Listening'


class Mostcategories(models.Model):
    id = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MostCategories'


class Mostphrases(models.Model):
    catid = models.IntegerField(db_column='catID', blank=True, null=True)  # Field name made lowercase.
    phrase = models.CharField(blank=True, null=True)
    audio = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MostPhrases'


class Mostwords(models.Model):
    catid = models.IntegerField(db_column='catID', blank=True, null=True)  # Field name made lowercase.
    word = models.CharField(blank=True, null=True)
    audio = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MostWords'


class Phrasalverb(models.Model):
    title = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PhrasalVerb'


class Proverbs(models.Model):
    title = models.CharField(blank=True, null=True)
    desc = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Proverbs'


class Sat(models.Model):
    title = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sat'


class Slangs(models.Model):
    title = models.CharField(blank=True, null=True)
    definition = models.CharField(blank=True, null=True)
    example = models.CharField(blank=True, null=True)
    etymology = models.CharField(blank=True, null=True)
    synonyms = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Slangs'


class Tenses(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tenses'


class Topicidioms(models.Model):
    name = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    desc = models.CharField(blank=True, null=True)
    example = models.CharField(blank=True, null=True)
    subcate = models.CharField(db_column='subCate', blank=True, null=True)  # Field name made lowercase.
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TopicIdioms'


class Topicphrases(models.Model):
    topicid = models.IntegerField(db_column='TopicId', blank=True, null=True)  # Field name made lowercase.
    explaination = models.TextField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TopicPhrases'


class Topics(models.Model):
    title = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Topics'


class Verbs(models.Model):
    id = models.IntegerField(blank=True, null=True)
    word = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Verbs'


class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CatalogIeltsstories(models.Model):

    class Meta:
        managed = False
        db_table = 'catalog_ieltsstories'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gmat(models.Model):
    title = models.TextField(blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmat'


class Grammars(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    menuid = models.IntegerField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grammars'


class Gramuse(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gramuse'


class Gre(models.Model):
    title = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gre'


class Ielts(models.Model):
    title = models.CharField(blank=True, null=True)
    desc = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ielts'


class Lessons(models.Model):
    type = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    question = models.CharField(blank=True, null=True)
    audio = models.CharField(blank=True, null=True)
    favorite = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lessons'


class Pronun(models.Model):
    id = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    category = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    desc = models.CharField(blank=True, null=True)
    image = models.CharField(blank=True, null=True)
    audio = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pronun'


class PronunDetail(models.Model):
    id = models.IntegerField(blank=True, null=True)
    catid = models.IntegerField(db_column='catID', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)
    audio = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pronun_detail'


class Rules(models.Model):
    id = models.IntegerField(blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    content = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules'


class Vocabs(models.Model):
    cate1 = models.CharField(blank=True, null=True)
    cate2 = models.CharField(blank=True, null=True)
    word = models.CharField(blank=True, null=True)
    meaning = models.CharField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.CharField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vocabs'
