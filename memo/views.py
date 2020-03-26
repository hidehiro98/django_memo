from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Memo
from .forms import MemoForm

def show(request): # idから表示するmemoを取得
    memo_id = request.GET.get('id')
    memo = Memo.objects.get(pk=memo_id)
    return HttpResponse("%s" % (memo.content))

def create(request): # GETメソッドの場合フォームを表示、POSTの場合memoを保存
    if request.method == 'GET':
        form = MemoForm()
        return render(request, 'create.html', {'form': form})
    elif request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('/memo?id=%s' % memo.pk)