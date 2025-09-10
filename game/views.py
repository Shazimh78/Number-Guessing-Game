from django.shortcuts import render
import random

def home(request):
    # Use session to store secret number so it doesn’t reset every time
    if "secret_number" not in request.session:
        request.session["secret_number"] = random.randint(1, 100)

    secret_number = request.session["secret_number"]
    result = ""

    guess = request.GET.get("guess")  # read guess from form
    if guess:
        guess = int(guess)
        if guess == secret_number:
            result = f"🎉 Correct! The number was {secret_number}."
            # Reset game
            request.session.pop("secret_number")
        elif guess < secret_number:
            result = "Too low! Try again."
        else:
            result = "Too high! Try again."

    return render(request, "game/home.html", {"result": result})
