#Author    :MrDan
# -*- coding: utf-8 -*-
import logging
import re

from django.utils.deprecation import MiddlewareMixin
from user.models import User
from lib.httplib import render_json
from common import errors,keys
from django.core.cache import cache

error_logger = logging.getLogger("err")

class AuthMiddleware(MiddlewareMixin):
    #请求过滤
    URL_NOT_LOGIN = [
        '/api/login/',
        '/api/sms/',
        '/admin/',

    ]
    URL_NOT_POST_LIST=[
        '/api/address/',
        '/admin/',
    ]

    def process_request(self, request):
        path = request.path
        not_login_allow = False
        for URL in  self.URL_NOT_LOGIN:
            patten = f".*{URL}.*"
            if re.match(patten, path):
                not_login_allow = True
                # print(111,patten, path)
                break
        #请求方式不为post且需POST请求,则抛出错误
        if request.method != "POST" :
            not_request_allow = False
            for URL in self.URL_NOT_POST_LIST:
                patten = f".*{URL}.*"
                # print(patten, path)
                if re.match(patten, path):
                    not_request_allow = True
                    # print(222, patten, path)
                    break
            if not not_request_allow:
                return render_json(None,'Request Method Error!', errors.Host_Error.BAD_REQUEST.code)
        uid = request.session.get('uid')
        if (not uid) and (not not_login_allow) :
            return render_json(None,'User Not Login!', errors.User_Error.NOT_IDENT.code)
        if not not_login_allow:
            try:
                user = User.objects.get(id=uid)
                request.user = user
            except User.DoesNotExist:
                return render_json('Not This User!', errors.User_Error.NOT_IDENT.code)

    # def process_response(self,wsgi, response):
        # response.append('Access-Control-Allow-Origin')
        # print(wsgi,response)

class ExceptionHandlerMiddleware(MiddlewareMixin):
    #报错模块
    def process_exception(self, request, exception):
        if isinstance(exception, errors.LogiceError):
            error_logger.error(f"Code:{exception.code}:\r Msg:{exception.msg}")
            return render_json(None,code=exception.code, msg=exception.msg)


class SeverHandlerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print(request.META.get("HTTP_HOST"))
        # HTTP_USER_AGENT
        key = keys.HOST_KEY%request.META.get("HTTP_HOST")
        count = cache.get(key,0)
        if count > 2:
            cache.set(key, count, 60)
            return render_json(errors.Host_Error.REQUEST_FORBID.msg, errors.Host_Error.REQUEST_FORBID.code)
        count += 1
        cache.set(key,count,1)
