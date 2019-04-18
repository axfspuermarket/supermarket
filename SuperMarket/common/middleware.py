#Author    :MrDan
# -*- coding: utf-8 -*-
import logging
from django.utils.deprecation import MiddlewareMixin
from user.models import User
from lib.httplib import render_json
from common import errors,keys
from django.core.cache import cache

error_logger = logging.getLogger("err")

class AuthMiddleware(MiddlewareMixin):
    #请求过滤
    URL_WHITE_LIST = [
        '/usr/api/submit_phone',
        '/usr/api/submit_vcode',
    ]
    URL_NOT_POST_LIST=[
        '/usr/api/get_profile',
        '/social/api/get_rcmd_user'
        '/social/api/regret',
        '/social/api/get_who_liked_me'
    ]

    def process_request(self, request):
        path = request.path
        for URL in  self.URL_WHITE_LIST:
            if path in URL:
                return
        if request.method != "POST" and not request.path in self.URL_NOT_POST_LIST:
            return render_json('Request Method Error!', errors.Host_Error.BAD_REQUEST.code)
        uid = request.session.get('uid')
        if not uid:
            return render_json('User Not Login!', errors.User_Error.NOT_IDENT.code)

        try:
            user = User.objects.get(id=uid)
            request.user = user
        except User.DoesNotExist:
            return render_json('Not This User!', errors.User_Error.NOT_IDENT.code)
    def process_response(self,request,response):
        # print(response)
        return response

class ExceptionHandlerMiddleware(MiddlewareMixin):
    #报错模块
    def process_exception(self, request, exception):
        if isinstance(exception, errors.LogiceError):
            error_logger.error(f"Code:{exception.code}:\r Msg:{exception.msg}")
            return render_json(exception.msg, exception.code)


class SeverHandlerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print(request.META.get("HTTP_HOST"))
        # HTTP_USER_AGENT
        key = keys.HOST_KEY%request.META.get("HTTP_HOST")
        count = cache.get(key,0)
        if count > 2:
            cache.set(key, count, 60)
            return render_json(errors.REQUEST_FORBID.msg, errors.REQUEST_FORBID.code)
        count += 1
        cache.set(key,count,2)
