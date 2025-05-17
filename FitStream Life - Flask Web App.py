# FitStream Life - Flask Web App (Python Equivalent)


from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FitStream Life</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-white text-gray-800 font-sans">
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-10 text-center">
        <h1 class="text-4xl font-bold mb-4">Get Fit. Stay Strong. On Your Terms.</h1>
        <p class="text-lg mb-6">Discover top fitness gear, workout plans, and nutrition tools — all from the comfort of your home.</p>
        <div class="space-x-4">
            <button class="bg-white text-blue-600 font-semibold px-6 py-2 rounded-xl shadow-md">Start Your Fitness Plan</button>
            <button class="bg-white text-purple-600 font-semibold px-6 py-2 rounded-xl shadow-md">Explore Gear Guides</button>
        </div>
    </section>

    <!-- Why FitStream Life -->
    <section class="p-10 grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
        <div>
            <h3 class="text-xl font-bold mb-2">🏋️‍♂️ Fitness Without Barriers</h3>
            <p>Everything you need to succeed — without an expensive gym membership.</p>
        </div>
        <div>
            <h3 class="text-xl font-bold mb-2">🔗 Curated, Trusted Products</h3>
            <p>Hand-picked fitness tools that we love (affiliate links included).</p>
        </div>
        <div>
            <h3 class="text-xl font-bold mb-2">📩 No-Nonsense Guidance</h3>
            <p>Get results with simple, sustainable workout and nutrition advice.</p>
        </div>
    </section>

    <!-- Featured Resources -->
    <section class="bg-gray-100 p-10">
        <h2 class="text-2xl font-bold text-center mb-6">✅ Top Picks This Month</h2>
        <ul class="max-w-xl mx-auto space-y-4 text-blue-600">
            <li><a href="#">Best Yoga Mats for Home Workouts – 2025 Edition</a></li>
            <li><a href="#">Top 5 Fitness Apps You Can Start Using Today</a></li>
            <li><a href="#">Adjustable Dumbbells: Our Favorite Budget Option</a></li>
        </ul>
    </section>

    <!-- Mailchimp Form -->
    <section class="p-10 text-center">
        <h2 class="text-2xl font-bold mb-4">🎁 Get Your Free 7-Day Home Workout Plan</h2>
        <p class="mb-6">Enter your email to receive a downloadable PDF with daily workouts and a meal plan.</p>
        <form action="https://YOUR_MAILCHIMP_URL" method="post" target="_blank" class="flex flex-col items-center space-y-4">
            <input type="email" name="EMAIL" placeholder="Your email" required class="px-4 py-2 border rounded-xl w-64">
            <button type="submit" class="bg-blue-600 text-white px-6 py-2 rounded-xl shadow-md">Get My Plan</button>
        </form>
    </section>

    <!-- Blog Section -->
    <section class="bg-gray-100 p-10">
        <h2 class="text-2xl font-bold text-center mb-6">📝 From the Blog</h2>
        <ul class="max-w-xl mx-auto space-y-4 text-gray-800">
            <li><a href="#" class="hover:underline">How to Start Working Out from Home [Beginner’s Guide]</a></li>
            <li><a href="#" class="hover:underline">My Honest Review of the WHOOP Strap</a></li>
            <li><a href="#" class="hover:underline">Best High-Protein Snacks for Muscle Recovery</a></li>
        </ul>
    </section>

    <!-- Article Example -->
    <section class="p-10">
        <article class="max-w-3xl mx-auto">
            <h2 class="text-3xl font-bold mb-4">10 Best Resistance Bands for Beginners (2025)</h2>
            <p class="mb-4 text-gray-600">Resistance bands are compact, versatile, and beginner-friendly. Here are our top 10 picks.</p>

            <h3 class="text-xl font-bold mt-6">1. FitSimplify Resistance Loop Bands</h3>
            <p class="mb-2">Best for beginners. Lightweight, color-coded, and affordable. <a href="#" class="text-blue-600 underline">Buy on Amazon</a></p>

            <h3 class="text-xl font-bold mt-6">2. TRX GO Suspension Trainer</h3>
            <p class="mb-2">Pro-level full-body system for home and travel. <a href="#" class="text-blue-600 underline">Check Price</a></p>

            <h3 class="text-xl font-bold mt-6">How to Choose</h3>
            <p>Start light if you're rehabbing, go heavier for strength training, or pick a full kit for variety.</p>
        </article>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white p-6 text-center text-sm">
        <p>© 2025 FitStream Life</p>
        <div class="mt-2 space-x-4">
            <a href="#" class="hover:underline">Affiliate Disclosure</a>
            <a href="#" class="hover:underline">Privacy Policy</a>
            <a href="#" class="hover:underline">Contact</a>
            <a href="#" class="hover:underline">About</a>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def homepage():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
