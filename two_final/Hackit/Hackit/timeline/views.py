from django.views import generic
from .models import Post, Like ,Post_1, Like_1
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm,PostForm_1
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http.response import JsonResponse

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    paginate_by = 10
    def get_queryset(self):
        posts = Post.objects.order_by('-created_at')
        return posts

index = IndexView.as_view()

class CreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    success_url = reverse_lazy('timeline:index')
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました。')
        return super(CreateView, self).form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました。')
        return redirect('timeline:index')

create = CreateView.as_view()

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('timeline:index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user:
            messages.success(self.request, '削除しました。')
            return super().delete(request, *args, **kwargs)

delete = DeleteView.as_view()

class LikeView(LoginRequiredMixin, generic.View):
    model = Like
    def post(self, request):
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        like_item = Like(user=self.request.user, post=post)
        like_item.save()
        like_count = Like.objects.filter(post=post).count()
        data = {'message': 'いいねしました', 'like_count': like_count}
        return JsonResponse(data)

like = LikeView.as_view()

#ここから下が変更箇所
#####
class IndexView_1(LoginRequiredMixin, generic.ListView):
    template_name = 'index_1.html'
    paginate_by = 10
    def get_queryset(self):
        posts_1 = Post_1.objects.order_by('-created_at')
        return posts_1

index_1 = IndexView_1.as_view()

