# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ChapterPicture.page'
        db.add_column(u'localchapters_chapterpicture', 'page',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 9, 13, 0, 0), related_name='Chapter Pictures', to=orm['localchapters.ChapterPage']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ChapterPicture.page'
        db.delete_column(u'localchapters_chapterpicture', 'page_id')


    models = {
        u'localchapters.chaptermember': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ChapterMember'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'bio': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'localchapters.chapterpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ChapterPage', '_ormbases': [u'pages.Page']},
            'aboutHeader': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'aboutText': ('django.db.models.fields.TextField', [], {}),
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Chapter'", 'to': u"orm['localchapters.LocalChapter']"}),
            'contactHeader': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contactText': ('django.db.models.fields.TextField', [], {}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'eventsHeader': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'eventsText': ('django.db.models.fields.TextField', [], {}),
            'firstBackgroundPicture': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True'}),
            'handsonHeader': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'handsonText': ('django.db.models.fields.TextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'secondBackgroundPicture': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True'}),
            'showsHeader': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'showsText': ('django.db.models.fields.TextField', [], {}),
            'thirdBackgroundPicture': ('mezzanine.core.fields.FileField', [], {'max_length': '200', 'null': 'True'})
        },
        u'localchapters.chapterpicture': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ChapterPicture'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Chapter Pictures'", 'to': u"orm['localchapters.ChapterPage']"}),
            'picture_category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'picture'", 'blank': 'True', 'to': u"orm['localchapters.ChapterPictureCategory']"})
        },
        u'localchapters.chapterpicturecategory': {
            'Meta': {'object_name': 'ChapterPictureCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'localchapters.localchapter': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'LocalChapter'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'chapterEmail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'chapterNumber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': u"orm['localchapters.ChapterMember']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Page'", 'null': 'True', 'to': u"orm['localchapters.ChapterPage']"}),
            'schoolAddress': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolCity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolState': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolZipCode': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'localchapters.localchapterspage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'LocalChaptersPage', '_ormbases': [u'pages.Page']},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'chapters'", 'blank': 'True', 'to': u"orm['localchapters.LocalChapter']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'extra_info': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'localchapters.section': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Section'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'heading_bar_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['localchapters.LocalChaptersPage']"}),
            'textfield': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'font_awesome_icon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'navbar_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'title_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['localchapters']