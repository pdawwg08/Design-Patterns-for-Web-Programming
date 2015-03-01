class PageData(object):
    def __init__(self):
        self.home = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="index.html">Home</a>
<a href="results.html">Results</a>
<a href="details.html">Details</a>
<a href="favorites.html">Favorites</a>
<a href="login.html">Login</a>
<a href="signup.html">Sign Up</a>
</nav>
</header>
<section>
<h1 id="huge">
Find the best cameras with <br/>Neil Lane
</h1>
<form action="results.html">
<input type="search"/>
<button type="submit">
Search Now!
</button>
</form>
</section>""" #index.html
        self.results = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="index.html">Home</a>
<a href="results.html">Results</a>
<a href="details.html">Details</a>
<a href="favorites.html">Favorites</a>
<a href="login.html">Login</a>
<a href="signup.html">Sign Up</a>
</nav>
</header>

<section class="white" id="results">
<form  action="results.html"><input type="text" /></form>
<div class="results">
<a href="details.html">
<img src="Images/Leica.png" alt="Leica Camera"/>
<p>Leica MP .72 Rangefinder Film Camera, Black</p>
</a>
</div>

<div class="results">
<a href="details.html">
<img src="Images/Fujifilm.png" alt="Fujifilm Camera"/>
<p>Fujifilm GF670 Professional Camera with Lens</p>
</a>
</div>

<div class="results">
<a href="details.html">
<img src="Images/Horseman.png" alt="Horseman Camera"/>
<p>Horseman SW-612 Pro Medium Format Panorama Camera with 65mm Grandagon-N Lens</p>
</a>
</div>

<div class="results">
<a href="details.html">
<img src="Images/Toyo.png" alt="Toyo Camera"/>
<p>Toyo 45CF Field Camera</p>
</a>
</div>

<div class="results">
<a href="details.html">
<img src="Images/Nikon.png" alt="Nikon Camera"/>
<p>Nikon FM-10 Body with 35-70 f/3.5-4.8 and Black and White Filters</p>
</a>
</div>

</section>""" #results.html
        self.details = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="index.html">Home</a>
<a href="results.html">Results</a>
<a href="details.html">Details</a>
<a href="favorites.html">Favorites</a>
<a href="login.html">Login</a>
<a href="signup.html">Sign Up</a>
</nav>
</header>
<section class="white" id="details">
<img src="Images/Leica_Large.png" alt="Leica Camera"/>
<h2>Leica MP .72 Rangefinder Film Camera, Black</h2>
Item: LC4916   Mfr: 10302
<br/>
By Leica
<form action="favorites.html"><button>Add to favorites</button></form>
<br/>
This product hasn't been rated yet. <a href="login.html">Write a Review</a>
<br/>
$ 4,995.00
</section>""" #details.html
        self.favorites = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="index.html">Home</a>
<a href="results.html">Results</a>
<a href="details.html">Details</a>
<a href="favorites.html">Favorites</a>
<a href="login.html">Login</a>
<a href="signup.html">Sign Up</a>
</nav>
</header>
<section class="white" id="favorites">
<h1>Favorites</h1>
<a href="details.html">
<img src="Images/Leica.png" alt="Leica Camera"/>
<p>Leica MP .72 Rangefinder Film Camera, Black</p>
</a>
</section>""" #favorites.html
        self.login = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="index.html">Home</a>
<a href="results.html">Results</a>
<a href="details.html">Details</a>
<a href="favorites.html">Favorites</a>
<a href="login.html">Login</a>
<a href="signup.html">Sign Up</a>
</nav>
</header>
<section class="white" id="login">
<h1>Login</h1>
<form>
<input type="email" placeholder="email"/>
<br/>
<input type="password" placeholder="password"/>
<br/>
<button type="submit">Submit</button>
</form>
<aside>
<a href="signup.html">Sign up</a>
</aside>
</section>""" #login.html
        self.signup = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="index.html">Home</a>
<a href="results.html">Results</a>
<a href="details.html">Details</a>
<a href="favorites.html">Favorites</a>
<a href="login.html">Login</a>
<a href="signup.html">Sign Up</a>
</nav>
</header>
<section class="white">
<h1>Sign Up</h1>
<form>
<input type="email" placeholder="email"/>
<br/>
<input type="password" placeholder="password"/>
<br/>
<input type="password" placeholder="confirm password"/>
<br/>
<button type="submit">Submit</button>
</form>
</section>""" #signup.html