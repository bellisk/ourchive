from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root),
    path('works/', views.WorkList.as_view(), name='work-list'),
    path('works/<int:pk>/', views.WorkDetail.as_view(), name='work-detail'),
    path('works/<int:pk>/publish-full/', views.PublishWork.as_view(), name='publish-work'),
    path('works/<int:pk>/draft', views.WorkDraftDetail.as_view(), name='work-draft-detail'),
    path('tags/<int:pk>/works', views.WorkByTagList.as_view(), name='work-by-tags'),
    path('tags/<int:pk>/bookmarks', views.BookmarkByTagList.as_view(), name='bookmark-by-tags'),
    path('chapters/', views.ChapterList.as_view(), name='chapter-list'),
    path('chapters/<int:pk>/', views.ChapterDetail.as_view(), name='chapter-detail'),
    path('chapters/<int:pk>/draft', views.ChapterDraftDetail.as_view(), name='chapter-draft-detail'),
    path('works/<int:work_id>/chapters/draft', views.WorkDraftChapterDetail.as_view(), name='work-chapter-draft-detail'),
    path('works/<int:work_id>/chapters/', views.WorkChapterDetail.as_view(), name='work-chapter-detail'),
    path('chapters/<int:pk>/comments/', views.ChapterCommentDetail.as_view(), name='chaptercomment-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('tagtypes/', views.TagTypeList.as_view(), name='tag-type-list'),
    path('tagtypes/<int:pk>/', views.TagTypeDetail.as_view(), name='tagtype-detail'),
    path('worktypes/', views.WorkTypeList.as_view(), name='work-type-list'),
    path('worktypes/<int:pk>/', views.WorkTypeDetail.as_view(), name='worktype-detail'),
    path('worktypes/<int:type_id>/works', views.WorkByTypeList.as_view(), name='work-by-type-list'),
    path('tags/', views.TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('bookmarks/', views.BookmarkList.as_view(), name='bookmark-list'),
    path('bookmarks/<int:pk>/', views.BookmarkDetail.as_view(), name='bookmark-detail'),
    path('bookmarks/<int:pk>/draft', views.BookmarkDetail.as_view(), name='bookmark-draft-detail'),
    path('bookmarks/<int:pk>/comments', views.BookmarkCommentDetail.as_view(), name='bookmarkcomment-detail'),
    path('bookmarkcollections/', views.BookmarkCollectionList.as_view(), name='bookmark-collection-list'),
    path('bookmarkcollections/<int:pk>/', views.BookmarkCollectionDetail.as_view(), name='bookmarkcollection-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('bookmarkcomments/', views.BookmarkCommentList.as_view(), name='bookmarkcomment-list'),
    path('bookmarkcomments/<int:pk>/', views.BookmarkPrimaryCommentDetail.as_view(), name='bookmarkprimarycomment-detail'),
    path('messages/', views.MessageList.as_view(), name='message-list'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name='message-detail'),
    path('notifications/', views.NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),
    path('notifications/<int:pk>/read', views.NotificationDetail.as_view(), name='notification-read-detail'),
    path('notificationtypes/', views.NotificationTypeList.as_view(), name='notification-type-list'),
    path('notificationtypes/<int:pk>/', views.NotificationTypeDetail.as_view(), name='notificationtype-detail'),
    path('settings/', views.OurchiveSettingList.as_view(), name='ourchive-setting-list'),
    path('settings/<int:pk>/', views.OurchiveSettingDetail.as_view(), name='ourchivesetting-detail'),
    path('settings/', views.OurchiveSettingList.as_view()),
    path('users/<int:pk>/',views.UserDetail.as_view(), name='user-detail'),
    path('users/<str:username>/', views.UserNameDetail.as_view(), name='user-detail'),
    path('users/<str:username>/works', views.UserWorkList.as_view(), name='user-works-drafts'),
    path('users/<str:username>/works/drafts', views.UserWorkDraftList.as_view(), name='user-drafts'),
    path('users/<str:username>/bookmarks', views.UserBookmarkList.as_view(), name='user-bookmarks'),
    path('users/<str:username>/bookmarkcollections', views.UserBookmarkCollectionList.as_view(), name='user-bookmark-collections'),
    path('users/<str:username>/notifications', views.UserNotificationList.as_view(), name='user-notifications'),
    path('users/<str:username>/bookmarks/drafts', views.UserBookmarkDraftList.as_view(), name='user-bookmarks-drafts'),
    path('userblocks', views.UserBlocksList.as_view(), name='user-blocks-list'),
    path('userblocks/<int:pk>/', views.UserBlocksDetail.as_view(), name='userblocks-detail'),
    path('users/<str:username>/userblocks', views.UserBlocksList.as_view(), name='user-blocks-list'),
    path('search/', views.SearchList.as_view(), name='search-list'),
    path('fingerguns/', views.FingergunList.as_view(), name='fingergun-list'),
    path('fingerguns/<int:pk>/', views.FingergunDetail.as_view(), name='fingergun-detail'),
    path('works/<int:work_id>/fingerguns', views.FingergunByWorkList.as_view(), name='fingergun-by-work-list'),
    path('tag-autocomplete', views.TagAutocomplete.as_view(), name='tag-autocomplete'),
    path('invitations/', views.Invitations.as_view(), name='invitations'),
    path('attributetypes/', views.AttributeTypeList.as_view(), name='attribute-type-list'),
    path('attributetypes/<int:pk>/', views.AttributeTypeDetail.as_view(), name='attributetype-detail'),
    path('attributevalues/', views.AttributeValueList.as_view(), name='attribute-value-list'),
    path('attributevalues/<int:pk>/', views.AttributeValueDetail.as_view(), name='attributevalue-detail'),
    path('file-upload/', views.FileUpload.as_view(), name='api-file-upload'),
    path('bookmark-autocomplete', views.BookmarkAutocomplete.as_view(), name='bookmark-autocomplete'),
    path('contentpages/', views.ContentPageList.as_view(), name='content-page-list'),
    path('contentpages/<int:pk>', views.ContentPageDetail.as_view(), name='content-page-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
