from django.shortcuts import render
from urllib.parse import parse_qs
from collections import Counter

# Create your views here.
secret_nums = [5, 1, 2, 9]


def index_view(request):
    return render(request, "index.html")


def create_solution(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        request.POST = request.body.decode()
        request_body = parse_qs(request.POST)
        if request_body.get("numbers"):
            numbers_str = request_body["numbers"][0].split()
            number_of_elements = len(numbers_str)
            set_numbers_str = set(numbers_str)
            try:
                numbers_int = [int(x) for x in numbers_str]
                number_of_elements = len(numbers_int)
                if number_of_elements != 4:
                    result = "vvedite 4 chsila"
                elif len(set_numbers_str) != len(numbers_str):
                    result = "vvedite unikalnie chisla"
                elif numbers_int[0] not in range(1, 10):
                    result = "vvedite chisla ot 1 do 9"
                elif numbers_int[1] not in range(1, 10):
                    result = "vvedite chisla ot 1 do 9"
                elif numbers_int[2] not in range(1, 10):
                    result = "vvedite chisla ot 1 do 9"
                elif numbers_int[3] not in range(1, 10):
                    result = "vvedite chisla ot 1 do 9"
                else:
                    bull, cow = 0, 0
                    s = list(secret_nums)
                    g = list(numbers_int)

                    i, j = 0, 0
                    while i < len(secret_nums):
                        if s[j] == g[j]:
                            bull += 1
                            s.pop(j)
                            g.pop(j)
                        else:
                            j += 1
                        i += 1

                    count = Counter(s)

                    for l in g:
                        if l in count and count[l] > 0:
                            cow += 1
                            count[l] -= 1

                    if bull == 4:
                        result = "You got it right!"
                    else:
                        result = "You got {bull} bulls, {cow} cows".format(bull=bull, cow=cow)
            except ValueError:
                result = "Vi vveli ne korrektnoe znachene"
            context = {
                "result": result
            }
            print(request_body.get("numbers"))
    return render(request, "solution.html", context)
