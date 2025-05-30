from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import JsonResponse
import jwt, datetime
from users.models import Users


# class JWTAuthenticationMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         token = request.COOKIES.get('jwt')
#         print('i am in middlewRE ...')
#         if not token:
#             request.user = None
#             return
#         try:
#             # token = token.encode('utf-8')
#
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#             user = Users.objects.get(id=payload['id'])
#             request.user = user
#         except (jwt.ExpiredSignatureError, jwt.DecodeError, Users.DoesNotExist):
#             request.user = None
#             return JsonResponse({"error": "Authentication Failed in middleware"}, status=401)


# zarino/middleware.py
class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token_str = request.COOKIES.get('jwt') # بهتر است نام را برای وضوح تغییر دهیم
        print('i am in middlewRE ...')
        if not token_str:
            request.user = None
            print("i am in middlewRE ----> not token_str")
            return
        try:
            token_bytes = token_str.encode('utf-8') # <<<<< این خط را فعال و اصلاح کنید
            payload = jwt.decode(token_bytes, 'secret', algorithms=['HS256'])
            user = Users.objects.get(id=payload['id'])
            request.user = user
            print(f"User {user.username} authenticated by middleware.") # برای دیباگ
        except jwt.ExpiredSignatureError:
            print("Middleware: Token expired.") # برای دیباگ
            request.user = None
            return JsonResponse({"detail": "Authentication Failed: Token has expired."}, status=401)
        except jwt.DecodeError as e:
            print(f"Middleware: Token decode error: {e}") # برای دیباگ
            request.user = None
            return JsonResponse({"detail": f"Authentication Failed: Invalid token ({e})."}, status=401)
        except Users.DoesNotExist:
            print("Middleware: User from token does not exist.") # برای دیباگ
            request.user = None
            return JsonResponse({"detail": "Authentication Failed: User not found."}, status=401)
        except Exception as e: # برای گرفتن خطاهای پیش‌بینی نشده دیگر
            print(f"Middleware: Unexpected error: {e}") # برای دیباگ
            request.user = None
            return JsonResponse({"detail": f"Authentication Failed: Unexpected error."}, status=401)