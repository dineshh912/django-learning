# api/views.py
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView
) 
from books.models import Book
from todos.models import Todo
from ..serializers.todo_serializers import TodoSerializers


class BookListAPIView(ListAPIView):
    """
        Book List API View
    """
    queryset = Book.objects.all()
    # serializer_class = BookSerializers


class TodoListAPIView(ListAPIView):
    """
        Todo List API View
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class TodoDetailAPIView(RetrieveAPIView):
    """
        Todo Detail API View
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers