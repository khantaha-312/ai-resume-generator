from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import google.generativeai as genai
api_key = "AIzaSyB553SsyZ1vYqTnCXUGBO7pZIY0Yufbo5g"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro")

# Separate objective text for each template
objectives = {
    "template1": "Motivated Python developer with strong programming skills...",
    "template2": "Experienced developer seeking a role in machine learning...",
    "template3": "Skilled in web development and eager to expand knowledge..."
}

def home(request):
    return render(request, 'index.html', {'objective': objectives.get("template1")})

def template1(request):
    return render(request, 'template1.html', {'objective': objectives.get("template1")})

def template2(request):
    return render(request, 'template2.html', {'objective': objectives.get("template2")})

def template3(request):
    return render(request, 'template3.html', {'objective': objectives.get("template3")})

def update_objective(request):
    if request.method == 'POST':
        template_name = request.POST.get('template')
        new_objective = request.POST.get('new_objective')
        if template_name and new_objective:
            objectives[template_name] = new_objective
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid request.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def generate_resume(request):
    if request.method == 'POST':
        template_name = request.POST.get('template')
        if template_name:
            objective = objectives.get(template_name, "Professional seeking a challenging role.")
            try:
                response = model.generate_content(
                    f"Write a professional resume for a {objective}. Include sections: Objective, Skills, Experience, Education, and Projects."
                )
                resume_text = response.text
            except Exception as e:
                resume_text = f"Error generating resume: {str(e)}"

            return render(request, 'resume_output.html', {
                'resume_text': resume_text,
                'objective': objective
            })
        else:
            return render(request, 'generate_resume.html', {'error': 'No template selected.'})
    return render(request, 'generate_resume.html', {'templates': objectives.keys()})




# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render, redirect
# import google.generativeai as genai
# api_key = "AIzaSyB553SsyZ1vYqTnCXUGBO7pZIY0Yufbo5g"
# genai.configure(api_key=api_key)
#
# model = genai.GenerativeModel("gemini-1.5-pro")
#
# # Separate objective text for each template
# objectives = {
#     "template1": "Motivated Python developer with strong programming skills...",
#     "template2": "Experienced developer seeking a role in machine learning...",
#     "template3": "Skilled in web development and eager to expand knowledge..."
# }
#
# def home(request):
#     return render(request, 'index.html', {'objective': objectives.get("template1")})
#
# def template1(request):
#     return render(request, 'template1.html', {'objective': objectives.get("template1")})
#
# def template2(request):
#     return render(request, 'template2.html', {'objective': objectives.get("template2")})
#
# def template3(request):
#     return render(request, 'template3.html', {'objective': objectives.get("template3")})
#
# # Function to generate text
# def generate_text(prompt):
#     response = model.generate_content(prompt)
#     return response.text
# def update_objective(request):
#     if request.method == "POST":
#         new_objective = request.POST.get('new_objective')
#         if new_objective == 'Other':
#             new_objective = request.POST.get('other_profession')
#
#         # Capture the origin template
#         origin_template = request.POST.get('origin_template')
#
#         # Update the objective in the objectives dictionary
#         objectives[origin_template] = new_objective
#
#         # Return success and new objective
#         return JsonResponse({'success': True, 'new_objective': new_objective})
#     return JsonResponse({'success': False})