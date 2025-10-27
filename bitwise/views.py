from django.shortcuts import render
from .forms import NumberForm
from pymongo import MongoClient

uri = 'mongodb://<MongoDB-EC2-IP>:27017/'

def process_numbers(request):
    result = {}
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            nums = [form.cleaned_data[x] for x in ['a', 'b', 'c', 'd', 'e']]
            negatives = [n for n in nums if n < 0]
            avg = sum(nums) / len(nums)
            positives = [n for n in nums if n > 0]
            even_odd = ['even' if n & 1 == 0 else 'odd' for n in nums]
            filtered_sorted = sorted([n for n in nums if n > 10])

            result = {
                'original': nums,
                'sorted': filtered_sorted,
                'average': avg,
                'positive_count': len(positives),
                'even_odd': even_odd,
                'warning': 'Negative values detected!' if negatives else None
            }

            # Save to MongoDB
            client = MongoClient(uri)
            db = client.assignment6
            db.entries.insert_one({'input': nums, 'result': result})

    else:
        form = NumberForm()

    return render(request, 'bitwise/results.html', {'form': form, 'result': result})