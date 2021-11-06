from rest_framework.views import APIView
from rest_framework.response import Response
from wishlist.models import *
from wishlist.serializers import *
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime, requests
from google_auth_oauthlib import flow
from google.cloud import bigquery
from google.oauth2 import service_account


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado!')

        if not user.check_password(password):
            raise AuthenticationFailed('contraseña incorrecta')

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm = 'HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
        }
        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class Index(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        return Response("API Google Book")

class Title_Author_Publisher(APIView):
    def get(self, request,title=None,author=None,publisher=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        book_search = requests.get('https://www.googleapis.com/books/v1/volumes?q=+intitle:'+title+'+inauthor:'+author+'+inpublisher:'+publisher+'+&'+apikey+'').json()
        items = book_search['items']
        books = []
        for book in items:
            try:
                id = book['id']
                titulo=book['volumeInfo']['title']
                autor=book['volumeInfo']['authors']
                editorial=book['volumeInfo']['publisher']
                data = {"ID":id,
                        "Titulo":titulo,
                        "Autor":autor,
                        "Editorial":editorial
                        }
                books.append(data)
            except KeyError:
                next
        return Response(books)


class Title_Author(APIView):
    def get(self, request,title=None,author=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        book_search = requests.get('https://www.googleapis.com/books/v1/volumes?q=+intitle:'+title+'+inauthor:'+author+'+&'+apikey+'').json()
        items = book_search['items']
        books = []
        for book in items:
            try:
                id = book['id']
                titulo=book['volumeInfo']['title']
                autor=book['volumeInfo']['authors']
                data = {"ID":id,
                        "Titulo":titulo,
                        "Autor":autor
                        }
                books.append(data)
            except KeyError:
                next
        return Response(books)

class Title_Publisher(APIView):
    def get(self, request,title=None,publisher=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        book_search = requests.get('https://www.googleapis.com/books/v1/volumes?q=+intitle:'+title+'+inpublisher:'+publisher+'+&'+apikey+'').json()
        items = book_search['items']
        books = []
        for book in items:
            try:
                id = book['id']
                titulo=book['volumeInfo']['title']
                editorial=book['volumeInfo']['publisher']
                data = {"ID":id,
                        "Titulo":titulo,
                        "Editorial":editorial
                        }
                books.append(data)
            except KeyError:
                next
        return Response(books)


class Author_Publisher(APIView):
    def get(self, request,author=None,publisher=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        book_search = requests.get('https://www.googleapis.com/books/v1/volumes?q=+inauthor:'+author+'+inpublisher:'+publisher+'+&'+apikey+'').json()
        items = book_search['items']
        books = []
        for book in items:
            try:
                id = book['id']
                autor=book['volumeInfo']['authors']
                editorial=book['volumeInfo']['publisher']
                data = {"ID":id,
                        "Autor":autor,
                        "Editorial":editorial
                        }
                books.append(data)
            except KeyError:
                next
        return Response(books)


class My_BookShelves_Public_All(APIView):
    def get(self, request,user=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        my_bookshelve = requests.get('https://www.googleapis.com/books/v1/users/'+str(user)+'/bookshelves?'+apikey+'').json()
        return Response(my_bookshelve)


class My_BookShelves_Public_Specific(APIView):
    def get(self, request,user=None,bookshelve=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        my_bookshelve = requests.get('https://www.googleapis.com/books/v1/users/'+str(user)+'/bookshelves/'+str(bookshelve)+'?'+apikey+'').json()
        return Response(my_bookshelve)


class List_BookShelves_Public(APIView):
    def get(self, request,user=None,bookshelve=None,volumes=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        list_bookshelve = requests.get('https://www.googleapis.com/books/v1/users/'+str(user)+'/bookshelves/'+str(bookshelve)+'/volumes?'+apikey+'').json()
        items = list_bookshelve['items']
        books = []
        for book in items:
            try:
                id = book['id']
                titulo=book['volumeInfo']['title']
                autor=book['volumeInfo']['authors']
                editorial=book['volumeInfo']['publisher']
                data = {"ID":id,
                        "Titulo":titulo,
                        "Autor":autor,
                        "Editorial":editorial
                        }
                books.append(data)
            except KeyError:
                next
        return Response(books)


class List_BookShelves_Private(APIView):
    def get(self, request,user=None,bookshelve=None,volumes=None,apikey=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Sin autenticar')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sin autenticar')
        
        list_bookshelve = requests.get('https://www.googleapis.com/books/v1/mylibrary/bookshelves?'+apikey+'').json()
        return Response(list_bookshelve)


class callAPI(APIView):
    def get(self, request):
        launch_browser = True


        appflow = flow.InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json", scopes=["https://www.googleapis.com/auth/bigquery"]
        )

        if launch_browser:
            appflow.run_local_server()
        else:
            appflow.run_console()

        credentials = appflow.credentials

class connectBigQuery(APIView):
    def get(self, request):
        project = 'vivid-access-326620'

        client = bigquery.Client(project=project, credentials="721070450478-ub4jtf0rfoli3vi5k2qe5q4sh86nastb.apps.googleusercontent.com")

        query_string = """SELECT name, SUM(number) as total
        FROM `bigquery-public-data.usa_names.usa_1910_current`
        WHERE name = 'William'
        GROUP BY name;
        """
        query_job = client.query(query_string)

        # Print the results.
        for row in query_job.result():  # Wait for the job to complete.
            print("{}: {}".format(row["name"], row["total"]))


class getToken(APIView):
    def get(self,request):
        target_audience = 'http://localhost:8000/'

        creds = service_account.IDTokenCredentials.from_service_account_file(
        r'C:\Users\Esteban Henao\Documents\book_wishlist4\client_secrets.json',
        target_audience=target_audience)