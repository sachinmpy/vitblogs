from django.shortcuts import render, redirect
from decorators import redirect_authenticated, redirect_non_staff
from django.contrib.auth.decorators import login_required
from .models import Tags, Blog
from .forms import BlogCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from images_urls import get_random_image
from categories.models import Category, CategoryList

# Typing imports
from django.http import HttpRequest
from django.shortcuts import HttpResponse, HttpResponseRedirect

# TODO
# - Convert function based views to Class based views
# - Add Likes and Dislike functionality
# - Add Image upload, or make handling images seamless


def blog_page(request: HttpRequest) -> HttpResponse:  # Not Working
    """
    Page dedicated to show all the blogs posted in recent times
    this is second most important page in entire website


    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    _blogs = Blog.objects.filter(is_approved=True).exclude(is_archived=True)

    context: dict = {"blogs": _blogs,  "image_func": get_random_image}

    return render(request, "blogs/allblogs.html", context=context)


def blog(request: HttpRequest, blog_id: str) -> HttpResponse:
    """
    Actual Blog which is written by users of the site,
    it takes blog_id to find the page in database

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    blog_id : str
        unique ID of blog to find blog in website

    Returns
    -------
    HttpResponse
        a HTML file
    """

    _blog = Blog.objects.get(blog_id=blog_id)

    context: dict = {"blog": _blog, "image_func": get_random_image}

    return render(request, "blogs/blog.html", context=context)


@login_required(login_url="loginuser")
def create_blog(request: HttpRequest) -> HttpResponse:
    """
    this function will send webpage to user where they can create their blogs

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    user = request.user
    form = BlogCreationForm(
        {"create_by": user}
    )

    context: dict = {"form": form}

    

    # Reciving to create and save forms
    if request.method == "POST":
        form = BlogCreationForm(request.POST)
        form_tags = request.POST["tags"]
        # cleans tags, adds new tags that are already not present
        # in the tags list
        cleaned_tags = handle_tags(form_tags)

        # Checking for category
        category_tag = request.POST["category"]
        _category = Category.objects.get(pk=int(category_tag))

        if form.is_valid():
            f = form.save()
            CategoryList.objects.create(category_name=_category, blog=f)
            messages.success(request, "Blog has been posted")
            return redirect("blog_page")
        else:
            messages.error(request, "Something went wrong")
            return redirect("create_blog")
    return render(request, "blogs/createblog.html", context=context)


def handle_tags(tags: str) -> None:
    """
    cleaning tag and adding new tags into database

    Parameters
    ----------
    tags: str
        tags are passed with #values

    Returns
    -------
    None
    """
    if not tags:
        return ""

    all_tags = Tags.objects.all()
    tags = tags.split(" ")
    cleaned_tags = []

    # Cleaning tags from its whitespace and #
    for tag in tags:
        if len(tag.strip()) > 16:
            continue
        tag = tag.strip()
        if tag[0] == "#":
            cleaned_tags.append(tag[1:])

    # Saving Cleaned tags that are new
    for cleaned_tag in cleaned_tags:
        if cleaned_tag not in all_tags:
            Tags(tag=cleaned_tag).save()

    k = " ".join(cleaned_tags)
    return k


@login_required(login_url="loginuser")
@redirect_non_staff
def unverifed_blogs(request: HttpRequest) -> HttpResponse:
    """
    list and displays all the unverified blogs

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    _unverified_blogs = Blog.objects.filter(is_approved=False)

    context: dict = {"blogs": _unverified_blogs, "image_func": get_random_image}

    return render(request, "blogs/unverifiedblogs.html", context=context)


@login_required(login_url="loginuser")
@redirect_non_staff
def verify_blog(
    request: HttpRequest, blog_id: str
) -> HttpResponseRedirect:  # Not working
    """
    function that will verify blog into a verifed blog

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """
    if not request.user.is_authenticated:
        return redirect("/")

    try:
        _blog = Blog.objects.get(blog_id=blog_id)

    except ObjectDoesNotExist as e:
        messages.error(request, message="Blog does not exist")
        return redirect("/")

    # if blog is already approved by someone
    # redirct them to the original page
    if _blog.is_approved:
        messages.error(request, message="Error? Blog was already approved")
        return redirect("unverified_blogs")

    _blog.is_approved = True
    _blog.approved_by = request.user
    _blog.save()

    messages.success(request, message=f"Blog Approved by {request.user}")
    return redirect("unverified_blogs")


@login_required(login_url="loginuser")
@redirect_non_staff
def archive_blog(
    request: HttpRequest, blog_id: str
) -> HttpResponseRedirect:  # Not working
    """
    function that will archive blog 

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    if not request.user.is_authenticated:
        return redirect("/")

    try:
        _blog = Blog.objects.get(blog_id=blog_id)

    except ObjectDoesNotExist as e:
        messages.error(request, message="Blog does not exist")
        return redirect("/")

    # if blog is already approved by someone
    # redirct them to the original page
    if _blog.is_archived:
        messages.error(request, message="Error? Blog was already archived")
        return redirect("unverified_blogs")

    _blog.is_archived = True
    _blog.is_approved = True
    _blog.approved_by = request.user
    _blog.save()

    messages.success(request, message=f"Blog Archived by {request.user}")
    return redirect("unverified_blogs")