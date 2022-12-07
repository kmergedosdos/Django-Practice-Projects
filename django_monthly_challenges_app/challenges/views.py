from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Challenge for january",
  "february": "Challenge for february",
  "march": "Challenge for march",
  "april": "Challenge for april",
  "may": "Challenge for may",
  "june": "Challenge for june",
  "july": "Challenge for july",
  "august": "Challenge for august",
  "september": "Challenge for september",
  "october": "Challenge for october",
  "november": "Challenge for november",
  "december": None
}

# Create your views here.
def index(request):
  context = {
    "months": list(monthly_challenges.keys())
  }
  return render(request, 'challenges/index.html', context)

def monthly_challenge_by_number(request, month):
  try:
    challenge_month = list(monthly_challenges.keys())[month - 1]
    route_redirect = reverse('monthly-challenge', args=[challenge_month])
    return HttpResponseRedirect(route_redirect)
  except:
    return HttpResponseNotFound("<h1>This month is not supported!!!</h1>")

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    context = {
      "month": month,
      "challenge": challenge_text
    }
    return render(request, 'challenges/challenge.html', context)
  except:
    raise Http404()