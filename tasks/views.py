from django.shortcuts import render


# Задание 1
def index(request):
    user_name = "Руслан"
    context = {
        'user_name': user_name
    }
    return render(request, 'index.html', context)

def task_2(request):
    context = {
        'name': 'Павел',
        'age': 45,
        'phone': '89234567891',
        'email': 'pavel@pavel.com'
    }
    return render(request, 'task_2.html', context )

def task_3(request):
    context = {
        'profile_data': {
            'name': 'Павел',
            'age': 45,
            'phone': '89234567891',
            'email': 'pavel@pavel.com'
        }
    }
    return render(request, 'task_3.html', context )

def task_4(request):
    profile_data = ['Павел', 45, '+79234567891', 'pavel@pavel.com']
    return render(request, 'task_4.html', {'profile_data': profile_data})

def task_5(request):
    return render(request, 'task_5.html' )

def task_6(request):
    name = "Павел"
    experience = 6

    context = {
        'name': name,
        'experience': experience
    }
    return render(request, 'task_6.html', context )

def task_7(request):
    user_list = ['Игорь', 'Андрей', 'Дмитрий', 'Алексей', 'Николай', 'Евгений', 'Иван', 'Павел', 'Руслан', 'Денис']
    return render(request, 'task_7.html', {'user_list': user_list} )

def task_8(request):
    user_list = [{'name': 'Дмитрий', 'experience': 9},
                 {'name': 'Павел', 'experience': 5},
                 {'name': 'Алексей', 'experience': 3},
                 {'name': 'Иван', 'experience': 0},
                 {'name': 'Денис', 'experience': 2},
                 {'name': 'Игорь', 'experience': 7},
                 {'name': 'Руслан', 'experience': 1},
                 {'name': 'Евгений', 'experience': 4},
                 {'name': 'Андрей', 'experience': 2},
                 {'name': 'Николай', 'experience': 8}]
    return render(request, 'task_8.html', {'user_list': user_list})

def task_9(request):
    return render(request, 'task_9.html' )

def task_10(request):
    tmpl_name = 'employee_list.html'
    return render(request, 'task_10.html', {'tmpl_name': tmpl_name} )

def employee_list(request):
    return render(request, 'employee_list.html' )

def default_employees(request):
    return render(request, 'default_employees.html')