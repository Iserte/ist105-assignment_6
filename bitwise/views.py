from django.shortcuts import render
from .forms import EntryForm
from .models import Entry

def process_numbers(request):
    result = {}
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nums = [data['a'], data['b'], data['c'], data['d'], data['e']]

            negatives = [n for n in nums if n < 0]
            avg = sum(nums) / len(nums)
            positives = [n for n in nums if n > 0]
            even_odd = ['even' if n & 1 == 0 else 'odd' for n in nums]
            sorted_values = sorted([n for n in nums if n > 10])
            warning = 'Negative values detected!' if negatives else ''

            entry = Entry.objects.create(
                a=data['a'],
                b=data['b'],
                c=data['c'],
                d=data['d'],
                e=data['e'],
                average=avg,
                positive_count=len(positives),
                even_odd=even_odd,
                sorted_values=sorted_values,
                warning=warning
            )

            result = {
                'original': nums,
                'sorted': sorted_values,
                'average': avg,
                'positive_count': len(positives),
                'even_odd': even_odd,
                'warning': warning
            }

    else:
        form = EntryForm()

    return render(request, 'bitwise/results.html', {'form': form, 'result': result})