from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UserAccount
from .forms import *

# Create your views here.

def home(request):
    useraccount = UserAccount.objects.order_by('name')
    return render(request, 'home.html', {'useraccount' : useraccount})

# create a user account record 
def create_user_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserAccountForm()
    return render(request, 'create_user_account.html', {'form' : form})

def update_user_account(request, pk):
    useraccount = get_object_or_404(UserAccount, pk=pk)
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=useraccount)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserAccountForm(instance=useraccount)
    return render(request, 'update_user_account.html', {'form' : form, 'useraccount' : useraccount})

# delete a user account 
def delete_user_account(request, pk):
    useraccount = get_object_or_404(UserAccount, pk=pk)
    if request.method == 'POST':
        useraccount.delete()
        return redirect('home')
    return render(request, 'delete_user_account.html', {'useraccount' : useraccount})

# view for a specific User account
def list_user_account(request, pk):
    user_account = get_object_or_404(UserAccount, pk=pk)
    entries = user_account.userdata_set.all().order_by('first_name')
    return render(request, 'list_user_account.html', {'user_account' : user_account, 'entries' : entries, 'count' : entries.count()})


# create a user entry
def create_user_data(request, pk):
    useraccount = get_object_or_404(UserAccount, pk=pk)
    if request.method == 'POST':
        form = UserDataForm(request.POST, useraccount=useraccount)
        if form.is_valid():
            form.save()
            return redirect('list_user_account', pk)
    else:
        form = UserDataForm(useraccount=useraccount)
    return render(request, 'create_user_data.html', {'form' : form, 'useraccount' : useraccount})


# list the user data entries
def list_user_data(request, pk):
    userdata = get_object_or_404(UserData, pk=pk)
    entries = userdata.entry_set.all()
    total = 0
    for entry in entries:
        total += entry.value

    return render(request, 'list_user_data.html', {'entries' : entries, 'userdata' : userdata, 'total' : total})

# update a user data
def update_user_data(request, pk):
    user_data = get_object_or_404(UserData, pk=pk)
    user_account = user_data.useraccount
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=user_data)
        if form.is_valid():
            form.save()
            return redirect('list_user_account', pk=user_account.pk)
    else:
        form = UserDataForm(instance=user_data)
    return render(request, 'update_user_data.html', {'form' : form, 'user_data' : user_data})

# delete a user data
def delete_user_data(request, pk):
    user_data = get_object_or_404(UserData, pk=pk)
    user_account = user_data.useraccount
    if request.method == 'POST':
        user_data.delete()
        return redirect('list_user_account', pk=user_account.pk)
    return render(request, 'delete_user_data.html', {'user_data' : user_data})
    
# create an entry
def create_entry(request, pk):
    userdata = get_object_or_404(UserData, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, userdata=userdata)
        if form.is_valid():
            form.save()
            return redirect('list_user_data', pk)
    else:
        form = EntryForm(userdata=userdata)
    return render(request, 'create_entry.html', {'form' : form, 'userdata' : userdata})

# view to update a given record in the form
# update an entry
def update_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    userdata = entry.userdata
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('list_user_data', pk=userdata.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'update_entry.html', {'form' : form})

# delete an entry for a data
def delete_entry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    userdata = entry.userdata
    if request.method == 'POST':
        entry.delete()
        return redirect('list_user_data', pk=userdata.pk)
    return render(request, 'delete_entry.html', {'userdata' : userdata})
