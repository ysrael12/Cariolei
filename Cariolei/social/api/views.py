
from django.shortcuts import render
from django.http import JsonResponse
from social.models import Post
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def TheModelView(request):

    if (request.method == "GET"):
        #Serialize the data into json
        data = serializers.serialize("json", Post.objects.all())
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

    if (request.method == "POST"):
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        #create the new item
        newrecord = Post.objects.create(item=body['item'])
        # Turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', [newrecord]))
        # send json response with new object
        return JsonResponse(data, safe=False)

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def TheModelViewTwo(request, id):
        if (request.method == "PUT"):
        # Turn the body into a dict
            body = json.loads(request.body.decode("utf-8"))
        # update the item
            Post.objects.filter(pk=id).update(item=body['item'])
            newrecord = Post.objects.filter(pk=id)
        # Turn the object to json to dict, put in array to avoid non-iterable error
            data = json.loads(serializers.serialize('json', newrecord))
        # send json response with updated object
            return JsonResponse(data, safe=False)

        if (request.method == "DELETE"):
        # delete the item, get all remaining records for response
            Post.objects.filter(pk=id).delete()
            newrecord = Post.objects.all()
        # Turn the results to json to dict, put in array to avoid non-iterable error
            data = json.loads(serializers.serialize('json', newrecord))
        # send json response with updated object
            return JsonResponse(data, safe=False)